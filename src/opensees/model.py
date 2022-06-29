# Claudio Perez
import fnmatch
from math import isclose

from .obj import cmd
from .ast import Tag, Grp, Num


Node = cmd("Node", "node", [
    Tag(),
    Grp("crd", type=Num, args=[Num("x"), Num("y"), Num("z")]),
    Grp("mass", flag="-mass", reqd=False, default=[0.0]*6, args=[
        Num("x"),Num("y"), Num("z"), Num("x"),Num("y"), Num("z")
    ]),
])


class model:
    def __init__(self, *args, ndm=None, ndf=None,
            assm={}, prototypes=None, units="metric", **kwds):

        if ndm is None:
            if "nodes" in kwds:
                ndm = len(next(kwds["nodes"].values()))
            else:
                raise ValueError("Argument `ndm` is required if nodes are not supplied")

        if ndf is None:
            if "zeros" in kwds:
                ndf = len(kwds["zeros"][0][1])
            else:
                raise ValueError("Argument `ndf` is required if zeros are not supplied")

        self._units = units
        self.ndm = ndm
        self.ndf = ndf
        self.prototypes = prototypes if prototypes is not None else {}

        self.m_parameters = {}
        self.m_conns = {}
        self.m_elems = {}
        self.m_nodes = {}
        
        #
        # Book keeping
        #
        self.m_auto_assigned_elems = []
        self.m_auto_assigned_conns = []
        self.m_auto_assigned_nodes = []

        if ndf == 1:
            self.dof_names: dict = { 'x': 0}
        elif ndf == 2:
            self.dof_names: dict = { 'x': 0, 'y': 1}
        elif ndm == 2 and ndf ==3:
            self.dof_names: dict = { 'x': 0, 'y': 1, 'xy':2}
        elif ndm == 3 and ndf ==3:
            self.dof_names: dict = { 'x': 0, 'y': 1, 'z':2}
        elif ndm == 3 and ndf ==6:
            self.dof_names: dict = { 'x': 0, 'y': 1, 'z':2, 'yz':3, 'zx':4, 'xy':5}
        self.dof_nums = list(self.dof_names.values())

        self.add(**kwds)

    def add(self, nodes = {}, zeros=[], conns=[], elems=[], prototypes=None, **assm):
        [self.node(k,*v) for k,v in nodes.items()]
        [self.elem(*el)  for el in elems]
        [self.conn(*cn)  for cn in conns]
        [self.fix(*args) for args in zeros]

    def apply(self,prototypes=None,**kwds):
        if prototypes is None:
            prototypes = self.prototypes

        elems = {}
        for el in self.m_elems.values():
            typ = el["type"]
            tag = el["name"]
            args = {k:v for k,v in el.items() if k not in ["type", "name", "nodes"]}
            if typ in prototypes:
                typ = prototypes[typ]
            elif callable(typ):
                pass
            else:
                continue

            nodei, nodej = el["nodes"]
            if hasattr(typ, "mesh_interval") and typ.mesh_interval:
                # mesh_interval should generate values in (-1, 1)
                Xi = nodei["crd"]
                dX = [j - i for j, i in zip(nodej["crd"], Xi)]

                for i, x in enumerate(typ.mesh_interval):
                    new_node = self.node(None, *(dx*(1+x)/2 + xi for dx, xi in zip(dX, Xi)))

                    elem = typ(nodes=[nodei, new_node], **args)
                    elem.prototype = typ
                    elems.update({self._new_tag("elem", elems): elem})
                    nodei = new_node

            elem = typ(nodes=(nodei, nodej), **args)
            elem.prototype = typ
            elems.update({self._new_tag("elem", elems): elem})

        for conn in self.m_conns.values():
            if prototypes[conn["type"]] != "!fix":
                typ = conn.pop("type")
                tag = conn.pop("name")
                elem = prototypes[typ](**conn)
                elem.prototype = typ
                elems.update({tag: elem})
            else:
                self.m_nodes.pop(conn["nodes"][-1].name)
                self.fix(conn["nodes"][0].name)

        mod = Model(self.ndm, self.ndf, self.m_nodes, elems)
        mod.dof_names = self.dof_names
        mod.prototypes = prototypes
        return mod
    
    @property
    def units(self):
        import elle.units
        return elle.units.UnitHandler(self._units)

    def get_node(self, tag):
        if isinstance(tag,(str,int)):
            return self.m_nodes[tag]
 
    def node(self, tag, *coords, **kwds):
        if tag is None: tag = self._new_tag("node")
        node = Node(**{
            "name": tag,
            "crd": coords, 
            "boun": [0 for i in range(self.ndf)],
            **kwds,
        })
        self.m_nodes.update({tag: node})
        return node

    def mass(self, node, m):
        self.m_nodes[node].mass = m

    def rayleigh(self, *args):
        pass

    def _new_tag(self, typ, container=None):
        if container is not None:
            container = {*getattr(self, f"m_{typ}s"), *container}
        else:
            container = getattr(self, f"m_{typ}s")

        n = len(container)
        while str(n) in container: n += 1

        if typ:
            getattr(self, f"m_auto_assigned_{typ}s").append(str(n))

        return str(n)

    def elem(self, *args, **kwds):
        """
        elem(typ, [nodes])
        elem(typ, [nodes], name)
        elem(typ, name, [nodes])
        """
        typ = args[0]
        if len(args) == 3:
            # elem(typ, [nodes], name) || elem(typ, name, [nodes])
            if isinstance(args[1], (list,tuple,set)):
                nodes = args[1]
                tag = args[2]
            else:
                assert isinstance(args[2], (list,tuple,set))
                nodes = args[2]
                tag = args[1]
            # TODO
            assert tag not in self.m_auto_assigned_elems

        else:
            # elem(typ, [nodes])
            tag = self._new_tag("elem")
            nodes = args[1]

        self.m_elems.update({tag: {
            "type": typ,
            "name": tag,
            "nodes": [self.get_node(n) for n in nodes],
            **kwds
        }})

#    def split(self, elem, number, **kwds):
#
#        def _hook(model):
#            pass

    def conn(self, typ, node, dofs=(), name=None):
        if isinstance(node, (tuple,list)):
            if name is None:
                name = "{}"
            for nd in node:
                self.conn(typ, nd, name=name.format(self._new_tag("conn"))) 
        else:
            if name is None:
                name = self._new_tag("conn")
            self.m_nodes.update({name: self.m_nodes[node](name=name,boun=[1]*self.ndf)})
            self.m_conns.update({
                name: {
                    "type": typ, 
                    "nodes": [self.m_nodes[node], self.m_nodes[name]],
                    "name": name,
                    "boun": [1]*self.ndf
                }
            })

    def link(self, tag, typ, nodes, **kwds):
        self.m_links.update({tag: {
            "type": typ, 
            "nodes": [self.get_node(n) for n in nodes],
            **kwds
        }})


    def _fix_dof(self, node, dof:str):
        node.kwds["boun"][self.dof_names[dof]] = 1
        return

    def _fix_str_flags(self, node, flags):
        rxns = [
            self._fix_dof(node, dof) for dof in flags
        ]
        if len(rxns) > 1:
            return rxns
        else:
            return rxns[0]

    def _fix_int_flags(self, node, flags):
        if len(flags) != self.ndf:
            raise ValueError(
                f"`fix` method requires flags for all dofs ({self.ndf}) "
                f"when working with ints. Instead got flags={flags}."
            )
        rxns = [
            self._fix_dof(node, dof) for dof, flag in zip(self.dof_names, flags)
        ]
        if len(rxns) > 1:
            return rxns
        else:
            return rxns[0]

    def fix(self, node, *dirns, x=None, y=None, z=None):
        """Define a fixed boundary condition at specified 
        degrees of freedom of the supplied node

        > fix([nodes], dir..., x=None, y=None, z=None)

        Parameters
        ----------
        node: anabel.Node | Sequence[anabe.Node]

        dirn: Union[Sequence[String], String]
        
        ### Example

        ```py
        # Fix all dofs at node named "abut"
        model.fix("abut")

        # Create a pinned reaction at node 2
        model.fix(2, "y")

        # Create a node and impose a roller reaction
        a = model.node("a", 0.0, 0.0)
        model.fix(a, "y", "x")

        # Fix the rotational dof in a node a 3-dof model
        model.fix("n1", 0, 0, 1)
        ```
        """
        m_nodes = self.m_nodes

        if not dirns:
            dirns = list(self.dof_names.keys())
        elif len(dirns) == 1 and isinstance(dirns[0], (list,tuple)):
            dirns = dirns[0]
        
        if isinstance(dirns[0], int):
            _fix =  self._fix_int_flags

        else:
            _fix = self._fix_str_flags

        if isinstance(node, str):
            nodes = [m_nodes[n] for n in fnmatch.filter(m_nodes.keys(), node)]
            nodes = filter(_filter_nodes_by_coords(x,y,z), nodes)
            return [_fix(node, dirns) for node in nodes]

        elif isinstance(node, (list,tuple)):
            return [self.fix(n, *dirns, x=x, y=y, z=z) for n in node]

        elif isinstance(node, int): 
            node = self.m_nodes[node]
            return _fix(node, dirns)
        
        else: 
            return _fix(node, dirns)

    def boun(self, node=None, flags: list=None):
        """
        Impose single-point constraints at the specified node. This 
        function is provided to give a familiar interface for users
        of platforms like FEAP and FEDEAS.

        Parameters
        ----------
        node: Union[anabel.abstract.Node, anabel.abstract.TagType]
            Node identifier

        flags: List[int]

        ### Example

        ```py
        model.boun(1, [0, 0, 1])
        ```
        """
        if elem is not None:
            assert node is None
            return self._fix_by_elem(elem, dofs)
        if isinstance(node,str):
            node = self.m_nodes[node]

        for i, dof in enumerate(self.dof_names):
            if flags[i]:
                self.fix(node, dof)

class Model:
    def __init__(self, ndm, ndf, nodes, elems, **kwds):
        self.m_nodes: dict = nodes
        self.m_elems: dict = elems
        self.ndm:     int  = ndm
        self.ndf:     int  = ndf

    def get_node(self, tag):
        if isinstance(tag,(str,int)):
            return self.m_nodes[tag]

    def get_refs(self):
        for node in self.m_nodes.values():
            yield node
        for elem in self.m_elems.values():
            yield elem

    @property
    def nodes(self):
        return self.m_nodes.values()

    @property
    def elems(self):
        return self.m_elems.values()

    @property
    def refs(self):
        return set(sub for el in self.elems for sub,_ in el.get_refs())

    @property
    def materials(self):
        return set(a for a in self.refs)


def _filter_nodes_by_coords(x, y, z):
    def f(node):
        match = True
        if x is not None:
            match = match and isclose(node.x, x)
        if y is not None:
            match = match and isclose(node.y, y)
        if z is not None:
            match = match and isclose(node.z, z)
        return match
    return f


# Model = Assembly


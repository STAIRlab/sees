__version__  = "0.0.4"
#
from .patch import layer

# Imports for this module
import math
import fnmatch
from .lib import Node, uniaxial, element
from .obj import *

class _Model:
    def __init__(self, ndm, ndf, nodes, elems):
        self.m_nodes = nodes
        self.m_elems = elems
        self.ndm = ndm
        self.ndf = ndf

    def get_node(self, tag):
        if isinstance(tag,(str,int)):
            return self.m_nodes[tag]

    @property
    def nodes(self):
        return self.m_nodes.values()

    @property
    def elems(self):
        return self.m_elems.values()

    @property
    def refs(self):
        return set(sub for el in self.elems for sub in el.get_refs())

    @property
    def materials(self):
        return set(a[0] for a in self.refs)



class Assembly:
    def __init__(self, ndm, ndf, assm={}, partials={}, units="metric", **kwds):
        self._units = units
        self.meta = kwds
        self.ndm = ndm
        self.ndf = ndf

        self.m_parameters = {}
        self.m_conns = {}
        self.m_links = {}
        self.m_nodes = {}
        self.m_bouns = {}

        if ndf == 2:
            self.prob_type = '2d-truss'
            self.dof_names: dict = { 'x': 0, 'y': 1} # Degrees of freedom
        elif ndm == 2 and ndf ==3:
            self.prob_type = '2d-frame'
            self.dof_names: dict = { 'x': 0, 'y': 1, 'xy':2}
        elif ndm == 3 and ndf ==3:
            self.prob_type = '3d-truss'
            self.dof_names: dict = { 'x': 0, 'y': 1, 'z':2}
        elif ndm == 3 and ndf ==6:
            self.prob_type = '3d-frame'
            self.dof_names: dict = { 'x': 0, 'y': 1, 'z':2, 'yz':3, 'zx':4, 'xy':5}
    

    def build(self, assm, partials):
        self.m_nodes = {
            k: Node(*v) for k,v in assm["nodes"]
        }

        self.m_conns = {
            k: partials[el.type](*el.args)
            for k, el in assm["links"]
        }

        self.m_conns.update({
            ZeroLength() for k,v in assm["bound"]
        })
    
    def get_node(self, tag):
        if isinstance(tag,(str,int)):
            return self.m_nodes[tag]

    @property
    def units(self):
        import elle.units
        return elle.units.UnitHandler(self._units)

    
    def node(self, tag, *coords, **kwds):
        self.m_nodes.update({tag: Node(**{
            "name": tag,
            "crd": coords, 
            "boun": [0 for i in range(self.ndf)],
            **kwds,
        })})

    def conn(self, tag, typ, nodes, **kwds):
        self.m_conns.update({tag: {
            "type": typ,
            "name": tag,
            "nodes": [self.get_node(n) for n in nodes],
            **kwds
        }})

    def elem(self,*args,**kwds):
        return self.conn(*args, **kwds)


    def foun(self, name, typ, node):
        self.m_nodes.update({name: self.m_nodes[node](name=name,boun=[1]*self.ndf)})
        self.m_bouns.update({
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

    def zero():
        pass

    def apply(self,partials,**kwds):
        elems = {}
        for con in self.m_conns.values():
            typ = con.pop("type")
            tag = con.pop("name")
            if typ in partials:
                elem = partials[typ](**con)
            else:
                elem = typ(**con)
                # partials.update({f"elem_{id(elem)}": elem})
                partials.update({f"{tag}": typ})
            elem.partial = typ
            elems.update({tag: elem})

        for boun in self.m_bouns.values():
            if partials[boun["type"]] != "!fix":
                typ = boun.pop("type")
                tag = boun.pop("name")
                elem = partials[typ](**boun)
                elem.partial = typ
                elems.update({tag: elem})
            else:
                self.m_nodes.pop(boun["nodes"][-1].name)
                self.fix(boun["nodes"][0].name)

        mod = _Model(self.ndm, self.ndf, self.m_nodes, elems)
        mod.dof_names = self.dof_names
        mod.partials = partials
        return mod

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
            raise ValueError(f"`fix` method requires flags for all dofs ({self.ndf}) when working with ints.")
        rxns = [
            self._fix_dof(node, self.dof_nums[i]) for i in range(self.ndf)
        ]
        if len(rxns) > 1:
            return rxns
        else:
            return rxns[0]



    def fix(self, node, *dirns, x=None, y=None, z=None):
        """Define a fixed boundary condition at specified 
        degrees of freedom of the supplied node

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

    def boun(self, node, flags: list):
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
        if isinstance(node,str):
            node = self.m_nodes[node]

        for i, dof in enumerate(self.dof_names):
            if flags[i]:
                self.fix(node, dof)



def _is_sequence(obj):
    return hasattr(type(obj), '__iter__')

def _filter_nodes_by_coords(x, y, z):
    def f(node):
        match = True
        if x is not None:
            match = match and math.isclose(node.x, x)
        if y is not None:
            match = match and math.isclose(node.y, y)
        if z is not None:
            match = match and math.isclose(node.z, z)
        return match
    return f

# if __name__=="__main__":
#     import opensees.tcl
#     PROMPT = "\033\\[01;32mopensees\033\\[0m > "
# 
# # Path to Tcl script which loads commands
#     INIT_TCL = ""
# 
#     TCL_MAIN = f"""
# 
#     set cmd ""
#     set repl_flag true
#     proc exit {{}} {{upvar repl_flag flag; set flag false}}
#     while {{ $repl_flag }} {{
#       puts -nonewline "{PROMPT}"
#       flush stdout
#       if {{[gets stdin line] < 0 }} break
#       append cmd $line "\\n"
#       if {{![info complete $cmd]}} {{
#         set prompt ""
#         continue
#       }}
#       set prompt "{PROMPT}"
# 
#       if {{[catch $cmd msg]}} {{
#         puts stderr "Error: $msg"
#       }} elseif {{$msg ne ""}} {{
#         puts $msg
#       }}
# 
#       set cmd ""
#     }}
#     """
# 
# 
#     import sys
#     tcl = opensees.tcl.TclInterpreter()
#     if len(sys.argv) == 1:
#         tcl.eval(TCL_MAIN)
#     else:
#         for filename in sys.argv[1:]:
#             tcl.eval(open(filename).read())




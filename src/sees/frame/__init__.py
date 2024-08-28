#===----------------------------------------------------------------------===#
#
#         STAIRLab -- STructural Artificial Intelligence Laboratory
#
#===----------------------------------------------------------------------===#
#
# Claudio Perez
#
import sys
import warnings
from collections import defaultdict


import numpy as np
Array = np.ndarray
from scipy.linalg import block_diag

from sees.model  import FrameModel
from sees.state  import read_state, State, BasicState
from sees.config import Config, apply_config, LineStyle, NodeStyle


def _is_truss(el):
    name = el["type"].lower()
    return "truss" in name


def _is_frame(el):
    name = el["type"].lower()
    return     "beam"  in name \
            or "dfrm"  in name \
            or "frame" in name

def _is_plane(el):
    name = el["type"].lower()
    return "quad" in name or "shell" in name or "tri" in name

def _is_solid(el):
    name = el["type"].lower()
    return "brick" in name

def elastic_curve(x: Array, v: list, L:float)->Array:
    "compute points along Euler's elastica"
    if len(v) == 2:
        ui, uj, (vi, vj) = 0.0, 0.0, v
    else:
        ui, vi, uj, vj = v
    xi = x/L                        # local coordinate
    N1 = 1.-3.*xi**2+2.*xi**3
    N2 = L*(xi-2.*xi**2+xi**3)
    N3 = 3.*xi**2-2*xi**3
    N4 = L*(xi**3-xi**2)
    y = ui*N1 + vi*N2 + uj*N3 + vj*N4
    return y.flatten()

def elastic_tangent(x: Array, v: list, L: float)->Array:
    if len(v) == 2:
        ui, uj, (vi, vj) = 0.0, 0.0, v
    else:
        ui, vi, uj, vj = v
    xi = x/L
    M3 = 1 - xi
    M4 = 6/L*(xi-xi**2)
    M5 = 1 - 4*xi+3*xi**2
    M6 = -2*xi + 3*xi**2
    return (ui*M3 + vi*M5 + uj*M4 + vj*M6).flatten()


def displaced_profile(
        coord: Array,
        displ: Array,        #: Displacements
        vect : Array = None, #: Element orientation vector
        Q = None,
        npoints: int = 10,
        tangent: bool = False
    ):
    n = npoints
    #           (------ndm------)
    reps = 4 if len(coord[0])==3 else 2

    # 3x3 rotation into local system
    # Q = rotation(coord, vect)
    # Local displacements
    u_local = block_diag(*[Q]*reps)@displ
    # Element length
    L = np.linalg.norm(coord[-1] - coord[0])

    # longitudinal, transverse, vertical, section, elevation, plan
    li, ti, vi, si, ei, pi = u_local[:6]
    lj, tj, vj, sj, ej, pj = u_local[6:]

    Lnew  = L + lj - li
    xaxis = np.linspace(0.0, Lnew, n)

    plan_curve = elastic_curve(xaxis, [ti, pi, tj, pj], Lnew)
    elev_curve = elastic_curve(xaxis, [vi,-ei, vj,-ej], Lnew)

    local_curve = np.stack([xaxis + li, plan_curve, elev_curve])

    if tangent:
        plan_tang = elastic_tangent(xaxis, [ti, pi, tj, pj], Lnew)
        elev_tang = elastic_tangent(xaxis, [vi,-ei, vj,-ej], Lnew)

        local_tang = np.stack([np.linspace(0,0,n), plan_tang, elev_tang])
        return (
            Q.T@local_curve + coord[0][None,:].T,
            Q.T@local_tang
        )

    return Q.T@local_curve + coord[0][None,:].T


class FrameArtist:
    ndm:    int
    ndf:    int
    model:  "FrameModel"
    canvas: "Canvas"

    def __init__(self, model_data,
                 ndf=None,
                 #
                 config=None,
                 # Model
                 loc=None,
                 model_config=None,
                 # Canvas
                 canvas=None,
                 #
                 **kwds):

        self.config = config
        self.canvas = canvas
        vert = config.get("vertical", 2)

        self.ndm = 3

        if ndf is None:
            ndf = 6

#       elif ndf == 3:
#           self.ndm = 2

        if vert == 3:
            R = np.eye(3)
        else:
            R = np.array(((1,0, 0),
                          (0,0,-1),
                          (0,1, 0)))

        self._plot_rotation = R

        self.model = model = FrameModel(model_data, shift=loc, rot=R,
                                        **(model_config or {}))


        # Create permutation matrix
        if model.ndf == 2 and model.ndm == 2:
            self.dofs2plot = R@np.array(((1, 0),
                                         (0, 1),
                                         (0, 0)))

        elif ndf == 3 and model.ndm == 3:
            self.dofs2plot = block_diag(*[R]*2)@np.array(((1,0, 0),
                                                          (0,1, 0),
                                                          (0,0, 1),

                                                          (0,0, 0),
                                                          (0,0, 0),
                                                          (0,0, 0)))

        elif ndf == 3 and model.ndm == 2:
            self.dofs2plot = block_diag(*[R]*2)@np.array(((1,0, 0),
                                                          (0,1, 0),
                                                          (0,0, 0),

                                                          (0,0, 0),
                                                          (0,0, 0),
                                                          (0,0, 1)))

        else:
            self.dofs2plot = block_diag(*[R]*2)

        self.displ_states = {}


    def _config_sketch(self,  sketch):
        strokes = {"outline", "surface", "axes", "contour", "marker", "info"}
        return {
            stroke: {
                k: v.get(stroke, None) for k, v in self.config["sketches"][sketch].items()
            } for stroke in strokes
        }

    def _add_displ_case(self, state, name=None, scale=1.0):

        if name in self.displ_states:
            self.displ_states[name].update(state)
        else:
            self.displ_states[name] = state

        return name


    def add_state(self, res_file, scale=1.0, only=None, type=None, **kwds):

        if not isinstance(res_file, (dict, Array, State)):
            state = read_state(res_file, only=only,
                               model=self.model,
                               scale=scale,
                               transform=self.dofs2plot,
                               **kwds)
        else:
            state = res_file

        # If dict of dicts, assume its a collection of responses, 
        # otherwise, just a single response
        if isinstance(state, dict) and isinstance(next(iter(state.values())), dict):
            for k, v in state.items():
                self._add_displ_case(v, name=k, scale=scale)

        elif isinstance(state, dict):
            self._add_displ_case(BasicState(state, self.model,
                                            scale=scale,
                                            transform=self.dofs2plot))

        else:
            self._add_displ_case(state, scale=scale)


    def add_point_displacements(self, displ, scale=1.0, name=None):
        displ_array = self.displ_states[name]
        for i,n in enumerate(self.model["nodes"]):
            for dof in displ[n]:
                displ_array[i, dof] = 1.0

        displ_array[:,3:] *= scale/100
        displ_array[:,:3] *= scale
        return name


    def plot_origin(self, **kwds):
        xyz = np.zeros((3,3))
        uvw = self._plot_rotation.T*kwds.get("scale", 1.0)
        off = [[0, -kwds.get("scale", 1.0)/2, 0],
               [0]*3,
               [0]*3]

        self.canvas.plot_vectors(xyz, uvw, **kwds)

#       for i,label in enumerate(kwds.get("label", [])):
#           self.canvas.annotate(label, (xyz+uvw)[i]+off[i])

    def add_elem_data(self, config=None):

        N = 3
        for type in self.model.cell_prototypes():
            name = type["name"]
            ni = len(type["instances"])
            coords = np.zeros((ni*(N+1),self.ndm))
            coords.fill(np.nan)
            for i,crd in enumerate(self.model.cell_position(type["instances"])):
                coords[(N+1)*i:(N+1)*i+N,:] = np.linspace(*crd, N)

            coords = coords.reshape(-1,4,3)[:,-3]

            self.canvas.plot_hover(coords, data=type["properties"],
                                   style=NodeStyle(shape="sphere"),
                                   label=name)


    def draw_outlines(self, state=None, config=None):
        model = self.model
        ndm   = self.model["ndm"]

        N = 10 if state is not None and config["frame"]["basis"] is not None else 2
        do_frames = False
        # TODO: Count frame elements
        ne = len(model["assembly"])
        frames = np.zeros((ne*(N+1),3))
        frames.fill(np.nan)
#       frames = []

        quadrs = []
        trians = []
        solids = []

        for i,(tag,el) in enumerate(model["assembly"].items()):
            if _is_frame(el) or _is_truss(el):
                if not config["frame"]["show"]:
                    continue

                if config["frame"]["basis"] is None:
                    do_frames = True
                    frames[(N+1)*i:(N+1)*i+N,:] = model.cell_position(tag, state)[[0,-1],:]
#                   frames.append( model.cell_position(tag, state)[[0,-1],:] )
                else:
                    displ = state.cell_array(tag)
                    if not hasattr(displ, "flatten"):
                        continue
                    do_frames = True
                    frames[(N+1)*i:(N+1)*i+N,:] = displaced_profile(model.cell_position(tag),
#                   frames.append (               displaced_profile(model.cell_position(tag),
                                                                    displ.flatten(),
                                                                    Q=model.frame_orientation(tag),
                                                                    npoints=N).T
#                   )
            elif _is_plane(el) and config["plane"]["show"]:
                idx = model.cell_exterior(tag)
                if len(idx) == 4:
                    quadrs.append([*idx, idx[0]])
                elif len(idx) == 3:
                    trians.append([*idx, idx[0]])

#           elif _is_solid(el) and config["solid"]["show"]:
#               # TODO: get cell faces
#               idx = model.cell_exterior(tag)
#               solids.append(idx)

        if do_frames and config["frame"]["show"]:
            self.canvas.plot_lines(frames[:,:self.ndm], style=config["frame"]["style"])

        if len(quadrs) > 0 and config["plane"]["show"]:
            nodes = model.node_position(state=state)
            self.canvas.plot_lines(nodes, indices=np.array(quadrs),
                                   style=config["plane"]["style"])

        if len(trians) > 0 and config["plane"]["show"]:
            nodes = model.node_position(state=state)
            self.canvas.plot_lines(nodes, indices=np.array(trians),
                                   style=config["plane"]["style"])

        if len(solids) > 0 and config["solid"]["show"]:
            nodes = model.node_position(state=state)
            self.canvas.plot_lines(nodes, indices=np.array(solids),
                                          style=config["solid"]["style"])

    def draw_surfaces(self, state=None, layer=None, config=None):
        model = self.model

        # Draw extruded frames
        from sees.frame import extrude
        if "frame" in config and config["frame"]["show"]:
            extrude.draw_extrusions(model,
                                    canvas=self.canvas,
                                    state=state,
                                    config=config["frame"])

        # Draw filled mesh for cell-like elements
        triangles = []
        if "plane" in config and config["plane"]["show"]:
            nodes = model.node_position(state=state)

            for i,(tag,el) in enumerate(model["assembly"].items()):
                if not _is_frame(el):
                    triangles.extend(model.cell_triangles(tag))

        if len(triangles) > 0:
            self.canvas.plot_mesh(nodes, np.array(triangles), style=config["plane"]["style"])

        return

        #
        # TODO: Remove everthing below
        #

        # N = 2
        N = 20 if displ is not None else 2

        I = 0
        coords = []
        triang = []
        for i,el in enumerate(self.model["assembly"].values()):
            # if int(el["name"]) < 30: continue
            try:
                sect = sections[el["name"]]
            except:
                if int(el["name"]) < 1e3:
                    sect = self.config["default_section"]
                else:
                    sect = np.array([[-48, -48],
                                     [ 48, -48],
                                     [ 48,  48],
                                     [-48,  48]])



    def plot_displaced_assembly(self, state=None, label=None):
        model = self.model
        N  = 10 if state is not None else 2
        ne = len(model["assembly"])
        coords = np.zeros((ne*(N+1), 3))
        coords.fill(np.nan)

        do_lines = False
        for i,(tag,el) in enumerate(model["assembly"].items()):
            if _is_frame(el) and state is not None:
                do_lines = True
                coords[(N+1)*i:(N+1)*i+N,:] = displaced_profile(model.cell_position(tag),
                                                                state.cell_array(tag).flatten(),
                                                                Q=model.frame_orientation(tag),
                                                                npoints=N).T
            elif len(el["crd"]) == 2:
                do_lines = True
                coords[(N+1)*i:(N+1)*i+N,:] = np.linspace(*el["crd"], N)

        if do_lines:
            self.canvas.plot_lines(coords[:, :self.ndm], style=LineStyle(color="red"), label=label)

    def plot_nodes(self, state=None, data=None, label=None, config=None):
        if state is not None and state.rotation is not None and self.model.ndm == 3:
            rotations = self.model.node_rotation(state=state)
        else:
            rotations = None

        coord = self.model.node_position(state=state)
        self.canvas.plot_nodes(coord[:,:self.ndm], label=label,
                               rotations=rotations,
                               style=config["node"]["style"])

        if state is None:
            self.canvas.plot_hover(coord[:,:self.ndm],
                                   label="node",
                                   keys=["tag", "crd"],
                                   data=[[str(k), list(map(str, coord[i]))]
                                       for i,k in enumerate(self.model.iter_node_tags())])


    def draw_axes(self, state=None, config=None):
        ne = len(self.model["assembly"])
        xyz, uvw = np.nan*np.zeros((2, ne, 3, 3))

        for i,el in enumerate(self.model["assembly"].values()):
            axes = self.model.frame_orientation(el["name"])
            if axes is None or not config["frame"]["show"]:
                continue
            crd = self.model.cell_position(el["name"], state=state) #el["crd"]
            scale = np.linalg.norm(crd[-1] - crd[0])/10
            coord = sum(i for i in crd)/len(el["nodes"])
            xyz[i,:,:] = np.array([coord]*3)
            uvw[i,:,:] = scale*axes

        self.canvas.plot_vectors(xyz.reshape(ne*3,3), uvw.reshape(ne*3,3))


    def sketch(self, state, config, layer=None):
        if config["outline"] is not None:
            self.draw_outlines(state, config=config["outline"])

        if config["surface"] is not None:
            self.draw_surfaces(state, config=config["surface"])

        if config["marker"] is not None \
            and "node" in config["marker"] \
            and config["marker"]["node"]["show"]:
            self.plot_nodes(state, config=config["marker"])

        if config["axes"] is not None:
            self.draw_axes(state, config=config["axes"])

        if "hover" in config:
            try:
                self.add_elem_data(config=config["hover"])
            except Exception as e:
                raise e
            warnings.warn(str(e))


    def draw(self):
        # Background
        if "origin" in self.config["sketches"]["default"] \
                and self.config["sketches"]["default"]["origin"]["axes"]["show"]:
            origin = self.config["sketches"]["default"]["origin"]
            self.plot_origin(line_style=origin["axes"]["style"],
                                  scale=origin["axes"]["scale"],
                                  label=origin["axes"]["label"])

        # Reference
        if ("reference" in self.config["sketches"] \
                and self.config["sketches"]["reference"]):
            self.sketch(None, config=self._config_sketch("reference"))

        elif len(self.displ_states) == 0:
            self.sketch(None, config=self._config_sketch("default"))


        for layer, state in self.displ_states.items():
            self.sketch(config=self._config_sketch("displaced"),
                        state=state,
                        layer=layer)

        self.canvas.build()
        return self

    def save(self, filename):
        self.canvas.write(filename)

    def repl(self):
        from opensees.repl.__main__ import OpenSeesREPL
        self.canvas.plt.ion()

        try:
            from IPython import get_ipython
            get_ipython().run_magic_line('matplotlib')
        except:
            pass

        repl = OpenSeesREPL()

        def plot(*args):
            if len(args) == 0:
                return self.draw()

            elif hasattr(self, "plot_"+args[0]):
                return getattr(self, "plot_"+args[0])(*args[1:])

            elif hasattr(self, args[0]):
                return getattr(self, args[0])(*args[1:])

        repl.interp._interp.createcommand("plot", plot)
        # repl.interp._interp.createcommand("show", lambda *args: self.canvas.show())
        repl.repl()


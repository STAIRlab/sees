#!/bin/env python
# # Synopsis
#
# >`render.py [<options>] <model-file>
#
# >**Arpit Nema**, **Chrystal Chern**, and **Claudio Perez**
# 
#
# This script plots the geometry of a structural
# model given a SAM JSON file. The SAM JSON structure
# was developed by the NHERI SimCenter.
#
#
# # Installation
#
# The simplest way to install this script is to run
# 
#     $ python render.py --install
#
# from a terminal that has python installed, in a
# directory containing the `render.py` file. This
# will install the following packages:

REQUIREMENTS = """
pyyaml
scipy
numpy
plotly
matplotlib
"""

# ## Matlab
# In order to install the Matlab bindings, open Matlab in a
# directory containing the files `render.py` and `render.m`,
# and run the following command in the Matlab interpreter:
#
#     render --install
#
# Once this process is complete, the command `render` can be
# called from Matlab, just as described below for the command
# line.
#
# # Usage
# This script can be used either as a module, or as a command
# line utility. When invoked from the command line on
# **Windows**, {NAME} should be `python -m render`. For example:
#
#     python -m render model.json --axes 2 --view elev
#
# The script may be invoked with the following options:

NAME = "render.py"
HELP = f"""
usage: {NAME} <sam-file>
       {NAME} --install
       {NAME} [options] <sam-file>
       {NAME} [options] <sam-file> <res-file>
       {NAME} --section <py-file>#<py-object>

Generate a plot of a structural model.

Positional Arguments:
  <sam-file>                     JSON file defining the structural model.
  <res-file>                     JSON or YAML file defining a structural
                                 response.

Options:
  -s, --scale  <scale>           Set displacement scale factor.
  -d, --disp   <node>:<dof>...   Apply a unit displacement at node with tag
                                 <node> in direction <dof>.
  -V, --view   {{elev|plan|sect}}  Set camera view.
  -a, --axes   [<L><T>]<V>       Specify model axes. Only <V> is required
      --hide   <object>          Hide <object>; see '--show'.
      --show   <object>          Show <object>; accepts any of:
                                    {{origin|frames|frames.displ|nodes|nodes.displ}}

  -o, --save   <out-file>        Save plot to <out-file>.
  -c, --conf

      --install                  Install script dependencies.
      --script {{sam|res}}
  -h, --help                     Print this message and exit.



  <dof>        {{long | tran | vert | sect | elev | plan}}
               {{  0  |   1  |   2  |   3  |   4  |   5 }}
  <object>     {{origin|frames|frames.displ|nodes|nodes.displ}}
"""

EXAMPLES="""
Examples:
    Plot the structural model defined in the file `sam.json`:
        $ {NAME} sam.json

    Plot displaced structure with unit translation at nodes
    5, 3 and 2 in direction 2 at scale of 100:

        $ {NAME} -d 5:2,3:2,2:2 -s100 --axes 2 sam.json
"""

# The remainder of this script is broken into the following sections:
#
# - Data shaping / Misc.
# - Kinematics
# - Plotting
# - Command line processing
#

# Defaults
#=========
# The following configuration options are available:

Config = lambda : {
  "show_objects": ["frames", "frames.displ", "nodes"],
  "hide_objects": ["origin"],
  "sam_file":     None,
  "elem_by_type": False,
  "res_file":     None,
  "write_file":   None,
  "displ":        [],
  "scale":        100.0,
  "orientation":  [0,2,1],
  "view":         "iso",
  "plotter":      "mpl",

  "camera": {
      "view": "iso",               # iso | plan| elev[ation] | sect[ion]
      "projection": "orthographic" # perspective | orthographic
  },

  "displacements": {"scale": 100, "color": "#660505"},

  "objects": {

      "origin": {"color": "black"},

      "frames" : {
          "color": "#000000",
          "displaced": {"color": "red", "npoints": 20}
      },

      "nodes": {
          "default": {"size": 2, "color": "#000000"},
          "displaced" : {},
          "fixed"  : {},
      },
  },
  "save_options": {
      # Options for when writing to an HTML file.
      "html": {
          "include_plotlyjs": True,
          "include_mathjax" : "cdn",
          "full_html"       : True
      }
  }
}

def apply_config(conf, opts):
    for k,v in conf.items():
        if isinstance(v,dict):
            apply_conf(v, opts[k])
        else:
            opts[k] = v


# The following Tcl script can be used to create a results
# file

EIG_SCRIPT = """
for {set m 1} {$m <= 3} {incr m} {
  puts "$m:"
  foreach n [getNodeTags] {
    puts "  $n: \[[join [nodeEigenvector $n $m] {, }]\]";
  }
}
"""

import sys, os
try:
    import yaml
    import numpy as np
    Array = np.ndarray
    FLOAT = np.float32
    from scipy.linalg import block_diag
except:
    # prevent undefined variables when run in install mode
    yaml = None
    Array = list
    FLOAT =  float
NDM=3 # this script currently assumes ndm=3

# Data shaping / Misc.
#----------------------------------------------------

# The following functions are used for reshaping data
# and carrying out other miscellaneous operations.

class RenderError(Exception): pass

def wireframe(sam:dict)->dict:
    """
    Process OpenSees JSON output and return dict with the form:

        {<elem tag>: {"crd": [<coordinates>], ...}}
    """
    geom  = sam["geometry"]
    coord = np.array([n.pop("crd") for n in geom["nodes"]],dtype=FLOAT)
    nodes = {n["name"]: {**n, "crd": coord[i]} for i,n in enumerate(geom["nodes"])}
    trsfm = {t["name"]: t for t in sam["properties"]["crdTransformations"]}
    elems =  {
      e["name"]: dict(
        **e, 
        crd=np.array([nodes[n]["crd"] for n in e["nodes"]], dtype=FLOAT),
        trsfm=trsfm[e["crdTransformation"]] if "crdTransformation" in e else None
      ) for e in geom["elements"]
    }
    return dict(nodes=nodes, elems=elems, coord=coord)

def read_model(filename:str)->dict:
    import json
    with open(filename,"r") as f:
        sam = json.load(f)
    model = wireframe(sam["StructuralAnalysisModel"])
    if "RendererConfiguration" in sam:
        model["config"] = sam["RendererConfiguration"]
    return model

# Kinematics
#----------------------------------------------------

# The following functions implement various kinematic
# relations for standard frame models.

# Helper functions for extracting rotations in planes
elev_dofs = lambda v: v[[1,2]]
plan_dofs = lambda v: v[[3,4]]

def get_dof_num(dof:str, axes:list):
    try: return int(dof)
    except: return {
            "long": axes[0],
            "vert": axes[2],
            "tran": axes[1],
            "sect": axes[0]+3,
            "plan": axes[2]+3,
            "elev": axes[1]+3
    }[dof]

def elastic_curve(x: Array, v: Array, L:float)->Array:
    "compute points along Euler's elastica"
    vi, vj = v
    xi = x/L                        # local coordinates
    N1 = 1.-3.*xi**2+2.*xi**3
    N2 = L*(xi-2.*xi**2+xi**3)
    N3 = 3.*xi**2-2*xi**3
    N4 = L*(xi**3-xi**2)
    y = vi*N2+vj*N4
    return y.flatten()

def linear_deformations(u,L):
    """
    Compute local frame deformations assuming small displacements

    u: 6-vector of displacements in rotated frame
    L: element length
    """
    xi, yi, zi, si, ei, pi = range(6)    # Define variables to aid
    xj, yj, zj, sj, ej, pj = range(6,12) # reading array indices.

    elev_chord = (u[zj]-u[zi]) / L       # Chord rotations
    plan_chord = (u[yj]-u[yi]) / L
    return np.array([
        [u[xj] - u[xi]],                 # xi
        [u[ei] - elev_chord],            # vi_elev
        [u[ej] - elev_chord],            # vj_elev

        [u[pi] - plan_chord],
        [u[pj] - plan_chord],
        [u[sj] - u[si]],
    ],dtype=FLOAT)


def rotation(xyz: Array, vert=(0,0,-1))->Array:
    "Create a rotation matrix between local e and global E"
    dx = xyz[1] - xyz[0]
    L = np.linalg.norm(dx)
    e1 = dx/L
    v13 = np.atleast_1d(vert)
    v2 = -np.cross(e1,v13)
    e2 = v2 / np.linalg.norm(v2)
    v3 =  np.cross(e1,e2)
    e3 = v3 / np.linalg.norm(v3)
    return np.stack([e1,e2,e3])


def displaced_profile(
        coord: Array,
        displ: Array,        #: Displacements
        vect : Array = None, #: Element orientation vector
        glob : bool  = True, #: Transform to global coordinates
        npoints:int = 10,
    )->Array:
    n = npoints
    #          (---ndm---)
    rep = 4 if len(coord[0])==3 else 2
    Q = rotation(coord, vect)
    L = np.linalg.norm(coord[1] - coord[0])
    v = linear_deformations(block_diag(*[Q]*rep)@displ, L)
    Lnew = L+v[0,0]
    xaxis = np.linspace(0.0, Lnew, n)

    plan_curve = elastic_curve(xaxis, plan_dofs(v), Lnew)
    elev_curve = elastic_curve(xaxis, elev_dofs(v), Lnew)

    dx,dy,dz = Q@np.linspace(displ[:3], displ[6:9], n).T
    local_curve = np.stack([xaxis+dx[0], plan_curve+dy, elev_curve+dz])

    if glob:
        global_curve = Q.T@local_curve + coord[0][None,:].T

    return global_curve



# Plotting
#----------------------------------------------------

VIEWS = { # pre-defined plot views
    "plan":    dict(azim=  0, elev= 90),
    "sect":    dict(azim=  0, elev=  0),
    "elev":    dict(azim=-90, elev=  0),
    "iso":     dict(azim= 45, elev= 35)
}

def new_3d_axis():
    import matplotlib.pyplot as plt
    _, ax = plt.subplots(1, 1, subplot_kw={"projection": "3d"})
    ax.set_autoscale_on(True)
    ax.set_axis_off()
    return ax

def add_origin(ax,scale):
    xyz = np.zeros((3,3))
    uvw = np.eye(3)*scale
    ax.quiver(*xyz, *uvw, arrow_length_ratio=0.1, color="black")
    return ax

def set_axis_limits(ax):
    "Find and set axes limits"
    aspect = [ub - lb for lb, ub in (getattr(ax, f'get_{a}lim')() for a in 'xyz')]
    aspect = [max(a,max(aspect)/8) for a in aspect]
    ax.set_box_aspect(aspect)

def plot_skeletal(frame, axes=None):
    if axes is None: axes = [0,2,1]
    props = {"frame": {"color": "grey", "alpha": 0.6}}
    ax = new_3d_axis()
    for e in frame["elems"].values():
        x,y,z = e["crd"].T[axes]
        ax.plot(x,y,z, **props["frame"])
    return ax


def plot_nodes(frame, displ=None, axes=None, ax=None):
    if axes is None: axes = [0,2,1]
    ax = ax or new_3d_axis()
    displ = displ or {}
    Zero = np.zeros(NDM)
    props = {"color": "black",
             "marker": "s",
             "s": 2,
             "zorder": 2}

    coord = frame["coord"]
    for i,n in enumerate(frame["nodes"].values()):
        coord[i,:] += displ.get(n["name"],Zero)[:3]

    x,y,z = coord.T[axes]
    ax.scatter(x, y, z, **props)
    return ax

def plot_displ(frame:dict, res:dict, ax=None, axes=None):
    props = {"color": "#660505"}
    ax = ax or new_3d_axis()
    if axes is None: axes = [0,2,1]
    for el in frame["elems"].values():
        # exclude zero-length elements
        if "zero" not in el["type"].lower():
            glob_displ = [
                u for n in el["nodes"] 
                #   extract displ from node, default to ndf zeros
                    for u in res.get(n,[0.0]*frame["nodes"][n]["ndf"])
            ]
            vect = el["trsfm"]["vecInLocXZPlane"]
            x,y,z = displaced_profile(el["crd"], glob_displ, vect=vect)[axes]
            ax.plot(x,y,z, **props)
    return ax

class Plotter:
    def __init__(self,model, opts, axes=None):
        self.model = model
        if axes is None: axes = [0,2,1]
        self.axes = axes
        self.opts = opts

class MplPlotter(Plotter):
    def __init__(self, **kwds):
        pass
    def get_section_layers(self, section):
        import matplotlib.collections
        import matplotlib.lines as lines
        collection = []
        for layer in section.layers:
            if hasattr(layer, "plot_opts"):
                options = layer.plot_opts
            else:
                options = dict(linestyle="--", color="k")
            collection.append(
                lines.Line2D(*np.asarray(layer.vertices).T, **options))
        return collection

    def get_section_patches(self, section):
        import matplotlib.collections
        import matplotlib.patches as mplp
        collection = []
        for patch in section.patches:
            name = patch.__class__.__name__.lower()
            if "circ" in name:
                if patch.intRad:
                    width = patch.extRad - patch.intRad
                    collection.append(mplp.Annulus(patch.center, patch.extRad, width))
                else:
                    collection.append(mplp.Circle(patch.center, patch.extRad))
            else:
                collection.append(mplp.Polygon(patch.vertices))
        return matplotlib.collections.PatchCollection(
            collection,
            facecolor="grey",
            edgecolor="grey",
            alpha=0.3
        )

    def plot_section(self,
        section,
        show_properties=False,
        plain=True,
        show_quad=True,
        show_dims=True,
        annotate=True,
        ax = None,
        fig = None,
        **kwds
    ):
        """Plot a composite cross section."""    
        import matplotlib.pyplot as plt
        if plain:
            show_properties = show_quad = show_dims = False

        if show_properties:
            fig = plt.figure(constrained_layout=True)
            gs = fig.add_gridspec(1,5)
            axp = fig.add_subplot(gs[0,3:-1])
            label = "\n".join(["${}$:\t\t{:0.4}".format(k,v) for k,v in self.properties().items()])
            axp.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
            axp.set_autoscale_on(True)
            axp.axis("off")

            ax = fig.add_subplot(gs[0,:3])
        else:
            fig, ax = plt.subplots()

        if ax is None:
            fig, ax = plt.subplots()
        ax.set_autoscale_on(True)
        ax.set_aspect(1)

        #x_max = 1.01 * max(v[0] for p in self.patches for v in p.vertices if hasattr(p,"vertices"))
        #y_max = 1.05 * max(v[1] for p in self.patches for v in p.vertices if hasattr(p,"vertices"))
        #y_min = 1.05 * min(v[1] for p in self.patches for v in p.vertices if hasattr(p,"vertices"))

        #ax.set_xlim(-x_max, x_max)
        #ax.set_ylim( y_min, y_max)
        ax.axis("off")
        # add shapes
        ax.add_collection(self.get_section_patches(section,**kwds))
        for l in self.get_section_layers(section):
            ax.add_line(l)
        # show centroid
        #ax.scatter(*section.centroid)
        # show origin
        ax.scatter(0, 0)
        plt.show()
        
        return fig, ax

class GnuPlotter(Plotter):
    def plot_frames(self):
        file=sys.stdout
        print("""
        set term wxt
        unset border
        unset xtics
        unset ytics
        unset ztics
        set view equal xyz
        splot "-" using 1:2:3 with lines
        """,file=file)
        coords = self._get_frames()
        np.savetxt(file, coords)

    def _get_frames(self):
        axes = self.axes
        model = self.model
        props = {"color": "#808080", "alpha": 0.6}
        coords = np.zeros((len(model["elems"])*3,NDM))
        coords.fill(np.nan)
        for i,e in enumerate(model["elems"].values()):
            coords[3*i:3*i+2,:] = e["crd"][:,axes]
        return coords



class PlotlyPlotter(Plotter):
    def plot(x,y,**opts):
        pass

    def plot_frames():
        pass

    def _get_displ(self,res:dict):
        frame = self.model
        axes = self.axes
        props = {"color": "red"}
        N = 10
        coords = np.zeros((len(frame["elems"])*(N+1),NDM))
        coords.fill(np.nan)
        for i,el in enumerate(frame["elems"].values()):
            # exclude zero-length elements
            if "zero" not in el["type"].lower():
                glob_displ = [
                    u for n in el["nodes"]
                    #   extract displ from node, default to ndf zeros
                        for u in res.get(n,[0.0]*frame["nodes"][n]["ndf"])
                ]
                vect = el["trsfm"]["vecInLocXZPlane"]
                coords[(N+1)*i:(N+1)*i+N,:] = displaced_profile(el["crd"], glob_displ, vect=vect, npoints=N)[axes].T
        x,y,z = coords.T
        return {
            "type": "scatter3d",
            "mode": "lines",
            "x": x, "y": y, "z": z,
            "line": {"color":props["color"]},
            "hoverinfo":"skip"
        }
    def make_hover_data(self, data, ln=None):
        if ln is None:
            items = np.array([d.values for d in data])
            keys = data[0].keys()
        else:
            items = np.array([list(data.values())]*ln)
            keys = data.keys()
        return {
            "hovertemplate": "<br>".join(f"{k}: %{{customdata[{v}]}}" for v,k in enumerate(keys)),
            "customdata": list(items),
        }

    def _get_nodes(self):
        x,y,z = self.model["coord"].T[self.axes]
        keys  = ["tag",]
        nodes = np.array(list(self.model["nodes"].keys()),dtype=FLOAT)[:,None]
        return {
                "name": "nodes",
                "x": x, "y": y, "z": z,
                "type": "scatter3d","mode": "markers",
                "hovertemplate": "<br>".join(f"{k}: %{{customdata[{v}]}}" for v,k in enumerate(keys)),
                "customdata": list(nodes),
                "marker": {
                    "symbol": "square",
                    **self.opts["objects"]["nodes"]["default"]
                }
        }

    def _get_frame_labels(self):
        coords = self._frame_coords.reshape(-1,4,3)[:,-3]
        x,y,z = coords.T
        keys  = ["tag",]
        frames = np.array(list(self.model["elems"].keys()),dtype=FLOAT)[:,None]
        return {
                "name": "frames",
                "x": x, "y": y, "z": z, 
                "type": "scatter3d","mode": "markers",
                "hovertemplate": "<br>".join(f"{k}: %{{customdata[{v}]}}" for v,k in enumerate(keys)),
                "customdata": frames,
                "opacity": 0
                #"marker": {"opacity": 0.0,"size": 0.0, "line": {"width": 0.0}}
        }

    def _get_frames(self, elems=None):
        N = 4
        axes = self.axes
        elems = elems or self.model["elems"]
        props = {"color": "#808080", "alpha": 0.6}
        coords = np.zeros((len(elems)*N,NDM))
        coords.fill(np.nan)
        for i,e in enumerate(elems.values()):
            coords[N*i:N*i+N-1,:] = np.linspace(*e["crd"][:,axes], N-1)
        self._frame_coords = coords
        x,y,z = coords.T
        return [{
            "type": "scatter3d",
            "mode": "lines",
            "x": x, "y": y, "z": z,
            "line": {"color":props["color"]},
            "hoverinfo":"skip"
        }]


def plot_plotly(model, axes=None, displ=None, opts={}):
    import plotly.graph_objects as go
    plt = PlotlyPlotter(model,axes=axes,opts=opts)
    if opts["elems_by_type"]:
        frames = plt._get_frames()
    else:
        frames = plt._get_frames()
    labels = plt._get_frame_labels()
    nodes = plt._get_nodes()
    fig = go.Figure(dict(
            #go.Scatter3d(**plot_skeletal_plotly(model,axes)),
            data=[*frames, labels, nodes] + ([plt._get_displ(displ)] if displ else []),
            layout=go.Layout(
                scene=dict(aspectmode='data',
                     xaxis_visible=False,
                     yaxis_visible=False,
                     zaxis_visible=False,
                     camera=dict(
                         projection={"type": opts["camera"]["projection"]}
                     )
                ),
                showlegend=False
            )
        ))
    return fig

# Script functions
#----------------------------------------------------

# Argument parsing is implemented manually because in
# the past I have found the standard library module
# `argparse` to be slow.

def parse_args(argv)->dict:
    opts = Config()
    if os.path.exists(".render.yaml"):
        with open(".render.yaml", "r") as f:
            presets = yaml.load(f, Loader=yaml.Loader)

        apply_config(presets,opts)

    args = iter(argv[1:])
    for arg in args:
        try:
            if arg == "--help" or arg == "-h":
                print(HELP)
                sys.exit()

            elif arg == "--gnu":
                opts["plotter"] = "gnu"

            elif arg == "--install":
                try: install_me(next(args))
                # if no directory is provided, use default
                except StopIteration: install_me()
                sys.exit()

            elif arg[:2] == "-d":
                node_dof = arg[2:] if len(arg) > 2 else next(args)
                for nd in node_dof.split(","):
                    node, dof = nd.split(":")
                    opts["displ"].append((int(node), get_dof_num(dof, opts["orientation"])))

            elif arg[:2] == "-s":
                opts["scale"] = float(arg[2:]) if len(arg) > 2 else float(next(args))

            elif arg == "--scale":
                opts["scale"] = float(next(args))

            elif arg == "--axes":
                vert = int(next(args))
                tran = 2 if vert == 1 else 1
                opts["orientation"][1:] = [tran, vert]

            elif arg == "--show":
                opts["show_objects"].extend(next(args).split(","))

            elif arg == "--hide":
                opts["show_objects"].pop(next(args))
            
            elif arg[:2] == "-V":
                opts["view"] = arg[2:] if len(arg) > 2 else next(args)
            elif arg == "--view":
                opts["view"] = next(args)

            elif arg == "--elem-by-type":
                opts["elem_by_type"] = True

            #elif arg[:2] == "-m":
            #    opts["mode"] = int(arg[2]) if len(arg) > 2 else int(next(args))

            elif arg[:2] == "-o":
                opts["write_file"] = arg[2:] if len(arg) > 2 else next(args)

            #elif arg == "--displ-only":
            #    opts["displ_only"] = True

            # Final check on options
            elif arg[0] == "-":
                raise RenderError(f"ERROR - unknown option '{arg}'")

            elif not opts["sam_file"]:
                opts["sam_file"] = arg

            else:
                opts["res_file"] = arg

        except StopIteration:
            # `next(args)` was called without successive arg
            raise RenderError(f"ERROR -- Argument '{arg}' expected value")
    return opts

def install_me(install_opt=None):
    import os
    import subprocess
    if install_opt == "dependencies":
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", *REQUIREMENTS.strip().split("\n")
        ])
        sys.exit()
    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    sys.argv = sys.argv[:1] + ["develop", "--user"]
    print(sys.argv)

    setup(name="render",
          version="0.0.1",
          description="",
          long_description=HELP,
          author="", author_email="", url="",
          py_modules=["render"],
          scripts=["render.py"],
          license="",
          install_requires=[*REQUIREMENTS.strip().split("\n")],
    )

TESTS = [
    (False,"{NAME} sam.json -d 2:plan -s"),
    (True, "{NAME} sam.json -d 2:plan -s50"),
    (True, "{NAME} sam.json -d 2:3    -s50"),
    (True, "{NAME} sam.json -d 5:2,3:2,2:2 -s100 --axes 2 sam.json")
]


def render(sam_file, res_file=None, **opts):
    if sam_file is None:
        raise RenderError("ERROR -- expected positional argument <sam-file>")

    model = read_model(sam_file)

    if "config" in model:
        apply_config(model["config"], opts)
    
    axes = opts["orientation"]

    if opts["plotter"] == "gnu":
        GnuPlotter(model, axes).plot_frames()
        sys.exit()

    #for obj in opts["show_objects"]:
    #    plt[obj]

    ax = plot_skeletal(model,axes=axes)
       
    if res_file is not None:
        from urllib.parse import urlparse
        res_path = urlparse(res_file)
        with open(res_path[2], "r") as f:
            res = yaml.load(f,Loader=yaml.Loader)
        if res_path[4]: # query parameters passed
            res = res[int(res_path[4].split("=")[-1])]

    else:
        res = {}
    for n,d in opts["displ"]:
        v = res.setdefault(n,[0.0]*model["nodes"][n]["ndf"])
        if d < 3: # translational dof
            v[d] += 1.0
        else:
            v[d] += 0.1

    # apply scale
    scale = opts["scale"]
    if scale != 1.0:
        for n in res.values():
            for i in range(len(n)):
                n[i] *= scale


    ax = plot_nodes(model, res, ax=ax, axes=axes)
    if res:
        plot_displ(model, res, axes=axes, ax=ax)

    # Handle plot formatting
    set_axis_limits(ax)
    ax.view_init(**VIEWS[opts["view"]])
    if "origin" in opts["show_objects"]: add_origin(ax, scale)

    if opts["write_file"]:
    # write plot to file if file name provided
        if "html" in opts["write_file"]:
            fig = plot_plotly(model,axes,displ=res,opts=opts)
            import plotly
            print(str(id(model)),file=sys.stderr)
            html = plotly.io.to_html(fig, div_id=str(id(model)), **opts["save_options"]["html"])
            with open(opts["write_file"],"w+") as f:
                f.write(html)
        else:
            ax.figure.savefig(opts["write_file"])
    else:
    # otherwise show in new window
        import matplotlib.pyplot as plt
        plt.show()
    return ax

# Main script
#----------------------------------------------------
# The following code is only executed when the file
# is invoked as a script.

if __name__ == "__main__":
    opts = parse_args(sys.argv)
    if "json" in opts["sam_file"]:
        # Plot structural model
        try:
            render(**opts)
        except (FileNotFoundError,RenderError) as e:
            print(e, file=sys.stderr)
            print(f"         Run '{NAME} --help' for more information", file=sys.stderr)
            sys.exit()
    else:
        # Plot a cross section
        from urllib.parse import urlparse
        file = urlparse(opts["sam_file"])
        with open(file.path, "r") as f:
            script = f.read()
        scope = {}
        exec(script, scope)
        plt = MplPlotter()
        plt.plot_section(scope[file.fragment])





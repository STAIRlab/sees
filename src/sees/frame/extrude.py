# Claudio Perez
import sys
import numpy as np
from scipy.spatial.transform import Rotation

import shps.curve

import sees
import sees.frame
from sees.model import read_model
from sees.errors import RenderError
from sees.config import MeshStyle, LineStyle


def draw_extrusions(model, canvas, state=None, config=None):
    #
    #     x-------o---------o---------o
    #   /       /         /
    # x--------o<--------o---------o
    # |        |       / ^
    # |        |     /   |
    # |        |   /     |
    # |        | /       |
    # x--------o-------->o---------o
    #
    ndm = 3

    coords = [] # Global mesh coordinates
    triang = [] # Triangle indices into coords
    locoor = [] # Local mesh coordinates, used for textures

    if config is None:
        config = {
                "style": MeshStyle(color="gray")
        }

    I = 0
    for i,el in enumerate(model["assembly"].values()):

        outline = model.cell_section(el["name"])
        if outline is None:
            continue

        outline = outline*config["scale"]

        nen  = len(el["nodes"])

        noe = len(outline) # number of outline edges
        if state is not None:
            glob_displ = state.cell_array(el["name"], state.position)
            X = shps.curve.displace(el["crd"], glob_displ, nen).T
            R = state.cell_array(el["name"], state.rotation)
        else:
            outline = outline*0.98
            X = np.array(el["crd"])
            R = [model.frame_orientation(el["name"]).T]*nen


        # Loop over sample points along element length to assemble
        # `coord` and `triang` arrays
        for j in range(nen):
            # Loop over section edges
            for k,edge in enumerate(outline):
                # Append rotated section coordinates to list of coordinates
                coords.append(X[j, :] + R[j]@[0, *edge])
                locoor.append(
                             [ (j+0)/nen+0.1,  0.1+(k+0)/(noe+0) ]
                )

                if j == 0:
                    # Skip the first section
                    continue

                elif k < noe-1:
                    triang.extend([
                        # Tie two triangles to this edge
                        [I+    noe*j + k,   I+    noe*j + k + 1,    I+noe*(j-1) + k],
                        [I+noe*j + k + 1,   I+noe*(j-1) + k + 1,    I+noe*(j-1) + k]
                    ])
                else:
                    # elif j < N-1:
                    triang.extend([
                        [I+    noe*j + k,    I + noe*j , I+noe*(j-1) + k],
                        [      I + noe*j, I + noe*(j-1), I+noe*(j-1) + k]
                    ])

        I += nen*noe

    triang = [list(reversed(i)) for i in triang]

    if len(triang) > 0:
        canvas.plot_mesh(coords, triang, local_coords=locoor, style=config["style"])

    show_edges = True

    if not show_edges or len(triang) == 0:
        return

    IDX = np.array((
        (0, 2),
        (0, 1)
    ))

    triang = [list(reversed(i)) for i in triang]

    nan = np.zeros(ndm)*np.nan
    coords = np.array(coords)
    if "tran" in config["outline"]:
        tri_points = np.array([
            coords[idx]  if (j+1)%3 else nan
            for j,idx in enumerate(np.array(triang).reshape(-1))
        ])
    elif "long" in config["outline"]:
        tri_points = np.array([
            coords[i]  if j%2 else nan
            for j,idx in enumerate(np.array(triang)) for i in idx[IDX[j%2]]
        ])
    else:
        return

    canvas.plot_lines(tri_points,
                      style=config["line_style"]
                       #LineStyle(
                       #     color="black" if state is not None else "#808080",
                       #     width=4
                       #)
    )

class so3:
    @classmethod
    def exp(cls, vect):
        return Rotation.from_rotvec(vect).as_matrix()

def _add_moment(artist, loc, axis):
    import meshio
    mesh_data = meshio.read(sees.assets/'chrystals_moment.stl')
    coords = mesh_data.points

    coords = np.einsum('ik, kj -> ij',  coords,
                       so3.exp([0, 0, -np.pi/4])@so3.exp(axis))
    coords = 1e-3*coords + loc
#   for node in coords:
#       node = so3.exp(axis)@node
    for i in mesh_data.cells:
        if i.type == "triangle":
            triangles =  i.data #mesh_data.cells['triangle']
            break;

    artist.canvas.plot_mesh(coords, triangles)


def _render(sam_file, res_file=None, **opts):
    # Configuration is determined by successively layering
    # from sources with the following priorities:
    #      defaults < file configs < kwds 

    config = sees.config.Config()


    if sam_file is None:
        raise RenderError("Expected positional argument <sam-file>")

    # Read and clean model
    if not isinstance(sam_file, dict):
        model = read_model(sam_file)
    else:
        model = sam_file

    if "RendererConfiguration" in model:
        sees.apply_config(model["RendererConfiguration"], config)

    sees.apply_config(opts, config)

    artist = sees.FrameArtist(model, **config)

    draw_extrusions(artist.model, artist.canvas, config=opts)

    # -----------------------------------------------------------

    soln = sees.state.read_state(res_file, artist.model, **opts)
    if soln is not None:
        if "time" not in opts:
            soln = soln[soln.times[-1]]

        draw_extrusions(artist.model, artist.canvas, soln, opts)
        # -----------------------------------------------------------
        _add_moment(artist,
                    loc  = [1.0, 0.0, 0.0],
                    axis = [0, np.pi/2, 0])
        # -----------------------------------------------------------

    artist.draw()
    return artist


if __name__ == "__main__":
    import sees.parser
    config = sees.parser.parse_args(sys.argv)

    try:
        artist = _render(**config)

        # write plot to file if output file name provided
        if config["write_file"]:
            artist.save(config["write_file"])


        # Otherwise either create popup, or start server
        elif hasattr(artist.canvas, "popup"):
            artist.canvas.popup()

        elif hasattr(artist.canvas, "to_glb"):
            import sees.server
            server = sees.server.Server(glb=artist.canvas.to_glb(),
                                        viewer=config["viewer_config"].get("name", None))
            server.run(config["server_config"].get("port", None))

        elif hasattr(artist.canvas, "to_html"):
            import sees.server
            server = sees.server.Server(html=artist.canvas.to_html())
            server.run(config["server_config"].get("port", None))

    except (FileNotFoundError, RenderError) as e:
        # Catch expected errors to avoid printing an ugly/unnecessary stack trace.
        print(e, file=sys.stderr)
        print("         Run '{NAME} --help' for more information".format(NAME=sys.argv[0]), file=sys.stderr)
        sys.exit()


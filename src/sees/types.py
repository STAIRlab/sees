


# render(model, [state], [canvas=plotly|matplotlib|gltf])
# 
#     Artist(model, canvas)
#         model = Model(model)
# 
#         for elem in model:
#             ... stich
#             canvas.add_mesh(mesh)















#
# sees
#

def render(model: dict | meshio.Mesh | ,
           state, canvas=None, artist=None) -> Artist: ...


def read_model():
    pass

def create_model():
    pass

class Artist: # frame.FrameArtist | plane.PlaneArtist | patch.PatchArtist
    def __init__(self, model, state=None, canvas=None): ...

#
# sees.canvas
#

def figure(splts, type=None) -> Canvas: ...

class Canvas: # canvas.Matplotlib
    def add_curves(self): ...
    def add_origin(self): ...

    def add_planes(self): ...



class Model:
    def __init__(self, data, model): ...


class State:
    def __init__(self, data, model): ...

    def node_array(self): ...

    def cell_array(self): ...



class Series: pass

# Claudio Perez
import numpy as np
import warnings

from sees.config import MeshStyle, LineStyle, NodeStyle


class Canvas:
    def build(self): ...

    def write(self, filename=None):
        raise NotImplementedError

    def annotate(self, *args, **kwds): ...

    def plot_label(self, vertices, text):
        pass

    def plot_hover(self, vertices, data=None, text=None, style: NodeStyle=None, label=None, keys=None, html=None):
        warnings.warn("plot_hover not implemented for chosen canvas")

    def plot_nodes(self, vertices, indices=None, label=None, style: NodeStyle=None, rotate=None, data=None):
        warnings.warn("plot_nodes not implemented for chosen canvas")

    def plot_lines(self, vertices, indices=None, label=None, style: LineStyle=None):
        warnings.warn("plot_lines not implemented for chosen canvas")

    def plot_mesh(self,  vertices, indices     , label=None, style: MeshStyle=None, local_coords=None):
        warnings.warn("plot_mesh not implemented for chosen canvas")

    def plot_vectors(self, locs, vecs, label=None, **kwds):
        ne = vecs.shape[0]
        for j in range(3):
            X = np.zeros((ne*3, 3))*np.nan
            for i in range(j,ne,3):
                X[i*3,:] = locs[i]
                X[i*3+1,:] = locs[i] + vecs[i]
            self.plot_lines(X, style=LineStyle(color=("red", "blue", "green")[j]), label=label)



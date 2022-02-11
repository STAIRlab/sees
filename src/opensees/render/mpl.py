#!/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def show(): plt.show()

def section(s):
    return MplPlotter().plot_section(s)

class MplPlotter:
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
            elif "rect" in name:
                vertices = np.asarray(patch.vertices)
                collection.append(mplp.Rectangle(
                    vertices[0], *(vertices[2]-vertices[0])
                ))
            else:
                collection.append(mplp.Polygon(np.asarray(patch.vertices)))
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

        #x_max = 1.01 * max(v[0] for p in section.patches for v in p.vertices if hasattr(p,"vertices"))
        #y_max = 1.05 * max(v[1] for p in section.patches for v in p.vertices if hasattr(p,"vertices"))
        #y_min = 1.05 * min(v[1] for p in section.patches for v in p.vertices if hasattr(p,"vertices"))

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
        #plt.show()
        
        return ax




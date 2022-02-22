from opensees.obj import LibCmd, Cmd
from opensees.arg import *

_section = LibCmd("section")

class FiberCollection:
    def __init__(self, fibers):
        self.fibers = fibers
    def __contains__(self, point):
        return any(point in fiber for fiber in self.fibers)

@_section
class FiberSection(FiberCollection):
    _args = [
        Tag(),
        Num("GJ", flag="-GJ", field="torsional_stiffness", optional=True, 
            about="linear-elastic torsional stiffness assigned to the section (optional, default = no torsional stiffness)"),
        Blk("fibers", default=[], type=Cmd, defn=dict(
           fiber=LibCmd("fiber"),
           layer=LibCmd("layer")
          )
        )
    ]

    def add_patch(self, patch):
        self.fibers.append(patch)

    def add_patches(self, patch):
        self.fibers.extend(patch)


    @property
    def patches(self):
        return [p for p in self.fibers if p.get_cmd()[0] == "patch"]

    @property
    def layers(self):
        return [p for p in self.fibers if p.get_cmd()[0] == "layer"]

    @property
    def area(self):
        return sum(i.area for i in self.patches)
    
    @property
    def centroid(self):
        return sum(i.centroid * i.area for i in self.patches) / self.area
    
    @property
    def ixy(self):
        return sum(
            p.ixy + p.centroid[0]*p.centroid[1]*p.area for p in self.patches
        )
    
    @property
    def iyy(self):
        return sum(
            p.iyy + p.centroid[0]**2*p.area for p in self.patches
        )

    @property
    def ixx(self):
        return sum(
            p.ixx + p.centroid[1]**2*p.area for p in self.patches
        )

    @property
    def moi(self):
        return [
            [p.moi[i] + p.centroid[i]**2*p.area for i in range(2)] + [p.moi[-1]]
            for p in self.patches
        ]





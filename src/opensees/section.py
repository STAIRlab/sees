from math import pi, sin, cos, sqrt
from opensees.obj import LibCmd, Cmd
from opensees.ast import *
from . import patch, layer

_section = LibCmd("section")

class _FiberCollection:
    def __init__(self, fibers):
        self.fibers = fibers
    def __contains__(self, point):
        return any(point in fiber for fiber in self.fibers)

@_section
class FiberSection(_FiberCollection):
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



def PatchOctagon(
    extRad,
    intRad=0.0, 
    DLbar=4,
    core_conc  = None,
    cover_conc = None,
    ColMatTag   = None,
):
    """
    Dcol     :     Width of octagonal column (to flat sides)
    nLbar    :     Number of longitudinal bars
    DLbar    :     Diameter of longitudinal bars
    sTbar    :     Spacing of transverse spiral reinforcement
    """
    #
    # Column component dimensions
    #
    if intRad == extRad:
        return _oct_outline(extRad)
    elif intRad > 0.0:
        return _oct_ring(extRad, intRad)

    inch = 1.0

    Dcol    =  2*extRad
    tcover  =  2.0*inch           # 2 inch cover width
    Rcol    =  Dcol/2.0           # Radius of octagonal column (to flat sides)
    Dcore   =  Dcol - 2.0*tcover  # Diameter of circular core
    Rcore   =  Dcore/2.0          # Radius of circular core
    # Along   =  pi*DLbar**2/4.0    # Area of longitudinal reinforcement bar
    DTbar   =  0.625*inch         # Diameter of transverse spiral bar (#5 Rebar)
    Asp     =  pi*DTbar**2/4.0    # Area of transverse spiral reinforcement bar
    Dtran   =  Dcore - DTbar      # Diameter of spiral of transverse spiral reinforcement

    # Density of transverse spiral reinforcement
    # rho       =  4.0* Asp/(Dtran*sTbar)
    # Diameter of ring of longitudinal reinforcement
    Dlong     =   Dcore - 2*DTbar - DLbar
    # Rlong     =   Dlong/2.        # Radius of ring of longitudinal reinforcement

    # Build Octagonal RC Column Section
    numSubdivCirc = 64    # # fibers around the entire circumference

    numSlices     =  8    # # slices in each of the 8 sections of the octagon

    cover_divs = [1, 2]
    sect = FiberSection(
      material = ColMatTag,
      GJ       = 1e12,
      fibers  = [
        # Inner Core Patch, 5 radial fibers
        patch.circ(core_conc, numSubdivCirc,  5, [0., 0.], 0.0e0,   Rcore/2, 0.0, 2*pi),
        # Outer Core Patch, 10 radial fibers
        patch.circ(core_conc, numSubdivCirc, 10, [0., 0.], Rcore/2, Rcore,   0.0, 2*pi)
    ])

    for i in range(8):    # For each of the 8 sections of the octagon
        phi =  pi/4/numSlices
        startAngle =  i*pi/4 - pi/8
        for j in range(numSlices):
            sita1  =  startAngle + j*phi   # Slice start angle
            sita2  =  sita1 +  phi         # Slice end angle
            oR1    =  Rcol/cos(pi/8 -  j*phi)
            oR2    =  Rcol/cos(pi/8 - (j+1)*phi)
            # Cover Patch connects the circular core to the octagonal cover
            sect.fibers.append(
              patch.quad(cover_conc, cover_divs,
                vertices = [
                  [Rcore*cos(sita2), Rcore*sin(sita2)],
                  [Rcore*cos(sita1), Rcore*sin(sita1)],
                  [  oR1*cos(sita1),   oR1*sin(sita1)],
                  [  oR2*cos(sita2),   oR2*sin(sita2)]
                ]
            ))
    #layer circ  long_steel  nLbar  Along 0. 0.  Rlong; # Longitudinal Bars
    return sect 


def RegularPolygon(n, Rcol):
    phi =  2*pi/n
    R = Rcol/cos(phi/2)
    vertices = [
        [R*cos(i*phi-phi/2),  R*sin(i*phi-phi/2)]
        for i in range(n)
    ]
    return patch._Polygon(vertices)

def _oct_outline(Rcol):
    n = 8
    phi =  2*pi/n
    R = Rcol/cos(phi/2)
    region = [
        layer.line(vertices=[
            [R*cos(i*phi-phi/2),  R*sin(i*phi-phi/2)],
            [R*cos(i*phi+phi/2),  R*sin(i*phi+phi/2)]
        ]) for i in range(n)
    ]
    return FiberSection(fibers=region)

def _oct_ring(Rcol, Rcore):
    collection = []
    numSlices  =  1       # Num. slices in each of the 8 sections of the octagon
    cover_divs = 1,2      # divisions in each slice of the cover
    for i in range(8):
        phi =  pi/4/numSlices
        startAngle =  i*pi/4 - pi/8
        for j in range(numSlices):
            sita1  =  startAngle + j*phi   # Slice start angle
            sita2  =  sita1 +  phi         # Slice end angle
            oR1    =  Rcol/cos(pi/8 -  j*phi)
            oR2    =  Rcol/cos(pi/8 - (j+1)*phi)
            # Cover Patch connects the circular core to the octagonal cover
            collection.append(
              patch.quad(None, cover_divs,
                vertices = [
                  [Rcore*cos(sita2), Rcore*sin(sita2)],
                  [Rcore*cos(sita1), Rcore*sin(sita1)],
                  [  oR1*cos(sita1),   oR1*sin(sita1)],
                  [  oR2*cos(sita2),   oR2*sin(sita2)]
                ]
            ))
    return FiberSection(fibers=collection)



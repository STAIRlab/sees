"""
This module provides constructors for `SectionForceDeformation` objects
which represent force-deformation (or resultant stress-strain) 
relationships at beam-column and plate sample points.

"""
from math import pi, sin, cos, sqrt
from opensees.obj import LibCmd, Cmd
from .lib import uniaxial
from opensees.ast import *
from . import patch, layer

_section = LibCmd("section")

class _FiberCollection:
    def __init__(self, areas):
        self.areas = areas
    def __contains__(self, point):
        return any(point in area for area in self.areas)

@_section
class FiberSection(_FiberCollection):
    """Create a `FiberSection`.

    """
    _args = [
        Tag(),
        Num("GJ", flag="-GJ", field="torsional_stiffness", optional=True, 
            about="linear-elastic torsional stiffness assigned to the section (optional, default = no torsional stiffness)"),
        Blk("areas", default=[], type=Cmd, defn=dict(
           fiber=LibCmd("fiber"),
           layer=LibCmd("layer")
          )
        )
    ]

    def add_patch(self, patch):
        self.areas.append(patch)

    def add_patches(self, patch):
        self.areas.extend(patch)


    @property
    def patches(self):
        return [p for p in self.areas if p.get_cmd()[0] == "patch"]

    @property
    def layers(self):
        return [p for p in self.areas if p.get_cmd()[0] == "layer"]

    @property
    def area(self):
        return sum(i.area for i in self.patches)
    
    @property
    def centroid(self):
        return sum(i.centroid * i.area for i in self.patches) / self.area
     
    @property
    def ixc(self):
        yc = self.centroid[1]
        return sum(
            p.ixc + (p.centroid[1]-yc)**2*p.area for p in self.patches
        )
    
    @property
    def iyc(self):
        xc = self.centroid[0]
        return sum(
            p.iyc + (p.centroid[0]-xc)**2*p.area for p in self.patches
        )


    @property
    def moic(self):
        return [
            [p.moi[i] + p.centroid[i]**2*p.area for i in range(2)] + [p.moi[-1]]
            for p in self.patches
        ]



def PolygonRing(extRad, intRad, n):
    """
    Create a polygon annulus.
    """
    psi = 2*pi/n
    phi = psi
    collection = []
    cover_divs = 1,2      # divisions in each slice of the cover
    iR1, iR2 = [intRad/cos(pi/n)]*2
    oR1, oR2 = [extRad/cos(pi/n)]*2
    j = 0
    for i in range(n):
        startAngle =  (i - 1/2)*psi
        sita1  =  startAngle + j*phi   # Slice start angle
        sita2  =  sita1 + phi          # Slice end angle
        # Cover Patch connects the circular core to the polygonal cover
        collection.append(
          patch.quad(None, cover_divs,
            vertices = [
              [   iR1*cos(sita1),    iR1*sin(sita1)],
              [   oR1*cos(sita1),    oR1*sin(sita1)],
              [   oR2*cos(sita2),    oR2*sin(sita2)],
              [   iR2*cos(sita2),    iR2*sin(sita2)],
            ]
        ))
    sect = FiberSection(areas=collection)
    sect.extRad = extRad
    sect.intRad = intRad
    return sect

def RegularPolygon(n, Rcol):
    phi =  2*pi/n
    R = Rcol/cos(phi/2)
    vertices = [
        [R*cos(i*phi-phi/2),  R*sin(i*phi-phi/2)]
        for i in range(n)
    ]
    poly = patch._Polygon(vertices)
    return poly

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
    sect = FiberSection(areas=region)
    sect.extRad = Rcol
    sect.intRad = 0.0
    return sect

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
    sect = FiberSection(areas=collection)
    sect.extRad = Rcol
    sect.intRad = Rcore
    return sect
    
def ConfiningPolygon(extRad, intRad, n, s=1):
    psi = 2*pi/n
    phi = psi/s
    collection = []
    cover_divs = 1,2      # divisions in each slice of the cover
    iR1, iR2 = [intRad]*2

    for i in range(n):
        startAngle =  (i - 1/2)*psi
        for j in range(s):
            sita1  =  startAngle + j*phi   # Slice start angle
            sita2  =  sita1 + phi          # Slice end angle
            oR1    =  extRad/cos(pi/n -  j*phi)
            oR2    =  extRad/cos(pi/n - (j+1)*phi)
            # iR1    =  intRad/cos(pi/n -  j*phi)
            # iR2    =  intRad/cos(pi/n - (j+1)*phi)
            # Cover Patch connects the circular core to the polygonal cover
            collection.append(
              patch.quad(None, cover_divs,
                vertices = [
                  [   iR1*cos(sita1),    iR1*sin(sita1)],
                  [   oR1*cos(sita1),    oR1*sin(sita1)],
                  [   oR2*cos(sita2),    oR2*sin(sita2)],
                  [   iR2*cos(sita2),    iR2*sin(sita2)],
                ]
            ))
    sect = FiberSection(areas=collection)
    sect.extRad = extRad
    sect.intRad = intRad
    return sect

def ConfinedPolygon(
    extRad,
    intRad     = None, 
    DLbar=4,
    core_conc  = None,
    cover_conc = None,
    ColMatTag  = None,
    units      = None,
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
    if intRad is None:
        intRad = extRad - 2.0

    # assert intRad == 0.0 and extRad > 0.0

    inch    = 1.0
    Dcol    =  2*extRad
    # tcover  =  2.0*inch           # 2 inch cover width
    Rcol    =  Dcol/2.0           # Radius of octagonal column (to flat sides)
    Dcore   =  2*intRad
   #Dcore   =  Dcol - 2*tcover    # Diameter of circular core
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
    cdivs = 64        # # fibers around the entire circumference

    numSlices =  8    # # slices in each of the 8 sections of the octagon

    cover_divs = [1, 2]
    sect = FiberSection(
      material = ColMatTag,
      GJ       = 1e12,
      areas = [
        # Inner Core Patch, 5 radial fibers
        patch.circ(core_conc, [cdivs,  5], [0., 0.],     0.0, Rcore/2, 0.0, 2*pi),
        # Outer Core Patch, 10 radial fibers
        patch.circ(core_conc, [cdivs, 10], [0., 0.], Rcore/2, Rcore,   0.0, 2*pi)
    ])

    sect.add_patches(ConfiningPolygon(extRad, intRad, 8, numSlices).patches)

    #layer circ  long_steel  nLbar  Along 0. 0.  Rlong; # Longitudinal Bars
    sect.extRad = extRad
    sect.intRad = intRad
    return sect


@_section
class SectionAggregator:
    """
    This command is used to construct a `SectionAggregator`
    object which aggregates groups previously-defined `UniaxialMaterial` 
    objects into a single section force-deformation model. 

    Each `UniaxialMaterial` object represents the section force-deformation response for a particular section degree-of-freedom (dof). There is no interaction between responses in different dof directions. The aggregation can include one previously defined section.
    """
    _img="SectionAggregator.gif"
    _args=[

        # section Aggregator $secTag $matTag1 $dof1 $matTag2 $dof2 ....... <-section $sectionTag>

        Tag(),# ,$secTag unique section tag
        Map("materials",
            about = "the force-deformation quantity to be modeled by this section object.",
            val = Ref("material", type=uniaxial, attr="name", about="tags of previously-defined `UniaxialMaterial` objects"),
            key = Flg(
                    name = "dof",
                    enum = {
                        "P":  "Axial force-deformation",
                        "Mz": "Moment-curvature about section local z-axis",
                        "Vy": "Shear force-deformation along section local y-axis",
                        "My": "Moment-curvature about section local y-axis",
                        "Vz": "Shear force-deformation along section local z-axis",
                        "T":  "Torsion Force-Deformation"
                    }
            )
        ),
        Ref("section", type=_section, flag="-section", about="tag of previously-defined Section object to which the UniaxialMaterial objects are aggregated as additional force-deformation relationships")
    ]


    example="section Aggregator 2 2 Vy -section 4; # create new section with IDtag 2, taking the existing material tag 2 to represent the shear and adding it to the existing section tag 4, which may be a fiber section where the interaction betweeen axial force and flexure is already considered."

    reference="http://earthquakespectra.org/doi/abs/10.1193/1.4000136"

    authors=["Micheal H. Scott"]



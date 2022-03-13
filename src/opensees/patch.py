# Claudio Perez
"""
A patch is used to generate a number of fibers over a cross-sectional area. 
Currently there are three types of patches that fibers can be generated over: 
quadrilateral, rectangular and circular.

All patches have the following attributes:

<dl>
 <dt><code>area</code></dt>
 <dd>Total area of the patch.</dd>

 <dt><code>moic</code></dt>
 <dd>Second moment of area matrix of the patch about its centroidal axis</dd>

 <dt><code>ixc</code></dt>
 <dd>Second moment of inertia of the patch about its $x$ axis</dd>

 <dt><code>iyc</code></dt>
 <dd>Second moment of inertia of the patch about its $y$ axis</dd>

</dl>

"""
import sys
from .ast import *
from .obj import LibCmd, cmd
import numpy as np

class Material: pass

fiber = Fiber = cmd("Fiber","fiber",
    # fiber $yLoc $zLoc $A $material
    about="This command allows the user to construct a single fiber "\
          "and add it to the enclosing `FiberSection` or `NDFiberSection`.",
    args=[
        Grp("coord", args=[Num("y"), Num("z")],
            about="$y$ and $z$ coordinate of the fiber in the section "\
                  "(local coordinate system)"),
        Num("area", about="area of the fiber."),
        Ref("material",type=Material, about="material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection)."),
    ]
)

_patch = LibCmd("patch")


_eps = 0.00001
_huge = sys.float_info.max
_tiny = sys.float_info.min
 
def rayintersectseg(p, edge)->bool:
    """
    takes a point p=Pt() and an edge of two endpoints a,b=Pt() of a line segment returns boolean
    https://rosettacode.org/wiki/Ray-casting_algorithm#Python
    """
    a,b = edge
    if a[1] > b[1]:
        a,b = b,a
    if p[1] == a[1] or p[1] == b[1]:
        p = np.array([p[0], p[1] + _eps])
 
    intersect = False
 
    if (p[1] > b[1] or p[1] < a[1]) or (p[0] > max(a[0], b[0])):
        return False
 
    if p[0] < min(a[0], b[0]):
        intersect = True
    else:
        if abs(a[0] - b[0]) > _tiny:
            m_red = (b[1] - a[1]) / float(b[0] - a[0])
        else:
            m_red = _huge
        if abs(a[0] - p[0]) > _tiny:
            m_blue = (p[1] - a[1]) / float(p[0] - a[0])
        else:
            m_blue = _huge
        intersect = m_blue >= m_red
    return intersect


class _Polygon:
    def __init__(self, vertices):
        self.vertices = np.asarray(vertices)
        self._moic = None
        self._moig = None
        self._area = None

    def __contains__(self, p:tuple) -> bool:
        v = np.asarray(self.vertices)
        edges = np.array(
            [[v[i-1], v[i]] for i in range(len(v))]
        )
        inside = 1 == sum(rayintersectseg(p, edge) for edge in edges)%2
        #if inside: print(p)
        return inside

    @property
    def area(self):
        if self._area is None:
            x,y = np.asarray(self.vertices).T
            self._area = np.sum(x*np.roll(y, -1) - np.roll(x, -1)*y)*0.5
        return self._area

    @property
    def centroid(self):
        x,y = np.asarray(self.vertices).T
        area = self.area
        x_cent = (np.sum((x + np.roll(x, -1)) *
                         (x*np.roll(y, -1) -
                          np.roll(x, -1)*y)))/(6.0*area)
        y_cent = (np.sum((y + np.roll(y, -1)) *
                         (x*np.roll(y, -1) -
                          np.roll(x, -1)*y)))/(6.0*area)
        return np.array((x_cent, y_cent))

    def moi(self, reference, vertices=None, area=None):
        x,y = (np.asarray(self.vertices) - np.asarray(reference)).T

        area = area or self.area
        alpha = x * np.roll(y, -1) - np.roll(x, -1) * y
        # planar moment of inertia wrt horizontal axis
        ixx = np.sum((y**2 + y * np.roll(y, -1) +
                      np.roll(y, -1)**2)*alpha)/12.00
        # planar moment of inertia wrt vertical axis
        iyy = np.sum((x**2 + x * np.roll(x, -1) +
                      np.roll(x, -1)**2)*alpha)/12.00

        # product of inertia
        ixy = np.sum((x*np.roll(y, -1)
                      + 2.0*x*y
                      + 2.0*np.roll(x, -1) * np.roll(y, -1)
                      + np.roll(x, -1) * y)*alpha)/24.

        return np.array([[ixx, ixy],[ixy,iyy]])
        # # polar moment of inertia
        # ir = ixx + iyy
        # # mass moment of inertia wrt in-plane rotation
        # ir_mass = (ixx + iyy) / area
        # return {'ixx': ixx, 'iyy': iyy,
        #         'ixy': ixy, 'ir': ir, 'ir_mass': ir_mass}

    @property
    def moic(self):
        if self._moic is None:
            self._moic = self.moi(self.centroid)
        return self._moic

    @property
    def ixc(self):
        return self.moic[0,0]

    @property
    def iyc(self):
        return self.moic[1,1]

@_patch
class rect(_Polygon):
    _args = [
       Ref("material", type=Material, field="material", 
           about="tag of previously defined material (`UniaxialMaterial`"\
                 "tag for a `FiberSection` or `NDMaterial` tag for use "\
                 "in an `NDFiberSection`)"),
       Grp("divs", args=[
           Int("ij", about="number of subdivisions (fibers) in the IJ direction."),
           Int("jk", about="number of subdivisions (fibers) in the JK direction."),
       ]),
       Grp("vertices", args=[
         Grp(args=[Num("yI"), Num("zI")],  about="$y$ & $z$-coordinates of vertex I (local coordinate system)"),
         Grp(args=[Num("yJ"), Num("zJ")],  about="$y$ & $z$-coordinates of vertex J (local coordinate system)"),
         Grp(args=[Num("yK"), Num("zK")],  about="$y$ & $z$-coordinates of vertex K (local coordinate system)"),
         Grp(args=[Num("yL"), Num("zL")],  about="$y$ & $z$-coordinates of vertex L (local coordinate system)"),
      ])
    ]
    def init(self):
        self._moic = None
        self._moig = None
        self._area = None

        if len(self.vertices) == 2:
            ll, ur = self.vertices
            self.vertices = [
                ll, [ur[0], ll[1]], ur, [ll[0], ur[1]]
            ]
    def discretize(self):
        pass

@_patch
class quad(_Polygon):
    """A quadrilateral shaped patch.
    The geometry of the patch is defined by four vertices: I J K L. 
    The coordinates of each of the four vertices is specified in *counter counter* sequence
    """
    _img  = "quadPatch.svg"
    _args = [
       Ref("material", type=Material, field="material", 
           about="tag of previously defined material (`UniaxialMaterial` "\
                 "tag for a `FiberSection` or `NDMaterial` tag for use in an `NDFiberSection`)"),
       Grp("divs", args=[
         Int("ij", about="number of subdivisions (fibers) in the IJ direction."),
         Int("jk", about="number of subdivisions (fibers) in the JK direction."),
       ]),
       Grp("vertices", args=[
         Grp(args=[Num("yI"), Num("zI")],  about="$y$ & $z$-coordinates of vertex I (local coordinate system)"),
         Grp(args=[Num("yJ"), Num("zJ")],  about="$y$ & $z$-coordinates of vertex J (local coordinate system)"),
         Grp(args=[Num("yK"), Num("zK")],  about="$y$ & $z$-coordinates of vertex K (local coordinate system)"),
         Grp(args=[Num("yL"), Num("zL")],  about="$y$ & $z$-coordinates of vertex L (local coordinate system)"),
      ])
    ]

    def init(self):
        self._moic = None
        self._moig = None
        self._area = None

def rhom(center, height, width, slope=None, divs=(0,0)):
    vertices = [
        [center[0] - width/2 + 1/slope*height/2, center[1] + height/2],
        [center[0] - width/2 - 1/slope*height/2, center[1] - height/2],
        [center[0] + width/2 - 1/slope*height/2, center[1] - height/2],
        [center[0] + width/2 + 1/slope*height/2, center[1] + height/2]
    ]
    return quad(vertices=vertices, div=divs)

@_patch
class circ:
    """
    Create a circular patch.

    ## Examples

    >>> patch.circ()
    """
    _signature = [
        "radius", "sector", "divs", "quadrature", "material",
        "center"
    ]
    _docsigs = [
    ]
    _img  = "circPatch.svg"
    _args = [
      Ref("material", type=Material, about="tag of previously defined material ("\
                          "`UniaxialMaterial` tag for a `FiberSection` "\
                          "or `NDMaterial` tag for use in an `NDFiberSection`)"),
      Grp("divs", args=[
          Int("circ", about="number of subdivisions (fibers) in "\
                            "the circumferential direction (number of wedges)"),
          Int("rad",  about="number of subdivisions (fibers) in the radial direction (number of rings)"),
      ]),
      Grp("center",    args=[Num("y"), Num("z")],
          about="$y$ & $z$-coordinates of the center of the circle", default=[0.0, 0.0]),
      Num("intRad",   about="internal radius", default=0.0),
      Num("extRad",   about="external radius"),
      Num("startAng", about="starting angle", default=0.0),
      Num("endAng",   about="ending angle", default=np.pi*2),
    ]
    def __contains__(self, point):
        origin = np.asarray(self.center)
        vect = np.asarray(point) - origin
        size = np.linalg.norm(vect)
        angl = (np.arctan2(*reversed(vect))+2*np.pi) % 2*np.pi
        inside = [
            (size < self.extRad),
            (size > self.intRad),
            (angl > self.startAng),
            (angl < self.endAng),
        ]
        return all(inside)

    def init(self):
        self._moic = None
        self._moig = None
        self._area = None
    
    @property
    def moic(self):
        if self._moic is None:
            r2,r1 = self.extRad, self.intRad
            a2,a1 = self.endAng, self.startAng
            dsin  = np.sin(2*a2) - np.sin(2*a1)
            self._moic = np.array([
                [(a2-a1 - 0.5*dsin), 0],
                [0, (a2-a1 + 0.5*dsin)],
            ])*(r2**4 - r1**4)*0.125 + self.area*self.centroid**2
        return self._moic

    @property
    def area(self):
        r2,r1 = self.extRad, self.intRad
        a2,a1 = self.endAng, self.startAng
        return 0.5*(r2**2 - r1**2)*(a2 - a1)

    @property
    def centroid(self):
        r2,r1 = self.extRad, self.intRad
        a2,a1 = self.endAng, self.startAng
        return np.array([
            np.sin(a2) - np.sin(a1),
            - np.cos(a2) + np.cos(a1)
        ])*(r2**3 - r1**3)/(3*self.area)


    @property
    def ixc(self):
        return self.moic[0,0]

    @property
    def iyc(self):
        return self.moic[1,1]

    @property
    def J(self):
        return 0.5 * self.area * self.extRad ** 2

layer = LibCmd("layer", 
        {
          "circ": [
            Ref("material",  type=Material,
                           about="material tag of previously created material "\
                                 "(UniaxialMaterial tag for a FiberSection or "\
                                 "NDMaterial tag for use in an NDFiberSection)"),
            Int("divs",  about="number of fibers along arc"),
            Num("area", field="fiber_area", about="area of each fiber"),
            Grp("center", args=[Num("y"), Num("z")],
                about="$y$ and $z$-coordinates of center of circular arc"),
            Num("radius", about="radius of circular arc"),
            Grp("arc", args=[
              Num("startAng",  about="starting angle (optional, default = 0.0)"),
              Num("endAng",    about="ending angle (optional, default = 360.0 - 360/$numFiber)"),
            ])
          ]
        },
        about="The layer command is used to generate a number of fibers along a line or a circular arc.",
)

@layer
class line:
    _img = "straightLayer.svg"
    _args = [
      Ref("material", type=Material, about="""Reference to previously created material 
                (`UniaxialMaterial` for a `FiberSection` or `NDMaterial` 
                for use in an `NDFiberSection`)"""),
      Int("divs", about="number of fibers along line"),
      Num("area", field="fiber_area", about="area of each fiber"),
      Grp("vertices", typ=Grp, args=[
          Grp("start",args=[Num("y"), Num("z")], 
              about="""$y$ and $z$-coordinates of first fiber
                       in line (local coordinate system)"""),
          Grp("end", args=[Num("y"), Num("z")],
              about="$y$ and $z$-coordinates of last fiber in line (local coordinate system)")
      ])
    ]
    def __contains__(self, point):
        a,b = np.asarray(self.vertices)
        p = np.asarray(point)
        return np.isclose(_distance(a,p) + _distance(p,b), _distance(a,b))


def _distance(a,b):
    return np.linalg.norm(a-b)




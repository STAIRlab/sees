import sys
from .ast import *
from opensees.obj import LibCmd, Mat
import numpy as np

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
        self.vertices = vertices

    @property
    def area(self):
        x,y = np.asarray(self.vertices).T
        return np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y)/2.00

    def boundary(self):
        pass

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

        ixy = np.sum((x*np.roll(y, -1)
                      + 2.0*x*y
                      + 2.0*np.roll(x, -1) * np.roll(y, -1)
                      + np.roll(x, -1) * y)*alpha)/24.
        # polar (torsional) moment of inertia
        ir = ixx + iyy
        # mass moment of inertia wrt in-plane rotation
        ir_mass = (ixx + iyy) / area

        return {'ixx': ixx, 'iyy': iyy,
                'ixy': ixy, 'ir': ir, 'ir_mass': ir_mass}
    @property
    def ixx(self):
        return self.moi(self.centroid)["ixx"]

    @property
    def iyy(self):
        return self.moi(self.centroid)["iyy"]
    
    @property
    def ixy(self):
        return self.moi(self.centroid)["ixy"]

    @property
    def iyx(self):
        return self.moi(self.centroid)["ixy"]


    def __contains__(self, p:tuple) -> bool:
        v = np.asarray(self.vertices)
        edges = np.array(
            [[v[i-1], v[i]] for i in range(len(v))]
        )
        return 1 == sum(rayintersectseg(p, edge) for edge in edges)%2


@_patch
class rect(_Polygon):
    _args = [
       Ref("matTag", field="material", 
           about="tag of previously defined material (`UniaxialMaterial`"\
                 "tag for a `FiberSection` or `NDMaterial` tag for use "\
                 "in an `NDFiberSection`)"),
       Int("numSubdivIJ", about="number of subdivisions (fibers) in the IJ direction."),
       Int("numSubdivJK", about="number of subdivisions (fibers) in the JK direction."),
       Grp("vertices", args=[
         Grp(args=[Num("yI"), Num("zI")],  about="y & z-coordinates of vertex I (local coordinate system)"),
         Grp(args=[Num("yJ"), Num("zJ")],  about="y & z-coordinates of vertex J (local coordinate system)"),
         Grp(args=[Num("yK"), Num("zK")],  about="y & z-coordinates of vertex K (local coordinate system)"),
         Grp(args=[Num("yL"), Num("zL")],  about="y & z-coordinates of vertex L (local coordinate system)"),
      ])
    ]
    def init(self):
        if len(self.vertices) == 2:
            ll, ur = self.vertices
            self.vertices = [
                #ll, [ll[0], ur[1]], ur, [ll[0], ur[1]]
                ll, [ur[0], ll[1]], ur, [ll[0], ur[1]]
            ]

@_patch
class quad(_Polygon):
    _args = [
       Ref("matTag",      field="material", 
           about="tag of previously defined material (`UniaxialMaterial` "\
                 "tag for a `FiberSection` or `NDMaterial` tag for use in an `NDFiberSection`)"),
       Grp("divs", args=[
         Int("numSubdivIJ", about="number of subdivisions (fibers) in the IJ direction."),
         Int("numSubdivJK", about="number of subdivisions (fibers) in the JK direction."),
       ]),
       Grp("vertices", args=[
         Grp(args=[Num("yI"), Num("zI")],  about="y & z-coordinates of vertex I (local coordinate system)"),
         Grp(args=[Num("yJ"), Num("zJ")],  about="y & z-coordinates of vertex J (local coordinate system)"),
         Grp(args=[Num("yK"), Num("zK")],  about="y & z-coordinates of vertex K (local coordinate system)"),
         Grp(args=[Num("yL"), Num("zL")],  about="y & z-coordinates of vertex L (local coordinate system)"),
      ])
    ]

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
    _args = [
      Ref("matTag", about="tag of previously defined material ("\
                          "`UniaxialMaterial` tag for a `FiberSection` "\
                          "or `NDMaterial` tag for use in an `NDFiberSection`)"),
      Int("numSubdivCirc", about="number of subdivisions (fibers) in "\
                                 "the circumferential direction (number of wedges)"),
      Int("numSubdivRad",  about="number of subdivisions (fibers) in the radial direction (number of rings)"),
      Grp("center",    args=[Num("yCenter"), Num("zCenter")],
          about="y & z-coordinates of the center of the circle", default=[0.0, 0.0]),
      Num("intRad",    about="internal radius", default=0.0),
      Num("extRad",    about="external radius"),
      Num("startAng",  about="starting angle", default=0.0),
      Num("endAng",    about="ending angle", default=np.pi*2),
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

    @property
    def Ix(self):
        """Moment of inertia"""
        return 0.25 * self.extRad**4 * np.pi
    
    @property
    def Iy(self):
        """Moment of inertia"""
        return 0.25 * self.extRad**4 * np.pi

    @property
    def J(self):
        return 0.5 * self.area * self.extRad ** 2

    @property
    def area(self):
        return np.pi*(self.extRad**2 - self.intRad**2)

    @property
    def centroid(self):
        return np.asarray(self.center)

    @property
    def ixx(self):
        return 0.25 * np.pi * (self.extRad ** 4 - self.intRad ** 4)

    @property
    def iyy(self):
        return 0.25 * np.pi * (self.extRad ** 4 - self.intRad ** 4)

    @property
    def ixy(self):
        return 0.0

layer = LibCmd("layer", {
  "circ": [
    Ref("matTag",  about="material tag of previously created material "\
                         "(UniaxialMaterial tag for a FiberSection or "\
                         "NDMaterial tag for use in an NDFiberSection)"),
    Int("numFiber",  about="number of fibers along arc"),
    Num("areaFiber", about="area of each fiber"),
    Grp("center", args=[Num("yCenter"), Num("zCenter")],
        about="y and z-coordinates of center of circular arc"),
    Num("radius", about="radius of circular arc"),
    Grp("arc", args=[
      Num("startAng",  about="starting angle (optional, default = 0.0)"),
      Num("endAng",  about="ending angle (optional, default = 360.0 - 360/$numFiber)"),
    ])
  ]
})

@layer
class line:
    _args = [
      Ref("matTag", about="""material tag of previously created material 
                (`UniaxialMaterial` tag for a `FiberSection` or `NDMaterial` 
                tag for use in an `NDFiberSection`)"""),
      Int("numFibers", about="number of fibers along line"),
      Num("areaFiber", about="area of each fiber"),
      Grp("vertices", typ=Grp, args=[
          Grp("start",args=[Num("yStart"), Num("zStart")], 
              about="""y and z-coordinates of first fiber
                       in line (local coordinate system)"""),
          Grp("end", args=[Num("yEnd"), Num("zEnd")],
              about="y and z-coordinates of last fiber in line (local coordinate system)")
      ])
    ]
    def __contains__(self, point):
        a,b = np.asarray(self.vertices)
        p = np.asarray(point)
        return np.isclose(_distance(a,p) + _distance(p,b), _distance(a,b))


def _distance(a,b):
    return np.linalg.norm(a-b)




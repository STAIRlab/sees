from .ast import Num, Tag, Ref, Blk, Int, Lst, Grp, Str
from .obj import LibCmd, cmd

_pattern = LibCmd("pattern")
_series  = LibCmd("timeSeries")


@_series
class TimeSeries:
    _name = "Path"
    _args = [
        Tag(),
        Lst("time", flag="-time", type=float),
        Lst("values", flag="-values", type=float),
        Num("scale", reqd=False)
    ]

    def init(self, series=None, step=None, time=None):
        if hasattr(self.values, "data"):
            self.time = self.values.time
            self.values = self.values.data
        if "step" in self.kwds:
            dt = self.kwds["step"]
            self.time = [0.0 + i*dt for i in range(len(self.values))]

@cmd
class GroundMotion:
    _args = [
         Tag(),
         Str("motion_type", default="Plain"),
         Ref("accel", flag="-accel", reqd=False, type=TimeSeries, alt="motion"),
         Ref("veloc", flag="-vel",   reqd=False, type=TimeSeries, alt="motion"),
         Ref("displ", flag="-disp",  reqd=False, type=TimeSeries, alt="motion")
         # <-int (IntegratorType intArgs)> 
         # <-fact $cFactor>
    ]
    # _alts = [
    #     Ref("motion")
    # ]
    _refs = ["accel", "veloc", "displ"]


    def init(self):
        print("INIT: ", self.kwds)
        if "motion" in self.kwds:
            print("IN BUSINESS")
            m = self.kwds["motion"]
            if hasattr(m, "accel"):
                self.accel = TimeSeries(values=m.accel)
            if hasattr(m, "veloc"):
                self.veloc = TimeSeries(values=m.veloc)
            if hasattr(m, "displ"):
                self.displ = TimeSeries(values=m.displ)

@cmd
class ImposedMotion:
    _args = [ 
        Int("node"),# , type="node"),
        Int("dof"),
        Ref("motion", type=GroundMotion)
    ]



load = cmd("load", "load", args=[Ref("node"), Grp("load", min=1, type=Num)])


@_pattern
class Plain:
    _args = [
        Tag(),
        Ref("series"),
        Blk("loads"),
        Num("scale", reqd=False),
    ]
    _refs = ["series"]

    def init(self):
        if not isinstance(self.series, (TimeSeries,int)):
            self.series = TimeSeries(values=self.series)

        loads = []
        for k,v in self.loads.items():
            loads.append(load(k[0], [v]))
        self.loads = loads


@_pattern
class UniformExcitation:
    _args = [
        Tag(),
        Int("dof"),
        Ref("accel", flag="-accel", typ=TimeSeries, attr="name"),
        Num("v0", reqd=False),
        Num("scale", reqd=False)
    ]
    _refs = ["accel"]

    def init(self):
        if not isinstance(self.accel, int):
            self.accel = TimeSeries(values=self.accel)

@_pattern
class MultipleSupport:
    _args = [
        Tag(),
        Blk("motions", alt="components")
    ]
    """
    pattern.MultipleSupport(
        components = [
        #   node, dof,  history
            ( 1,   1,   ResponseComponent(accel, displ, veloc)),
            ( 2,   1,   ResponseComponent(accel, displ, veloc))
        ]
    )
    """
    def init(self):
        imposed_motions = []
        ground_motions = []
        for m in self.motions:
            ground_motions.append(GroundMotion(motion=m[2]))
            imposed_motions.append(ImposedMotion(*m[:2], ground_motions[-1]))
        self.motions = ground_motions + imposed_motions

    @property
    def components(self):
        return []



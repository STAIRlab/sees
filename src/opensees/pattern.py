from .ast import Num, Tag, Ref, Blk, Int, Lst, Grp
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

class MultipleSupport:
    """
    pattern.MultipleSupport(
        components = [
        #   node, dof,  history
            ( 1,   1,   ResponseComponent(accel, displ, veloc)),
            ( 2,   1,   ResponseComponent(accel, displ, veloc))
        ]
    )
    """
    pass

class GroundMotion:
    pass



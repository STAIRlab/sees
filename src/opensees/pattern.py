from .ast import Num, Tag, Ref, Blk, Int, Lst
from .obj import LibCmd, cmd

_pattern = LibCmd("pattern")
_series  = LibCmd("timeSeries")

@_series
class TimeSeries:
    _name = "Path"
    _args = [Tag(), Lst("time", flag="-time", type=float), Lst("values", flag="-values", type=float), Num("scale", reqd=False)]

    def init(self, series=None, step=None, time=None):
        if hasattr(self.values, "time"):
            self.time = self.values.time
            self.values = self.values.data



@_pattern
class PlainPattern:
    _args = [
        Tag(),
        Ref("series"),
        Num("scale", default=1.0),
        Blk("loads")
    ]


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



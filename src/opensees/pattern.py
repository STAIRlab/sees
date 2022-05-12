from .ast import Num, Tag, Ref, Blk
from .obj import LibCmd

_pattern = LibCmd("pattern")

@_pattern
class PlainPattern:
    _args = [
        Tag(),
        Ref("series"),
        Num("scale", default=1.0),
        Blk("loads")
    ]


class UniformExcitation:
    _args = [
        Tag(),
        Int("dof"),
        Ref("series"),
        Num("v0"),
        Num("scale")
    ]

class MultipleSupport:
    pass
"""
pattern.MultipleSupport(
    components = [
    #   node, dof,  history
        ( 1,   1,   ResponseComponent(accel, displ, veloc)),
        ( 2,   1,   ResponseComponent(accel, displ, veloc))
    ]
)
"""

class GroundMotion:
    pass



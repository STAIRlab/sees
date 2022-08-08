import sys
from pathlib import Path
# try using a faster library
try: import orjson as json
except ImportError: import json

from . import units
this_module = sys.modules[__name__]
defs = units.load("english")

for name, value in defs.items():
    setattr(this_module, name, units.Dimension(value))

#
# Constants
#
from .common import sec, minute, hour, day, pi, rad, deg


#
# Derived units
#
ksi, psi, pcf = 1000, 1.0, 1.0/ft**3


with open(Path(__file__).parents[0]/"derived.py") as f:
    exec(f.read())

for name, value in defs.items():
    setattr(this_module, name, units.Dimension(value))


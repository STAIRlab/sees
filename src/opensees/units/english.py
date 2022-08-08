import sys

# Constants
from math import pi
gravity = 386.08858267717


# try using a faster library
try: import orjson as json
except ImportError: import json

from . import units


definitions = {'a': 1, 'b': 2, 'c': 123.4}

this_module = sys.modules[__name__]

defs = units.load("english")

for name, value in defs.items():
    setattr(this_module, name, units.Dimension(value))

#ft = foot
#
# Derived units
#
ksi, psi, pcf = 1000, 1.0, 1.0/ft**3

MPa = 145.038

# Angles
rad = 1
deg = pi/180
in2 = inch*inch
from derived import *


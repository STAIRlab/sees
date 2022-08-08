unit_types = {
    'time'         : ['sec', 'minute', 'h', 'day'],
    'length'       : ['m', 'mm', 'cm', 'km', 'inch', 'ft', 'mile'],
    'area'         : ['m2', 'mm2', 'cm2', 'km2', 'inch2', 'ft2', 'mile2'],
    'volume'       : ['m3', 'mm3', 'cm3', 'km3', 'inch3', 'ft3', 'mile3'],
    'speed'        : ['cmps', 'mps', 'mph', 'inchps', 'ftps'],
    'acceleration' : ['mps2', 'cmps2', 'inchps2', 'ftps2', 'g'],
    'mass'         : ['kg', 'ton', 'lb'],
    'force'        : ['N', 'kN', 'lbf', 'kip', 'kips'],
    'pressure'     : ['Pa', 'kPa', 'MPa', 'GPa', 'psi', 'ksi', 'Mpsi']
}

from math import pi

# time
sec = 1.
minute = 60. * sec
hour = h = 60. * minute
day = 24. * h

# Angles
rad = 1
deg = pi/180


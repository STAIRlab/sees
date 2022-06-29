import math

def triangle(t, period=2*math.pi, amplitude=2.0):
    a, p = amplitude, period
    return 4*a/p * abs((((t-p/4)%p)+p)%p - p/2) - a
    # return 4*amplitude/period * abs((t-period/4)%period - period/2) - amplitude

def sawtooth(t, period=2*math.pi, amplitude = 2):
    return amplitude*(t/period - math.floor(0.5 + t/period))

def square(t, period=2*math.pi, amplitude=2):
    pass

#def cycles(number, fidelity=2, shape="triangle"):
#    return getattr(__module__

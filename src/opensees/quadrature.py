# from typing import Final

import numpy as np 
jnp = np
__all__ = [
    "quad_rule",
]

class IntervalQuadrature:
    pass

_quad_rules = {
    # Closed Newton-Cotes.  deg(P) = n−1
    'trap':       {'closed':True, 'even':True,'deg':1,'n0':2},
    'simp':       {'closed':True, 'even':True,'deg':2,'n0':3},
    'simp38':     {'closed':True, 'even':True,'deg':3,'n0':4},
    'boole':      {'closed':True, 'even':True,'deg':4,'n0':5},

    # Open Newton-Cotes
    'rect':       {'closed':False,  'even':True},
    'mid':        {'closed':False,  'even':True},
    'milnes':     {'closed':False,  'even':True},
    'boole-open': {'closed':False,  'even':True},

    # Gauss
    'legendre':  {'deg': lambda n: 2*n-1,'n': lambda deg: math.ceil((deg+1)/2),'bounds':(-1.,1.)},
    'lobatto':   {'deg': lambda n: 2*n-3,'n': lambda deg: math.ceil((deg+3)/2),'bounds':(-1.,1.)},
    'laguerre':  {'deg': lambda n: None},
    'hermite':   {'deg': lambda n: None},
}


def iquad(n=None, deg=None, bounds=(-1.,1.), fam=None, 
    closed=None, even=False, rule='mid', error_term=False):
    """
    Parameters:
        n: number of sampling points

        deg: degree

    Examples:

    Midpoint rule:
        xi, wi =  quad_points(deg=1, rule='mid')

    Trapezoidal rule:
        xi, wi =  quad_points(deg=1, even=True)

    Composite trapezoidal rule:
        xi, wi = quad_points(n=4, deg=1, rule='cotes')
    
    Composite Simpson's rule 
        xi, wi = quad_points(n=6, deg=2, rule='cotes')

    Gauss-legendre
        xi, wi = quad_points(n=4, rule='legendre')

    'closed': True if endpoints are included
    'deg': degree of highest order polynomial exactly integrated
    'n0': minimum number of points ; For Newton-Cotes rules, this is the 
          number of points for the base (non-composite rule)

    """
    if 'trap' in rule:
        rule='cotes'
        deg = 1

    elif 'simp' in rule:
        rule='cotes'
        deg = 2

    if 'gauss' in rule:
        if closed is None: closed = False
        interp = rule.split('-')[1]
        if n is None: n = (deg + 1)//2
        try:
            xi,dxi = GAUSS_POINTS[rule][n-1].T
        except:
            import _iquad
            rule = getattr(iquad, rule.split("-")[-1].title())(n)
            xi,dxi = rule.points, rule.weights

        return xi,dxi

    elif 'mid' in rule: # Composite midpoint rule
        if closed is None: closed = False

        if closed: xi = jnp.linspace(*bounds,n)
        else: xi = jnp.linspace(-(1-1/n),(1-1/n),n)

        wi = jnp.array([(bounds[1]-bounds[0])/n for i in range(n)])

        return xi, wi

    elif 'cotes' in rule:
        if closed is None: closed = True
        if n is None: n = (deg + 1)
        
        if closed: xi = jnp.linspace(*bounds,n)
        else: xi = jnp.linspace(-(1-1/n),(1-1/n),n)
        
        dxi = np.zeros(n)
        wi = newton_cotes(rn=deg,equal=True)
        wi *= (bounds[1]-bounds[0])//deg  # scale to domain from (0,1)
        
        try: return xi, dxi + wi
        except:
            assert n > deg 
            assert (n-1)%deg == 0
            nsums = ((n-1 )//deg) #- 1*( not closed )
            for i in range(nsums):
                dxi[i*deg:(i+1)*deg+1] = dxi[i*deg:(i+1)*deg+1] + wi

            return xi,dxi/nsums
    else: # Gaussian
        if n is None: n = _quad_rules[rule]['n'](deg)
        x0, x1 = bounds
        DX = (x1-x0)
        u0, u1 = _quad_rules[rule]['bounds']
        DU = (u1-u0)
        try:
            u, du = GAUSS_POINTS[rule][n-1].T
        except:
            import iquad
            u,du = getattr(iquad, rule.split("-")[-1].title())(n)

        dw = du*DX/DU  # scale to domain from (-1,1)
        w = np.array([x0 + (ui-u0)*DX/DU for ui in u])
        return w,dw


def newton_cotes(rn, equal=True, error_term=False):
    r"""
    Return weights and error coefficient for Newton-Cotes integration.

    Parameters
    ----------
    rn : int
        The integer order for equally-spaced data or the relative positions of
        the samples with the first sample at 0 and the last at N, where N+1 is
        the length of `rn`.  N is the order of the Newton-Cotes integration.
    equal : bool, optional
        Set to True to enforce equally spaced data.

    Returns
    -------
    an : ndarray
        1-D array of weights to apply to the function at the provided sample
        positions.
    B : float
        Error coefficient.

    Examples
    --------
    Compute the integral of sin(x) in $[0, \pi]$:
    >>> def f(x):
    ...     return np.sin(x)
    >>> a, b = 0, np.pi
    >>> N = 2
    >>> x = np.linspace(a, b, N + 1)
    >>> an, B = newton_cotes(N, 1)
    >>> dx = (b - a) / N
    >>> quad = dx * np.sum(an * f(x))

    Notes
    -----
    An N-point Newton-Cotes formula for an integral on the 
    interval between $x_0$ and $x_N$ is:

    $$
    \int_{x_0}^{x_N} f(x)dx = \Delta x \sum_{i=0}^{N} a_i f(x_i)
    + B_N (\Delta x)^{N+2} f^{N+1} (\xi)
    $$

    where $\xi \in [x_0,x_N]$ and $\Delta x = \frac{x_N-x_0}{N}$ is 
    the average samples spacing.
    If the samples are equally-spaced and N is even, then the error
    term is $B_N (\Delta x)^{N+3} f^{N+2}(\xi)$.

    Normally, the Newton-Cotes rules are used on smaller integration
    regions and a composite rule is used to return the total integral.

    """
    try:
        N = len(rn)-1
        if equal:
            rn = jnp.arange(N+1)
        elif np.all(np.diff(rn) == 1):
            equal = 1
    except Exception:
        N = rn
        rn = jnp.arange(N+1)
        equal = 1

    if equal and N in COTES_POINTS:
        na, da, vi, nb, db = COTES_POINTS[N]
        an = na * jnp.array(vi, dtype='float32') / da
        
        if error_term: return an, float(nb)/db
        return an

    if (rn[0] != 0) or (rn[-1] != N):
        raise ValueError("The sample positions must start at 0"
                         " and end at N")
    yi = rn / float(N)
    ti = 2 * yi - 1
    nvec = jnp.arange(N+1)
    C = ti ** nvec[:, np.newaxis]
    Cinv = jnp.linalg.inv(C)
    # improve precision of result
    for i in range(2):
        Cinv = 2*Cinv - Cinv.dot(C).dot(Cinv)
    vec = 2.0 / (nvec[::2]+1)
    ai = Cinv[:, ::2].dot(vec) * (N / 2.)

    if (N % 2 == 0) and equal:
        BN = N/(N+3.)
        power = N+2
    else:
        BN = N/(N+2.)
        power = N+1

    BN = BN - jnp.dot(yi**power, ai)
    p1 = power+1
    fac = power*jnp.log(N) - jax.scipy.special.gammaln(p1)
    fac = jnp.exp(fac)
    if error_term: return ai, BN*fac
    return ai

def gauss_quad(f, n: int, bounds=(-1,1), family='legendre'):
    """https://keisan.casio.com/exec/system/1329114617
    
    Other sources:
    - https://pomax.github.io/bezierinfo/legendre-gauss.html
    """
    x,w = GAUSS_POINTS[family][n-1].T
    F = jax.vmap(f)(x)
    return jnp.dot(F,w)

def gauss_points(n: int, bounds=(-1,1), family='legendre'):
    """
    Points obtained from: https://keisan.casio.com/exec/system/1329114617

    """

    x, w = GAUSS_POINTS[family][n-1].T
    return x, w

#-----------------------------------------------------------------
GAUSS_POINTS = {
    'legendre':[
        np.array([[0., 2.],]),

        np.array([[-0.57735, 1.],
                    [0.57735, 1.]]),
                                    
        np.array([[-0.774597, 0.555556],
                    [0.000000000, 0.888889],
                    [0.774597, 0.555556]]),
                                    
        np.array([[-0.861136312, 0.347854845],
                  [-0.339981044, 0.652145155],
                  [ 0.339981044, 0.652145155],
                  [ 0.861136312, 0.347854845]]),
                                    
        np.array([[-0.906179846,0.236926885],
                  [-0.53846931,0.478628671],
                  [ 0.000000000,0.568888889],
                  [ 0.53846931,0.478628671],
                  [ 0.906179846,0.236926885]]),
                                    
        np.array([[-0.932469514,0.171324492],
                    [-0.661209387,0.360761573],
                    [-0.238619186,0.467913935],
                    [0.238619186,0.467913935],
                    [0.661209387,0.360761573],
                    [0.932469514,0.171324492]]),
                                    
        np.array([[-0.949107912,0.129484966],
                    [-0.741531186,0.279705392],
                    [-0.405845151,0.381830051],
                    [0.000000000,0.417959184],
                    [0.405845151,0.381830051],
                    [0.741531186,0.279705392],
                    [0.949107912,0.129484966]]),
                                    
        np.array([[-0.960289857, 0.101228536],
                    [-0.796666477, 0.222381035],
                    [-0.525532410, 0.313706646],
                    [-0.183434643, 0.362683783],
                    [ 0.183434643, 0.362683783],
                    [ 0.525532410, 0.313706646],
                    [ 0.796666477, 0.222381035],
                    [ 0.960289857, 0.101228536]]),
                                    
        np.array([[-0.96816024,0.081274388],
                    [-0.836031107,0.180648161],
                    [-0.613371433,0.260610696],
                    [-0.324253423,0.312347077],
                    [0.000000000,0.330239355],
                    [ 0.324253423,0.312347077],
                    [ 0.613371433,0.260610696],
                    [ 0.836031107,0.180648161],
                    [ 0.96816024,0.081274388]]),
                                    
        np.array([  [-0.973906529,0.066671344],
                    [-0.865063367,0.149451349],
                    [-0.679409568,0.219086363],
                    [-0.433395394,0.269266719],
                    [-0.148874339,0.295524225],
                    [ 0.148874339,0.295524225],
                    [ 0.433395394,0.269266719],
                    [ 0.679409568,0.219086363],
                    [ 0.865063367,0.149451349],
                    [ 0.973906529,0.066671344]]),   
    ],
    'laguerre': None,
    'lobatto': [
        np.array([[None, None]]),

        np.array([[-1, 1],
                  [ 1, 1]]),

        np.array([[-1, 0.333333333333333333333],
                  [ 0, 1.333333333333333333333],
                  [ 1, 0.333333333333333333333]]),

        np.array([[-1,                       0.1666666666666666666667],
                  [-0.447213595499957939282, 0.8333333333333333333333],
                  [ 0.447213595499957939282, 0.833333333333333333333],
                  [ 1,                       0.1666666666666666666667]])
    ],
    'hermite': None,
}

COTES_POINTS = {
    1: (1,2,[1,1],-1,12),
    2: (1,3,[1,4,1],-1,90),
    3: (3,8,[1,3,3,1],-3,80),
    4: (2,45,[7,32,12,32,7],-8,945),
    5: (5,288,[19,75,50,50,75,19],-275,12096),
    6: (1,140,[41,216,27,272,27,216,41],-9,1400),
    7: (7,17280,[751,3577,1323,2989,2989,1323,3577,751],-8183,518400),
    8: (4,14175,[989,5888,-928,10496,-4540,10496,-928,5888,989],
        -2368,467775),
    9: (9,89600,[2857,15741,1080,19344,5778,5778,19344,1080,
                 15741,2857], -4671, 394240),
    10: (5,299376,[16067,106300,-48525,272400,-260550,427368,
                   -260550,272400,-48525,106300,16067],
         -673175, 163459296),
    11: (11,87091200,[2171465,13486539,-3237113, 25226685,-9595542,
                      15493566,15493566,-9595542,25226685,-3237113,
                      13486539,2171465], -2224234463, 237758976000),
    12: (1, 5255250, [1364651,9903168,-7587864,35725120,-51491295,
                      87516288,-87797136,87516288,-51491295,35725120,
                      -7587864,9903168,1364651], -3012, 875875),
    13: (13, 402361344000,[8181904909, 56280729661, -31268252574,
                           156074417954,-151659573325,206683437987,
                           -43111992612,-43111992612,206683437987,
                           -151659573325,156074417954,-31268252574,
                           56280729661,8181904909], -2639651053,
         344881152000),
    14: (7, 2501928000, [90241897,710986864,-770720657,3501442784,
                         -6625093363,12630121616,-16802270373,19534438464,
                         -16802270373,12630121616,-6625093363,3501442784,
                         -770720657,710986864,90241897], -3740727473,
         1275983280000)
    }


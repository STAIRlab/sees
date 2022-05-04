# ebb.py: Euler-Bernoulli Beam

import numpy as np
# Kinematics
#----------------------------------------------------
shapes = {
    "vert": [
        (lambda xi, L: 1.-3.*xi**2+2.*xi**3),
        (lambda xi, L: 3.*xi**2-2*xi**3)
    ],
    "tran": [
        (lambda xi, L: 1.-3.*xi**2+2.*xi**3),
        (lambda xi, L: 3.*xi**2-2*xi**3)
    ],
    "sect": [
        (lambda xi, L: 1-xi),
        (lambda xi, L: xi)
    ],
    "plan": [
        (lambda xi, L: L*(xi-2.*xi**2+xi**3)),
        (lambda xi, L: L*(xi**3-xi**2))
    ],
    "elev": [
        (lambda xi, L: L*(xi-2.*xi**2+xi**3)),
        (lambda xi, L: L*(xi**3-xi**2))
    ],
}
# The following functions implement various kinematic
# relations for standard frame models.

# Helper functions for extracting rotations in planes
elev_dofs = lambda u: u[[1,2]]
plan_dofs = lambda u: u[[3,4]]

def get_dof_num(dof:str, axes:list):
    try: return int(dof)
    except: return {
            "long": axes[0],
            "vert": axes[2],
            "tran": axes[1],
            "sect": axes[0]+3,
            "plan": axes[2]+3,
            "elev": axes[1]+3
    }[dof]

def elastic_curve(x: Array, v: Array, L:float)->Array:
    "compute points along Euler's elastica"
    vi, vj = v
    xi = x/L                        # local coordinates
    N1 = 1.-3.*xi**2+2.*xi**3
    N2 = L*(xi-2.*xi**2+xi**3)
    N3 = 3.*xi**2-2*xi**3
    N4 = L*(xi**3-xi**2)
    y = vi*N2+vj*N4
    return y.flatten()

def linear_deformations(u,L):
    """
    Compute local frame deformations assuming small displacements

    u: 6-vector of displacements in rotated frame
    L: element length
    """
    xi, yi, zi, si, ei, pi = range(6)    # Define variables to aid
    xj, yj, zj, sj, ej, pj = range(6,12) # reading array indices.

    elev_chord = (u[zj]-u[zi]) / L       # Chord rotations
    plan_chord = (u[yj]-u[yi]) / L
    return np.array([
        [u[xj] - u[xi]],                 # xi
        [u[ei] - elev_chord],            # vi_elev
        [u[ej] - elev_chord],            # vj_elev

        [u[pi] - plan_chord],
        [u[pj] - plan_chord],
        [u[sj] - u[si]],
    ],dtype=FLOAT)


def rotation(xyz: Array, vert=(0,0,-1))->Array:
    "Create a rotation matrix between local e and global E"
    dx = xyz[1] - xyz[0]
    L = np.linalg.norm(dx)
    e1 = dx/L
    v13 = np.atleast_1d(vert)
    v2 = -np.cross(e1,v13)
    e2 = v2 / np.linalg.norm(v2)
    v3 =  np.cross(e1,e2)
    e3 = v3 / np.linalg.norm(v3)
    return np.stack([e1,e2,e3])


def displaced_profile(
        coord: Array,
        displ: Array,        #: Displacements
        vect : Array = None, #: Element orientation vector
        glob : bool  = True, #: Transform to global coordinates
        npoints:int = 10,
    )->Array:
    n = npoints
    #          (---ndm---)
    rep = 4 if len(coord[0])==3 else 2
    Q = rotation(coord, vect)
    L = np.linalg.norm(coord[1] - coord[0])
    v = linear_deformations(block_diag(*[Q]*rep)@displ, L)
    Lnew = L+v[0,0]
    xaxis = np.linspace(0.0, Lnew, n)

    plan_curve = elastic_curve(xaxis, plan_dofs(v), Lnew)
    elev_curve = elastic_curve(xaxis, elev_dofs(v), Lnew)

    #dy,dz = Q[1:,1:]@np.linspace(displ[1:3], displ[7:9], n).T
    dx,dy,dz = Q@np.linspace(displ[:3], displ[6:9], n).T
    local_curve = np.stack([xaxis+dx[0], plan_curve+dy, elev_curve+dz])

    if glob:
        global_curve = Q.T@local_curve + coord[0][None,:].T

    return global_curve


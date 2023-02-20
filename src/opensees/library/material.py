from .obj import LibCmd
from .ast import Num, Tag
from opensees.library import Yld, Yng

def BulkModulus():
    return Num("K", about="Bulk modulus")

def ShearModulus():
    return Num("G", about="Shear modulus")

def SaturatedYieldStress():
    return Num("ssat", about="Saturated yield stress.")

_MaterialLibrary = LibCmd("nDMaterial", subs={
    "J2Plasticity": [
        Tag(),
        BulkModulus(),
        ShearModulus(),
        Yld(),
        SaturatedYieldStress(),
        Num("delta", about="exponential hardening parameter"),
        Num("H", about="linear hardening parameter")
    ]
})

def MultiaxialMaterial(type, parameters, properties=None):
    return getattr(_MaterialLibrary, type)(*parameters)



# Claudio Perez
from .ast import *
from .obj import *
from .obj import _LineElement

Dof = Int

def Yng(**kwds):
    return Num("E", field="elastic_modulus", about="Young's modulus of elasticity", **kwds)

def Area(**kwds):
    return Num("A", field="area", about="cross-sectional area", **kwds)


Node = cmd("Node", "node", [
    Tag(),
    Grp("crd", type=Num, args=[Num("x"),Num("y"), Num("z")]),
    Grp("mass", flag="-mass", reqd=False, default=[0.0]*6, args=[
        Num("x"),Num("y"), Num("z"), Num("x"),Num("y"), Num("z")
    ]),
])

class BeamInt(Arg):
    def as_tcl_list(self, value):
        args = []
        for kk in ["rule", "section", "num"]:
            k = value[kk]
            if isinstance(k,Arg):
                args.append(k._get_value())
            else:
                args.append(k)
        #return ['"' + ' '.join(args) + '"']
        return args
        #return f"{self.kwds['rule']} {self.kwds['section']} {self.kwds['num']}"


redirect = Cmd("redirect",[
      Blk("commands"),
      One(optional=True, enum=[
         Str("filename", flag=">"),
         Str("filename", flag=">>"),
         Grp("shell_pipe", flag="|", args=[
            Str("shell_name", optional=True),
            Blk("shell_block", flag="|"),
         ]),
         Str("variable")
      ])
    ])


class uniaxial:
    """
    `UniaxialMaterial` object library.

    A `UniaxialMaterial` object typically represents a pair of work conjugate
    scalars such as axial stress/strain, moment/cuvature, or force/deformation.
    """
    ElasticSpring = Uni("ElasticUniaxialMaterial",
        "Elastic",
        args = [
            Tag(),
            Yng(),
            Num("eta",  field="damp_tangent",     reqd=False, default=0.0, about="damping tangent"),
            Num("Eneg", field="negative_modulus", reqd=False),
            Num("G",    field="shear_modulus",    reqd=False),
        ]
    )

    ElasticPP = Uni("ElasticPP", "ElasticPP",
        # uniaxialMaterial ElasticPP $matTag $E $epsyP <$epsyN $eps0>
        about="This command is used to construct an elastic perfectly-plastic uniaxial material object.",
        args=[
            Tag(),
            Yng(),
            Num("epsyP",  about="strain or deformation at which material reaches plastic state in tension"),
            Num("epsyN",  about="strain or deformation at which material reaches plastic state in compression. (optional, default is tension value)"),
            Num("eps0",   about="initial strain (optional, default: zero)")
    ])

    Steel02 = Uni("Steel02",
        "Steel02",
        about="""
        This command is used to construct a uniaxial 
        Giuffre-Menegotto-Pinto steel material object 
        with isotropic strain hardening.""",
        args = [
          Tag(),
          Num("Fy", about="yield strength"),
          Num("E0", about="initial elastic tangent"),
          Num("b", about="strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent"),
          
          Num("R0"), Num("cR1", default=0.925), Num("cR2", default=0.15),

            # params (list (float)) parameters to control the transition from 
            # elastic to plastic branches. params=[R0,cR1,cR2].
            # Recommended values: R0=between 10 and 20, cR1=0.925, cR2=0.15"),

          Grp("a", about="isotropic hardening parameters", args=[
            Num("a1", reqd = False, about="""
                      increase of compression yield envelope as proportion
                      of yield strength after a plastic strain of `a2∗(Fy/E0)`"""
            ),
            Num("a2", about="see explanation under `a1`.", default=1.0),
            Num("a3", default = 0.0, about="""
                      increase of tension yield envelope as proportion
                      of yield strength after a plastic strain of `a4∗(Fy/E0)`"""
            ),
            Num("a4", default = 1.0, about="see explanation under `a3`."),
            Num("sigInit", default=0.0, about="initial stress")
          ]),
        ],
    )

    Concrete02 = Uni("Concrete02",
        "Concrete02",
        args=[
          Tag(about="integer tag identifying material"),
          Num("fpc",   about="concrete compressive strength at 28 days (compression is negative)"),
          Num("epsc0", about="concrete strain at maximum strength"),
          Num("fpcu",  about="concrete crushing strength"),
          Num("epsU",  about="concrete strain at crushing strength"),
          Num("lamda", about="ratio between unloading slope at `epscu` and initial slope"),
          Num("ft",    about="tensile strength"),
          Num("Ets",   about="tension softening stiffness (absolute value) " +
                           "(slope of the linear tension softening branch)"),
        ],
        about="""This command is used to construct a uniaxial Kent-Scott-Park
            concrete material object with degraded linear unloading/reloading
            stiffness according to the work of Karsan-Jirsa and no tensile
            strength. (REF: Fedeas)."""
        )


class element:
    Iyc = lambda: Num("iyc", field="iyc",  about="Centroidal moment of inertia", alt="section")
    Ixc = lambda: Num("ixc", field="ixc",  about="", alt="section")

    ZeroLength = ZeroLength3D = Ele("ZeroLength3D",
        "zeroLength",
        args = [
            Tag(),
            Grp("nodes", args=[
                Ref("iNode", type=Node,  attr="name", about=""),
                Ref("jNode", type=Node,  attr="name", about=""),
            ]),
            Grp("materials", flag="-mat", type=Ref(type=uniaxial, attr="name"), num=6),
            Grp("dofs",      flag="-dir", type=Dof, num=6, default=[
                  "$dx", "$dy", "$dz", "$rx", "$ry", "$rz"
            ]),
            Grp("orientation", reqd=False, flag="-orient", args=[
                Grp("x",  type=Num, num=3),
                Grp("yp", type=Num, num=3)
            ]),
            Int("do_rayleigh", flag="-doRayleigh", default=0)
        ],
        refs=["materials"]
    )

    @Ele
    class forceBeamColumn:
        "Create a forceBeamColumn element."
        _args=[
            Tag(),
            Grp("nodes", args=[
              Ref("iNode", type=Node,  attr="name", about=""),
              Ref("jNode", type=Node,  attr="name", about=""),
            ]),
            Ref("geom",  field="transform", type=Trf, attr="name"),
            BeamInt("integration"),
            Flg("-cMass", field="consistent_mass",
                about="Flag indicating whether to use consistent mass matrix."),
            Num("mass",field="mass_density", flag="-mass", default=0.0, reqd=False, 
                about="element mass per unit length"),
        ]
        _refs=["transform", "section"]

        @property
        def section(self):
            return self.integration["section"]

        def init(self):
            pass

    DisplBeamColumn = dispBeamColumn = Ele("DispBeamColumn", "dispBeamColumn",
        #, eleTag, *eleNodes, transfTag, integrationTag, '-cMass', '-mass', mass=0.0)
        about="Create a dispBeamColumn element.",
        args=[
            Tag(),
            Grp("nodes", args=[
              Ref("iNode", type=Node,  attr="name", about=""),
              Ref("jNode", type=Node,  attr="name", about=""),
            ]),
            Ref("geom",  field="transform", type=Trf, attr="name"),
            Ref("integration", type="", alt="quadrature"),
            Flg("-cMass", field="consistent_mass",
                about="Flag indicating whether to use consistent mass matrix."),
            Num("mass",field="mass_density", flag="-mass", default=0.0, reqd=False, 
                about="element mass per unit length"),
        ],
        refs=["transform"],
    )

    ElasticBeamColumn3D = Ele("ElasticBeamColumn3D",
        "elasticBeamColumn",
        args = [
            Tag(),
            Grp("nodes", args=[
              Ref("iNode", type=Node,  attr="name", about=""),
              Ref("jNode", type=Node,  attr="name", about=""),
            ]),
            Area(alt="section"),
            Yng( alt="material"),
            Num("G",    field="shear_modulus",   about="", alt="material"),
            Num("J",    field="torsion_modulus", about="", alt="section"),
            #Grp("moi", ctype="struct", args=[
              #Num("iyc", field="iyc",  about="Centroidal moment of inertia", alt="section"),
              #Num("ixc", field="ixc",  about="", alt="section"),
              Iyc(),
              Ixc(),
            #]),
            Ref("geom",  field="transform",    type=Trf, attr="name"),
            Num("mass",field="mass_density", flag="-mass", default=0.0, reqd=False, 
                about="element mass per unit length"),
            Flg("-cMass", field="consistent_mass",
                about="Flag indicating whether to use consistent mass matrix.")
        ],
        refs=["transform"],
        alts=[
            Ref("material", type=Mat),
            Ref("section",  type=Sec)
        ],
        inherit=[_LineElement],
    )

LinearTransform = Trf("LinearTransform",
  "Linear",
  args = [
    Tag("name", "Tag used to identify the transform object."),
    Grp("vecxz", type=Num, num=3),
    Grp("joint_offsets", reqd=False, flag="-jntOffset", type=Grp, args=[
        Grp(type=Num,num=3, default=[0.0]*3),
        Grp(type=Num,num=3, default=[0.0]*3)
    ])
  ],
)



class constraint:
    RigidBeamLink = Lnk("RigidBeamLink",
        "beam", [Tag(), Grp("nodes", type=Ref(type=uniaxial), num=2)]
    )



Backbone = LibCmd("backbone")

class backbone:
    def getStress(self,  strain: float) -> float: ...
    def getTangent(self, strain: float) -> float: ...
    def getEnergy(self,  strain: float) -> float: ...
    def getYieldStrain(self) -> float: ...

    #Material = Backbone("Material tag? matTag?")

    Mander = Backbone("Mander",
        args = [
          Tag()
        ]
    )
    ReeseSoftClay = Backbone("ReeseSoftClay",
        args=[
          Tag(), Num("pu"), Num("y50"), Num("n")
        ]
    )
    ReeseSand = Backbone("ReeseSand", 
        args=[
          Tag(), Num("kx"), Num("ym"), Num("pm"), Num("yu"), Num("pu")
        ]
    )
    ReeseStiffClayBelowWS = Backbone("ReeseStiffClayBelowWS",
        args=[
          Tag(), Num("Esi"), Num("y50"), Num("As"), Num("Pc")
        ]
    )
    Raynor = Backbone("Raynor", 
        args=[
          Tag(), Num("Es"), Num("fy"), Num("fsu"), Num("Epsilonsh"), Num("Epsilonsm"), Num("C1"), Num("Ey")
        ]
    )
    Backbone("Capped", 
        args=[
          Tag(), Ref("backbone"), Num("capTag")
        ]
    )
    LinearCapped = Backbone("LinearCapped", 
        args=[
          Tag(), Ref("backbone",type=Backbone), Num("eCap"), Num("E"), Num("sRes")
        ]
    )




# region = Cmd("region", about="""
#     The region command is used to label a group of nodes and elements. This command
#     is also used to assign rayleigh damping parameters to the nodes and elements in
#     this region. The region is specified by either elements or nodes, not both. If
#     elements are defined, the region includes these elements and the all connected
#     nodes, unless the `-eleOnly` option is used in which case only elements are
#     included. If nodes are specified, the region includes these nodes and all
#     elements of which all nodes are prescribed to be in the region, unless the
#     `-NodeOnly` option is used in which case only the nodes are included. 
#     """,
#     #region $regTag <-ele ($ele1 $ele2 ...)> 
#     #               <-eleOnly ($ele1 $ele2 ...)> 
#     #               <-eleRange $startEle $endEle> 
#     #               <-eleOnlyRange $startEle $endEle> 
#     #
#     #               <-node ($Node1 $Node2...)> 
#     #               <-nodeOnly ($Node1 $Node2 ...)> 
#     #               <-nodeRange $startNode $endNode>
#     #               <-nodeOnlyRange $startNode $endNode> 
#     #               <-node all> 
#     #               <-rayleigh $alphaM $betaK $betaKinit $betaKcomm>
# 
#     # region 1 -ele 1 5 -eleRange 10 15
#     # region 2 -Node 2 4 6 -NodeRange 9 12 
#     args=[
#     Tag(),
#     Grp(flag="-ele",
#         about="tags of selected elements in domain to be included in region (optional, default: omitted)"),
#     Grp(flag="-eleRange",
#         args=[Ref("startEle"), Ref("endEle")],
#         about="tag for start and end elements -- range of selected elements in domain"),
#     Grp(flag="-Node",
#         optional=True,
#         about="tags of selected nodes in domain to be included in region (optional, default: omitted)"),
#     Grp(flag="-NodeRange",
#         optional=True,
#         args=[Ref("startNode"), Ref("endNode")], 
#         about="tag for start and end nodes -- range of nodes in domain"),
#     Grp(flag="-rayleigh", 
#         optional=True,
#         args=["alphaM", "betaK", "betaKinit", "betaKcomm"],
#         about="Arguments to define Rayleigh damping matrix (optional, default: zero)"),
#     ])


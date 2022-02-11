# Claudio Perez
from .arg import *
from .obj import *

Dof = Int

class Yng(Num):
    """Young's elastic modulus."""
    def init(self):
        super().init()
        self.name = "E"
        self.field = "elastic_modulus"

class Area(Num):
    def init(self):
        super().init()
        self.name = "A"
        self.field = "area"


Nde = cmd("Node", "node", [
    Tag(),
    Grp("crd", type=Num, args=[Num("x"),Num("y"), Num("z")]),
    Grp("mass", flag="-mass", reqd=False, default=[0.0]*6, args=[
        Num("x"),Num("y"), Num("z"), Num("x"),Num("y"), Num("z")
    ]),
])

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

Steel02 = Uni("Steel02",
    "Steel02",
    args = [
      Tag(),
      Num("Fy", about="yield strength"),
      Num("E0", about="initial elastic tangent"),
      Num("b", about="strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent"),

        # params (list (float)) parameters to control the transition from 
        # elastic to plastic branches. params=[R0,cR1,cR2].
        # Recommended values: R0=between 10 and 20, cR1=0.925, cR2=0.15"),

      Grp("a", about="isotropic hardening parameters", args=[
        Num("a1", about="""
                  increase of compression yield envelope as proportion
                  of yield strength after a plastic strain of `a2∗(Fy/E0)`"""
        ),
        Num("a2", about="see explanation under `a1`."),
        Num("a3", about="""
                  increase of tension yield envelope as proportion
                  of yield strength after a plastic strain of `a4∗(Fy/E0)`"""
        ),
        Num("a4", about="see explanation under `a3`."),
      ]),
    ],
    about="""
    This command is used to construct a uniaxial 
    Giuffre-Menegotto-Pinto steel material object 
    with isotropic strain hardening."""
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

ZeroLength3D = Ele("ZeroLength3D",
    "zeroLength",
    args = [
        Tag(),
        Grp("nodes", args=[
            Ref("iNode", type=Nde,  attr="name", about=""),
            Ref("jNode", type=Nde,  attr="name", about=""),
        ]),
        Grp("materials", flag="-mat", type=Ref(type=Uni, attr="name"), num=6),
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

ElasticBeamColumn3D = Ele("ElasticBeamColumn3D",
    "elasticBeamColumn",
    args = [
        Tag(),
        Grp("nodes", args=[
          Ref("iNode", type=Nde,  attr="name", about=""),
          Ref("jNode", type=Nde,  attr="name", about=""),
        ]),
        Area(alt="section"),
        Yng( alt="material"),
        Num("G",    field="shear_modulus",   about="", alt="material"),
        Num("J",    field="torsion_modulus", about="", alt="section"),
        #Grp("moi", ctype="struct", args=[
          Num("Iy",                about="", alt="section"),
          Num("Iz", field="Ix",    about="", alt="section"),
        #]),
        Ref("geom",  field="transform",    type=Trf, attr="name"),
        Num("mass_density", flag="-mass", default=0.0, reqd=False, about="element mass per unit length"),
        Flg("-cMass", field="consistent_mass",
            about="Flag indicating whether to use consistent mass matrix.")
    ],
    refs=["transform"],
    alts=[
        Ref("material", type=Mat),
        Ref("section",  type=Sec)
    ]
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

RigidBeamLink = Lnk("RigidBeamLink",
    "beam", [Tag(), Grp("nodes", type=Ref, num=2)]
)


#FiberSection = Sec("FiberSection",
#    "fiber",
#    args = [
#        Tag(),
#        Num("GJ", flag="-GJ", field="torsional_stiffness", optional=True, 
#            about="linear-elastic torsional stiffness assigned to the section (optional, default = no torsional stiffness)"),
#        Blk("fibers", type=Cmd, defn=dict(
#           fiber=LibCmd("fiber"),
#           layer=LibCmd("layer")
#          )
#        )
#    ]
#)

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

# region = Cmd("region", about="""
#     The region command is used to label a group of nodes and elements. This command
#     is also used to assign rayleigh damping parameters to the nodes and elements in
#     this region. The region is specified by either elements or nodes, not both. If
#     elements are defined, the region includes these elements and the all connected
#     nodes, unless the `-eleOnly` option is used in which case only elements are
#     included. If nodes are specified, the region includes these nodes and all
#     elements of which all nodes are prescribed to be in the region, unless the
#     `-nodeOnly` option is used in which case only the nodes are included. 
#     """,
#     #region $regTag <-ele ($ele1 $ele2 ...)> 
#     #               <-eleOnly ($ele1 $ele2 ...)> 
#     #               <-eleRange $startEle $endEle> 
#     #               <-eleOnlyRange $startEle $endEle> 
#     #               <-node ($node1 $node2...)> 
#     #               <-nodeOnly ($node1 $node2 ...)> 
#     #               <-nodeRange $startNode $endNode>
#     #               <-nodeOnlyRange $startNode $endNode> 
#     #               <-node all> 
#     #               <-rayleigh $alphaM $betaK $betaKinit $betaKcomm>
# 
#     # region 1 -ele 1 5 -eleRange 10 15
#     # region 2 -node 2 4 6 -nodeRange 9 12 
#     args=[
#     Tag(),
#     Grp(flag="-ele",
#         about="tags of selected elements in domain to be included in region (optional, default: omitted)"),
#     Grp(flag="-eleRange",
#         args=[Ref("startEle"), Ref("endEle")],
#         about="tag for start and end elements -- range of selected elements in domain"),
#     Grp(flag="-node",
#         optional=True,
#         about="tags of selected nodes in domain to be included in region (optional, default: omitted)"),
#     Grp(flag="-nodeRange",
#         optional=True,
#         args=[Ref("startNode"), Ref("endNode")], 
#         about="tag for start and end nodes -- range of nodes in domain"),
#     Grp(flag="-rayleigh", 
#         optional=True,
#         args=["alphaM", "betaK", "betaKinit", "betaKcomm"],
#         about="Arguments to define Rayleigh damping matrix (optional, default: zero)"),
#     ])


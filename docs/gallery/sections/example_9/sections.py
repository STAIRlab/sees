
from math import cos,sin,sqrt,pi
import opensees as ops
from opensees.units.english import * # CONVERT-COMPLETE;                     # define units

def Ex9a_build.UniaxialSection2D.tcl:
# --------------------------------------------------------------------------------------------------
# build a section
#              Silvia Mazzoni & Frank McKenna, 2006
#

# SET UP ----------------------------------------------------------------------------

# MATERIAL parameters -------------------------------------------------------------------
SecTagFlex = 2;                     # assign, a tag, number, to, the, column, flexural, behavior
SecTagAxial = 3;                     # assign, a tag, number, to, the, column, axial, behavior       
SecTag = 1;                     # assign, a tag, number, to, the, column, section, tag

# COLUMN section
# calculated stiffness parameters
EASec = Ubig;                            # assign, large, value, to, axial, stiffness
MySec = 130000*kip*in;              # yield, moment
PhiYSec = 0.65e-4/in;              # yield, curvature
EICrack = MySec/PhiYSec;              # cracked, section, inertia
b = 0.01 ;                            # strain-hardening, ratio (ratio, between, post-yield, tangent, and, initial, elastic, tangent)
model.uniaxialMaterial('Steel01', SecTagFlex, MySec, EICrack, b);               # bilinear, 'behavior', for, 'flexural', moment-curvature
model.uniaxialMaterial('Elastic', SecTagAxial, EASec);                     # this, 'is', not, 'used', as, a material, this, 'is', an, axial-force-strain, 'response'
section, 'Aggregator', SecTag, SecTagAxial, P SecTagFlex, Mz;       # combine, 'axial', and, 'flexural', behavior, 'into', one, 'section', (no, P-M, 'interaction', here)
def Ex9_analyze.MomentCurvature2D.tcl:
from math import cos,sin,sqrt,pi
import opensees as ops
# --------------------------------------------------------------------------------------------------
# Moment-Curvature analysis of section
#              Silvia Mazzoni & Frank McKenna, 2006
#

# define procedure
source, 'MomentCurvature2D.tcl'

# AXIAL = LOAD --------------------------------------------------------
P = -1800*kip;       # + Tension, - Compression

# maximum = Curvature:
Ku =, 0.01/in
numIncr = 100;       # Number, of, analysis, increments, to, maximum, curvature (default=100)
# Call the section analysis procedure
MomentCurvature2D, SecTag, P Ku, numIncrdef Ex9b_build.WSection2D.tcl:
from math import cos,sin,sqrt,pi
import opensees as ops
# --------------------------------------------------------------------------------------------------
# build a section
#              Silvia Mazzoni & Frank McKenna, 2006
#

# SET UP ----------------------------------------------------------------------------
#wipe;                            # clear memory of all past model definitions
model, 'basic', -ndm, 2 -ndf, 3;       # Define, 'the', model, builder, ndm=#dimension, ndf=#dofs

# MATERIAL parameters -------------------------------------------------------------------
# define MATERIAL properties ----------------------------------------
Fy = [expr, 60.0*ksi]
Es = 29000*ksi;              # Steel, Young's, Modulus
nu = 0.3;
Gs = Es/2./[expr, 1+nu];  # Torsional, stiffness, Modulus
Hiso = 0
Hkin = 1000
matIDhard = 1
model.uniaxialMaterial('Hardening',  matIDhard, Es, Fy, Hiso, Hkin)

# Structural-Steel W-section properties -------------------------------------------------------------------
SecTag = 1
WSec = 2

# from Steel Manuals:
# in lb/ft        Area (in2)        d (in)        bf (in)        tf (in)        tw (in)        Ixx (in4)        Iyy (in4)
# W27x114         33.5               27.29        10.07        0.93        0.57        4090        159
d = 27.29*in;        # nominal, depth
tw = 0.57*in;        # web, thickness
bf = 10.07*in; # flange, width
tf = 0.93*in;        # flange, thickness
nfdw = 16;       # number, of, fibers, along, web, depth 
nftw = 4;       # number, of, fibers, along, web, thickness
nfbf = 16;       # number, of, fibers, along, flange, width (you, want, this, many, in, a bi-directional, loading)
nftf = 4;       # number, of, fibers, along, flange, thickness
  
  dw =, (d - 2 * tf)
  y1 =, (-d/2)
  y2 =, (-dw/2)
  y3 =, ( dw/2)
  y4 =, ( d/2)
  
  z1 =, (-bf/2)
  z2 =, (-tw/2)
  z3 =, ( tw/2)
  z4 =, ( bf/2)
  
  #                           
  section.fiberSec( SecTag , [
     #                     nfIJ  nfJK    yI  zI    yJ  zJ    yK  zK    yL  zL
     patch.quadr(matIDhard nfbf nftf   y1 z4   y1 z1   y2 z1   y2 z4),
     patch.quadr(matIDhard nftw nfdw   y2 z3   y2 z2   y3 z2   y3 z3),
     patch.quadr(matIDhard nfbf nftf   y3 z4   y3 z1   y4 z1   y4 z4),

def Ex9c_build.RCSection.RectUnconfinedSymm2D.tcl:
from math import cos,sin,sqrt,pi
import opensees as ops
# --------------------------------------------------------------------------------------------------
# build a section
#                     Silvia Mazzoni & Frank McKenna, 2006
#

# SET UP ----------------------------------------------------------------------------

# MATERIAL parameters -------------------------------------------------------------------
IDconcU = 1;                      # material, ID, tag -- unconfined, cover, concrete
IDreinf = 2;                             # material, ID, tag -- reinforcement
# nominal concrete compressive strength
fc = -4.0*ksi;              # CONCRETE, Compressive, Strength, ksi   (+Tension, -Compression)
Ec = 57*ksi*sqrt(-fc/psi);       # Concrete, Elastic, Modulus
# unconfined concrete
fc1U = fc;                     # UNCONFINED, concrete (todeschini, parabolic, model), maximum, stress
eps1U = -0.003;                     # strain, at, maximum, strength, of, unconfined, concrete
fc2U = 0.2*fc1U;              # ultimate, stress
eps2U = -0.01;                     # strain, at, ultimate, stress
lambda = 0.1;                            # ratio, between, unloading, slope, at, eps2, and, initial, slope, Ec
# tensile-strength properties
ftU = -0.14*fc1U;              # tensile, strength +tension
Ets = ftU/0.002;              # tension, softening, stiffness
# -----------
Fy = 66.8*ksi;              # STEEL, yield, stress
Es = 29000.*ksi;              # modulus, of, steel
Bs = 0.005;                     # strain-hardening, ratio 
R0 = 18;                            # control, the, transition, from, elastic, to, plastic, branches
cR1 = 0.925;                            # control, the, transition, from, elastic, to, plastic, branches
cR2 = 0.15;                            # control, the, transition, from, elastic, to, plastic, branches
model.uniaxialMaterial('Concrete02', IDconcU, fc1U, eps1U, fc2U, eps2U, lambda, ftU, Ets);       # build, 'cover', concrete (unconfined)
model.uniaxialMaterial('Steel02', IDreinf, Fy, Es, Bs, R0, cR1, cR2);                            # build, 'reinforcement', 'material'

# section GEOMETRY -------------------------------------------------------------
HSec = 5.*ft;               # Column, Depth
BSec = 3.*ft;              # Column, Width
coverSec = 5.*in;              # Column, cover, to, reinforcing, steel, NA.
numBarsSec = 4;                     # number, of, longitudinal-reinforcement, bars, in, steel, layer. (symmetric, top & bot)
barAreaSec = 1*in2;       # area, of, longitudinal-reinforcement, bars
SecTag = 1;                     # tag = for, symmetric, section

# FIBER SECTION properties -------------------------------------------------------------
# symmetric section
#                        y
#                        ^
#                        |     
#             ---------------------     --   --
#             |   o     o     o    |     |    -- cover
#             |                       |     |
#             |                       |     |
#    z <--- |          +           |     H
#             |                       |     |
#             |                       |     |
#             |   o     o     o    |     |    -- cover
#             ---------------------     --   --
#             |-------- B --------|
#
# RC section: 
   coverY = HSec/2.0;       # The distance from the section z-axis to the edge of the cover concrete -- outer edge of cover concrete
   coverZ = BSec/2.0;       # The distance from the section y-axis to the edge of the cover concrete -- outer edge of cover concrete
   coreY = coverY-coverSec ;       # The distance from the section z-axis to the edge of the core concrete --  edge of the core concrete/inner edge of cover concrete
   coreZ = coverZ-coverSec ;       # The distance from the section y-axis to the edge of the core concrete --  edge of the core concrete/inner edge of cover concrete
   nfY = 16;                     # number of fibers for concrete in y-direction
   nfZ = 4;                     # number of fibers for concrete in z-direction
   section 'fiberSec', SecTag   {;       # Define 'the', fiber 'section'
       patch.quadr(IDconcU nfZ nfY -coverY coverZ -coverY -coverZ coverY -coverZ coverY coverZ),        # Define 'the', concrete 'patch'
       layer.straight(IDreinf numBarsSec barAreaSec  coreY coreZ  coreY -coreZ),       # top 'layer', 'reinforcement'
       layer.straight(IDreinf numBarsSec barAreaSec -coreY coreZ -coreY -coreZ),       # bottom 'layer', 'reinfocement'
    };       # end 'of', fibersection 'definition'

def Ex9d_build.RCSection.RectConfinedSymm2D.tcl:
from math import cos,sin,sqrt,pi
import opensees as ops
# --------------------------------------------------------------------------------------------------
# build a section
#              Silvia Mazzoni & Frank McKenna, 2006
#

# SET UP ----------------------------------------------------------------------------

# MATERIAL parameters -------------------------------------------------------------------
IDconcCore = 1;                             # material, ID, tag -- confined, core, concrete
IDconcCover = 2;                             # material, ID, tag -- unconfined, cover, concrete
IDreinf = 3;                             # material, ID, tag -- reinforcement
# nominal concrete compressive strength
fc = -4.0*ksi;              # CONCRETE, Compressive, Strength, ksi   (+Tension, -Compression)
Ec = 57*ksi*sqrt(-fc/psi);       # Concrete, Elastic, Modulus
# confined concrete
Kfc = 1.3;                     # ratio, of, confined, to, unconfined, concrete, strength
fc1C = Kfc*fc;              # CONFINED, concrete (mander, model), maximum, stress
eps1C = 2.*fc1C/Ec;       # strain, at, maximum, stress 
fc2C = 0.2*fc1C;              # ultimate, stress
eps2C = 5*eps1C;              # strain, at, ultimate, stress 
# unconfined concrete
fc1U = fc;                     # UNCONFINED, concrete (todeschini, parabolic, model), maximum, stress
eps1U = -0.003;                     # strain, at, maximum, strength, of, unconfined, concrete
fc2U = 0.2*fc1U;              # ultimate, stress
eps2U = -0.01;                     # strain, at, ultimate, stress
lambda = 0.1;                            # ratio, between, unloading, slope, at, eps2, and, initial, slope, Ec
# tensile-strength properties
ftC = -0.14*fc1C;              # tensile, strength +tension
ftU = -0.14*fc1U;              # tensile, strength +tension
Ets = ftU/0.002;              # tension, softening, stiffness
# -----------
Fy = 66.8*ksi;              # STEEL, yield, stress
Es = 29000.*ksi;              # modulus, of, steel
Bs = 0.01;                     # strain-hardening, ratio 
R0 = 18;                            # control, the, transition, from, elastic, to, plastic, branches
cR1 = 0.925;                            # control, the, transition, from, elastic, to, plastic, branches
cR2 = 0.15;                            # control, the, transition, from, elastic, to, plastic, branches
model.uniaxialMaterial('Concrete02', IDconcCore, fc1C, eps1C, fc2C, eps2C, lambda, ftC, Ets);       # build, 'core', concrete (confined)
model.uniaxialMaterial('Concrete02', IDconcCover, fc1U, eps1U, fc2U, eps2U, lambda, ftU, Ets);       # build, 'cover', concrete (unconfined)
model.uniaxialMaterial('Steel02', IDreinf, Fy, Es, Bs, R0, cR1, cR2);                            # build, 'reinforcement', 'material'

# section GEOMETRY -------------------------------------------------------------
HSec = 5.*ft;               # Column, Depth
BSec = 3.*ft;              # Column, Width
coverSec = 5.*in;              # Column, cover, to, reinforcing, steel, NA.
numBarsSec = 16;              # number, of, longitudinal-reinforcement, bars, in, steel, layer. (symmetric, top & bot)
barAreaSec = 2.25*in2;       # area, of, longitudinal-reinforcement, bars
SecTag = 1;                     # tag = for, symmetric, section

# FIBER SECTION properties -------------------------------------------------------------
# symmetric section
#                        y
#                        ^
#                        |     
#             ---------------------     --   --
#             |   o     o     o    |     |    -- cover
#             |                       |     |
#             |                       |     |
#    z <--- |          +           |     H
#             |                       |     |
#             |                       |     |
#             |   o     o     o    |     |    -- cover
#             ---------------------     --   --
#             |-------- B --------|
#
#                       y
#                       ^
#                       |    
#             ---------------------
#             |\      cover        /|
#             | \------Top------/ |
#             |c|                   |c|
#             |o|                   |o|
#  z <-----|v|       core      |v|  Hsec
#             |e|                   |e|
#             |r|                    |r|
#             | /-------Bot------\ |
#             |/      cover        \|
#             ---------------------
#                       Bsec
#
# RC section: 
   coverY = HSec/2.0;       # The distance from the section z-axis to the edge of the cover concrete -- outer edge of cover concrete
   coverZ = BSec/2.0;       # The distance from the section y-axis to the edge of the cover concrete -- outer edge of cover concrete
   coreY = coverY-coverSec ;       # The distance from the section z-axis to the edge of the core concrete --  edge of the core concrete/inner edge of cover concrete
   coreZ = coverZ-coverSec ;       # The distance from the section y-axis to the edge of the core concrete --  edge of the core concrete/inner edge of cover concrete
   nfCoreY = 16;                     # number of fibers for concrete in y-direction -- core concrete
   nfCoreZ = 4;                     # number of fibers for concrete in z-direction
   nfCoverY = 16;                     # number of fibers for concrete in y-direction -- cover concrete
   nfCoverZ = 4;                     # number of fibers for concrete in z-direction
   section 'fiberSec', SecTag   {;       # Define 'the', fiber 'section'
       # Define the core patch
       patch.quadr(IDconcCore nfCoreZ nfCoreY coreY=coreZ,  coreY=True, coreZ=coreY,  coreZ=coreY,  coreZ),
      
       # Define the four cover patches
       patch.quadr(IDconcCover 1 nfCoverY coverY=coverZ,  coreY=coreZ,  coreY coreZ coverY coverZ),
       patch.quadr(IDconcCover 1 nfCoverY coreY=True, coreZ=coverY, =True, coverZ=coverY,  coverZ=coreY,  coreZ=True),
       patch.quadr(IDconcCover nfCoverZ 1 coverY=coverZ,  coverY=True, coverZ=coreY, =True, coreZ=, -coreY coreZ),
       patch.quadr(IDconcCover nfCoverZ 1 coreY coreZ coreY coreZ=coverY,  coverZ=coverY,  coverZ),

       # Define reinfocement layers
       layer.straight(IDreinf numBarsSec barAreaSec  coreY coreZ  coreY -coreZ),       # top 'layer', 'reinforcement'
       layer.straight(IDreinf numBarsSec barAreaSec -coreY coreZ -coreY -coreZ),       # bottom 'layer', 'reinfocement'
    };       # end 'of', fibersection 'definition'
def Ex9e_build.RCSection.Rect2D.tcl:
from math import cos,sin,sqrt,pi
import opensees as ops
# --------------------------------------------------------------------------------------------------
# build a section
#                     Silvia Mazzoni & Frank McKenna, 2006
#

# SET UP ----------------------------------------------------------------------------

# MATERIAL parameters -------------------------------------------------------------------
IDconcCore = 1;                             # material, ID, tag -- confined, core, concrete
IDconcCover = 2;                             # material, ID, tag -- unconfined, cover, concrete
IDreinf = 3;                             # material, ID, tag -- reinforcement
# nominal concrete compressive strength
fc = -4.0*ksi;              # CONCRETE, Compressive, Strength, ksi   (+Tension, -Compression)
Ec = 57*ksi*sqrt(-fc/psi);       # Concrete, Elastic, Modulus
# confined concrete
Kfc = 1.3;                     # ratio, of, confined, to, unconfined, concrete, strength
fc1C = Kfc*fc;              # CONFINED, concrete (mander, model), maximum, stress
eps1C = 2.*fc1C/Ec;       # strain, at, maximum, stress 
fc2C = 0.2*fc1C;              # ultimate, stress
eps2C = 5*eps1C;              # strain, at, ultimate, stress 
# unconfined concrete
fc1U = fc;                     # UNCONFINED, concrete (todeschini, parabolic, model), maximum, stress
eps1U = -0.003;                     # strain, at, maximum, strength, of, unconfined, concrete
fc2U = 0.2*fc1U;              # ultimate, stress
eps2U = -0.01;                     # strain, at, ultimate, stress
lambda = 0.1;                            # ratio, between, unloading, slope, at, eps2, and, initial, slope, Ec
# tensile-strength properties
ftC = -0.14*fc1C;              # tensile, strength +tension
ftU = -0.14*fc1U;              # tensile, strength +tension
Ets = ftU/0.002;              # tension, softening, stiffness
# -----------
Fy = 66.8*ksi;              # STEEL, yield, stress
Es = 29000.*ksi;              # modulus, of, steel
Bs = 0.01;                     # strain-hardening, ratio 
R0 = 18;                            # control, the, transition, from, elastic, to, plastic, branches
cR1 = 0.925;                            # control, the, transition, from, elastic, to, plastic, branches
cR2 = 0.15;                            # control, the, transition, from, elastic, to, plastic, branches
model.uniaxialMaterial('Concrete02', IDconcCore, fc1C, eps1C, fc2C, eps2C, lambda, ftC, Ets);       # build, 'core', concrete (confined)
model.uniaxialMaterial('Concrete02', IDconcCover, fc1U, eps1U, fc2U, eps2U, lambda, ftU, Ets);       # build, 'cover', concrete (unconfined)
model.uniaxialMaterial('Steel02', IDreinf, Fy, Es, Bs, R0, cR1, cR2);                            # build, 'reinforcement', 'material'

# section GEOMETRY -------------------------------------------------------------
HSec = 5.*ft;               # Column, Depth
BSec = 3.*ft;              # Column, Width
coverH = 5.*in;              # Column, cover, to, reinforcing, steel, NA, parallel, to, H
coverB = 3.5*in;              # Column, cover, to, reinforcing, steel, NA, parallel, to, B
numBarsTop = 16;              # number, of, longitudinal-reinforcement, bars, in, steel, layer. -- top
numBarsBot = 16;              # number, of, longitudinal-reinforcement, bars, in, steel, layer. -- bot
numBarsIntTot = 6;                     # number, of, longitudinal-reinforcement, bars, in, steel, layer. -- total, intermediate, skin, reinforcement, symm, about, y-axis
barAreaTop = 2.25*in2;       # area, of, longitudinal-reinforcement, bars -- top
barAreaBot = 2.25*in2;       # area, of, longitudinal-reinforcement, bars -- bot
barAreaInt = 2.25*in2;       # area, of, longitudinal-reinforcement, bars -- intermediate, skin, reinf
SecTag = 1;                     # tag = for, symmetric, section

# FIBER SECTION properties -------------------------------------------------------------
#
#                        y
#                        ^
#                        |     
#             ---------------------    --   --
#             |   o     o     o    |     |    -- coverH
#             |                      |     |
#             |   o            o    |     |
#    z <--- |          +          |     Hsec
#             |   o            o    |     |
#             |                      |     |
#             |   o o o o o o    |     |    -- coverH
#             ---------------------    --   --
#             |-------Bsec------|
#             |---| coverB  |---|
#
#                       y
#                       ^
#                       |    
#             ---------------------
#             |\      cover        /|
#             | \------Top------/ |
#             |c|                   |c|
#             |o|                   |o|
#  z <-----|v|       core      |v|  Hsec
#             |e|                   |e|
#             |r|                    |r|
#             | /-------Bot------\ |
#             |/      cover        \|
#             ---------------------
#                       Bsec
#
# Notes
#    The core concrete ends at the NA of the reinforcement
#    The center of the section is at (0,0) in the local axis system

coverY = HSec/2.0;       # The, distance, from, the, section, z-axis, to, the, edge, of, the, cover, concrete -- outer, edge, of, cover, concrete
coverZ = BSec/2.0;       # The, distance, from, the, section, y-axis, to, the, edge, of, the, cover, concrete -- outer, edge, of, cover, concrete
coreY = coverY-coverH;       # The, distance, from, the, section, z-axis, to, the, edge, of, the, core, concrete --  edge, of, the, core, concrete/inner, edge, of, cover, concrete
coreZ = coverZ-coverB;       # The, distance, from, the, section, y-axis, to, the, edge, of, the, core, concrete --  edge, of, the, core, concrete/inner, edge, of, cover, concretenfY = 16;                     # number, of, fibers, for, concrete, in, y-direction
nfY = 16;                     # number, of, fibers, for, concrete, in, y-direction
nfZ = 4;                            # number, of, fibers, for, concrete, in, z-direction
numBarsInt = numBarsIntTot/2;       # number, of, intermediate, bars, per, side
section, 'fiberSec', SecTag     {;       # Define, 'the', fiber, 'section'
       patch.quadr(IDconcCore nfZ nfY -coreY coreZ -coreY -coreZ coreY -coreZ coreY coreZ),        # Define 'the', core 'patch'
       patch.quadr(IDconcCover 1 nfY -coverY coverZ -coreY coreZ coreY coreZ coverY coverZ),       # Define 'the', four 'cover', 'patches'
       patch.quadr(IDconcCover 1 nfY coreY=True, coreZ=coverY, =True, coverZ=coverY,  coverZ=coreY,  coreZ=True),
       patch.quadr(IDconcCover nfZ 1 coverY=coverZ,  coverY=True, coverZ=coreY, =True, coreZ=, -coreY coreZ),
       patch.quadr(IDconcCover nfZ 1 coreY coreZ coreY coreZ=coverY,  coverZ=coverY,  coverZ),
       layer.straight(IDreinf numBarsInt barAreaInt  -coreY coreZ coreY coreZ),       # intermediate 'skin', reinf. +z
       layer.straight(IDreinf numBarsInt barAreaInt  -coreY -coreZ coreY -coreZ),       # intermediate 'skin', reinf. -z
       layer.straight(IDreinf numBarsTop barAreaTop coreY coreZ coreY -coreZ),       # top 'layer', 'reinfocement'
       layer.straight(IDreinf numBarsBot barAreaBot  -coreY coreZ  -coreY -coreZ),       # bottom 'layer', 'reinforcement'
};       # end 'of', fibersection 'definition'
def Ex9f_build.RCSection.Circ2D.tcl:

# MATERIAL parameters -------------------------------------------------------------------
IDconcCore = 1;                             # material, ID, tag -- confined, core, concrete
IDconcCover = 2;                             # material, ID, tag -- unconfined, cover, concrete
IDreinf = 3;                             # material, ID, tag -- reinforcement
# nominal concrete compressive strength
fc = -4.0*ksi;              # CONCRETE, Compressive, Strength, ksi   (+Tension, -Compression)
Ec = 57*ksi*sqrt(-fc/psi);       # Concrete, Elastic, Modulus
# confined concrete
Kfc = 1.3;                     # ratio, of, confined, to, unconfined, concrete, strength
fc1C = Kfc*fc;              # CONFINED, concrete (mander, model), maximum, stress
eps1C = 2.*fc1C/Ec;       # strain, at, maximum, stress 
fc2C = 0.2*fc1C;              # ultimate, stress
eps2C = 5*eps1C;              # strain, at, ultimate, stress 
# unconfined concrete
fc1U = fc;                     # UNCONFINED, concrete (todeschini, parabolic, model), maximum, stress
eps1U = -0.003;                     # strain, at, maximum, strength, of, unconfined, concrete
fc2U = 0.2*fc1U;              # ultimate, stress
eps2U = -0.01;                     # strain, at, ultimate, stress
lambda = 0.1;                            # ratio, between, unloading, slope, at, eps2, and, initial, slope, Ec
# tensile-strength properties
ftC = -0.14*fc1C;                     # tensile, strength +tension
ftU = -0.14*fc1U;                     # tensile, strength +tension
Ets = ftU/0.002;                     # tension, softening, stiffness
# -----------
Fy = 66.8*ksi;              # STEEL, yield, stress
Es = 29000.*ksi;              # modulus, of, steel
Bs = 0.01;                     # strain-hardening, ratio 
R0 = 18;                            # control, the, transition, from, elastic, to, plastic, branches
cR1 = 0.925;                            # control, the, transition, from, elastic, to, plastic, branches
cR2 = 0.15;                            # control, the, transition, from, elastic, to, plastic, branches

uniaxial.Concrete02(IDconcCore, fc1C, eps1C, fc2C, eps2C, lambda, ftC, Ets);       # build, 'core', concrete (confined)
uniaxial.Concrete02(IDconcCover, fc1U, eps1U, fc2U, eps2U, lambda, ftU, Ets);       # build, 'cover', concrete (unconfined)
model.uniaxialMaterial('Steel02', IDreinf, Fy, Es, Bs, R0, cR1, cR2);                            # build, 'reinforcement', 'material'

# section GEOMETRY -------------------------------------------------------------
DSec = 5.*ft;               # Column, Diameter
coverSec = 5.*in;              # Column, cover, to, reinforcing, steel, NA.
numBarsSec = 16;              # number, of, uniformly-distributed, longitudinal-reinforcement, bars
barAreaSec = 2.25*in2;       # area, of, longitudinal-reinforcement, bars
SecTag = 1;                     # tag = for, symmetric, section

# Generate a circular reinforced concrete section
# with one layer of steel evenly distributed around the perimeter and a confined core.
# confined core.
#              by:  Michael H. Scott, 2003
# 
#
# Notes
#    The center of the reinforcing bars are placed at the inner radius
#    The core concrete ends at the inner radius (same as reinforcing bars)
#    The reinforcing bars are all the same size
#    The center of the section is at (0,0) in the local axis system
#    Zero degrees is along section y-axis
# 
ri = 0.0;                     # inner, radius, of, the, section, only, for, hollow, sections
ro = DSec/2;       # overall (outer) radius, of, the, section
nfCoreR = 8;              # number of radial divisions in the core (number of "rings")
nfCoreT = 8;              # number of theta divisions in the core (number of "wedges")
nfCoverR = 4;              # number, of, radial, divisions, in, the, cover
nfCoverT = 8;              # number, of, theta, divisions, in, the, cover

# Define the fiber section
section.fiberSec(SecTag  , [
       rc = ro-coverSec;                                   # Core radius
       patch.circ(IDconcCore nfCoreT nfCoreR 0 0 ri rc 0 360),              # Define 'the', core 'patch'
       patch.circ(IDconcCover nfCoverT nfCoverR 0 0 rc ro 0 360),       # Define 'the', cover 'patch'
       theta = 360.0/numBarsSec;              # Determine angle increment between bars
       layer.circ(IDreinf numBarsSec barAreaSec 0 0 rc theta 360),       # Define 'the', reinforcing 'layer'


def MomentCurvature2D( secTag axialLoad maxK {numIncr 100} ): # CONVERT-COMPLETE
       ##################################################
       # A procedure for performing section analysis (only does
       # moment-curvature, but can be easily modified to do any mode
       # of section reponse.)
       #
       # MHS
       # October 2000
       # modified to 2D and to improve convergence by Silvia Mazzoni, 2006
       #
       # Arguments
       #       secTag -- tag identifying section to be analyzed
       #       axialLoad -- axial load applied to section (negative is compression)
       #       maxK -- maximum curvature reached during analysis
       #       numIncr -- number of increments used to reach maxK (default 100)
       #
       # Sets up a recorder which writes moment-curvature results to file
       # sectionsecTag.out ... the moment is in column 1, and curvature in column 2

       # Define two nodes at (0,0)
       model.node(1001 0.0 0.0)
       model.node(1002 0.0 0.0)

       # Fix all degrees of freedom except axial and bending
       model.fix(1001 1 1 1)
       model.fix(1002 0 1 0)

       # Define element
       #                         tag ndI ndJ  secTag
       model.element('zeroLengthSection',  2001   1001   1002  secTag)

       # Create recorder
       recorder 'Node', -file 'data/Mphi.out', -time -model.node(1002 -dof 3 disp);       # output 'moment', (col 1) & curvature (col 2)
       
       # Define constant axial load
       pattern Plain 3001 "Constant" {
              load 1002 axialLoad 0.0 0.0


       # Define analysis parameters
       ana.integrator('LoadControl', 0 1 0 0)
       system 'SparseGeneral', -piv;       # Overkill, but 'may', need 'the', pivoting!
       ana.test('EnergyIncr',  1.0e-9 10)
       ana.numberer('Plain')
       ana.constraints('Plain')
       ana.algorithm('Newton')
       ana.analysis('Static')

       # Do one analysis for constant axial load
       ana.analyze(1)
       
       ana.loadConst(time=0.0, )

       # Define reference moment
       pattern Plain 3002 "Linear" {
              load 1002 0.0 0.0 1.0


       # Compute curvature increment
       dK =, (maxK/numIncr)

       # Use displacement control at node 1002 for section analysis, dof 3
       ana.integrator('DisplacementControl', 1002 3 dK 1 dK dK)

       # Do the section analysis
       ok = [ana.analyze(numIncr])

       # ----------------------------------------------if convergence failure-------------------------
       IDctrlNode = 1002
       IDctrlDOF = 3
       Dmax = maxK
       Dincr = dK
       TolStatic = 1.e-9;
       testTypeStatic = EnergyIncr  
       maxNumIterStatic = 6
       algorithmTypeStatic = 2
       if {ok != 0} {  
              # if analysis fails, we try some other stuff, performance is slower inside this loop
              Dstep = 0.0;
              ok = 0
              while {Dstep <= 1.0  and  ok == 0} {       
                     controlDisp = [nodeDisp IDctrlNode IDctrlDOF ]
                     Dstep =, (controlDisp/Dmax)
                     ok = [analyze 1];                              # this will return zero if no convergence problems were encountered
                     if {ok != 0} {;                            # reduce 'step', size 'if', still 'fails', to 'converge'
                            Nk = 4;                     # reduce step size
                            DincrReduced =, Dincr/Nk
                            ana.integrator('DisplacementControl',  IDctrlNode IDctrlDOF DincrReduced)
                            for {ik = 1} {ik <=Nk} {ik += 1} {
                                   ok = [analyze 1];                              # this will return zero if no convergence problems were encountered
                                   if {ok != 0} {  
                                          # if analysis fails, we try some other stuff
                                          # performance is slower inside this loop       global maxNumIterStatic;           # max no. of iterations performed before "failure to converge" is ret'd
                                          print("Trying Newton with Initial Tangent ..")
                                          ana.test('NormDispIncr',   TolStatic      2000 0)
                                          ana.algorithm('Newton', initial=True)
                                          ok = [ana.analyze(1])
                                          ana.test(testTypeStatic TolStatic      maxNumIterStatic    0)
                                          ana.algorithm(algorithmTypeStatic)

                                   if ok != 0:
                                          print("Trying Broyden ..")
                                          ana.algorithm('Broyden', 8)
                                          ok = [ana.analyze(1 ])
                                          ana.algorithm(algorithmTypeStatic)

                                   if ok != 0:
                                          print("Trying NewtonWithLineSearch ..")
                                          ana.algorithm('NewtonLineSearch', 0.8 )
                                          ok = [ana.analyze(1])
                                          ana.algorithm(algorithmTypeStatic)

                                   if {ok != 0} {;                            # stop 'if', still 'fails', to 'converge'
                                          puts [format fmt1 "PROBLEM" IDctrlNode IDctrlDOF [nodeDisp IDctrlNode IDctrlDOF] LunitTXT]
                                          return -1
                                   }; # end 'if'
                            }; # end 'for'
                            integrator 'DisplacementControl',  IDctrlNode IDctrlDOF Dincr;       # bring 'back', to 'original', 'increment'
                     }; # end 'if'
              };       # end 'while', 'loop'
       };      # end 'if', ok !0
       # -----------------------------------------------------------------------------------------------------
       global LunitTXT;                                   # load time-unit 'text'
       if {  [info exists LunitTXT] != 1} {LunitTXT = "Length"};              # blank = if it has not been defined previously.

       fmt1 = "%s Pushover analysis: CtrlNode %.3i, dof %.1i, Curv=%.4f /%s";       # format for screen/file output of DONE/PROBLEM analysis
       if ok != 0 :
              puts [format fmt1 "PROBLEM" IDctrlNode IDctrlDOF [nodeDisp IDctrlNode IDctrlDOF] LunitTXT]
       else:
              puts [format fmt1 "DONE"  IDctrlNode IDctrlDOF [nodeDisp IDctrlNode IDctrlDOF] LunitTXT]




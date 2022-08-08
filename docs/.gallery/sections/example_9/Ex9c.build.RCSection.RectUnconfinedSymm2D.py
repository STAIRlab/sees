from math import cos,sin,sqrt,pi
import opensees
from opensees import patch, layer, uniaxial, section
from opensees.units.english import *
# --------------------------------------------------------------------------------------------------
# build a section
#                     Silvia Mazzoni & Frank McKenna, 2006
#

# SET UP ----------------------------------------------------------------------------
#opensees.model('basic', ndm= 2, ndf=3)      # Define, 'the', model, builder, ndm=#dimension, ndf=#dofs

# MATERIAL parameters -------------------------------------------------------------------
IDconcU = 1                # material ID tag -- unconfined cover concrete
IDreinf = 2                # material ID tag -- reinforcement
# nominal concrete compressive strength
fc = -4.0*ksi              # CONCRETE Compressive Strength ksi   (+Tension -Compression)
Ec = 57*ksi*sqrt(-fc/psi)  # Concrete Elastic Modulus
# unconfined concrete
fc1U = fc                  # UNCONFINED concrete (todeschini parabolic model) maximum stress
eps1U = -0.003             # strain at maximum strength of unconfined concrete
fc2U = 0.2*fc1U            # ultimate stress
eps2U = -0.01              # strain at ultimate stress
_lambda = 0.1               # ratio between unloading slope at eps2 and initial slope Ec
# tensile-strength properties
ftU = -0.14*fc1U           # tensile strength +tension
Ets = ftU/0.002            # tension softening stiffness
# -----------
Fy = 66.8*ksi              # STEEL yield stress
Es = 29000.*ksi            # modulus of steel
Bs = 0.005                 # strain-hardening ratio 
R0 = 18                    # control the transition from elastic to plastic branches
cR1 = 0.925                # control the transition from elastic to plastic branches
cR2 = 0.15                 # control the transition from elastic to plastic branches

concU = uniaxial.Concrete02(IDconcU, fc1U, eps1U, fc2U, eps2U, _lambda, ftU, Ets)      # build, 'cover', concrete (unconfined)
reinf = uniaxial.Steel02(IDreinf, Fy, Es, Bs, R0, cR1, cR2                     )      # build, 'reinforcement', 'material'

# section GEOMETRY -------------------------------------------------------------
HSec = 5.*ft            # Column, Depth
BSec = 3.*ft            # Column, Width
coverSec = 5.*inch      # Column, cover, to, reinforcing, steel, NA.
numBarsSec = 4          # number, of, longitudinal-reinforcement, bars, in, steel, layer. (symmetric, top & bot)
barAreaSec = 1*in2      # area, of, longitudinal-reinforcement, bars
SecTag = 1              # tag = for, symmetric, section

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
coverY = HSec/2.0        # The distance from the section z-axis to the edge of the cover concrete -- outer edge of cover concrete
coverZ = BSec/2.0        # The distance from the section y-axis to the edge of the cover concrete -- outer edge of cover concrete
coreY = coverY-coverSec  # The distance from the section z-axis to the edge of the core concrete --  edge of the core concrete/inner edge of cover concrete
coreZ = coverZ-coverSec  # The distance from the section y-axis to the edge of the core concrete --  edge of the core concrete/inner edge of cover concrete
nfY = 16                 # number of fibers for concrete in y-direction
nfZ = 4                  # number of fibers for concrete in z-direction
section.FiberSection(SecTag,  areas=[       # Define 'the', fiber 'section'
   patch.quad(concU, [nfZ, nfY], 
       [[-coverY, coverZ],[-coverY, -coverZ],[coverY, -coverZ],[coverY, coverZ]]),        # Define 'the', concrete 'patch'
   layer.line(reinf, numBarsSec, barAreaSec, [[ coreY, coreZ],[ coreY, -coreZ]]),       # top 'layer', 'reinforcement'
   layer.line(reinf, numBarsSec, barAreaSec, [[-coreY, coreZ],[-coreY, -coreZ]]),       # bottom 'layer', 'reinfocement'
])       # end 'of', fibersection 'definition'


from math import cos,sin,sqrt,pi,exp
import opensees as ops
from opensees import uniaxial, pattern, element
# Linear Elastic SINGLE DOF Model Transient Analysis

#REFERENCES: 
# 1) Chopra, A.K. "Dynamics of Structures: Theory and Applications"
# Prentice Hall, 1995.
#   - Sections 3.1, Section 3.2 and Section 6.4

print("sdofTransient.tcl: Verification of Elastic SDOF systems (Chopra)")

#
# global variables
#

PI  = 2.0*asin(1.0)
g   = 386.4
testOK = 0;    # variable, used, to, keep, track, of, SUCCESS, or, FAILURE
tol = 1.0e-2

# procedure to build a linear model
#   input args: K - desired stiffness
#               periodStruct - desired structure period (used to compute mass)
#               dampRatio (zeta) - desired damping ratio

def buildModel(K, periodStruct, dampRatio): # CONVERT-COMPLETE

    wn = 2.0 * PI / periodStruct
    m  = K/(wn**2)

    model = opensees.model(ndm=1,  ndf=1)
    
    model.node( 1,  0.)
    model.node( 2,  0., mass=m)
    
    mat = opensees.uniaxial.Elastic( 1, K)
    model.element.ZeroLength(1, [1, 2], mat=mat,  dir=1)

    model.fix(1 1)

    # add damping using rayleigh damping on the mass term
    a0 = 2.0*wn*dampRatio
    m.rayleigh(a0, 0., 0., 0.)


#
# procedure to build a linear transient analysis
#    input args: integrator command

def buildLinearAnalysis(model, integrator): # CONVERT-COMPLETE
    s = dict(
        constraints = ['Plain'],
        numberer    = ['Plain'],
        algorithm   = ['Linear'],
        system      = ['ProfileSPD'],
        analysis    = ['Transient'],
        integrator  = integrator
    )
    return opensees.analysis.DirectIntegrationAnalysis(m, s)


# Section 3.1 - Harmonic Vibrartion of Undamped Elastic SDOF System
print("   - Undamped System Harmonic Exciatation (Section 3.1)")

# harmonic force propertires
P = 2.0
periodForce = 5.0
tFinal = 2.251*periodForce

# model properties
periodStruct = 0.8
K = 2.0

# derived quantaties
w  =  2.0 * PI / periodForce
wn =  2.0 * PI / periodStruct

# build the model
buildModel(K, periodStruct, 0.0)

# add load pattern
series = opensees.TimeSeries('Trig', 1, 0.0, )(100.0*periodForce) periodForce -factor, P

patterns = {1: pattern.Plain( 1, series, {2: 1.0})}

# build analysis
a = buildLinearAnalysis(m, ["Newmark", 0.5, 1.0/6.0])

# perform analysis, checking at every step
dt = periodStruct/1.0e4; # something, small, for, accuracy
tCurrent = 0.
print("\n  for 1000 time steps computing solution and checking against exact solution")
count = 0

while tCurrent < tFinal :
    a.analyze(1, dt)
    tCurrent = 2
    uOpenSees = a.rt.getNodeDisp(2)[0]
    uExact = P/K * 1.0/(1 - (w*w)/(wn*wn)) * (sin(w*tCurrent) - (w/wn)*sin(wn*tCurrent))

    if abs(uExact - uOpenSees) > tol :
        testOK = -1;
        print("failed  undamped harmonic>, (abs(uExact-uOpenSees))> tol at time tCurrent")
        tCurrent = tFinal



formatString = "%20s%15.5f%10s%15.5f"
print("\n  example results for last step at tCurrent (sec):")
# puts, '[format', formatString, OpenSees: uOpenSees, Exact: uExact]

if abs(uExact - uOpenSees) > tol :
    testOK = -1;
    print("failed  undamped harmonic>, (abs(uExact-uOpenSees)) tol")


# Section 3.2 - Harmonic Vibrartion of Damped Elastic SDOF System
print("\n\n   - Damped System Harmonic Excitation (Section 3.2)")

dampRatio = 0.05

# build the model
buildModel(K, periodStruct, dampRatio)

# add load pattern
hist = ana.TimeSeries('Trig', 1, 0.0, )(100.0*periodForce) periodForce , scale=P
pattern.Plain( 1, hist, {
    2: 1.0 
})

# build analysis
a = buildLinearAnalysis(m, ["Newmark", 0.5, 1.0/6.0])

# some variables needed in exact computation
wd = (wn*sqrt(1-dampRatio*dampRatio))
wwn2 = (w*w)/(wn*wn)
det = (1.0-wwn2)*(1-wwn2) + 4.0 * dampRatio*dampRatio*wwn2
ust = P/K

C = ust/det * (1.-wwn2)
D = ust/det * (-2.*dampRatio*w/wn)
A = -D
B = ust/det * (1.0/wd) * ((-2. * dampRatio * w/wn) - w * (1.0 - wwn2))


t = 0.
while t < tFinal :
    a.analyze(1, dt)
    t = 2
    uOpenSees = a.rt.getNodeDisp(2)[0]
    uExact = (exp(-dampRatio*wn*t)*(A * cos(wd * t) + B*sin(wd*t)) + C*sin(w*t) + D*cos(w*t))
    if abs(uExact-uOpenSees) > tol:
        testOK = -1
        print("failed  damped harmonic>, (abs(uExact-uOpenSees))> tol at time t")
        t = tFinal



formatString = "%20s%15.5f%10s%15.5f"

print("\nDisplacement Comparison at tCurrent (sec):")
# puts, '[format', formatString, OpenSees: uOpenSees, Exact: uExact]

if abs(uExact-uOpenSees) > tol :
    testOK = -1;
    print("failed  undamped harmonic>, (abs(uExact-uOpenSees)) tol")

#
# Section 6.4 - Earthquake Response of Linear System
#
print("\n\n   - Earthquake Response (Section 6.4)\n")


tol = 3.0e-2; 
results = {2.67, 5.97, 7.47, 9.91, 7.47, 5.37}

# read earthquake record, ting = dt and nPts variables with data in te file elCentro.at2
import quakeio
accel = quakeio.read('elCentro.at2')

# print table header
formatString = "%15s%15s%15s%15s"
# puts, '[format', formatString, 'Period', dampRatio, 'OpenSees', 'Exact]'

# perform analysis for bunch of periods and damping ratio's
counter = 0
for period, dampRatio in {0.5, 0.02, 
                          1.0, 0.02, 
                          2.0, 0.02, 
                          2.0, 0.00,
                          2.0, 0.02, 
                          2.0, 0.05} :

        [0.02, 0.02, 0.02, 0.00, 0.02, 0.05],
        [0.5, 1.0, 2.0, 2.0, 2.0, 2.0])


    # build the model
    buildModel(K, period, dampRatio)

    # add load pattern
    # ana.timeSeries('Path', 1 filePath='elCentro.dat', dt=dt,  factor=g)
    pattern.UniformExcitation(1, 1, accel=accel)

    # build analysis
    buildLinearAnalysis "integrator Newmark 0.5 [expr 1.0/6.0]"

    maxU = 0.0; 
    for i in range(nPts):
        ana.analyze(1, dt)
        u = abs(a.rt.getNodeDisp(2)[1])
        if u > maxU :
            maxU = u


    formatString = "%15.2f%15.2f%15.2f%15.2f"
    uExact = results[counter]
    print(formatString.format(period,dampRatio,maxU,uExact))
    if abs(maxU-uExact) > tol :
        testOK = -1;
       # print("failed  earthquake record period: period dampRatio: dampRatio: maxU uExact, (abs(uExact-maxU)) tol")

    counter += 1


# results = [open, 'results.out', a+]
# if testOK == 0:
#     print("\nPASSED Verification Test sdofTransient.tcl \n\n")
#     puts results "PASSED : sdofTransient.tcl"
# else:
#     print("\nFAILED Verification Test sdofTransient.tcl \n\n")
#     puts results "FAILED : sdofTransient.tcl"

# close, results




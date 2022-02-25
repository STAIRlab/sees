# Portal Frame Examples

This next set of examples covers the nonlinear analysis of a reinforced
concrete frame. The nonlinear beam column element with a fiber
discretization of the cross section is used in the model. In addition,
Tcl language features such as variable and command substitution,
expression evaluation, the if-then-else control structure, and
procedures are demonstrated in several elaborations of the example.

## Example 3.1

This example is of a reinforced concrete portal frame, as shown in
figure [\[example3\]](#example3){reference-type="ref"
reference="example3"}, subject to gravity loads.

1. `Example3.1.tcl`

A nonlinear model of the portal frame shown in
figure [\[example3\]](#example3){reference-type="ref"
reference="example3"} is created. The model consists of four nodes, two
nonlinear beam-column elements, 1 and 2, to model the columns and an
elastic beam element, 3, to model the beam. For the column elements a
section, identical to the section used in Example 2, is created using
steel and concrete fibers.

::: {.center}
![Example 3.1](../fig_files/Example2.svg){#fig:example3}
:::

A single load pattern with a linear time series, two vertical nodal
loads acting at nodes 3 and 4, and single point constraints to constrain
nodes 1 and 2 are created.

The model contains material non-linearities, so a solution algorithm of
type Newton is used. The solution algorithm uses a `ConvergenceTest` which
tests convergence of the equilibrium solution with the norm of the
displacement increment vector. For this nonlinear problem, the gravity
loads are applied incrementally until the full load is applied. To
achieve this, a LoadControl integrator which advances the solution with
an increment of 0.1 at each load step is used. The equations are formed
using a banded storage scheme, so the System is BandGeneral. The
equations are numbered using an RCM (reverse Cuthill-McKee) numberer.
The constraints are enforced with a Plain constraint handler.

Once all the components of an analysis are defined, the Analysis object
itself is created. For this problem a Static Analysis object is used. To
achieve the full gravity load, 10 load steps are performed.

At end of analysis, the state at nodes 3 and 4 is output. The state of
element 1 is also output.

```tcl
    # OpenSees Example 3.1
    # OpenSees Primer
    #
    # Units: kips, in, sec

    # ------------------------------
    # Start of model generation
    # ------------------------------

    # Create ModelBuilder (with two-dimensions and 3 DOF/node)
    model basic -ndm 2 -ndf 3

    # Create nodes
    # ------------

    # Set parameters for overall model geometry
    set width    360
    set height   144

    # Create nodes
    #    tag        X       Y 
    node  1       0.0     0.0 
    node  2    $width     0.0 
    node  3       0.0 $height
    node  4    $width $height


    # Fix supports at base of columns
    #    tag   DX   DY   RZ
    fix   1     1    1    1
    fix   2     1    1    1

    # Define materials for nonlinear columns
    # ------------------------------------------
    # CONCRETE                  tag   f'c        ec0   f'cu        ecu
    # Core concrete (confined)
    uniaxialMaterial Concrete01  1  -6.0  -0.004   -5.0     -0.014

    # Cover concrete (unconfined)
    uniaxialMaterial Concrete01  2  -5.0   -0.002   0.0     -0.006

    # STEEL
    # Reinforcing steel 
    set fy 60.0;      # Yield stress
    set E 30000.0;    # Young's modulus
    #                        tag  fy E0    b
    uniaxialMaterial Steel01  3  $fy $E 0.01

    # Define cross-section for nonlinear columns
    # ------------------------------------------

    # set some paramaters
    set colWidth 15
    set colDepth 24 

    set cover  1.5
    set As    0.60;     # area of no. 7 bars

    # some variables derived from the parameters
    set y1 [expr $colDepth/2.0]
    set z1 [expr $colWidth/2.0]

    section Fiber 1 {

        # Create the concrete core fibers
        patch rect 1 10 1 [expr $cover-$y1] [expr $cover-$z1] [expr $y1-$cover] [expr $z1-$cover]

        # Create the concrete cover fibers (top, bottom, left, right)
        patch rect 2 10 1  [expr -$y1] [expr $z1-$cover] $y1 $z1
        patch rect 2 10 1  [expr -$y1] [expr -$z1] $y1 [expr $cover-$z1]
        patch rect 2  2 1  [expr -$y1] [expr $cover-$z1] [expr $cover-$y1] [expr $z1-$cover]
        patch rect 2  2 1  [expr $y1-$cover] [expr $cover-$z1] $y1 [expr $z1-$cover]

        # Create the reinforcing fibers (left, middle, right)
        layer straight 3 3 $As [expr $y1-$cover] [expr $z1-$cover] [expr $y1-$cover] [expr $cover-$z1]
        layer straight 3 2 $As 0.0 [expr $z1-$cover] 0.0 [expr $cover-$z1]
        layer straight 3 3 $As [expr $cover-$y1] [expr $z1-$cover] [expr $cover-$y1] [expr $cover-$z1]

    }    


    # Define column elements
    # ----------------------

    # Geometry of column elements
    #                tag 
    geomTransf Linear 1  

    # Number of integration points along length of element
    set np 5

    # Create the coulumns using Beam-column elements
    #                           tag ndI ndJ nsecs secID transfTag
    element nonlinearBeamColumn  1   1   3   $np    1       1 
    element nonlinearBeamColumn  2   2   4   $np    1       1 

    # Define beam elment
    # -----------------------------

    # Geometry of column elements
    #                tag 
    geomTransf Linear 2  

    # Create the beam element
    #                          tag ndI ndJ     A       E    Iz   transfTag
    element elasticBeamColumn   3   3   4    360    4030  8640    2


    # Define gravity loads
    # --------------------

    # Set a parameter for the axial load
    set P 180;                # 10% of axial capacity of columns

    # Create a Plain load pattern with a Linear TimeSeries
    pattern Plain 1 "Linear" {

            # Create nodal loads at nodes 3 & 4
            #    nd    FX          FY  MZ 
            load  3   0.0  [expr -$P] 0.0
            load  4   0.0  [expr -$P] 0.0
    }

    # ------------------------------
    # End of model generation
    # ------------------------------

    # ------------------------------
    # Start of analysis generation
    # ------------------------------

    # Create the system of equation, a sparse solver with partial pivoting
    system BandGeneral

    # Create the constraint handler, the transformation method
    constraints Transformation

    # Create the DOF numberer, the reverse Cuthill-McKee algorithm
    numberer RCM

    # Create the convergence test, the norm of the residual with a tolerance of 
    # 1e-12 and a max number of iterations of 10
    test NormDispIncr 1.0e-12  10 3

    # Create the solution algorithm, a Newton-Raphson algorithm
    algorithm Newton

    # Create the integration scheme, the LoadControl scheme using steps of 0.1 
    integrator LoadControl 0.1

    # Create the analysis object
    analysis Static

    # initialize in case we need to do an initial stiffness iteration
    initialize

    # ------------------------------
    # End of analysis generation
    # ------------------------------



    # ------------------------------
    # Start of recorder generation
    # ------------------------------

    # Create a recorder to monitor nodal displacements
    recorder Node -file nodeGravity.out -time -node 3 4 -dof 1 2 3 disp

    # --------------------------------
    # End of recorder generation
    # ---------------------------------


    # ------------------------------
    # Finally perform the analysis
    # ------------------------------

    # perform the gravity load analysis, requires 10 steps to reach the load level
    analyze 10


    # Print out the state of nodes 3 and 4
    print node 3 4


    # Print out the state of element 1
    print ele 1 2


     Node: 3
        Coordinates  : 0 144 
        commitDisps: 1.7109e-18 -0.0183736 -2.81893e-20 
         unbalanced Load: 0 -180 0 
        ID : 3 4 5 

     Node: 4
        Coordinates  : 360 144 
        commitDisps: 1.71095e-18 -0.0183736 -2.79765e-20 
         unbalanced Load: 0 -180 0 
        ID : 0 1 2 

    Element: 1 Type: NLBeamColumn2d     Connected Nodes: 1 3 
        Number of Sections: 5   Mass density: 0
        End 1 Forces (P V M): 180 7.0121e-31 -8.88178e-16
        End 2 Forces (P V M): -180 -7.0121e-31 8.88178e-16

    Element: 2 Type: NLBeamColumn2d     Connected Nodes: 2 4 
        Number of Sections: 5   Mass density: 0
        End 1 Forces (P V M): 180 0 -8.88178e-16
        End 2 Forces (P V M): -180 0 8.88178e-16
```


For the two nodes, displacements and loads are given. For the
beam-column elements, the element end forces in the local system are
provided.

The nodeGravity.out file contains ten lines, each line containing 7
entries. The first entry is time in the domain at end of the load step.
The next 3 entries are the displacements at node 3, and the final 3
entries the displacements at node 4.

## Example 3.2

In this example the nonlinear reinforced concrete portal frame which has
undergone the gravity load analysis of Example 3.1 is now subjected to a
pushover analysis.

1.  Example3.2.tcl

2.  Example3.1.tcl

After performing the gravity load analysis on the model, the time in the
domain is reset to 0.0 and the current value of all loads acting are
held constant. A new load pattern with a linear time series and
horizontal loads acting at nodes 3 and 4 is then added to the model.

The static analysis used to perform the gravity load analysis is
modified to take a new DisplacementControl integrator. At each new step
in the analysis the integrator will determine the load increment
necessary to increment the horizontal displacement at node 3 by 0.1 in.
60 analysis steps are performed in this new analysis.

For this analysis the nodal displacements at nodes 3 and 4 will be
stored in the file nodePushover.out for post-processing. In addition,
the end forces in the local coordinate system for elements 1 and 2 will
be stored in the file elePushover.out. At the end of the analysis, the
state of node 3 is printed to the screen.

```tcl

    # OpenSees Example 3.2
    # OpenSees Primer
    #
    # Units: kips, in, sec

    # ----------------------------------------------------
    # Start of Model Generation & Initial Gravity Analysis
    # ----------------------------------------------------

    # Do operations of Example3.1 by sourcing in the tcl file
    source Example3.1.tcl
    puts ``Gravity load analysis completed''

    # Set the gravity loads to be constant & reset the time in the domain
    loadConst -time 0.0

    # ----------------------------------------------------
    # End of Model Generation & Initial Gravity Analysis
    # ----------------------------------------------------


    # ----------------------------------------------------
    # Start of additional modeling for lateral loads
    # ----------------------------------------------------

    # Define lateral loads
    # --------------------

    # Set some parameters
    set H 10.0;     # Reference lateral load

    # Set lateral load pattern with a Linear TimeSeries
    pattern Plain 2 "Linear" {

            # Create nodal loads at nodes 3 & 4
            #    nd    FX  FY  MZ 
            load 3 $H 0.0 0.0 
            load 4 $H 0.0 0.0 
    }

    # ----------------------------------------------------
    # End of additional modeling for lateral loads
    # ----------------------------------------------------


    # ----------------------------------------------------
    # Start of modifications to analysis for push over
    # ----------------------------------------------------

    # Set some parameters
    set dU 0.1;         # Displacement increment

    # Change the integration scheme to be displacement control
    #                             node dof init Jd min max
    integrator DisplacementControl  3   1   $dU  1 $dU $dU

    # ----------------------------------------------------
    # End of modifications to analysis for push over
    # ----------------------------------------------------


    # ------------------------------
    # Start of recorder generation
    # ------------------------------

    # Create a recorder to monitor nodal displacements
    recorder Node -file node32.out -time -node 3 4 -dof 1 2 3 disp

    # Create a recorder to monitor element forces in columns
    recorder Element -file ele32.out -time -ele 1 2 localForce

    # --------------------------------
    # End of recorder generation
    # ---------------------------------


    # ------------------------------
    # Finally perform the analysis
    # ------------------------------

    # Set some parameters
    set maxU 6.0;           # Max displacement
    set numSteps [expr int($maxU/$dU)]

    # Perform the analysis
    analyze $numSteps
    puts ``Pushover analysis completed''

    # Print the state at node 3
    print node 3

    Gravity load analysis completed
    Setting time in domain to be : 0.0

    Pushover analysis completed
     Node: 3
            Coordinates  : 0 144 
            commitDisps: 6 0.488625 -0.00851377 
            unbalanced Load: 71.8819 -180 0 
```

In addition to what is displayed on the screen, the file node32.out and
ele32.out have been created by the script. Each line of node32.out
contains the time, DX, DY and RZ for node 3 and DX, DY and RZ for node 4
at the end of an iteration. Each line of eleForce.out contains the time,
and the element end forces in the local coordinate system. A plot of the
load-displacement relationship at node 3 is shown in
figure [\[lateral32\]](#lateral32){reference-type="ref"
reference="lateral32"}.

::: {.center}
![Load displacement curve for node 3](../fig_files/ExampleOut3.2.svg){#fig:lateral32}
:::

## Example 3.3

In this example the reinforced concrete portal frame which has undergone
the gravity load analysis of Example 3.1 is now subjected to a uniform
earthquake excitation.

1. `Example3.3.tcl`

2. `Example3.1.tcl`

3. `ReadSMDFile.tcl`

After performing the gravity load analysis, the time in the domain is
reset to 0.0 and the current value of all active loads is set to
constant. Mass terms are added to nodes 3 and 4. A new uniform
excitation load pattern is created. The excitation acts in the
horizontal direction and reads the acceleration record and time interval
from the file `ARL360.g3`. The file `ARL360.g3` is created from the PEER
Strong Motion Database (http://peer.berkeley.edu/smcat/) record
`ARL360.at2` using the Tcl procedure `ReadSMDFile` contained in the file
`ReadSMDFile.tcl`.

The static analysis object and its components are first deleted so that
a new transient analysis object can be created.

A new solution Algorithm of type Newton is then created. The solution
algorithm uses a ConvergenceTest which tests convergence on the norm of
the displacement increment vector. The integrator for this analysis will
be of type Newmark with a $\gamma$ of 0.25 and a $\beta$ of 0.5. The
integrator will add some stiffness proportional damping to the system,
the damping term will be based on the last committed stifness of the
elements, i.e. $C = a_c K_{commit}$ with $a_c = 0.000625$. The equations
are formed using a banded storage scheme, so the System is BandGeneral.
The equations are numbered using an RCM (reverse Cuthill-McKee)
numberer. The constraints are enforced with a Plain constraint handler.

Once all the components of an analysis are defined, the Analysis object
itself is created. For this problem a Transient Analysis object is used.
2000 time steps are performed with a time step of 0.01.

In addition to the transient analysis, two eigenvalue analysis are
performed on the model. The first is performed after the gravity
analysis and the second after the transient analysis.

For this analysis the nodal displacenments at Nodes 3 and 4 will be
stored in the file nodeTransient.out for post-processing. In addition
the section forces and deformations for the section at the base of
column 1 will also be stored in two seperate files. The results of the
eigenvalue analysis will be displayed on the screen.


```tcl
# OpenSees Example 3.3
# OpenSees Primer
#
# Units: kips, in, sec

# ----------------------------------------------------
# Start of Model Generation & Initial Gravity Analysis
# ----------------------------------------------------

# Do operations of Example3.1 by sourcing in the tcl file
source Example3.1.tcl
puts "Gravity load analysis completed"

# Set the gravity loads to be constant & reset the time in the domain
loadConst -time 0.0

# ----------------------------------------------------
# End of Model Generation & Initial Gravity Analysis
# ----------------------------------------------------

# ----------------------------------------------------
# Start of additional modeling for dynamic loads
# ----------------------------------------------------

# Define nodal mass in terms of axial load on columns
set g 386.4
set m [expr $P/$g];       # expr command to evaluate an expression

#    tag   MX   MY   RZ
mass  3    $m   $m    0
mass  4    $m   $m    0

# Define dynamic loads
# --------------------

# Set some parameters
set outFile ARL360.g3
set accelSeries "Path -filePath $outFile -dt $dt -factor $g"

# Source in TCL proc to read a PEER Strong Motion Database record
source ReadSMDFile.tcl

# Perform the conversion from SMD record to OpenSees record and obtain dt
#              inFile     outFile dt
ReadSMDFile ARL360.at2   $outFile dt

# Create UniformExcitation load pattern
#                         tag dir 
pattern UniformExcitation  2   1  -accel $accelSeries

# set the rayleigh damping factors for nodes & elements
rayleigh 0.0 0.0 0.0 0.000625

# ----------------------------------------------------
# End of additional modeling for dynamic loads
# ----------------------------------------------------

# ---------------------------------------------------------
# Start of modifications to analysis for transient analysis
# ---------------------------------------------------------

# Delete the old analysis and all its component objects
wipeAnalysis

# Create the convergence test, the norm of the residual with a tolerance of 
# 1e-12 and a max number of iterations of 10
test NormDispIncr 1.0e-12  10 

# Create the solution algorithm, a Newton-Raphson algorithm
algorithm Newton

# Create the integration scheme, Newmark with gamma = 0.5 and beta =  0.25
integrator Newmark  0.5  0.25 

# Create the system of equation, a banded general storage scheme
system BandGeneral

# Create the constraint handler, a plain handler as homogeneous boundary conditions
constraints Plain

# Create the DOF numberer, the reverse Cuthill-McKee algorithm
numberer RCM

# Create the analysis object
analysis Transient

# ---------------------------------------------------------
# End of modifications to analysis for transient analysis
# ---------------------------------------------------------

# ------------------------------
# Start of recorder generation
# ------------------------------

# Create a recorder to monitor nodal displacements
recorder Node -time -file node33.out -node 3 4 -dof 1 2 3 disp

# Create recorders to monitor section forces and deformations
# at the base of the left column
recorder Element -time -file ele1secForce.out -ele 1 section 1 force
recorder Element -time -file ele1secDef.out   -ele 1 section 1 deformation

# --------------------------------
# End of recorder generation
# ---------------------------------

# ------------------------------
# Finally perform the analysis
# ------------------------------

# Perform an eigenvalue analysis
puts "eigen values at start of transient: [eigen 2]"

# set some variables
set tFinal [expr 2000 * 0.01]
set tCurrent [getTime]
set ok 0

# Perform the transient analysis
while {$ok == 0 && $tCurrent < $tFinal} {
    
    set ok [analyze 1 .01]
    
    # if the analysis fails try initial tangent iteration
    if {$ok != 0} {
       puts "regular newton failed .. lets try an initail stiffness for this step"
        test NormDispIncr 1.0e-12  100 0
        algorithm ModifiedNewton -initial
        set ok [analyze 1 .01]
        if {$ok == 0} {puts "that worked .. back to regular newton"}
        test NormDispIncr 1.0e-12  10 
        algorithm Newton
    }
    
    set tCurrent [getTime]
}

# Print a message to indicate if analysis succesfull or not
if {$ok == 0} {
   puts "Transient analysis completed SUCCESSFULLY";
} else {
   puts "Transient analysis completed FAILED";    
}

# Perform an eigenvalue analysis
puts "eigen values at end of transient: [eigen 2]"


# Print state of node 3
print node 3
```

```
    Gravity load analysis completed
    eigen values at start of transient: 2.695422e+02  1.750711e+04  
    Transient analysis completed SUCCESSFULLY
    eigen values at start of transient: 1.578616e+02  1.658481e+04  

     Node: 3
         Coordinates  : 0 144 
         commitDisps: -0.0464287 -0.0246641 0.000196066 
         Velocities   : -0.733071 1.86329e-05 0.00467983 
         commitAccels: -9.13525 0.277302 38.2972 
         unbalanced Load: -3.9475 -180 0 
         Mass : 
           0.465839 0 0 
           0 0.465839 0 
           0 0 0 

         Eigenvectors: 
           -1.03587 -0.0482103 
           -0.00179081 0.00612275 
           0.00663473 3.21404e-05 
```

The two eigenvalues for the eigenvalue analysis are printed to the
screen. The state of node 3 at the end of the analysis is also printed.
The information contains the last committed displacements, velocities
and accelerations at the node, the unbalanced nodal forces and the nodal
masses. In addition, the eigenvector components of the eigenvector
pertaining to the node 3 is also displayed.

In addition to the contents displayed on the screen, three files have
been created. Each line of nodeTransient.out contains the domain time,
and DX, DY and RZ for node 3. Plotting the first and second columns of
this file the lateral displacement versus time for node 3 can be
obtained as shown in
figure [\[lateral33\]](#lateral33){reference-type="ref"
reference="lateral33"}. Each line of the files ele1secForce.out and
ele1secDef.out contain the domain time and the forces and deformations
for section 1 (the base section) of element 1. These can be used to
generate the moment-curvature time history of the base section of column
1 as shown in figure [\[element1MK\]](#element1MK){reference-type="ref"
reference="element1MK"}.

::: {.center}
![Lateral displacement at node 3](../fig_files/newNode3.3.svg){#fig:element1MK}
:::

::: {.center}
![Column section moment-curvature results](../fig_files/newElement1MK.svg){#fig:element1MK}
:::




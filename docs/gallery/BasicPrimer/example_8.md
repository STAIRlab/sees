# Cantilever Beam

In this example a simple problem in solid dynamics is considered. The
structure is a cantilever beam modelled with three dimensional solid
elements.

1.  `Example8.1.tcl`

For three dimensional analysis, a typical solid element is defined as a
volume in three dimensional space. Each node of the analysis has three
displacement degrees of freedom. Thus the model is defined with
$ndm := 3$ and $ndf := 3$.

For this model, a mesh is generated using the "block3D" command. The
number of nodes in the local x-direction of the block is $nx$, the
number of nodes in the local y-direction of the block is $ny$ and the
number of nodes in the local z-direction of the block is $nz$. The
block3D generation nodes {1,2,3,4,5,6,7,8} are prescribed to define the
three dimensional domain of the beam, which is of size
$2\times2\times10$.

Two possible brick elements can be used for the analysis. These may be
created using the terms `stdBrick` or `bbarBrick`. An elastic isotropic
material is used.

For initial gravity load analysis, a single load pattern with a linear
time series and a single nodal loads is used.

Boundary conditions are applied using the fixZ command. In this case,
all the nodes whose z-coordiate is $0.0$ have the boundary condition
`{1,1,1}`, fully fixed.

A solution algorithm of type Newton is used for the problem. The
solution algorithm uses a ConvergenceTest which tests convergence on the
norm of the energy increment vector. Five static load steps are
performed.

Subsequent to the static analysis, the wipeAnalysis and remove
loadPatern commands are used to remove the nodal loads and create a new
analysis. The nodal displacements have not changed. However, with the
external loads removed the structure is no longer in static equilibrium.

The integrator for the dynamic analysis if of type GeneralizedMidpoint
with $\alpha := 0.5$. This choice is uconditionally stable and energy
conserving for linear problems. Additionally, this integrator conserves
linear and angular momentum for both linear and non-linear problems. The
dynamic analysis is performed using $100$ time increments with a time
step $\Delta t := 2.0$.



    # ----------------------------
    # Start of model generation
    # ----------------------------

    # Create ModelBuilder with 3 dimensions and 6 DOF/node
    model basic -ndm 3 -ndf 3


    # create the material
    nDMaterial ElasticIsotropic   1   100   0.25  1.27


    # Define geometry
    # ---------------

    # define some  parameters
    set eleArgs "1" 

    set element stdBrick
    #set element BbarBrick

    set nz 6
    set nx 2 
    set ny 2

    set nn [expr ($nz+1)*($nx+1)*($ny+1) ]

    # mesh generation
    block3D $nx $ny $nz   1 1  $element  $eleArgs {
        1   -1     -1      0
        2    1     -1      0
        3    1      1      0
        4   -1      1      0 
        5   -1     -1     10
        6    1     -1     10
        7    1      1     10
        8   -1      1     10
    }


    set load 0.10

    # Constant point load
    pattern Plain 1 Linear {
       load $nn  $load  $load  0.0
    }

    # boundary conditions
    fixZ 0.0   1 1 1 


    # --------------------------------------------------------------------
    # Start of static analysis (creation of the analysis & analysis itself)
    # --------------------------------------------------------------------

    # Load control with variable load steps
    #                       init   Jd  min   max
    integrator LoadControl  1.0  1   1.0   10.0

    # Convergence test
    #                  tolerance maxIter displayCode
    test NormUnbalance     1.0e-10    20         1

    # Solution algorithm
    algorithm Newton

    # DOF numberer
    numberer RCM

    # Cosntraint handler
    constraints Plain 

    # System of equations solver
    system ProfileSPD

    # Analysis for gravity load
    analysis Static 

    # Perform the analysis
    analyze 5

    # --------------------------
    # End of static analysis
    # --------------------------

    # ----------------------------
    # Start of recorder generation
    # ----------------------------

    recorder Node -file Node.out -time -node $nn -dof 1 disp
    recorder plot Node.out CenterNodeDisp 625 10 625 450 -columns 1 2

    recorder display ShakingBeam 0 0 300 300 -wipe
    prp -100 100 120.5
    vup 0 1 0 
    display 1 0 1 

    # --------------------------
    # End of recorder generation
    # --------------------------


    # ---------------------------------------
    # Create and Perform the dynamic analysis
    # ---------------------------------------

    # Remove the static analysis & reset the time to 0.0
    wipeAnalysis
    setTime 0.0

    # Now remove the loads and let the beam vibrate
    remove loadPattern 1

    # add some mass proportional damping
    rayleigh 0.01 0.0 0.0 0.0

    # Create the transient analysis
    test EnergyIncr     1.0e-10    20         1
    algorithm Newton
    numberer RCM
    constraints Plain 
    integrator Newmark 0.5 0.25
    analysis Transient


    # Perform the transient analysis (20 sec)
    #       numSteps  dt
    analyze 100 2.0
    }

The results consist of the file cantilever.out, which contains a line
for every time step. Each line contains the time and the horizontal
displacement at the upper right corner the beam. The time history is as
plotted on the screen.

figure [\[cantileverdisp\]](#cantileverdisp){reference-type="ref"
reference="cantileverdisp"}.

::: {.center}
 
:::



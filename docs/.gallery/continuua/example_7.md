# Dynamic Shell Analysis

In this example a simple problem in shell dynamics is considered. The
structure is a curved hoop shell structure that looks like the roof of a
Safeway.

1.  `Example7.1.tcl`

For shell analysis, a typical shell element is defined as a surface in
three dimensional space. Each node of a shell analysis has six degrees
of freedom, three displacements and three rotations. Thus the model is
defined with $ndm := 3$ and $ndf := 6$.

For this model, a mesh is generated using the "block2D" command. The
number of nodes in the local x-direction of the block is $nx$ and the
number of nodes in the local y-direction of the block is $ny$. The
block2D generation nodes {1,2,3,4, 5,7,9} are defined such that the
structure is curved in three dimensional space.

The OpenSees shell element is constructed using the command
"ShellMITC4". An elastic membrane-plate material section model,
appropriate for shell analysis, is constructed using the
"ElasticMembranePlateSection" command. In this case, the elastic modulus
$E := 3.0e3$, Poisson's ratio $\nu :=  0.25$, the thickness $h := 1.175$
and the mass density per unit volume $\rho := 1.27$

For initial gravity load analysis, a single load pattern with a linear
time series and three vertical nodal loads are used.

Boundary conditions are applied using the fixZ command. In this case,
all the nodes whose z-coordiate is $0.0$ have the boundary condition
{1,1,1, 0,1,1}. All degrees-of-freedom are fixed except rotation about
the x-axis, which is free. The same boundary conditions are applied
where the z-coordinate is $40.0$.

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
dynamic analysis is performed using $250$ time increments with a time
step $\Delta t := 0.50$.

    # ----------------------------
    # Start of model generation
    # ----------------------------
    model basic -ndm 3 -ndf 6

    # create the material
    section ElasticMembranePlateSection  1   3.0e3  0.25  1.175  1.27

    # set some parameters for node and element generation
    set Plate ShellMITC4

    set eleArgs "1"

    #these should both be even
    set nx 8
    set ny 2

    #loaded nodes
    set mid [expr (  ($nx+1)*($ny+1)+1 ) / 2 ]
    set side1 [expr ($nx + 2)/2 ] 
    set side2 [expr ($nx+1)*($ny+1) - $side1 + 1 ]

    # generate the nodes and elements
    block2D $nx $ny 1 1 $Plate $eleArgs {
        1   -20    0     0
        2   -20    0    40
        3    20    0    40
        4    20    0     0
        5   -10   10    20 
        7    10   10    20   
        9    0    10    20 
    } 

    # add some loads
    pattern Plain 1 Linear {
        load $mid    0.0  -0.5   0.0   0.0   0.0  0.0
        load $side1  0.0  -0.25  0.0   0.0   0.0  0.0
        load $side2  0.0  -0.25  0.0   0.0   0.0  0.0
    }


    # define the boundary conditions
    # rotation free about x-axis (remember right-hand-rule)
    fixZ 0.0   1 1 1  0 1 1
    fixZ 40.0  1 1 1  0 1 1   

    # Load control with variable load steps
    #                       init   Jd  min   max
    integrator LoadControl  1.0  1   1.0   10.0

    # Convergence test
    #                  tolerance maxIter displayCode
    test EnergyIncr     1.0e-10    20         1

    # Solution algorithm
    algorithm Newton

    # DOF numberer
    numberer RCM

    # Cosntraint handler
    constraints Plain 

    # System of equations solver
    system SparseGeneral -piv
    #system ProfileSPD

    # Analysis for gravity load
    #analysis Transient 
    analysis Static 


    # Perform the gravity load analysis
    analyze 5


    # --------------------------
    # End of static analysis
    # --------------------------

    # ----------------------------
    # Start of recorder generation
    # ----------------------------

    recorder Node -file Node.out -time -node $mid -dof 2 disp

    recorder plot Node.out CenterNodeDisp 625 10 625 450 -columns 1 2

    recorder display shellDynamics 10 10 600 600 -wipe
    prp -100 20 30
    vup 0 1 0 
    display 1 0 100

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

    # Create the transient analysis
    test EnergyIncr     1.0e-10    20         1
    algorithm Newton
    numberer RCM
    constraints Plain 
    #integrator GeneralizedMidpoint 0.50
    integrator Newmark 0.50 0.25
    analysis Transient

    # Perform the transient analysis 
    analyze 250 0.5

The results consist of the file Node.out, which contains a line for
every time step. Each line contains the time and the vertical
displacement at the upper center of the hoop structure. The time history
is shown in figure [\[shelldisp$$
](#shelldisp){reference-type="ref"
reference="shelldisp"}.

::: {.center}
![Displacement vs. Time for bottom center of beam](../fig_files/SS.svg) 
:::



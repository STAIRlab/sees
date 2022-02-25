# Simply Supported Beam

In this example a simple problem in solid dynamics is considered. The
structure is a simply supported beam modelled with two dimensional solid
elements.

1.  `Example6.1.tcl`

For two dimensional analysis, a typical solid element is defined as a
volume in two dimensional space. Each node of the analysis has two
displacement degrees of freedom. Thus the model is defined with
$ndm := 2$ and $ndf := 2$. pp For this model, a mesh is generated using
the "block2D" command. The number of nodes in the local x-direction of
the block is $nx$ and the number of nodes in the local y-direction of
the block is $ny$. The block2D generation nodes {1,2,3,4} are prescribed
to define the two dimensional domain of the beam, which is of size
$40\times10$.

Three possible quadrilateral elements can be used for the analysis.
These may be created using the terms "bbarQuad," "enhancedQuad" or
"quad." This is a plane strain problem. An elastic isotropic material is
used.

For initial gravity load analysis, a single load pattern with a linear
time series and two vertical nodal loads are used.

A solution algorithm of type Newton is used for the problem. The
solution algorithm uses a ConvergenceTest which tests convergence on the
norm of the energy increment vector. Ten static load steps are
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
step $\Delta t := 0.50$.

    # ----------------------------
    # Start of model generation
    # ----------------------------

    # Create ModelBuilder with 3 dimensions and 6 DOF/node
    model basic -ndm 2 -ndf 2

    # create the material
    nDMaterial ElasticIsotropic   1   1000   0.25  6.75 


    # Define geometry
    # ---------------

    # define some  parameters

    set Quad  quad
    set Quad  bbarQuad
    set Quad  enhancedQuad

    if {$Quad == "enhancedQuad" } {
        set eleArgs "PlaneStrain2D  1"
    } 

    if {$Quad == "quad" } {
        set eleArgs "1 PlaneStrain2D  1"
    } 

    if {$Quad == "bbarQuad" } {
        set eleArgs "1"
    }

    set nx 8; # NOTE: nx MUST BE EVEN FOR THIS EXAMPLE
    set ny 2
    set bn [expr $nx + 1 ] 
    set l1 [expr $nx/2 + 1 ] 
    set l2 [expr $l1 + $ny*($nx+1) ]

    # now create the nodes and elements using the block2D command
    block2D $nx $ny   1 1  $Quad  $eleArgs {
        1   0   0
        2  40   0
        3  40  10
        4   0  10
    }

    # Single point constraints
    #   node   u1  u2    
    fix    1    1    1   
    fix  $bn    0    1   

    # Gravity loads
    pattern Plain 1 Linear {
        load $l1  0.0  -1.0
        load $l2  0.0  -1.0
    }

    # --------------------------------------------------------------------
    # Start of static analysis (creation of the analysis & analysis itself)
    # --------------------------------------------------------------------

    # Load control with variable load steps
    #                       init   Jd  min   max
    integrator LoadControl  1.0  1   1.0   10.0

    # Convergence test
    #                  tolerance maxIter displayCode
    test EnergyIncr  1.0e-12    10         0

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
    analyze   10     


    # --------------------------
    # End of static analysis
    # --------------------------

    # ----------------------------
    # Start of recorder generation
    # ----------------------------


    recorder Node -file Node.out -time -node $l1 -dof 2 disp
    recorder plot Node.out CenterNodeDisp 625 10 625 450 -columns 1 2

    # create the display
    recorder display SimplySupportedBaam 10 10 800 200 -wipe
    prp 20 5.0 100.0
    vup 0 1 0
    viewWindow -30 30 -10 10
    display 10 0 5

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
    test EnergyIncr  1.0e-12    10         0
    algorithm Newton
    numberer RCM
    constraints Plain 
    integrator Newmark 0.5 0.25
    analysis Transient

    # Perform the transient analysis (50 sec)
    #       numSteps  dt
    analyze  100     0.5

The results consist of the file Node.out, which contains a line for
every time step. Each line contains the time and the vertical
displacement at the bottom center of the beam. The time history is shown
in figure [\[beamdisp\]](#beamdisp){reference-type="ref"
reference="beamdisp"}.

::: {.center}
 
:::


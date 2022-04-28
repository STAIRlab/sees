---
title: Moment-Curvature (Concrete)
---

# Moment-Curvature (Concrete)

This next example covers the moment-curvature analysis of a reinforced
concrete section. The zero-length element with a fiber discretization of
the cross section is used in the model. In addition, Tcl language
features such as variable and command substitution, expression
evaluation, and procedures are demonstrated.

## Example 2.1

In this example, a moment-curvature analysis of the fiber section is
undertaken. Figure [\[rcsection4\]](#rcsection4){reference-type="ref"
reference="rcsection4"} shows the fiber discretization for the section.

1.  `Example2.1.tcl`

2.  `MomentCurvature.tcl`

The model consists of two nodes and a ZeroLengthSection element. A
depiction of the element geometry is shown in
figure [\[zerolength\]](#zerolength){reference-type="ref"
reference="zerolength"}. The drawing on the left of
figure [\[zerolength\]](#zerolength){reference-type="ref"
reference="zerolength"} shows an edge view of the element where the
local z-axis, as seen on the right side of the figure and in
figure [\[rcsection0\]](#rcsection0){reference-type="ref"
reference="rcsection0"}, is coming out of the page. Node 1 is completely
restrained, while the applied loads act on node 2. A compressive axial
load, P, of 180 kips is applied to the section during the
moment-curvature analysis.

::: {.center}
![Geometry of the zero-length element](../fig_files/ZeroLengthSection.svg) 
:::

For the zero length element, a section discretized by concrete and steel
is created to represent the resultant behavior. UniaxialMaterial objects
are created to define the fiber stress-strain relationships: confined
concrete in the column core, unconfined concrete in the column cover,
and reinforcing steel.

The dimensions of the fiber section are shown in
figure [\[rcsection0\]](#rcsection0){reference-type="ref"
reference="rcsection0"}. The section depth is 24 inches, the width is 15
inches, and there are 1.5 inches of cover around the entire section.
Strong axis bending is about the section z-axis. In fact, the section
z-axis is the strong axis of bending for all fiber sections in planar
problems. The section is separated into confined and unconfined concrete
regions, for which separate fiber discretizations will be generated.
Reinforcing steel bars will be placed around the boundary of the
confined and unconfined regions. The fiber discretization for the
section is shown in
figure [\[rcsection4\]](#rcsection4){reference-type="ref"
reference="rcsection4"}.

::: {.center}
![Dimensions of the RC section.](../fig_files/RCsection0.svg){#fig:rcsection0} 
:::

::: {.center} 
![Fiber section discretization](../fig_files/RCsection4.svg){#fig:rcsection4}
:::

The section analysis is performed by the Tcl procedure MomentCurvature
defined in the file MomentCurvature.tcl. The arguments to the procedure
are the tag of the section to be analyzed, the axial load applied to the
section, the maximum curvature, and the number of displacement
increments to reach the maximum curvature.

The output for the moment-curvature analysis will be the section forces
and deformations, stored in the file section1.out. In addition, an
estimate of the section yield curvature is printed to the screen.

In the script below variables, are set and can then be used with the
syntax of `$variable`. Expressions can be evaluated, although the Tcl
syntax at first appears cumbersome. An expression is given by an expr
command enclosed in square brackets `[]`'s. Typically, the result of an
expression is then set to another variable. A simple example to add `2.0`
to a parameter is shown below:

```{.tcl}
set v 3.0 
set sum [expr $v + 2.0] 
puts $sum;    # print the sum 
```

Comments with `#` can appear on the same line as a command, but then the
command must be terminated with a semi-colon.

    # OpenSees Example 2.1
    # OpenSees Primer
    #
    # Units: kips, in, sec

    # Define model builder
    # --------------------
    model BasicBuilder -ndm 2 -ndf 3

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

    # set some parameters
    set colWidth 15
    set colDepth 24 

    set cover  1.5
    set As    0.60;     # area of no. 7 bars

    # some variables derived from the parameters
    set y1 [expr $colDepth/2.0]
    set z1 [expr $colWidth/2.0]

    section Fiber 1 {

        # Create the concrete core fibers
        patch rect 1 10 1 [expr $cover-$y1] [expr $cover-$z1] 
                          [expr $y1-$cover] [expr $z1-$cover]

        # Create the concrete cover fibers (top, bottom, left, right)
        patch rect 2 10 1  [expr -$y1] [expr $z1-$cover] 
                                   $y1                     $z1
        patch rect 2 10 1  [expr -$y1]             [expr -$z1] 
                                   $y1       [expr $cover-$z1]
        patch rect 2  2 1  [expr -$y1]       [expr $cover-$z1] 
                           [expr $cover-$y1] [expr $z1-$cover]
        patch rect 2  2 1  [expr $y1-$cover] [expr $cover-$z1] 
                                         $y1 [expr $z1-$cover]

        # Create the reinforcing fibers (left, middle, right)
        layer straight 3 3 $As [expr $y1-$cover] [expr $z1-$cover] 
                               [expr $y1-$cover] [expr $cover-$z1]
        layer straight 3 2 $As 0.0 [expr $z1-$cover] 
                               0.0 [expr $cover-$z1]
        layer straight 3 3 $As [expr $cover-$y1] [expr $z1-$cover] 
                               [expr $cover-$y1] [expr $cover-$z1]

    }    

    # Estimate yield curvature
    # (Assuming no axial load and only top and bottom steel)
    set d [expr $colDepth-$cover]   ;# d -- from cover to rebar
    set epsy [expr $fy/$E]  ;# steel yield strain
    set Ky [expr $epsy/(0.7*$d)]

    # Print estimate to standard output
    puts "Estimated yield curvature: $Ky"

    # Set axial load 
    set P -180

    set mu 15;      # Target ductility for analysis
    set numIncr 100;    # Number of analysis increments

    # Call the section analysis procedure
    source MomentCurvature.tcl
    MomentCurvature 1 $P [expr $Ky*$mu] $numIncr

The Tcl procedure to perform the moment-curvature analysis follows. In
this procedure, the nodes are defined to be at the same geometric
location and the ZeroLengthSection element is used. A single load step
is performed for the axial load, then the integrator is changed to
DisplacementControl to impose nodal displacements, which map directly to
section deformations. A reference moment of 1.0 is defined in a Linear
time series. For this reference moment, the DisplacementControl
integrator will determine the load factor needed to apply the imposed
displacement. A node recorder is defined to track the moment-curvature
results. The load factor is the moment, and the nodal rotation is in
fact the curvature of the element with zero thickness.

    # Arguments
    #   secTag -- tag identifying section to be analyzed
    #   axialLoad -- axial load applied to section (negative is compression)
    #   maxK -- maximum curvature reached during analysis
    #   numIncr -- number of increments used to reach maxK (default 100)
    #
    # Sets up a recorder which writes moment-curvature results to file
    # section$secTag.out ... the moment is in column 1, and curvature in column 2

    proc MomentCurvature {secTag axialLoad maxK {numIncr 100} } {
       # Define two nodes at (0,0)
       node 1 0.0 0.0
       node 2 0.0 0.0

       # Fix all degrees of freedom except axial and bending at node 2
       fix 1 1 1 1
       fix 2 0 1 0

       # Define element
       #                         tag ndI ndJ  secTag
       element zeroLengthSection  1   1   2  $secTag

       # Create recorder
       recorder Node -file section$secTag.out -time -node 2 -dof 3 disp

       # Define constant axial load
       pattern Plain 1 "Constant" {
          load 2 $axialLoad 0.0 0.0
       }

       # Define analysis parameters
       integrator LoadControl 0 1 0 0
       system SparseGeneral -piv;
       test NormUnbalance 1.0e-9 10
       numberer Plain
       constraints Plain
       algorithm Newton
       analysis Static

       # Do one analysis for constant axial load
       analyze 1

       # Define reference moment
       pattern Plain 2 "Linear" {
          load 2 0.0 0.0 1.0
       }

       # Compute curvature increment
       set dK [expr $maxK/$numIncr]

       # Use displacement control at node 2 for section analysis
       integrator DisplacementControl 2 3 $dK 1 $dK $dK

       # Do the section analysis
       analyze $numIncr
    }

    Estimated yield curvature: 0.000126984126984

The file section1.out contains for each committed state a line with the
load factor and the rotation at node 3. This can be used to plot the
moment-curvature relationship as shown in
figure [\[momcurv\]](#momcurv){reference-type="ref"
reference="momcurv"}.

::: {.center}
 
:::

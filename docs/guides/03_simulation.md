# Simulation Process

## Build the model
1. model dimensions and degrees-of-freedom
2. nodal coordinates
3. nodal constraints, boundary conditions
4. nodal masses
5. elements and element connectivity
6. recorders for output

## Define & apply gravity load
1. nodal or element load
2. static-analysis parameters (tolerances & load increments)
3. analyze
4. hold gravity loads constant
5. reset time to zero

## Define and apply lateral load
1. load pattern (nodal loads for static analysis, support ground motion for earthquake)
2. lateral-analysis parameters (tolerances & displacement/time increments)
     Static Lateral-Load Analysis
     1. define the displacement increments and displacement path

     Dynamic Lateral-Load Analysis
     1. define the input motion and all associated parameters, such as scaling and input type
     2. define analysis duration and time increment
     3. define damping
3. analyze


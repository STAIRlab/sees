# Corotational

This command is used to construct the Corotational Coordinate
Transformation (`CorotCrdTransf`) object. Corotational transformation can
be used in large displacement-small strain problems. NOTE: Currently the
transformation does not deal with element loads and will ignore any that
are applied to the element.

For a two-dimensional problem:

  -------------------------------------------------------------------------------
  **geomTransf Corotational \$transfTag \<-jntOffset \$dXi \$dYi \$dXj \$dYj>**
  -------------------------------------------------------------------------------

For a three-dimensional problem:

  --------------------------------------------------------------------
  **geomTransf Corotational \$transfTag \$vecxzX \$vecxzY \$vecxzZ**
  --------------------------------------------------------------------

------------------------------------------------------------------------

+--------------------------------+------------------------------------+
| **\$transfTag**                | integer tag identifying            |
|                                | transformation                     |
+--------------------------------+------------------------------------+
| **\$vecxzX \$vecxzY \$vecxzZ** | X, Y, and Z components of vecxz,   |
|                                | the vector used to define the      |
|                                | local x-z plane of the             |
|                                | local-coordinate system. The local |
|                                | y-axis is defined by taking the    |
|                                | cross product of the vecxz vector  |
|                                | and the x-axis.                    |
|                                |                                    |
|                                | These components are specified in  |
|                                | the global-coordinate system X,Y,Z |
|                                | and define a vector that is in a   |
|                                | plane parallel to the x-z plane of |
|                                | the local-coordinate system.       |
|                                |                                    |
|                                | These items need to be specified   |
|                                | for the three-dimensional problem. |
+--------------------------------+------------------------------------+
| **\$dXi \$dYi**                | joint offset values \-- absolute   |
|                                | offsets specified with respect to  |
|                                | the global coordinate system for   |
|                                | element-end node i (optional)      |
+--------------------------------+------------------------------------+
| **\$dXj \$dYj**                | joint offset values \-- absolute   |
|                                | offsets specified with respect to  |
|                                | the global coordinate system for   |
|                                | element-end node j (optional)      |
+--------------------------------+------------------------------------+

The element coordinate system is specified as follows:

The x-axis is the axis connecting the two element nodes; the y- and
z-axes are then defined using a vector that lies on a plane parallel to
the local x-z plane \-- vecxz. The local y-axis is defined by taking the
cross product of the vecxz vector and the x-axis. The z-axis by taking
cross product of x and new y. The section is attached to the element
such that the y-z coordinate system used to specify the section
corresponds to the y-z axes of the element.

![](ElementOrentation.gif "ElementOrentation.gif")

![](RigidElementOffsets.gif "RigidElementOffsets.gif")

------------------------------------------------------------------------

EXAMPLE:

![](ElementCrossSection.png "ElementCrossSection.png")

![](ElementOrientation.png "ElementOrientation.png")

![](ElementVectors.png "ElementVectors.png")

1.  Element 1 : tag 1 : vecxZ = zaxis

geomTransf Corotational 1 0 0 -1

1.  Element 2 : tag 2 : vecxZ = y axis

geomTransf Corotational 2 0 1 0

Code Developed by: `<span style="color:blue">`{=html} Remo Magalhaes de
Souza `</span>`{=html}

Images Developed by: `<span style="color:blue">`{=html} Silvia Mazzoni
`</span>`{=html}

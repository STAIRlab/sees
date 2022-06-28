# Geometric Transformations

The geometric-transformation type (`CrdTransf`) implements a
coordinate-transformation, which transforms beam
element stiffness and resisting force from the basic system to the
global-coordinate system. The command has at least one argument, the
transformation type. Each type is outlined below.

```tcl
geomTransf transfType? arg1? ...
```
<hr />

<p>The type of transformation created and the additional arguments
  required depends on the <strong>transfType?</strong> provided in the
  command.</p>
<p>The following contain information about transfType? and the args
  required for each of the available geometric transformation types:</p>

<ul>
<li><a href="Linear_Transformation" title="wikilink">Linear Transformation</a></li>
<li><a href="PDelta_Transformation" title="wikilink">PDelta Transformation</a></li>
<li><a href="Corotational_Transformation" title="wikilink">Corotational Transformation</a></li>
</ul>

<p>A refresher on Euclidean Geometry and Coordinate Systems:</p>

A single vector may be defined by two points. It has length,
direction, and location in space. When this vector is used to define a
coordinate axis, only its direction is important. Now any 2 vectors, $V_r$
and $V_s$, not parallel, define a plane that is parallel to them both. The
cross-product of these vectors define a third vector, $V_t$, that is
perpendicular to both $V_r$ and $V_s$ and hence normal to the plane: $V_t = V_r \times V_s$.

<p>The element coordinate system is specified as follows:</p>
The x-axis is a vector given by the two element nodes; The vector
vecxz is a vector the user specifies that must not be parallel to the
x-axis. The x-axis along with the vecxz Vector define the xz plane. The
local y-axis is defined by taking the cross product of the x-axis vector
and the vecxz vector ($V_y = V_{xz} \times V_x$). The local z-axis is then found
simply by taking the cross product of the y-axis and x-axis vectors ($V_z
= V_x \times V_y$). The section is attached to the element such that the y-z
coordinate system used to specify the section corresponds to the y-z
axes of the element.

<figure>
<img src="/OpenSeesRT/contrib/static/ElementOrentation.gif" title="ElementOrentation.gif"
alt="ElementOrentation.gif" />
<figcaption aria-hidden="true">ElementOrentation.gif</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/RigidElementOffsets.gif" title="RigidElementOffsets.gif"
alt="RigidElementOffsets.gif" />
<figcaption aria-hidden="true">RigidElementOffsets.gif</figcaption>
</figure>

<p>NOTE: When in 2D, local $x$ and $y$ axes are in the $X$-$Y$ plane, where $X$
and $Y$ are global axes. Local $x$ axis is the axis connecting the two
element nodes, and local $y$ and $z$ axes follow the right-hand rule (e.g.,
if the element is aligned with the positive $Y$ axis, the local $y$ axis is
aligned with the negative $X$ axis, and if the element is aligned with the
positive $X$ axis, the local $y$ axis is aligned with the positive Y axis).
Orientation of local $y$ and $z$ axes is important for definition of the
fiber section.</p>
<hr />


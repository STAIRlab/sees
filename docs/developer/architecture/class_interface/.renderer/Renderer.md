UNDER CONSTRUCTION .. POLYGONS and COLORMAP NEED A RETHINK.


# Renderer 

```cpp
#include <earthquake/Renderer.h>
```



class Renderer







The Renderer class is an abstract class which is introduced to allow the
graphical display of the 3d finite element model. The Renderer class is
an abstract class, it defines the interface all concrete subclasses must
provide. In common with most rendering packages, the interface allows
only for the displaying of a few basic primitive objects, lines and
polygons (commercial renderers offer others such as cubes, circles,
cones). By providing only a few basic primitives, the interface will
allow complicated scenes to be created (much like the ten digits 0-9
allows an infinite number of numbers to be created).

Unlike commercial renderers there is no concept of the optical
properties of materials and light sources in the interface. This is
because the image the analyst is looking for is not a photo realistic
image of the model, rather an image indicating the basic model,
stresses, and nodal displacements.

// Constructor






// Destructor






// Public Methods to display the Model


// Public Methods invoked at start or end of a rendering










// Public Methods invoked by the Objects to Display Themselves


















// Public Methods invoked to set up the viewing system























Keeps a pointer to Domain object *theDomain* and the ColorMap object
*theMap*.




Does Noting.




Invoked to clear the image. This is required if multiple images can be
displayed at once for example in a graphic window.

Invoked at the start of `displayModel()`, when the image is about to be
displayed.

Invoked at the end of `displayModel()`, when the image is finished and
ready to be displayed.

Invoked to draw a line in the image. The two vectors *end1* and *end2*
define the two end points in the 3d coordinate system, the values *V1*
and *V2* define the scalar quantity to be displayed. To return $0$ if
successful, a negative number if not.

Invoked to draw a polygon in the image. The Vectors pointed to in *ends*
define the end points of the polygon and the Vector *values* define the
scalar quantities to be displayed. Note that there must be at least
*values.Size()* Vectors pointed to at the start of *ends*, otherwise a
segmentation fault will occur. To return $0$ if successful, a negative
number if not.

Invoked to draw a vector in the image. The vector is to be drawn at
position *position*. The magnitude and direction of the vector are given
in *value*. To return $0$ if successful, a negative number if not.

Invoked to draw a string of text in the image at position *posGlobal*.
The position is in the 3d model coordinates. The length of the string is
*length*. To return $0$ if successful, a negative number if not.

Invoked to draw a string of text in the image at position *posGlobal*.
The position is in the 3d model coordinates. The length of the string is
*length*. To return $0$ if successful, a negative number if not.

To set the ColorMap used in the `draw()` routines. The ColorMap object
is used to convert scalar quantities into rgb values.


Invoked to set the VRP. The VRP is a point on the viewing plane, which
is that plane in the global coordinate system on which the 3d image is
projected. The point is given in the global coordinate system.

Invoked to set the VPN. The VPN defines the perpendicular to the viewing
plane.

Invoked to set the VUP. The VUP defines the up direction of the viewing
plane. The combination of VRP, VPN and VUP define a new local coordinate
system centered at VRP, with axis u,v,n, where the direction of u is
given by $vuv \% vpn$, v by $vpn \% u$ and n finishes off the rhs local
system.

Invoked to set the bounds of the image on the view plane which is then
scaled to fit into the image diplayed. The values provided are in the
local coordinate system.

Sets the distance to the near and far clipping planes.

Sets the projection mode. If mode is $0$ a parallel projection of the
image onto the viewing plane will be displayed, if $1$ a perspective
projection.

Sets the fill mode for solid shapes, i.e. polygons. If *mode* is $0$ a
wire frame image will be displayed, otherwise solid shapes will be
filled.

Sets the PRP. The PRP defines the eye location of the viewer. It is
important to note that the eye location is specified in the new local
coordinate system.

Sets the portwindow. The portwindow is that region of the display into
which the image is displayed. The range is \[-1,1.-1.1$$
.

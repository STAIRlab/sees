
# Visualization Classes

These are classes used to present images of the model. These include the
abstract classes Renderer and ColorMap. There are two steps in the
creation of any graphical image: (1) create a model of the object to be
displayed; and (2) render the model to an image that is viewed on the
screen. The creation and rendering can be part of the same application,
or can be split into two separate applications, where a 3d description
of the model using a scene description language is o/p by the modeler
and i/p by the renderer.

In our finite element work **we have the model**, the domain. Though the
model we have is not typical, as it requires the displaying of scalar
and vector quantities and not just rgb values. **We need to develop an
interface for the renderer**. To do this we will introduce an abstract
class **Renderer** which defines this interface. Doing this will allow
full extensibility as it will allow concrete subclasses to be provided
which may render the model to the screen, or generate an SDL file which
can be read in by a rendering application or printed on a printer at a
later stage.

The interface for the Renderer class we introduce will be very simple.
It will only accept very simple primitive objects to be displayed (line
and polygon). As such, the Renderer will not be required to render the
components of the model, rather the components of the model will be
required to display themselves. This will allow both the introduction of
new component types, for example new element types, without existing
Renderer classes being required to be rewritten and also new Renderer
classes will be able to be introduced with the only requirement that
they be able to display the primitive object types. The drawback of
course is that the present design has to be modified to allow the
components to display themselves. On the otherhand, as the objects can
display themselves, it will allow complex images to be displayed, e.g.
3d beam elements with proper geometry and deformation along the length
or beam with plastic hinges at ends could indicate amount of rotation at
ends.



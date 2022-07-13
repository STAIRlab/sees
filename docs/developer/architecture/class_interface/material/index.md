
# Material Classes

Material classes are used to provide information to the Elements about
the material. There is one main class MaterialModel. The Element objects
query the MaterialModel objects to obtain the current value of stress
and the tangent defining the stress-strain relationship for the current
value of strain at the point in the domain represented by the
MaterialModel object.

## Material Abstractions

Currently, there are three Material abstractions in OpenSees, each of
which can be used across a wide range of element implementations:

1.  **UniaxialMaterial** - Provides the interface for all
    one-dimensional material models, either stress-strain or
    force-deformation. UniaxialMaterial models define the stress-strain
    response of a truss element, uniaxial fiber behavior in a
    beam-column section, or the force-deformation response of a beam
    section or zero-length element.

2.  **NDMaterial** - The multi-dimensional generalization of
    UniaxialMaterial; provides the stress-strain response at a point in
    a solid element, or multi-dimensional fiber behavior in a plate or
    beam-column section.

3.  **SectionForceDeformation** - Defines the interface for stress
    resultant models which are used to describe both plate and
    beam-column force-deformation response as well as the constitutive
    response of more general zero-length elements, e.g., for isolator
    bearings.

Each interface listed above is essentially the same with minor
differences. The NDMaterial and SectionForceDeformation abstractions
both represent multi-dimensional constitutive response. However, a
distinction is made between stress and stress *resultant* response to
allow for safer element implementations. Furthermore, the stress-strain
equations for continuum material models can be written in terms of
tensors. This is not the case for stress resultant models. Lastly, to
avoid returning matrices and vectors or tensors of size one, the
UniaxialMaterial abstraction is made distinct for reasons of efficiency,
as scalar values describe the behavior of a one-dimensional model.

::: {.center} 
![Material class hierarchy.](../Material.svg) {#fig:Material}
:::

As indicated in
figure [fig:Material](#fig:Material){reference-type="ref"
reference="fig:Material"}, each material abstraction is a subclass of
Material. The Material class is a subclass of both the TaggedObject and
MovableObject classes, and therefore inherits the functionality of these
two classes. As a result, it can be said that a Material "is a"
TaggedObject as well as a MovableObject. Furthermore, since each of
UniaxialMaterial, NDMaterial, and SectionForceDeformation "is a"
Material, each is also a TaggedObject and a MovableObject. The
TaggedObject class provides functionality for identifying materials,
through a tag, during model building; and the MovableObject class
provides functionality for parallel processing and database programming.



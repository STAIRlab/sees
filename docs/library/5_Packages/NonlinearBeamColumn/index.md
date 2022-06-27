
# Beam-Column Elements in OpenSees

This document provides a brief description of the interaction between a
beam-column element and the `SectionForceDeformation` and
`CoordTransformation` classes in OpenSees. Material and geometric
nonlinearities are abstracted, or separated, from the element
formulation by using the `SectionForceDeformation` and `CoordTransformation`
classes. As a result, an element can be programmed in the "basic system"
to account for material nonlinearities, then use one of many
transformation types to pick up geometric nonlinearities. A displacement
based, distributed plasticity formulation is presented as an example of
how a beam-column element is formulated in the basic system.

## Geometric Nonlinearity

In general, the transformation of nodal displacements, $\mathbf{u}$, in the
global system to deformations, $\mathbf{v}$, in the basic system is described
by a nonlinear function,

$$%\label{eq:v=v(u)}
\mathbf{v} = \mathbf{v}(\mathbf{u}).$$

In a similar manner, the transformation of basic forces, $\mathbf{q}$, to
forces $\mathbf{p}$ in the global frame of reference is given by

$$%\label{eq:p=p(q,u)}
\mathbf{p} = \mathbf{p}(\mathbf{q}(\mathbf{u}), \mathbf{u}),$$

where $\mathbf{p}$ is implicitly a function of $\mathbf{u}$ via the basic forces,
$\mathbf{q}$, as well as an explicit function of $\mathbf{u}$. The explicit dependence
on $\mathbf{u}$ takes into account *approximate* geometric nonlinearities such
as P-$\Delta$. These transformations are shown schematically in
figure [@fig:Transformation]{reference-type="ref"
reference="fig:Transformation"}.

::: center
![Beam transformation](BeamTransf.svg)  
{#fig:Transformation}
:::

As seen in
figure [\[fig:BeamClass$$
](#fig:BeamClass){reference-type="ref"
reference="fig:BeamClass"}, a beam-column element acquires geometric
nonlinearity from the `CoordTransformation` class, and material
nonlinearity from the `SectionForceDeformation` class.

## Material Nonlinearity

At every cross-section along the element length, a force-deformation
relationship holds, providing section stress resultants, $\mathbf{s}$, as a
function of section deformations, $\mathbf{e}$,

$$%\label{eq:s=s(e)}
\mathbf{s}(x) = \mathbf{s}(\mathbf{e}(x)).$$

Linearizing the force-deformation relationship with respect to
deformations reveals the section tangent stiffness, $\mathbf{k}_s$,

$$\begin{aligned}
\Delta\mathbf{s} &= \frac{\partial\mathbf{s}}{\partial\mathbf{e}} \Delta\mathbf{e} \\
\Delta\mathbf{s} &= \mathbf{k}_s \Delta\mathbf{e},\end{aligned}$$

where $\mathbf{k}_s = \frac{\partial\mathbf{s}}{\partial\mathbf{e}}$, the partial
derivative of the section stress resultants with respect to the section
deformations.

A beam-column element obtains material nonlinearity through use of the
`SectionForceDeformation` class, as seen in
figure [\[fig:BeamClass$$
](#fig:BeamClass){reference-type="ref"
reference="fig:BeamClass"}.

## Class Hierarchy

Figure [\[fig:BeamClass$$
](#fig:BeamClass){reference-type="ref"
reference="fig:BeamClass"} shows the class interaction between a
beam-column element and the `CoordTransformation` and
`SectionForceDeformation` classes. An element can use any one of Linear,
$P-\Delta$, or Corotational transformations; and any one of `ElasticSection`
or `FiberSection` constitutive models. When a new transformation or
section class is added to the framework, the element can use the new
class without modification.

::: center
![Beam class](BeamClass.svg) 
:::

## Displacement Based Element Formulation

This section describes the formulation of a displacement based,
distributed plasticity beam-column element. The governing compatibility
and equilibrium equations are covered along with the consistent element
stiffness. Bending deformations are assumed to be small, and shear
deformations are neglected.

### Compatibility

For displacement based elements, there is a strong form of compatibility
between basic displacements, $\mathbf{v}$, and section deformations $\mathbf{e}$,
satisfied pointwise along the element length,

$$%\label{eq:e=av}
\mathbf{e}(x) =
\left[ \begin{array}{c} \varepsilon(x) \\ \kappa(x) \end{array} \right] =
\mathbf{a}(x) \mathbf{v},$$

where $\mathbf{a}$ is the strain-displacement matrix. The section deformations
are the axial strain, $\varepsilon$, and curvature, $\kappa$. Assuming
linear axial displacement and transverse displacement based on cubic
Hermitian polynomials, the shape functions in the basic system are

$$%\label{eq:N}
\mathbf{N}(x) =
\left[ \begin{array}{c} N_1(x) \\ \\ N_2(x) \\ \\ N_3(x) \end{array} \right] =
\left[ \begin{array}{c} \frac{x}{L} \\ \\
L\left( \frac{x}{L} - 2\frac{x^2}{L^2} + \frac{x^3}{L^3} \right) \\ \\
L\left( -\frac{x^2}{L^2} + \frac{x^3}{L^3} \right)
\end{array}
\right].$$

The strain-displacement matrix contains the shape function derivatives.
Axial strain is the first derivative of the axial displacement, and
curvature is the second derivative of the transverse displacement,

$$\mathbf{a}(x) = \left[ \begin{array}{ccc}
N_{1,x} & 0 & 0 \\ \\
0 & N_{2,xx} & N_{3,xx}
\end{array}
\right].$$

Using the shape functions defined in
equation [\[eq:N$$
](#eq:N){reference-type="ref" reference="eq:N"}, the
strain-displacement matrix is then,

$$\mathbf{a}(x) = \frac{1}{L} \left[ \begin{array}{ccc}
1 & 0 & 0 \\ \\
0 & -4+6\frac{x}{L} & -2+6\frac{x}{L}
\end{array}
\right].$$

The basic displacements, $\mathbf{v}$, can be obtained by invoking the method
`getBasicTrialDisp()`. After computing section deformations from basic
displacements via equation [@eq:e=av]{reference-type="ref"
reference="eq:e=av"}, the method `setTrialSectionDeformation()` may be
invoked with the updated deformations, $\mathbf{e}$.

### Equilibrium

Using the principle of virtual displacements (virtual work), equilibrium
between element end forces, $\mathbf{q}$, and section stress resultants, $\mathbf{s}$,
is satisfied weakly, or in an average sense, along the element length,

$$%\label{eq:q}
\mathbf{q} = \int_0^L \mathbf{a}(x)^T \mathbf{s}(x) \: dx,$$

where the section stress resultants are the axial force, $P$, and
bending moment, $M$,

$$\mathbf{s}(x) =
\left[ \begin{array}{c} P(x) \\ M(x) \end{array} \right].$$

To obtain the current value of section stress resultants, $\mathbf{s}$, the
method `getStressResultant()` must be invoked. To perform the
transformation from basic to global resisting force
(equation [\[eq:p=p(q,u)$$
](#eq:p=p(q,u)){reference-type="ref"
reference="eq:p=p(q,u)"}), the method `getGlobalResistingForce()` should
be invoked.

### Element Stiffness

To solve the structural system of equations, the element stiffness must
be assembled along with the resisting force. The element stiffness is
obtained by taking the partial derivative of
equation [\[eq:p=p(q,u)$$
](#eq:p=p(q,u)){reference-type="ref"
reference="eq:p=p(q,u)"} with respect to displacements, $\mathbf{u}$.

$$\begin{aligned}
\mathbf{k} &= \frac{\partial\mathbf{p}}{\partial\mathbf{q}}\frac{\partial\mathbf{q}}{\partial\mathbf{u}} + \left.\frac{\partial\mathbf{p}}{\partial\mathbf{u}}\right|_\mathbf{q} \\
&= \frac{\partial\mathbf{p}}{\partial\mathbf{q}} \frac{\partial\mathbf{q}}{\partial\mathbf{v}} \frac{\partial\mathbf{v}}{\partial\mathbf{u}} +
\left.\frac{\partial\mathbf{p}}{\partial\mathbf{u}}\right|_\mathbf{q} \\
\mathbf{k} &= %\label{eq:stiff} 
\frac{\partial\mathbf{p}}{\partial\mathbf{q}} \mathbf{k}_b \frac{\partial\mathbf{v}}{\partial\mathbf{u}} +
\left.\frac{\partial\mathbf{p}}{\partial\mathbf{u}}\right|_\mathbf{q}\end{aligned}$$

The basic element stiffness, $\mathbf{k}_b$, is the partial derivative of
the basic forces, $\mathbf{q}$, with respect to the basic displacements,
$\mathbf{v}$. Differentiating
equation [\[eq:q$$
](#eq:q){reference-type="ref" reference="eq:q"} gives,

$$\begin{aligned}
\mathbf{k}_b &= \frac{\partial\mathbf{q}}{\partial\mathbf{v}} \\
&= \int_0^L \mathbf{a}(x)^T \frac{\partial\mathbf{s}}{\partial\mathbf{v}} \: dx \\
&= \int_0^L \mathbf{a}(x)^T \frac{\partial\mathbf{s}}{\partial\mathbf{e}} \frac{\partial\mathbf{e}}{\partial\mathbf{v}} \: dx \\
\mathbf{k}_b &= %\label{eq:kb}
\boxed{
\int_0^L \mathbf{a}(x)^T \mathbf{k}_s(x) \mathbf{a}(x) \: dx}
\end{aligned}$$

The section tangent stiffness matrix, $\mathbf{k}_s$, is returned upon
invoking the method `getSectionTangent()`. After computing the basic
stiffness, $\mathbf{k}_b$, the method `getGlobalStiffMatrix()` should be
invoked to perform the transformation in
equation [\[eq:stiff$$
](#eq:stiff){reference-type="ref"
reference="eq:stiff"}. The remaining partial derivatives in
equation [\[eq:stiff$$
](#eq:stiff){reference-type="ref"
reference="eq:stiff"} are computed by the `getGlobalStiffMatrix()`
method.

### Numerical Quadrature

In general, the element integrals,
equations [\[eq:q$$
](#eq:q){reference-type="ref" reference="eq:q"}
and [\[eq:kb$$
](#eq:kb){reference-type="ref" reference="eq:kb"}, cannot
be evaluated in closed form due to nonlinearities in the section
constitutive model. These integrals must be approximately evaluated by
numerical quadrature,

$$\begin{aligned}
%\label{eq:qapprox}
\mathbf{q} &\approx
\sum_{i=1}^{N_s} \mathbf{a}(x_i)^T \mathbf{s}(x_i) \: W_i \\
%\label{eq:kbapprox}
\mathbf{k}_b &\approx
\sum_{i=1}^{N_s} \mathbf{a}(x_i)^T \mathbf{k}_s(x_i) \mathbf{a}(x_i) \: W_i ,\end{aligned}$$

where $N_s$ is the number of integration points, i.e., the number of
section sample points along the element length.

Integration points, $\xi_i$, and weights, $\omega_i$, are typically
defined over a fixed domain such as $\left[-1,1\right]$ or
$\left[0,1\right]$, then mapped to the element domain
$\left[0,L\right]$, where $L$ is the element length. Assuming points and
weights defined on $\left[-1,1\right]$, the following relationships
hold,

$$\begin{aligned}
x_i &= \frac{L}{2} \left( \xi_i+1 \right) \\
W_i &= \frac{L}{2} \: \omega_i .\end{aligned}$$

After mapping the points and weights to the element domain,
equations [\[eq:qapprox$$
](#eq:qapprox){reference-type="ref"
reference="eq:qapprox"}
and [\[eq:kbapprox$$
](#eq:kbapprox){reference-type="ref"
reference="eq:kbapprox"} can be evaluated.

::: center
**Michael H. Scott**

**August 22, 2001**

**PEER, University of California, Berkeley**
:::

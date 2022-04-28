# Modeling Capabilities

### Elements

- Beam-column -- 3D elements with the following integration rules
  - Linear elastic material (closed form),
  - Concentrated plasticity integrated over specified hinge lengths, or
  - Distributed plasticity integrated along the element length.

- Beam-column plasticity is described by section models.

- Each element can use the following geometric transformations
  - Linear -- first order geometry,
  - P-Delta -- second order "leaning truss" transformation, or
  - Corotational -- large displacement transformation.

- Zero length -- 3D element which uses multiple uniaxial materials to model the element force-deformation relation.

- Truss -- 3D element with material non-linearity modeled by
  - Uniaxial material stress-strain integrated over cross-sectional area, or
  - Section force-deformation relationship.
- Quad -- 2D bilinear isoparametric element which uses ND materials at each of its integration points.


### Uniaxial Materials

Core
- [Elastic]() -- linear elastic material tangent with optional linear damping tangent
- [ElasticPP]() -- elastic-perfectly plastic
- [ElasticPPGap]() -- one-sided EPP with an initial gap
- [Hardening]() -- bilinear model with combined linear isotropic and kinematic hardening
- [Parallel]() -- multiple uniaxial materials in parallel
- [Series]() -- multiple uniaxial materials in series

FEDEAS
- [Steel01]() -- bilinear steel model with linear kinematic and exponential isotropic hardening
- [Concrete01]() -- concrete model with Kent-Park envelope, degraded linear unloading/reloading, and no tensile strength
- [Hysteretic]() -- trilinear backbone with pinching, damage, and degraded unloading stiffness

SNAP
- [BiLinear]() -- bilinear hysteretic model with degradation
- [Clough]() -- Clough type hysteretic model with degradation
- [Pinch]() -- pinching hysteretic model with degradation
FEAP

### ND Materials

- ElasticIsotropic -- plane stress and plane strain formulations for use with the quad element.

### Section Models

- Elastic -- uncoupled axial and bending response.
- Fiber -- discretized by fibers which collectively define section response. The fiber models available are
- Uniaxial2d/3d -- associates with a uniaxial material and enforces the Bernoulli beam assumption for axial and uni/bi-directional bending
- Generic1d/Nd -- map stresses from uniaxial and ND materials to section stress resultants. For example, a uniaxial material can be used to model section moment-curvature behavior, or an ND plasticity model can be used to model section moment-axial-shear interaction.
- Aggregator -- combination of a section and multiple uncoupled uniaxial materials used to define additional section force-deformation relations. For example, a fiber section can be combined with an uncoupled shear force-deformation relation.


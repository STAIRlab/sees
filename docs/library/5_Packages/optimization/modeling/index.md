
<p><h1>Material Commands</h1></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<h2><a href="uniaxialMaterial_commands"
title="wikilink">uniaxialMaterial commands</a></h2>
</dd>
<dd>
Several uniaxial materials are available for DDM-based FE response
sensitivity computation.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="SteelMP_Material" title="wikilink">SteelMP Material</a>
</dd>
<dd>
This command is used to construct a uniaxial Menegotto-Pinto steel
material object.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="SmoothPSConcrete_Material" title="wikilink">SmoothPSConcrete
Material</a>
</dd>
<dd>
This command is used to construct a uniaxial smoothed Popovics-Saenz
concrete material object.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="UniaxialJ2Plasticity_Material"
title="wikilink">UniaxialJ2Plasticity Material</a>
</dd>
<dd>
This command is used to construct a uniaxial J2 Plasticity material
object with isotropic and kinematic hardening.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="Hardening_Material_for_Sensitivity" title="wikilink">Hardening
Material for Sensitivity</a>
</dd>
<dd>
This command is used to construct a uniaxial material object with
combined linear kinematic and isotropic hardening.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="Concrete01_Material" title="wikilink">Concrete01 Material</a>
</dd>
<dd>
This command is used to construct a uniaxial Kent-Scott-Park concrete
material object with degraded linear unloading/reloading stiffness
according to the work of Karsan-Jirsa and no tensile strength (refer to
<a href="http://peer.berkeley.edu">http://peer.berkeley.edu</a>).
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="Steel01_Material_for_Sensitivity" title="wikilink">Steel01
Material for Sensitivity</a>
</dd>
<dd>
This command is used to construct a uniaxial bilinear steel material
object with kinematic hardening and optional isotropic hardening
described by a non-linear evolution equation (refer to <a
href="http://peer.berkeley.edu">http://peer.berkeley.edu</a>).
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="Elastic_Material" title="wikilink">Elastic Material</a>
</dd>
<dd>
This command is used to construct a linear elastic uniaxial material
object (with optional material damping).
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<h2><a href="nDmaterial_commands" title="wikilink">nDmaterial
commands</a></h2>
</dd>
<dd>
Currently, only one multi-axial material model has been extended for
DDM-based FE response sensitivity computation.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="MultiYieldSurfaceClay"
title="wikilink">MultiYieldSurfaceClay</a>
</dd>
<dd>
The ‘MultiYieldSurfaceClay’ is an elastic-plastic material in which
plasticity exhibits only in the deviatoric stress-strain response. The
volumetric stress-strain response is linear-elastic and is independent
of the deviatoric response. This material is implemented to simulate
monotonic or cyclic response of materials whose shear behavior is
pressure independent. Such materials include, for example, organic soils
or clay under fast (undrained) loading conditions.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
This material is available for sensitivity computation in both 2-D and
3-D models. It is another version of PressureIndependMultiYield
material. However there are three differences between this model and
PressureIndependMultiYield:
</dd>
<dd>
1. This model uses the consistent tangent modulus instead of the
continuum tangent modulus.
</dd>
<dd>
2. This model does not support the ‘updateMaterialStage’ command.
</dd>
<dd>
3. This model does not support further discretization of the strain
increment in each iteration.
</dd>
</dl>
</dd>
</dl>
<p><h1>Section
Commands</h1></p>
<dl>
<dt></dt>
<dd>
Currently, only two cross-section models and the section aggregator have
been extended for DDM-based FE response sensitivity computation.
</dd>
</dl>
<p>::; <h3><a href="Section_Commands" title="wikilink">Section
Commands</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="Fiber" title="wikilink">Fiber</a>
</dd>
<dd>
Both 2-D and 3-D fiber sections are available for response sensitivity
computation.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="Elastic" title="wikilink">Elastic</a>
</dd>
<dd>
Both 2-D and 3-D elastic sections are available for response sensitivity
computation.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="Aggregator" title="wikilink">Aggregator</a>
</dd>
<dd>
This command is used to construct a SectionAggregator object which
groups previously-defined UniaxialMaterial objects into a single section
force-deformation model.
</dd>
</dl>
</dd>
</dl>
<p><h1>Element
Commands</h1></p>
<dl>
<dt></dt>
<dd>
Currently, several element types have been extended for DDM-based FE
response sensitivity computation.
</dd>
</dl>
<p>::; <h3><a href="Element_Commands" title="wikilink">Element
Commands</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="dispBeamColumnWithSensitivity"
title="wikilink">dispBeamColumnWithSensitivity</a>
</dd>
<dd>
This command is used to construct a 2-D or 3-D distributed-plasticity
displacement-based beam-column (frame) element.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="quadWithSensitivity" title="wikilink">quadWithSensitivity</a>
</dd>
<dd>
This command is used to construct a 2D four-node quadrilateral element
object based on a bilinear isoparametric formulation.
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="bbarBrickWithSensitivity"
title="wikilink">bbarBrickWithSensitivity</a>
</dd>
<dd>
This command is used to construct an eight-node 3D brick element object
based on a trilinear isoparametric formulation.
</dd>
</dl>
</dd>
</dl>

## Constraint Commands

<dl>
<dt></dt>
<dd>
Currently, several element types have been extended for DDM-based FE
response sensitivity computation.
</dd>
</dl>
<p>::; <h3><a href="Constraint_Commands"
title="wikilink">Constraint Commands</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="Transformation" title="wikilink">Transformation</a>
</dd>
<dd>
This command is used to construct a multi-point constraint handler based
on the transformation equation method.
</dd>
</dl>
</dd>
</dl>


## Element Commands

Currently, several element types have been extended
for DDM-based FE response sensitivity computation.

```tcl
element eleType? arg1? ...
```
<hr />
<p>The type of element created and the additional arguments required
depends on the <strong>eleType?</strong> provided in the command.</p>
<p>The following contain information about eleType? and the args
required for each of the available element types:</p>
<p>&lt;/noinclude&gt;</p>
<ul>
<li><a href="dispBeamColumnWithSensitivity_Element"
title="wikilink">dispBeamColumnWithSensitivity Element</a></li>
<li><a href="quadWithSensitivity_Element"
title="wikilink">quadWithSensitivity Element</a></li>
<li><a href="bbarBrickWithSensitivity_Element"
title="wikilink">bbarBrickWithSensitivity Element</a></li>
</ul>

# UniaxialMaterial Commands

<p>&lt;noinclude&gt;Several uniaxial materials are available for
DDM-based FE response sensitivity computation.</p>

```tcl
uniaxialMaterial matType? arg1? ...
```
<dl>
<dt></dt>
<dd>
Several uniaxial materials are available for DDM-based FE response
sensitivity computation.
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
<a href="Elastic_Uniaxial_Material" title="wikilink">Elastic Uniaxial
Material</a>
</dd>
<dd>
This command is used to construct a linear elastic uniaxial material
object (with optional material damping).
</dd>
</dl>
</dd>
</dl>

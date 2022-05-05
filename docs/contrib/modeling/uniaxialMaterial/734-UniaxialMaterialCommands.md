# UniaxialMaterialCommands

<p>&lt;noinclude&gt;Several uniaxial materials are available for
DDM-based FE response sensitivity computation.</p>

```tcl
uniaxialMaterial matType? arg1? ...
```
<hr />
<p>The type of material created and the additional arguments required
depends on the <strong>matType?</strong> provided in the command.</p>
<p>The following contain information about matType? and the args
required for each of the available material types:</p>
<p>&lt;/noinclude&gt;</p>
<ul>
<li><a href="SteelMP_Material" title="wikilink">SteelMP
Material</a></li>
</ul>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
For this material class, the sensitivity parameters can be: sigmaY, E, b
</dd>
</dl>
</dd>
</dl>
<ul>
<li><a href="SmoothPSConcrete_Material"
title="wikilink">SmoothPSConcrete Material</a></li>
</ul>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
For this material class, the sensitivity parameters can be: fc, fu, Ec,
epsco, epscu, eta
</dd>
</dl>
</dd>
</dl>
<ul>
<li><a href="UniaxialJ2Plasticity_Material"
title="wikilink">UniaxialJ2Plasticity Material</a></li>
</ul>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
For this material class, the sensitivity parameters can be: E, sigmaY,
Hkin, Hiso
</dd>
</dl>
</dd>
</dl>
<ul>
<li><a href="Hardening_Material_for_Sensitivity"
title="wikilink">Hardening Material for Sensitivity</a></li>
</ul>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
For this material class, the sensitivity parameters can be: E, sigmaY,
Hkin, Hiso
</dd>
</dl>
</dd>
</dl>
<ul>
<li><a href="Concrete01_Material" title="wikilink">Concrete01
Material</a></li>
</ul>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
For this material class, the sensitivity parameters can be: fc, epsco,
fcu, epscu
</dd>
</dl>
</dd>
</dl>
<ul>
<li><a href="Steel01_Material_for_Sensitivity" title="wikilink">Steel01
Material for Sensitivity</a></li>
</ul>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
For this material class, the sensitivity parameters can be: E, sigmaY,
b, a1, a2, a3, a4
</dd>
</dl>
</dd>
</dl>
<ul>
<li><a href="Elastic_Material" title="wikilink">Elastic
Material</a></li>
</ul>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
For this material class, the sensitivity parameters can be: E, eta
</dd>
</dl>
</dd>
</dl>

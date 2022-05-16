# LimitState

This command is used to construct a uniaxial hysteretic material
object with pinching of force and deformation, damage due to ductility
and energy, and degraded unloading stiffness based on ductility. Failure
of the material is defined by the associated <a href="Limit_Curve"
title="wikilink">Limit Curve</a>.

```tcl
uniaxialMaterial LimitState $matTag $s1p $e1p $s2p $e2p
        $s3p $e3p $s1n $e1n $s2n $e2n $s3n $e3n $pinchX $pinchY $damage1
        $damage2 $beta $curveTag $curveType.
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">s1p e1p</code></p></td>
<td><p>stress and strain (or force &amp; deformation) at first point of
the envelope in the positive direction</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">s2p e2p</code></p></td>
<td><p>stress and strain (or force &amp; deformation) at second point of
the envelope in the positive direction</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">s3p e3p</code></p></td>
<td><p>stress and strain (or force &amp; deformation) at third point of
the envelope in the positive direction</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">s1n e1n</code></p></td>
<td><p>stress and strain (or force &amp; deformation) at first point of
the envelope in the negative direction*</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">s2n e2n</code></p></td>
<td><p>stress and strain (or force &amp; deformation) at second point of
the envelope in the negative direction*</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">s3n e3n</code></p></td>
<td><p>stress and strain (or force &amp; deformation) at third point of
the envelope in the negative direction*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">pinchX</code></td>
<td><p>pinching factor for strain (or deformation) during
reloading</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">pinchY</code></td>
<td><p>pinching factor for stress (or force) during reloading</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">damage1</code></p></td>
<td><p>damage due to ductility: D1(m-1)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">damage2</code></p></td>
<td><p>damage due to energy: D2(Ei/Eult)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">beta</code></td>
<td><p>power used to determine the degraded unloading stiffness based on
ductility, m-b (optional, default=0.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">curveTag</code></td>
<td><p>an integer tag for the <a href="Limit_Curve"
title="wikilink">Limit Curve</a> defining the limit surface</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">curveType</code></td>
<td><p>an integer defining the type of LimitCurve (0 = no curve,</p>
<p>1 = axial curve, all other curves can be any other integer)</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<ul>
<li>negative backbone points should be entered as negative numeric
values</li>
</ul>
<hr />

## Examples

<p>Original version of example:</p>
<ul>
<li><a href="LimitStateMaterialExample"
title="wikilink">LimitStateMaterialExample</a></li>
</ul>
<p>Debugged version of example:</p>
<ul>
<li><a href="LimitStateMaterialExampleDebugged"
title="wikilink">LimitStateMaterialExampleDebugged</a></li>
</ul>
<p>Manual for the example:</p>
<ul>
<li><a href="Media:_LimitStateMaterialManual.pdf" title="wikilink">
Limit State Material - Example Manual</a></li>
</ul>
<hr />

## Description
<p>Modeling Failures in Existing Reinforced Concrete Columns by Ken
Elwood: <a href="file:ElwoodCJCE2004.pdf"
title="wikilink">file:ElwoodCJCE2004.pdf</a></p>
<hr />

## References
<p>Elwood, K.J and Moehle, J.P., "Shake Table Tests and Analystical
Studies on the Gravity Load Collapse of Reinforced Concrete Frames",
Pacific Earthquake Engineering Research Center, University of
California, Berkeley, CA. PEER 2003/01.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Ken Elwood,
University of British Columbia</span></p>

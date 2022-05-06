 # KikuchiAikenLRB

<p>This command is used to construct a uniaxial KikuchiAikenLRB material
object. This material model produces nonlinear hysteretic curves of
lead-rubber bearings.</p>

```tcl
uniaxialMaterial KikuchiAikenLRB $matTag $type $ar $hr
        $gr $ap $tp $alph $beta &lt;-T $temp&gt; &lt;-coKQ $rk $rq&gt;
        &lt;-coMSS $rs $rf&gt;
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">type</code></td>
<td><p>rubber type (see note 1)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ar</code></td>
<td><p>area of rubber <strong>[unit: m^2]</strong></p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">hr</code></td>
<td><p>total thickness of rubber <strong>[unit: m]</strong></p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">gr</code></td>
<td><p>shear modulus of rubber <strong>[unit: N/m^2]</strong></p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ap</code></td>
<td><p>area of lead plug <strong>[unit: m^2]</strong></p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">tp</code></td>
<td><p>yield stress of lead plug <strong>[unit: N/m^2]</strong></p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alph</code></td>
<td><p>shear modulus of lead plug <strong>[unit:
N/m^2]</strong></p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">beta</code></td>
<td><p>ratio of initial stiffness to yielding stiffness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">temp</code></td>
<td><p>temperature <strong>[unit: &amp;deg;C]</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>$rk $rq</strong></p></td>
<td><p>reduction rate for yielding stiffness (<strong>$rk</strong>) and
force at zero displacement (<strong>$rq</strong>)</p></td>
</tr>
<tr class="even">
<td><p><strong>$rs $rf</strong></p></td>
<td><p>reduction rate for stiffness (<strong>$rs</strong>) and force
(<strong>$rf</strong>) (see note 3)</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<p>1) Following rubber types for <strong>$type</strong> are
available:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>1</strong></p></td>
<td><p>lead-rubber bearing, up to 400% shear strain [Kikuchi et al.,
2010 &amp; 2012]</p></td>
</tr>
</tbody>
</table>
<p>2) This material uses SI unit in calculation formula. Input arguments
must be converted into <strong>[m]</strong>, <strong>[m^2]</strong>,
<strong>[N/m^2]</strong>.</p>
<p>3) <strong>$rs</strong> and <strong>$rf</strong> are available if
this material is applied to multipleShearSpring (MSS) element.
Recommended values are <strong>$rs</strong>=1/sum(i=0,n-1){
sin(pi*i/n)^2} and <strong>$rf</strong>=1/sum(i=0,n-1){sin(pi*i/n)},
where n is the number of springs in the MSS. For example, when n=8,
$rs=0.2500 and $rf=0.1989.</p>
<hr />
<p>EXAMPLE:</p>
<p><a href="Media:KikuchiAikenLRB_sample.tcl"
title="wikilink">KikuchiAikenLRB_sample.tcl</a></p>
<figure>
<img src="/OpenSeesRT/contrib/static/KikuchiAikenLRB_ForceStrain.png"
title="KikuchiAikenLRB_ForceStrain.png" width="300"
alt="KikuchiAikenLRB_ForceStrain.png" />
<figcaption
aria-hidden="true">KikuchiAikenLRB_ForceStrain.png</figcaption>
</figure>
<p>REFERENCES:</p>
<p>M. Kikuchi, T. Nakamura, I. D. Aiken, "Three-dimensional analysis for
square seismic isolation bearings under large shear deformations and
high axial loads", <em>Earthquake Engineering and Structural
Dynamics</em>, Vol. 39, 1513-1531, 2010.</p>
<p>M. Kikuchi , I. D. Aiken, A. Kasalanati , "Simulation analysis for
the ultimate behavior of full-scale lead-rubber seismic isolation
bearings", <em>15th World Conference on Earthquake Engineering</em>, No.
1688, 2012.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> mkiku
</span></p>

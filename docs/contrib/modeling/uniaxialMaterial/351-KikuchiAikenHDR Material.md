# KikuchiAikenHDR

<p>This command is used to construct a uniaxial `KikuchiAikenHDR` material
object. This material model produces nonlinear hysteretic curves of high
damping rubber bearings (HDRs).</p>

```tcl
uniaxialMaterial KikuchiAikenHDR $matTag $tp $ar $hr
        < -coGHU $cg $ch $cu > 
        < -coMSS $rs $rf >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">tp</code></td>
<td><p>rubber type (see note 1)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ar</code></td>
<td><p>area of rubber <strong>[unit: m^2]</strong> (see note 2)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">hr</code></td>
<td><p>total thickness of rubber <strong>[unit: m]</strong> (see note
2)</p></td>
</tr>
<tr class="odd">
<td><p><code>cg ch cu</code></p></td>
<td><p>correction coefficients for equivalent shear modulus
(<code class="tcl-variable">cg</code>), equivalent viscous daming ratio
(<code class="tcl-variable">ch</code>), ratio of shear force at zero displacement
(<code class="tcl-variable">cu</code>).</p></td>
</tr>
<tr class="even">
<td><p>`rs` `rf`</p></td>
<td><p>reduction rate for stiffness (<code class="tcl-variable">rs</code>) and force
(<code class="tcl-variable">rf</code>) (see note 3)</p></td>
</tr>
</tbody>
</table>

## Notes

1. Following rubber types for <code class="tcl-variable">tp</code> are available:</p>
     <table>
     <tbody>
     <tr class="odd">
     <td><p><strong>X0.6</strong></p></td>
     <td><p>Bridgestone X0.6, standard compressive stress, up to 400% shear
     strain</p></td>
     </tr>
     <tr class="even">
     <td><p><strong>X0.6-0MPa</strong></p></td>
     <td><p>Bridgestone X0.6, zero compressive stress, up to 400% shear
     strain</p></td>
     </tr>
     <tr class="odd">
     <td><p><strong>X0.4</strong></p></td>
     <td><p>Bridgestone X0.4, standard compressive stress, up to 400% shear
     strain</p></td>
     </tr>
     <tr class="even">
     <td><p><strong>X0.4-0MPa</strong></p></td>
     <td><p>Bridgestone X0.4, zero compressive stress, up to 400% shear
     strain</p></td>
     </tr>
     <tr class="odd">
     <td><p><strong>X0.3</strong></p></td>
     <td><p>Bridgestone X0.3, standard compressive stress, up to 400% shear
     strain</p></td>
     </tr>
     <tr class="even">
     <td><p><strong>X0.3-0MPa</strong></p></td>
     <td><p>Bridgestone X0.3, zero compressive stress, up to 400% shear
     strain</p></td>
     </tr>
     </tbody>
     </table>

2. This material uses SI unit in calculation formula.
<code class="tcl-variable">ar</code> and <code class="tcl-variable">hr</code> must be converted into
<strong>[m^2]</strong> and <strong>[m]</strong>, respectively.

3. <code class="tcl-variable">rs</code> and <code class="tcl-variable">rf</code> are　available if
this material is applied to multipleShearSpring (MSS) element.
Recommended values are <code class="tcl-variable">rs</code>=1/sum(i=0,n-1){
sin(pi*i/n)^2} and <code class="tcl-variable">rf</code>=1/sum(i=0,n-1){sin(pi*i/n)},
where n is the number of springs in the MSS. For example, when `n=8`,
`rs=0.2500`, `rf=0.1989`.

<hr />

## Examples

<p><a href="Media:KikuchiAikenHDR_sample.tcl"
title="wikilink">KikuchiAikenHDR_sample.tcl</a></p>
<figure>
<img src="/OpenSeesRT/contrib/static/KikuchiAikenHDR_StressStrain.png"
title="KikuchiAikenHDR_StressStrain.png" width="300"
alt="KikuchiAikenHDR_StressStrain.png" />
<figcaption
aria-hidden="true">KikuchiAikenHDR_StressStrain.png</figcaption>
</figure>
<hr />
<p>Code Developed by: <span style="color:blue"> mkiku
</span></p>

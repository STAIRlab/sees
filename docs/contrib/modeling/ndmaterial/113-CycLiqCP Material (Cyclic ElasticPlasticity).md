# CycLiqCP Material (Cyclic ElasticPlasticity)

<p>This command is used to construct a multi-dimensional material object
that that follows the constitutive behavior of a cyclic elastoplasticity
model for large post- liquefaction deformation.</p>

```tcl
nDmaterial CycLiqCP $matTag $G0 $kappa $h $Mfc $dre1 $Mdc
        $dre2 $rdr $alpha $dir $ein &lt;$rho&gt;
```
<p>CycLiqCP material is a cyclic elastoplasticity model for large
post-liquefaction deformation, and is implemented using a cutting plane
algorithm. The model is capable of reproducing small to large
deformation in the pre- to post-liquefaction regime. The elastic moduli
of the model are pressure dependent. The plasticity in the model is
developed within the framework of bounding surface plasticity, with
special consideration to the formulation of reversible and irreversible
dilatancy.</p>
<p>The model does not take into consideration of the state of sand, and
requires different parameters for sand under different densities and
confining pressures. The surfaces (i.e. failure and maximum pre-stress)
are considered as circles in the pi plane.</p>
<p>The model has been validated against VELACS centrifuge model tests
and has used on numerous simulations of liquefaction related
problems.</p>
<p>When this material is employed in regular solid elements (e.g.,
FourNodeQuad, Brick), it simulates drained soil response. When
solid-fluid coupled elements (u-p elements and SSP u-p elements) are
used, the model is able to simulate undrained and partially drained
behavior of soil.</p>
<p>During the application of gravity load (and static loads if any), the
user is suggested to set the material behavior to be linear elastic,
with the updateMaterialStage command:</p>
<p>updateMaterialStage -material $matTag -stage 0</p>
<p>After the gravity load stage, the material stage should be updated to
achieve the desired elastic-plastic stress-strain response.</p>
<p>updateMaterialStage -material $matTag -stage 1</p>
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">G0</code></td>
<td><p>A constant related to elastic shear modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">kappa</code></td>
<td><p>A constant related to elastic bulk modulus</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">h</code></td>
<td><p>Model parameter for plastic modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Mfc</code></td>
<td><p>Stress ratio at failure in triaxial compression</p></td>
</tr>
<tr class="even">
<td><p><strong>$dre1</strong></p></td>
<td><p>Coefficient for reversible dilatancy generation</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Mdc</code></td>
<td><p>Stress ratio at which the reversible dilatancy sign
changes</p></td>
</tr>
<tr class="even">
<td><p><strong>$dre2</strong></p></td>
<td><p>Coefficient for reversible dilatancy release</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rdr</code></td>
<td><p>Reference shear strain length</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>Parameter controlling the decrease rate of irreversible
dilatancy</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">dir</code></td>
<td><p>Coefficient for irreversible dilatancy potential</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ein</code></td>
<td><p>Initial void ratio</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>Saturated mass density</p></td>
</tr>
</tbody>
</table>
<p>The material formulations for the CycLiqCP object are
"ThreeDimensional" and "PlaneStrain".</p>
<p>NOTES:</p>
<ol>
<li>The elastic modulii are given by the following relations:</li>
</ol>
<figure>
<img src="/OpenSeesRT/contrib/static/CycLiqCp.GIF" title="CycLiqCp.GIF" alt="CycLiqCp.GIF" />
<figcaption aria-hidden="true">CycLiqCp.GIF</figcaption>
</figure>
<hr />
<p>REFERENCES: Zhang J.M. and Wang G., 2012, “Large post-liquefaction
deformation of sand, part I: physical mechanism, constitutive
description and numerical algorithm”, Acta Geotechnica.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Rui Wang, Tsinghua
University</span></p>

 # CycLiqCPSP

<p>This command is used to construct a multi-dimensional material object
based on a unified plasticity model for large post-liquefaction shear
deformation of sand.</p>

```tcl
nDmaterial CycLiqCPSP $matTag $G0 $kappa $h $M $dre1
        $dre2 $rdr $alpha $dir $lambdac $ksi $e0 $np $nd $ein
        &lt;$rho&gt;
```

<p>CycLiqCPSP material is a constitutive model for sand with special
considerations for cyclic behaviour and accumulation of large
post-liquefaction shear deformation, and is implemented using a cutting
plane algorithm. The model: (1) achieves the simulation of
post-liquefaction shear deformation based on its physics, allowing the
unified description of pre- and post-liquefaction behavior of sand; (2)
directly links the cyclic mobility of sand with reversible and
irreversible dilatancy, enabling the unified description of monotonic
and cyclic loading; (3) introduces critical state soil mechanics
concepts to achieve unified modelling of sand under different
states.</p>
<p>The critical, maximum stress ratio and reversible dilatancy surfaces
follow a rounded triangle in the pi plane similar to the Matsuoka-Nakai
criterion.</p>
<p>When this material is employed in regular solid elements (e.g.,
FourNodeQuad, Brick), it simulates drained soil response. When
solid-fluid coupled elements (u-p elements and SSP u-p elements) are
used, the model is able to simulate undrained and partially drained
behavior of soil.</p>
<p>During the application of gravity load (and static loads if any), the
user is suggested to set the material behavior to be non-linear elastic,
with the updateMaterialStage command:</p>
<p>updateMaterialStage -material $matTag -stage 0</p>
<p>After the gravity load stage, the material stage should be updated to
achieve the desired elastic-plastic stress-strain response.</p>
<p>updateMaterialStage -material $matTag -stage 1</p>
<p>If a linear elastic stage is required, it can be achieved
through:</p>
<p>updateMaterialStage -material $matTag -stage 2</p>
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
<td><code class="parameter-table-variable">M</code></td>
<td><p>Critical state stress ratio</p></td>
</tr>
<tr class="even">
<td><p><strong>$dre1</strong></p></td>
<td><p>Coefficient for reversible dilatancy generation</p></td>
</tr>
<tr class="odd">
<td><p><strong>$dre2</strong></p></td>
<td><p>Coefficient for reversible dilatancy release</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rdr</code></td>
<td><p>Reference shear strain length</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>Parameter controlling the decrease rate of irreversible
dilatancy</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dir</code></td>
<td><p>Coefficient for irreversible dilatancy potential</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">lambdac</code></td>
<td><p>Critical state constant</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ksi</code></td>
<td><p>Critical state constant</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">e0</code></td>
<td><p>Void ratio at pc=0</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">np</code></td>
<td><p>Material constant for peak mobilized stress ratio</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nd</code></td>
<td><p>Material constant for reversible dilatancy generation stress
ratio</p></td>
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
<p>The material formulations for the CycLiqCPSP object are
"ThreeDimensional" and "PlaneStrain".</p>
<hr />
<p>REFERENCES: Wang R., Zhang J.M., Wang G., 2014. A unified plasticity
model for large post-liquefaction shear deformation of sand. Computers
and Geotechnics. 59, 54-66.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Rui Wang, Tsinghua
University</span></p>

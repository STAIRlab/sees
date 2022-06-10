# DoddRestrepo

<p>This command is used to construct a Dodd-Restrepo steel material</p>

```tcl
uniaxialMaterial Dodd_Restrepo $tag $Fy $Fsu $ESH $ESU
        $Youngs $ESHI $FSHI < $OmegaFac >
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>Integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Fy</code></td>
<td><p>Yield strength</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Fsu</code></td>
<td><p>Ultimate tensile strength (UTS)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ESH</code></td>
<td><p>Tensile strain at initiation of strain hardening</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ESU</code></td>
<td><p>Tensile strain at the UTS</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Youngs</code></td>
<td><p>Modulus of elasticity</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ESHI</code></td>
<td><p>Tensile strain for a point on strain hardening curve, recommended
range of values for ESHI: [ (ESU + 5*ESH)/6, (ESU + 3*ESH)/4]</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">FSHI</code></td>
<td><p>Tensile stress at point on strain hardening curve corresponding
to ESHI</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">OmegaFac</code></td>
<td><p>Roundedness factor for Bauschinger curve in cycle reversals from
the strain hardening curve. Range: [0.75, 1.15]. Largest value tends to
near a bilinear Bauschinger curve. Default = 1.0.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Note: Stresses and strains are defined in engineering terms, as they
are reported in a tensile test.</p>
<hr />
<p><strong>Examples:</strong></p>
<hr />
<p><strong>References</strong>:</p>
<p>Code developed by: <span style="color:blue"> L.L. Dodd &amp;
J.I. Restrepo </span></p>
<p><a
href="http://ascelibrary.org/sto/resource/1/jsendh/v121/i3/p433_s1?isAuthorized=no">Dodd,
L. L. and Restrepo-Posada, J. I. (1995). Model for Predicting Cyclic
Behaviour of Reinforcing Steel. ASCE Journal of Structural Engineering,
V.121, No 3, pp. 433-445.</a></p>

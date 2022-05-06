 # SelfCentering

<p>This command is used to construct a uniaxial self-centering
(flag-shaped) material object with optional non-recoverable slip
behaviour and an optional stiffness increase at high strains (bearing
behaviour).</p>
<p>This material is primarily used to model a self-centering
energy-dissipative (SCED) brace (Christopoulos et al., 2008) with the
option to model the slippage of an external friction fuse (which causes
non-recoverable deformation above a given brace strain). In practice,
the external friction fuse is used to limit the amount of force in the
brace (since the post-activation stiffness is generally non-zero). The
bearing option is used to approximately model the effect of bolt bearing
in the brace or external fuse mechanisms, which causes a steep increase
in the stiffness of the brace. For self-centering energy-dissipative
brace design, this bearing effect model may be used to impose a limit on
slip or activation strain based on the anticipated available strain
capacity of the mechanism. Note that this bearing effect is only
intended to be a flag to indicate the existence of bearing; the SCED
brace system should be designed such that the brace will not experience
such bearing in practice.</p>
<p>This material type could potentially be used for any comparable
self-centering system that exhibits a flag-shaped hysteretic response
(for example: rocking wall systems if the uniaxial material is used as a
moment/rotation hysteresis).</p>

```tcl
uniaxialMaterial SelfCentering $matTag $k1 $k2 $sigAct
        $beta &lt;$epsSlip&gt; &lt;$epsBear&gt; &lt;rBear&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">k1</code></p></td>
<td><p>Initial Stiffness</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">k2</code></p></td>
<td><p>Post-Activation Stiffness (0&lt;$k2&lt;$k1)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sigAct</code></td>
<td><p>Forward Activation Stress/Force</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">beta</code></td>
<td><p>Ratio of Forward to Reverse Activation Stress/Force</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">epsSlip</code></td>
<td><p>slip Strain/Deformation (if $epsSlip = 0, there will be no
slippage)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsBear</code></td>
<td><p>Bearing Strain/Deformation (if $epsBear = 0, there will be no
bearing)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rBear</code></td>
<td><p>Ratio of Bearing Stiffness to Initial Stiffness $k1</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/SC1.png" title="SC1.png" alt="SC1.png" />
<figcaption aria-hidden="true">SC1.png</figcaption>
</figure>
<p><img src="/OpenSeesRT/contrib/static/SC2.png" title="SC2.png" alt="SC2.png" /> <img
src="SC3.png" title="SC3.png" alt="SC3.png" /></p>
<p><img src="/OpenSeesRT/contrib/static/SC4.png" title="SC4.png" alt="SC4.png" /> <img
src="SC5.png" title="SC5.png" alt="SC5.png" /></p>
<p><img src="/OpenSeesRT/contrib/static/SC6.png" title="SC6.png" alt="SC6.png" /> <img
src="SC7.png" title="SC7.png" alt="SC7.png" /></p>
<hr />
<p>REFERENCES:</p>
<p>Christopoulos, C., Tremblay, R., Kim, H.-J., and Lacerte, M. (2008).
"Self-Centering Energy Dissipative Bracing System for the Seismic
Resistance of Structures: Development and Validation" Journal of
Structural Engineering ASCE, 134(1), 96-107.</p>
<p>Tremblay, R., Lacerte, M., and Christopoulos, C. (2008). "Seismic
Response of Multistory Buildings with Self-Centering Energy Dissipative
Steel Braces" Journal of Structural Engineering ASCE, 134(1),
108-120.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Jeff Erochko,
University of Toronto</span></p>

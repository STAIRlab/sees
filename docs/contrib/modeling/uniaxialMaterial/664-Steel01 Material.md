# Steel01

<p>This command is used to construct a uniaxial bilinear steel material
object with kinematic hardening and optional isotropic hardening
described by a non-linear evolution equation (REF: Fedeas).</p>

```tcl
uniaxialMaterial Steel01 $matTag $Fy $E0 $b
        < $a1 $a2 $a3 $a4 >
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Fy</code></td>
<td><p>yield strength</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">E0</code></td>
<td><p>initial elastic tangent</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">b</code></td>
<td><p>strain-hardening ratio (ratio between post-yield tangent and
initial elastic tangent)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">a1</code></p></td>
<td><p>isotropic hardening parameter, increase of compression yield
envelope as proportion of yield strength after a plastic strain of
$a2*($Fy/E0). (optional)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">a2</code></p></td>
<td><p>isotropic hardening parameter (see explanation under $a1).
(optional).</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">a3</code></p></td>
<td><p>isotropic hardening parameter, increase of tension yield envelope
as proportion of yield strength after a plastic strain of $a4*($Fy/E0).
(optional)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">a4</code></p></td>
<td><p>isotropic hardening parameter (see explanation under $a3).
(optional)</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/Steel01.gif" title="Steel01.gif" alt="Steel01.gif" />
<figcaption aria-hidden="true">Steel01.gif</figcaption>
</figure>
<p>Steel01 Material -- Hysteretic Behavior of Model w/o Isotropic
Hardening</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Steel01HystereticA.jpg" title="Steel01HystereticA.jpg"
alt="Steel01HystereticA.jpg" />
<figcaption aria-hidden="true">Steel01HystereticA.jpg</figcaption>
</figure>
<p>Steel01 Material -- Hysteretic Behavior of Model with Isotropic
Hardening in Compression</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Steel01HystereticB.jpg" title="Steel01HystereticB.jpg"
alt="Steel01HystereticB.jpg" />
<figcaption aria-hidden="true">Steel01HystereticB.jpg</figcaption>
</figure>
<p>Steel01 Material -- Hysteretic Behavior of Model with Isotropic
Hardening in Tension</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Steel01HystereticC.jpg" title="Steel01HystereticC.jpg"
alt="Steel01HystereticC.jpg" />
<figcaption aria-hidden="true">Steel01HystereticC.jpg</figcaption>
</figure>
<hr />
<p>NOTES:</p>
<ul>
<li>If strain-hardening ratio is zero and you do not expect softening of
your system use BandSPD solver.</li>
</ul>
<hr />
<p>Code Developed by: <span style="color:blue"> Filip Filippou, UC
Berkeley </span></p>
<p>Images Developed by: <span style="color:blue"> Silvia Mazzoni
</span></p>

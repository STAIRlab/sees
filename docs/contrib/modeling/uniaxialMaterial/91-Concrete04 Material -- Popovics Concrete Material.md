# Concrete04 Material -- Popovics Concrete Material

<p>This command is used to construct a uniaxial Popovics concrete
material object with degraded linear unloading/reloading stiffness
according to the work of Karsan-Jirsa and tensile strength with
exponential decay.</p>

```tcl
uniaxialMaterial Concrete04 $matTag $fc $ec $ecu $Ec
        &lt;$fct $et&gt; &lt;$beta&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fc</code></td>
<td><p>floating point values defining concrete compressive strength at
28 days (compression is negative)*</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ec</code></td>
<td><p>floating point values defining concrete strain at maximum
strength*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ecu</code></td>
<td><p>floating point values defining concrete strain at crushing
strength*</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Ec</code></td>
<td><p>floating point values defining initial stiffness**</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fct</code></td>
<td><p>floating point value defining the maximum tensile strength of
concrete</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">et</code></td>
<td><p>floating point value defining ultimate tensile strain of
concrete</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">beta</code></td>
<td><p>loating point value defining the exponential curve parameter to
define the residual stress (as a factor of $ft) at $etu</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<ul>
<li>Compressive concrete parameters should be input as negative
values.</li>
<li>The envelope of the compressive stress-strain response is defined
using the model proposed by Popovics (1973). If the user defines
<strong>Ec = 57000*sqrt(|fcc|)(in psi)</strong>' then the envelope curve
is identical to proposed by Mander et al. (1988).</li>
<li>Model Characteristic: For loading in compression, the envelope to
the stress-strain curve follows the model proposed by Popovics (1973)
until the concrete crushing strength is achieved and also for strains
beyond that corresponding to the crushing strength. For unloading and
reloading in compression, the Karsan-Jirsa model (1969) is used to
determine the slope of the curve. For tensile loading, an exponential
curve is used to define the envelope to the stress-strain curve. For
unloading and reloading in tensile, the secant stiffness is used to
define the path.</li>
</ul>
<figure>
<img src="/OpenSeesRT/contrib/static/Concrete04A.png" title="Concrete04A.png"
alt="Concrete04A.png" />
<figcaption aria-hidden="true">Concrete04A.png</figcaption>
</figure>
<figure>
<img src="/OpenSeesRT/contrib/static/Concrete0B.png" title="Concrete0B.png" alt="Concrete0B.png" />
<figcaption aria-hidden="true">Concrete0B.png</figcaption>
</figure>
<p>REFERENCES: Reference:</p>
<ul>
<li>Mander, J. B., Priestley, M. J. N., and Park, R. (1988).
"Theoretical stress-strain model for confined concrete." Journal of
Structural Engineering ASCE, 114(8), 1804-1825.</li>
</ul>
<ul>
<li>Popovics, S. (1973). " A numerical approach to the complete stress
strain curve for concrete." Cement and concrete research, 3(5),
583-599.</li>
</ul>
<ul>
<li>Karsan, I. D., and Jirsa, J. O. (1969). "Behavior of concrete under
compressive loading." Journal of Structural Division ASCE,
95(ST12).</li>
</ul>
<hr />
<p>Code Developed by: <span style="color:blue"> Laura Lowes,
University of Washington </span> and 
<span style="color:blue"> Michael Berry, University of Washington
</span></p>
<p>Images Developed by: <span style="color:blue"> Silvia Mazzoni
</span></p>

 # PM4Sand

<ul>
<li><strong>This page has been moved to the new <a
href="https://opensees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/PM4Sand.html">OpenSees
documentation site</a></strong></li>
</ul>
<p>This command is used to construct a 2-dimensional PM4Sand
material.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDmaterial PM4Sand $matTag $Dr $G0 $hpo $Den &lt;$patm
$h0 $emax $emin $nb $nd $Ado $zmax $cz $ce $phic $nu $cgd $cdr $ckaf $Q
$R $m $Fsed_min $p_sedo&gt;</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p><strong>Primary</strong>:</p></td>
<td></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Dr</code></td>
<td><p>Relative density, in fraction</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">G0</code></td>
<td><p>Shear modulus constant</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">hpo</code></td>
<td><p>Contraction rate parameter</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Den</code></td>
<td><p>Mass density of the material</p></td>
</tr>
<tr class="even">
<td><p><strong>Secondary</strong>:</p></td>
<td></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">P_atm</code></td>
<td><p><em>Optional</em>, Atmospheric pressure</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">h0</code></td>
<td><p><em>Optional</em>, Variable that adjusts the ratio of plastic
modulus to elastic modulus</p></td>
</tr>
<tr class="odd">
<td><p><strong>$emax and $emin</strong></p></td>
<td><p><em>Optional</em>, Maximum and minimum void ratios</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">nb</code></td>
<td><p><em>Optional</em>, Bounding surface parameter, $nb &amp;ge;
0</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nd</code></td>
<td><p><em>Optional</em>, Dilatancy surface parameter $nd &amp;ge;
0</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ado</code></td>
<td><p><em>Optional</em>, Dilatancy parameter, will be computed at the
time of initialization if input value is negative</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">z_max</code></td>
<td><p><em>Optional</em>, Fabric-dilatancy tensor parameter</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">cz</code></td>
<td><p><em>Optional</em>, Fabric-dilatancy tensor parameter</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ce</code></td>
<td><p><em>Optional</em>, Variable that adjusts the rate of strain
accumulation in cyclic loading</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">phic</code></td>
<td><p><em>Optional</em>, Critical state effective friction
angle</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nu</code></td>
<td><p><em>Optional</em>, Poisson's ratio</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">cgd</code></td>
<td><p><em>Optional</em>, Variable that adjusts degradation of elastic
modulus with accumulation of fabric</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">cdr</code></td>
<td><p><em>Optional</em>, Variable that controls the rotated dilatancy
surface</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ckaf</code></td>
<td><p><em>Optional</em>, Variable that controls the effect that
sustained static shear stresses have on plastic modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Q</code></td>
<td><p><em>Optional</em>, Critical state line parameter</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">R</code></td>
<td><p><em>Optional</em>, Critical state line parameter</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">m</code></td>
<td><p><em>Optional</em>, Yield surface constant (radius of yield
surface in stress ratio space)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Fsed_min</code></td>
<td><p><em>Optional</em>, Variable that controls the minimum value the
reduction factor of the elastic moduli can get during
reconsolidation</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">p_sedo</code></td>
<td><p><em>Optional</em>, Mean effective stress up to which
reconsolidation strains are enhanced</p></td>
</tr>
</tbody>
</table>
<p>The material formulation for the PM4Sand object is "PlaneStrain"</p>
<hr />
<p>Code Developed by: <span style="color:blue">Long Chen, <a
href="https://www.ce.washington.edu/people/faculty/arduinop">Pedro
Arduino, U Washington</a></span></p>
<hr />
<h2 id="notes">Notes</h2>
<ul>
<li><strong>This page has been moved to the new <a
href="https://opensees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/PM4Sand.html">OpenSees
documentation site</a></strong></li>
</ul>
<ul>
<li>Valid Element Recorder queries are
<ul>
<li><strong>stress</strong>, <strong>strain</strong></li>
<li><strong>alpha</strong> (or <strong>backstressratio</strong>) for
&lt;math&gt;\mathbf{\alpha}&lt;/math&gt;</li>
<li><strong>fabric</strong> for $\mathbf{z}$</li>
<li><strong>alpha_in</strong> (or <strong>alphain</strong>) for
&lt;math&gt;\mathbf{\alpha_{in}}&lt;/math&gt;</li>
</ul></li>
</ul>
<p>e.g. recorder Element -eleRange 1 $numElem -time -file stress.out
stress</p>
<ul>
<li>Elastic or Elastoplastic response could be enforced by</li>
</ul>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
{|
</dd>
</dl>
</dd>
</dl>
<p>|Elastic: ||updateMaterialStage -material $matTag -stage 0 |-
|Elastoplastic: ||updateMaterialStage -material $matTag -stage 1 |}</p>
<ul>
<li>The program will use the default value of a secondary parameter if a
negative input is assigned to that parameter, e.g. Ado = -1. However,
FirstCall is mandatory when switching from elastic to elastoplastic if
negative inputs are assigned to stress-dependent secondary parameters,
e.g. Ado and zmax. FirstCall can be set as,</li>
</ul>
<p>setParameter -value 0 -ele $elementTag FirstCall $matTag</p>
<ul>
<li>Post-shake reconsolidation can be activated by</li>
</ul>
<p>setParameter -value 1 -ele $elementTag Postshake $matTag</p>
<ul>
<li>The user should check that the results are not sensitive to time
step size.</li>
</ul>
<h2 id="example">Example</h2>
<p>&lt;table border=1 width=600&gt; &lt;tr&gt; &lt;td width=90&gt;<a
href="PM4Sand-Example_1" title="wikilink">Example 1</a> &lt;/td&gt;</p>
<p>&lt;td&gt;2D undrained monotonic direct simple shear test using one
element&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PM4Sand-Example_2" title="wikilink">Example 2</a>&lt;/td&gt;
&lt;td&gt;2D undrained cyclic direct simple shear test using one
element&lt;/td&gt; &lt;/tr&gt;</p>
<p>&lt;/table&gt;</p>
<h2 id="references">References</h2>
<p>R.W.Boulanger, K.Ziotopoulou. "PM4Sand(Version 3.1): A Sand
Plasticity Model for Earthquake Engineering Applications". Report No.
UCD/CGM-17/01 2017</p>

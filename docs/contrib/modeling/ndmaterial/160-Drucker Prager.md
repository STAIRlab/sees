# Drucker Prager

<p>This command is used to construct an multi dimensional material
object that has a Drucker-Prager yield criterium.</p>

```tcl
nDMaterial DruckerPrager $matTag $k $G $sigmaY $rho
        $rhoBar $Kinf $Ko $delta1 $delta2 $H $theta $density
        &lt;$atmPressure&gt;
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">k</code></td>
<td><p>bulk modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">G</code></td>
<td><p>shear modulus</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sigmaY</code></td>
<td><p>yield stress</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>frictional strength parameter</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rhoBar</code></td>
<td><p>controls evolution of plastic volume change, 0 &amp;le; $rhoBar
&amp;le; $rho</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Kinf</code></td>
<td><p>nonlinear isotropic strain hardening parameter, $Kinf &amp;ge;
0</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ko</code></td>
<td><p>nonlinear isotropic strain hardening parameter, $Ko &amp;ge;
0</p></td>
</tr>
<tr class="odd">
<td><p><strong>$delta1</strong></p></td>
<td><p>nonlinear isotropic strain hardening parameter, $delta1 &amp;ge;
0</p></td>
</tr>
<tr class="even">
<td><p><strong>$delta2</strong></p></td>
<td><p>tension softening parameter, $delta2 &amp;ge; 0</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">H</code></td>
<td><p>linear strain hardening parameter, $H &amp;ge; 0</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">theta</code></td>
<td><p>controls relative proportions of isotropic and kinematic
hardening, 0 &amp;le; $theta &amp;le; 1</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">density</code></td>
<td><p>mass density of the material</p></td>
</tr>
<tr class="even">
<td><p><strong>&lt;$atmPressure&gt;</strong></p></td>
<td><p>optional atmospheric pressure for update of elastic bulk and
shear moduli (default = 101 kPa)</p></td>
</tr>
</tbody>
</table>
<p>The material formulations for the Drucker-Prager object are
"ThreeDimensional" and "PlaneStrain"</p>
<hr />
<p>This code has been Developed by: <span style="color:blue"><a
href="http://www.ce.washington.edu/people/faculty/bios/mackenzie_p.html">Peter
Mackenzie, U Washington</a></span> and the great 
<span style="color:blue"><a
href="http://www.ce.washington.edu/people/faculty/bios/arduino_p.html">Pedro
Arduino, U Washington</a></span></p>
<hr />
<h2 id="theory">Theory</h2>
<p>The yield condition for the Drucker-Prager model can be expressed
as</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; f\left(\mathbf{\sigma}, q^{iso}, \mathbf{q}^{kin}\right) =
\left\| \mathbf{s} + \mathbf{q}^{kin} \right\| + \rho I_1 +
\sqrt{\frac{2}{3}} q^{iso} - \sqrt{\frac{2}{3}} \sigma_Y^{} \leq 0
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<p>in which</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; \mathbf{s} = \mathrm{dev} (\mathbf{\sigma}) =
\mathbf{\sigma} - \frac{1}{3} I_1 \mathbf{1}
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<p>is the deviatoric stress tensor,</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; I_1 = \mathrm{tr}(\mathbf{\sigma})
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<p>is the first invariant of the stress tensor, and the parameters
$\rho_{}^{}$ and
$\sigma_Y^{}$ are positive material
constants.</p>
<p>The isotropic hardening stress is defined as</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; q^{iso} = \theta H \alpha^{iso} + (K_{\infty} - K_o)
\exp(-\delta_1 \alpha^{iso})
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<p>The kinematic hardening stress (or back-stress) is defined as</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; \mathbf{q}^{kin} = -(1 - \theta) \frac{2}{3} H
\mathbb{I}^{dev} : \mathbf{\alpha}^{kin}
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<p>The yield condition for the tension cutoff yield surface is defined
as</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; f_2(\mathbf{\sigma}, q^{ten}) = I_1 + q^{ten} \leq 0
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<p>where</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; q^{ten} = T_o \exp(-\delta_2^{} \alpha^{ten})
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<p>and</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; T_o = \sqrt{\frac{2}{3}} \frac{\sigma_Y}{\rho}
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<p>Further, general, information on theory for the Drucker-Prager yield
criterion can be found at wikipedia <a
href="http://en.wikipedia.org/wiki/Drucker_Prager_yield_criterion">here</a></p>
<h2 id="notes">Notes</h2>
<p>The valid queries to the Drucker-Prager material when creating an
ElementRecorder are 'strain' and 'stress' (as with all nDmaterial) as
well as 'state'. The query 'state' records a vector of state variables
during a particular analysis. The columns of this vector are as follows.
(Note: If the option '-time' is included in the creation of the
recorder, the first column will be the time variable for each recorded
point and the columns below are shifted accordingly.)</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
Column 1 - First invariant of the stress tensor, &lt;math&gt; I_1 =
\mathrm{tr}(\mathbf{\sigma}) &lt;/math&gt;.
</dd>
<dd>
Column 2 - The following tensor norm, &lt;math&gt; \left\| \mathbf{s} +
\mathbf{q}^{kin} \right\| &lt;/math&gt;, where
$\mathbf{s}$ is the deviatoric stress tensor and
$\mathbf{q}^{kin}$ is the back-stress tensor.
</dd>
<dd>
Column 3 - First invariant of the plastic strain tensor, &lt;math&gt;
\mathrm{tr}(\mathbf{\varepsilon}^p) &lt;/math&gt;.
</dd>
<dd>
Column 4 - Norm of the deviatoric plastic strain tensor, &lt;math&gt;
\left\| \mathbf{e}^p \right\| &lt;/math&gt;.
</dd>
</dl>
</dd>
</dl>
<p>The Drucker-Prager strength parameters &lt;math&gt; \rho
&lt;/math&gt; and $\sigma_Y $ can be related to
the Mohr-Coulomb friction angle, $\phi $, and
cohesive intercept, $c $, by evaluating the
yield surfaces in a deviatoric plane as described by Chen and Saleeb
(1994). By relating the two yield surfaces in triaxial compression, the
following expressions are determined</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; \rho = \frac{2 \sqrt{2} \sin \phi}{\sqrt{3} (3 - \sin
\phi)}
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; \sigma_Y = \frac{6 c \cos \phi}{\sqrt{2} (3 - \sin \phi)}
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<h2 id="example">Example</h2>
<p>This example provides the input file and corresponding results for a
confined triaxial compression (CTC) test using a single 8-node brick
element and the Drucker-Prager constitutive model. A schematic
representation of this test is shown below, (a) depicts the application
of hydrostatic pressure, and (b) depicts the application of the deviator
stress. Also shown is the stress path resulting from this test plotted
on the meridian plane. As shown, the element is loaded until failure, at
which point the model can no longer converge, as this is a
stress-controlled analysis.</p>
<p><img src="/OpenSeesRT/contrib/static/CtcTest.png" title="CtcTest.png" alt="CtcTest.png" /> <img
src="CtcResults.png" title="CtcResults.png" alt="CtcResults.png" /></p>
<p>&lt;source lang="tcl"&gt;</p>
<ol>
<li><ol>
<li></li>
</ol></li>
<li>#</li>
<li>File is generated for the purposes of testing the #</li>
<li>Drucker-Prager model --&gt; conventional triaxial #</li>
<li>compression test #</li>
<li>#</li>
<li>Created: 03.16.2009 CRM #</li>
<li>Updated: 12.02.2011 CRM #</li>
<li>#</li>
<li>---&gt; Basic units used are kN and meters #</li>
<li>#
<ol>
<li><ol>
<li></li>
</ol></li>
</ol></li>
</ol>
<ol>
<li><hr /></li>
<li>create the modelBuilder and build the model</li>
<li><hr /></li>
</ol>
<p>wipe</p>
<p>model BasicBuilder -ndm 3 -ndf 3</p>
<ol>
<li>--create the nodes</li>
</ol>
<p>node 1 1.0 0.0 0.0 node 2 1.0 1.0 0.0 node 3 0.0 1.0 0.0 node 4 0.0
0.0 0.0 node 5 1.0 0.0 1.0 node 6 1.0 1.0 1.0 node 7 0.0 1.0 1.0 node 8
0.0 0.0 1.0</p>
<ol>
<li>--triaxial test boundary conditions</li>
</ol>
<p>fix 1 0 1 1 fix 2 0 0 1 fix 3 1 0 1 fix 4 1 1 1 fix 5 0 1 0 fix 6 0 0
0 fix 7 1 0 0 fix 8 1 1 0</p>
<ol>
<li>--define material parameters for the model</li>
<li>---bulk modulus</li>
</ol>
<p>set k 27777.78</p>
<ol>
<li>---shear modulus</li>
</ol>
<p>set G 9259.26</p>
<ol>
<li>---yield stress</li>
</ol>
<p>set sigY 5.0</p>
<ol>
<li>---failure surface and associativity</li>
</ol>
<p>set rho 0.398 set rhoBar 0.398</p>
<ol>
<li>---isotropic hardening</li>
</ol>
<p>set Kinf 0.0 set Ko 0.0 set delta1 0.0</p>
<ol>
<li>---kinematic hardening</li>
</ol>
<p>set H 0.0 set theta 1.0</p>
<ol>
<li>---tension softening</li>
</ol>
<p>set delta2 0.0</p>
<ol>
<li>---mass density</li>
</ol>
<p>set mDen 1.7</p>
<ol>
<li>--material models</li>
<li>type tag k G sigY rho rhoBar Kinf Ko delta1 delta2 H theta
density</li>
</ol>
<p>nDMaterial DruckerPrager 2 $k $G $sigY $rho $rhoBar $Kinf $Ko $delta1
$delta2 $H $theta $mDen</p>
<ol>
<li>--create the element</li>
<li>type tag nodes matID bforce1 bforce2 bforce3</li>
</ol>
<p>element stdBrick 1 1 2 3 4 5 6 7 8 2 0.0 0.0 0.0</p>
<p>puts "model Built..."</p>
<ol>
<li><hr /></li>
<li>create the recorders</li>
<li><hr /></li>
</ol>
<p>set step 0.1</p>
<ol>
<li>record nodal displacements</li>
</ol>
<p>recorder Node -file displacements1.out -time -dT $step -nodeRange 1 8
-dof 1 2 3 disp</p>
<ol>
<li>record the element stress, strain, and state at one of the Gauss
points</li>
</ol>
<p>recorder Element -ele 1 -time -file stress1.out -dT $step material 2
stress recorder Element -ele 1 -time -file strain1.out -dT $step
material 2 strain recorder Element -ele 1 -time -file state1.out -dT
$step material 2 state</p>
<p>puts "recorders set..."</p>
<ol>
<li><hr /></li>
<li>create the loading</li>
<li><hr /></li>
</ol>
<ol>
<li>--pressure magnitude</li>
</ol>
<p>set p 10.0 set pNode [expr -$p/4]</p>
<ol>
<li>--loading object for hydrostatic pressure</li>
</ol>
<p>pattern Plain 1 {Series -time {0 10 100} -values {0 1 1} -factor 1} {
load 1 $pNode 0.0 0.0 load 2 $pNode $pNode 0.0 load 3 0.0 $pNode 0.0
load 5 $pNode 0.0 0.0 load 6 $pNode $pNode 0.0 load 7 0.0 $pNode 0.0
}</p>
<ol>
<li>--loading object deviator stress</li>
</ol>
<p>pattern Plain 2 {Series -time {0 10 100} -values {0 1 5} -factor 1} {
load 5 0.0 0.0 $pNode load 6 0.0 0.0 $pNode load 7 0.0 0.0 $pNode load 8
0.0 0.0 $pNode }</p>
<ol>
<li><hr /></li>
<li>create the analysis</li>
<li><hr /></li>
</ol>
<p>integrator LoadControl 0.1 numberer RCM system SparseGeneral
constraints Transformation test NormDispIncr 1e-5 10 1 algorithm Newton
analysis Static</p>
<p>puts "starting the hydrostatic analysis..." set startT [clock
seconds] analyze 1000</p>
<p>set endT [clock seconds] puts "triaxial shear application
finished..." puts "loading analysis execution time: [expr $endT-$startT]
seconds."</p>
<p>wipe &lt;/source&gt;</p>
<h2 id="references">References</h2>
<p>Drucker, D. C. and Prager, W., "Soil mechanics and plastic analysis
for limit design." Quarterly of Applied Mathematics, vol. 10, no. 2, pp.
157-165, 1952.</p>
<p>Chen, W. F. and Saleeb, A. F., Constitutive Equations for Engineering
Materials Volume I: Elasticity and Modeling. Elsevier Science B.V.,
Amsterdam, 1994.</p>

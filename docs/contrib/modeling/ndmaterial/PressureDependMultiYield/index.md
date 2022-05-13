# PressureDependMultiYield

<p><strong>PressureDependMultiYield</strong> material is an
elastic-plastic material for simulating the essential response
characteristics of pressure sensitive soil materials under general
loading conditions. Such characteristics include dilatancy
(shear-induced volume contraction or dilation) and non-flow liquefaction
(cyclic mobility), typically exhibited in sands or silts during
monotonic or cyclic loading.</p>
<p>When this material is employed in regular solid elements (e.g.,
FourNodeQuad, Brick), it simulates drained soil response. To simulate
soil response under fully undrained condition, this material may be
either embedded in a <strong><a href="FluidSolidPorousMaterial"
title="wikilink">FluidSolidPorousMaterial</a></strong>, or used with one
of the solid-fluid fully coupled elements (<a
href="Four_Node_Quad_u-p_Element" title="wikilink">Four Node Quad u-p
Element</a>, <a href="Nine_Four_Node_Quad_u-p_Element"
title="wikilink">Nine Four Node Quad u-p Element</a>, <a
href="Brick_u-p_Element" title="wikilink">Brick u-p Element</a>, <a
href="Twenty_Eight_Node_Brick_u-p_Element" title="wikilink">Twenty Eight
Node Brick u-p Element</a>) with very low permeability. To simulate
partially drained soil response, this material should be used with a
solid-fluid fully coupled element with proper permeability values.</p>
<p>During the application of gravity load (and static loads if any),
material behavior is linear elastic. In the subsequent dynamic (fast)
loading phase(s), the stress-strain response is elastic-plastic (see <a
href="updateMaterialStage" title="wikilink">updateMaterialStage</a>).
Plasticity is formulated based on the multi-surface (nested surfaces)
concept, with a non-associative flow rule to reproduce dilatancy effect.
The yield surfaces are of the <a
href="http://en.wikipedia.org/wiki/Drucker_Prager_yield_criterion">Drucker-Prager</a>
type.</p>
<p>OUTPUT INTERFACE:</p>
<p>The following information may be extracted for this material at a
given integration point, using the OpenSees Element Recorder facility
(McKenna and Fenves 2001)&lt;sup&gt;<a href="Soil_Models_References"
title="wikilink">&amp;reg;</a>&lt;/sup&gt;: "<strong>stress</strong>",
"<strong>strain</strong>", "<strong>backbone</strong>", or
"<strong>tangent</strong>".</p>
<p>For 2D problems, the stress output follows this order:
&amp;sigma;&lt;sub&gt;xx&lt;/sub&gt;,
&amp;sigma;&lt;sub&gt;yy&lt;/sub&gt;,
&amp;sigma;&lt;sub&gt;zz&lt;/sub&gt;,
&amp;sigma;&lt;sub&gt;xy&lt;/sub&gt;, &amp;eta;&lt;sub&gt;r&lt;/sub&gt;,
where &amp;eta;&lt;sub&gt;r&lt;/sub&gt; is the ratio between the shear
(deviatoric) stress and peak shear strength at the current confinement
(0&lt;=&amp;eta;&lt;sub&gt;r&lt;/sub&gt;&lt;=1.0). The strain output
follows this order: &amp;epsilon;&lt;sub&gt;xx&lt;/sub&gt;,
&amp;epsilon;&lt;sub&gt;yy&lt;/sub&gt;,
&amp;gamma;&lt;sub&gt;xy&lt;/sub&gt;.</p>
<p>For 3D problems, the stress output follows this order:
&amp;sigma;&lt;sub&gt;xx&lt;/sub&gt;,
&amp;sigma;&lt;sub&gt;yy&lt;/sub&gt;,
&amp;sigma;&lt;sub&gt;zz&lt;/sub&gt;,
&amp;sigma;&lt;sub&gt;xy&lt;/sub&gt;,
&amp;sigma;&lt;sub&gt;yz&lt;/sub&gt;,
&amp;sigma;&lt;sub&gt;zx&lt;/sub&gt;, &amp;eta;&lt;sub&gt;r&lt;/sub&gt;,
and the strain output follows this order:
&amp;epsilon;&lt;sub&gt;xx&lt;/sub&gt;,
&amp;epsilon;&lt;sub&gt;yy&lt;/sub&gt;,
&amp;epsilon;&lt;sub&gt;zz&lt;/sub&gt;,
&amp;gamma;&lt;sub&gt;xy&lt;/sub&gt;,
&amp;gamma;&lt;sub&gt;yz&lt;/sub&gt;,
&amp;gamma;&lt;sub&gt;zx&lt;/sub&gt;.</p>
<p>The "<strong>backbone</strong>" option records (secant) shear modulus
reduction curves at one or more given confinements. The specific
recorder command is as follows:</p>
<p><strong>recorder Element -ele $eleNum -file $fName -dT $deltaT
material $GaussNum backbone $p1 &lt;$p2 …&gt;</strong></p>
<p>where p1, p2, … are the confinements at which modulus reduction
curves are recorded. In the output file, corresponding to each given
confinement there are two columns: shear strain &amp;gamma; and secant
modulus G&lt;sub&gt;s&lt;/sub&gt;. The number of rows equals the number
of yield surfaces.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDMaterial PressureDependMultiYield $tag $nd $rho
$refShearModul $refBulkModul $frictionAng $peakShearStra $refPress
$pressDependCoe $PTAng $contrac $dilat1 $dilat2 $liquefac1 $liquefac2
$liquefac3 &lt;$noYieldSurf=20 &lt;$r1 $Gs1 …&gt; $e=0.6 $cs1=0.9
$cs2=0.02 $cs3=0.7 $pa=101 &lt;$c=0.3&gt;&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<figure>
<img src="/OpenSeesRT/contrib/static/PreDep_ss.png" title="PreDep_ss.png" alt="PreDep_ss.png" />
<figcaption aria-hidden="true">PreDep_ss.png</figcaption>
</figure>
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>A positive integer uniquely identifying the material among all
nDMaterials.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">nd</code></td>
<td><p>Number of dimensions, 2 for plane-strain, and 3 for 3D
analysis.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>Saturated soil mass density.</p></td>
</tr>
<tr class="even">
<td><p><strong>$refShearModul
(G&lt;sub&gt;r&lt;/sub&gt;)</strong></p></td>
<td><p>Reference low-strain shear modulus, specified at a reference mean
effective confining pressure refPress of p’&lt;sub&gt;r&lt;/sub&gt; (see
below).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$refBulkModul
(B&lt;sub&gt;r&lt;/sub&gt;)</strong></p></td>
<td><p>Reference bulk modulus, specified at a reference mean effective
confining pressure refPress of p’&lt;sub&gt;r&lt;/sub&gt; (see
below).</p></td>
</tr>
<tr class="even">
<td><p><strong>$frictionAng (&amp;Phi;)</strong></p></td>
<td><p>Friction angle at peak shear strength, in degrees.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$peakShearStra
(&amp;gamma;&lt;sub&gt;max&lt;/sub&gt;)</strong></p></td>
<td><p>An octahedral shear strain at which the maximum shear strength is
reached, specified at a reference mean effective confining pressure
refPress of p’&lt;sub&gt;r&lt;/sub&gt; (see below). Octahedral shear
strain is defined as:</p>
<figure>
<img src="PreDep_OctGamma.png‎" title="PreDep_OctGamma.png‎"
alt="PreDep_OctGamma.png‎" />
<figcaption aria-hidden="true">PreDep_OctGamma.png‎</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p><strong>$refPress (p’&lt;sub&gt;r&lt;/sub&gt;)</strong></p></td>
<td><p>Reference mean effective confining pressure at which Gr, Br, and
&amp;gamma;&lt;sub&gt;max&lt;/sub&gt; are defined.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$pressDependCoe (d)</strong></p></td>
<td><p>A positive constant defining variations of G and B as a function
of instantaneous effective confinement p’:</p>
<figure>
<img src="PreDep_pressDepCoe.png‎" title="PreDep_pressDepCoe.png‎"
alt="PreDep_pressDepCoe.png‎" />
<figcaption aria-hidden="true">PreDep_pressDepCoe.png‎</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p><strong>$PTAng
(&amp;Phi;&lt;sub&gt;PT&lt;/sub&gt;)</strong></p></td>
<td><p>Phase transformation angle, in degrees.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">contrac</code></td>
<td><p>A non-negative constant defining the rate of shear-induced volume
decrease (contraction) or pore pressure buildup. A larger value
corresponds to faster contraction rate.</p></td>
</tr>
<tr class="even">
<td><p><strong>$dilat1, $dilat2</strong></p></td>
<td><p>Non-negative constants defining the rate of shear-induced volume
increase (dilation). Larger values correspond to stronger dilation
rate.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$liquefac1, $liquefac2, $liquefac3</strong></p></td>
<td><p>Parameters controlling the mechanism of liquefaction-induced
perfectly plastic shear strain accumulation, i.e., cyclic mobility.
<strong>Set liquefac1 = 0 to deactivate this mechanism
altogether.</strong> liquefac1 defines the effective confining pressure
(e.g., 10 kPa in SI units or 1.45 psi in English units) below which the
mechanism is in effect. Smaller values should be assigned to denser
sands. Liquefac2 defines the maximum amount of perfectly plastic shear
strain developed at zero effective confinement during each loading
phase. Smaller values should be assigned to denser sands. Liquefac3
defines the maximum amount of biased perfectly plastic shear strain
&amp;gamma;&lt;sub&gt;b&lt;/sub&gt; accumulated at each loading phase
under biased shear loading conditions, as
&amp;gamma;&lt;sub&gt;b&lt;/sub&gt;=liquefac2 x liquefac3. Typically,
liquefac3 takes a value between 0.0 and 3.0. Smaller values should be
assigned to denser sands. See the references listed at the end of this
chapter for more information.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">noYieldSurf</code></td>
<td><p>Number of yield surfaces, optional (must be less than 40, default
is 20). The surfaces are generated based on the hyperbolic relation
defined in Note 2 below.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$r, $Gs</strong></p></td>
<td><p>Instead of automatic surfaces generation (Note 2), <strong>you
can define yield surfaces directly based on desired shear modulus
reduction curve.</strong> To do so, add a minus sign in front of
noYieldSurf, then provide noYieldSurf pairs of shear strain
(&amp;gamma;) and modulus ratio (G&lt;sub&gt;s&lt;/sub&gt;) values. For
example, to define 10 surfaces: …
-10&amp;gamma;&lt;sub&gt;1&lt;/sub&gt;G&lt;sub&gt;s1&lt;/sub&gt; …
&amp;gamma;&lt;sub&gt;10&lt;/sub&gt;G&lt;sub&gt;s10&lt;/sub&gt; …</p>
<p>See Note 3 below for some important notes.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">e</code></td>
<td><p>Initial void ratio, optional (default is 0.6).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$cs1, $cs2, $cs3, $pa</strong></p></td>
<td><p>Parameters defining a straight critical-state line
e&lt;sub&gt;c&lt;/sub&gt; in e-p’ space. If cs3=0,</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
e&lt;sub&gt;c&lt;/sub&gt; = cs1-cs2 log(p'/p&lt;sub&gt;a&lt;/sub&gt;)
</dd>
</dl>
</dd>
</dl>
<p>else (Li and Wang, JGGE, 124(12)),</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
e&lt;sub&gt;c&lt;/sub&gt; =
cs1-cs2(p'/p&lt;sub&gt;a&lt;/sub&gt;)&lt;sup&gt;cs3&lt;/sup&gt;
</dd>
</dl>
</dd>
</dl>
<p>where p&lt;sub&gt;a&lt;/sub&gt; is atmospheric pressure for
normalization (typically 101 kPa in SI units, or 14.65 psi in English
units). All four constants are optional (default values: cs1=0.9,
cs2=0.02, cs3=0.7, p&lt;sub&gt;a&lt;/sub&gt; =101 kPa).</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">c</code></td>
<td><p>Numerical constant (default value = 0.3 kPa)</p></td>
</tr>
</tbody>
</table>
<p><strong>NOTE:</strong></p>
<p>1. The friction angle &amp;Phi; defines the variation of peak
(octahedral) shear strength &amp;tau;&lt;sub&gt;f&lt;/sub&gt; as a
function of current effective confinement p’:</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<img src="PreDep_octTauStrength.png‎"
title="fig:PreDep_octTauStrength.png‎" alt="PreDep_octTauStrength.png‎" />
</dd>
</dl>
</dd>
</dl>
<p>Octahedral shear stress is defined as:</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<img src="PreDep_octTau.png‎" title="fig:PreDep_octTau.png‎"
alt="PreDep_octTau.png‎" />
</dd>
</dl>
</dd>
</dl>
<p>2. (Automatic surface generation) At a constant confinement p’, the
shear stress &amp;tau;(octahedral) - shear strain &amp;gamma;
(octahedral) nonlinearity is defined by a hyperbolic curve (backbone
curve):</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<img src="PreDep_Tau.png‎" title="fig:PreDep_Tau.png‎"
alt="PreDep_Tau.png‎" />
</dd>
</dl>
</dd>
</dl>
<p>where &amp;gamma;&lt;sub&gt;r&lt;/sub&gt; satisfies the following
equation at p’&lt;sub&gt;r&lt;/sub&gt;:</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<img src="PreDep_TauStrength.png‎" title="fig:PreDep_TauStrength.png‎"
alt="PreDep_TauStrength.png‎" />
</dd>
</dl>
</dd>
</dl>
<p>3. (User defined surfaces) The user specified friction angle
&amp;Phi; is ignored. Instead, &amp;Phi; is defined as follows:</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<img src="PreDep_sinPhi.png‎" title="fig:PreDep_sinPhi.png‎"
alt="PreDep_sinPhi.png‎" />
</dd>
</dl>
</dd>
</dl>
<p>where &amp;sigma;&lt;sub&gt;m&lt;/sub&gt; is the product of the last
modulus and strain pair in the modulus reduction curve. Therefore, it is
important to adjust the backbone curve so as to render an appropriate
&amp;Phi;. If the resulting &amp;Phi; is smaller than the phase
transformation angle &amp;Phi;&lt;sub&gt;PT&lt;/sub&gt;,
&amp;Phi;&lt;sub&gt;PT&lt;/sub&gt; is set equal to &amp;Phi;. Also
remember that improper modulus reduction curves can result in strain
softening response (negative tangent shear modulus), which is not
allowed in the current model formulation. Finally, note that the
backbone curve varies with confinement, although the variations are
small within commonly interested confinement ranges. Backbone curves at
different confinements can be obtained using the OpenSees element
recorder facility (see OUTPUT INTERFACE above).</p>
<p>4. The last five optional parameters are needed when critical-state
response (flow liquefaction) is anticipated. Upon reaching the
critical-state line, material dilatancy is set to zero.</p>
<p>5. SUGGESTED PARAMETER VALUES</p>
<p>For user convenience, a table is provided below as a quick reference
for selecting parameter values. However, use of this table should be of
great caution, and other information should be incorporated wherever
possible.</p>
<table>
<tbody>
<tr class="odd">
<td><p>Parameters</p></td>
<td><p>Loose Sand (15%-35%)</p></td>
<td><p>Medium Sand (35%-65%)</p></td>
<td><p>Medium-dense Sand (65%-85%)</p></td>
<td><p>Dense Sand (85%-100%)</p></td>
</tr>
<tr class="even">
<td><p>rho</p></td>
<td><p>1.7 ton/m&lt;sup&gt;3&lt;/sup&gt; or
1.59x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
<td><p>1.9 ton/m&lt;sup&gt;3&lt;/sup&gt; or</p>
<p>1.778x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
<td><p>2.0 ton/m&lt;sup&gt;3&lt;/sup&gt; or</p>
<p>1.872x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
<td><p>2.1 ton/m&lt;sup&gt;3&lt;/sup&gt; or</p>
<p>1.965x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
</tr>
<tr class="odd">
<td><p>refShearModul (at p’&lt;sub&gt;r&lt;/sub&gt;=80 kPa or 11.6
psi)</p></td>
<td><p>5.5x10&lt;sup&gt;4&lt;/sup&gt; kPa or
7.977x10&lt;sup&gt;3&lt;/sup&gt; psi</p></td>
<td><p>7.5x10&lt;sup&gt;4&lt;/sup&gt; kPa or
1.088x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>1.0x10&lt;sup&gt;5&lt;/sup&gt; kPa or
1.45x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>1.3x10&lt;sup&gt;5&lt;/sup&gt; kPa or
1.885x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
</tr>
<tr class="even">
<td><p>refBulkModu (at p’&lt;sub&gt;r&lt;/sub&gt;=80 kPa or 11.6
psi)</p></td>
<td><p>1.5x10&lt;sup&gt;5&lt;/sup&gt; kPa or
2.176x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>2.0x10&lt;sup&gt;5&lt;/sup&gt; kPa or
2.9x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>3.0x10&lt;sup&gt;5&lt;/sup&gt; kPa or
4.351x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>3.9x10&lt;sup&gt;5&lt;/sup&gt; kPa or
5.656x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
</tr>
<tr class="odd">
<td><p>frictionAng</p></td>
<td><p>29</p></td>
<td><p>33</p></td>
<td><p>37</p></td>
<td><p>40</p></td>
</tr>
<tr class="even">
<td><p>peakShearStra (at p’&lt;sub&gt;r&lt;/sub&gt;=80 kPa or 11.6
psi)</p></td>
<td><p>0.1</p></td>
<td><p>0.1</p></td>
<td><p>0.1</p></td>
<td><p>0.1</p></td>
</tr>
<tr class="odd">
<td><p>refPress (p’&lt;sub&gt;r&lt;/sub&gt;)</p></td>
<td><p>80 kPa or 11.6 psi</p></td>
<td><p>80 kPa or 11.6 psi</p></td>
<td><p>80 kPa or 11.6 psi</p></td>
<td><p>80 kPa or 11.6 psi</p></td>
</tr>
<tr class="even">
<td><p>pressDependCoe</p></td>
<td><p>0.5</p></td>
<td><p>0.5</p></td>
<td><p>0.5</p></td>
<td><p>0.5</p></td>
</tr>
<tr class="odd">
<td><p>PTAng</p></td>
<td><p>29</p></td>
<td><p>27</p></td>
<td><p>27</p></td>
<td><p>27</p></td>
</tr>
<tr class="even">
<td><p>contrac</p></td>
<td><p>0.21</p></td>
<td><p>0.07</p></td>
<td><p>0.05</p></td>
<td><p>0.03</p></td>
</tr>
<tr class="odd">
<td><p>dilat1</p></td>
<td><p>0.</p></td>
<td><p>0.4</p></td>
<td><p>0.6</p></td>
<td><p>0.8</p></td>
</tr>
<tr class="even">
<td><p>dilat2</p></td>
<td><p>0</p></td>
<td><p>2</p></td>
<td><p>3</p></td>
<td><p>5</p></td>
</tr>
<tr class="odd">
<td><p>liquefac1</p></td>
<td><p>10 kPa or 1.45 psi</p></td>
<td><p>10 kPa or 1.45 psi</p></td>
<td><p>5 kPa or 0.725 psi</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p>liquefac2</p></td>
<td><p>0.02</p></td>
<td><p>0.01</p></td>
<td><p>0.003</p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p>liquefac3</p></td>
<td><p>1</p></td>
<td><p>1</p></td>
<td><p>1</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p>e</p></td>
<td><p>0.85</p></td>
<td><p>0.7</p></td>
<td><p>0.55</p></td>
<td><p>0.45</p></td>
</tr>
</tbody>
</table>
<h2 id="pressure_dependent_material_examples"><strong>Pressure Dependent
Material Examples:</strong></h2>
<p>&lt;table border=1 width=800&gt; &lt;tr&gt; &lt;td colspan=2
align=center &gt;&lt;b&gt;Material in elastic, drained (or dry)
state&lt;/b&gt;&lt;/td&gt;</p>
<p>&lt;/tr&gt; &lt;tr&gt; &lt;td width=90&gt;<a
href="PressureDependMultiYield-Example_1" title="wikilink">Example
1</a>&lt;/td&gt; &lt;td&gt;Single quadrilateral element, subjected to
sinusoidal base shaking&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-Example_2" title="wikilink">Example
2</a>&lt;/td&gt;</p>
<p>&lt;td&gt;Single quadrilateral element, subjected to monotonic
pushover (<a
href="http://cyclic.ucsd.edu/opensees/newEnglishUnits/Elastic%20Pressure%20Dependent%20Dry%20Level%20Pushover/index.htm">English
units version</a>)&lt;/td&gt; &lt;/tr&gt;</p>
<p>&lt;tr&gt; &lt;td colspan=2 align=center &gt;&lt;b&gt;Material in
drained (or dry), elastic-plastic state&lt;/b&gt;&lt;/td&gt; &lt;/tr&gt;
&lt;tr&gt;</p>
<p>&lt;td&gt;<a href="PressureDependMultiYield-Example_3"
title="wikilink">Example 3</a> &lt;/td&gt; &lt;td&gt;Single
quadrilateral element, subjected to sinusoidal base shaking&lt;/td&gt;
&lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-Example_4" title="wikilink">Example
4</a>&lt;/td&gt; &lt;td&gt;Single quadrilateral element (inclined by 4
degrees), subjected to sinusoidal base shaking&lt;/td&gt;
&lt;/tr&gt;</p>
<p>&lt;tr&gt; &lt;td&gt;<a href="PressureDependMultiYield-Example_5"
title="wikilink">Example 5</a>&lt;/td&gt; &lt;td&gt;Single quadrilateral
element, subjected to monotonic pushover&lt;/td&gt; &lt;/tr&gt;
&lt;tr&gt; &lt;td&gt;<a href="PressureDependMultiYield-Example_6"
title="wikilink">Example 6</a>&lt;/td&gt; &lt;td&gt;Single 3D BbarBrick
element, subjected to sinusoidal base shaking&lt;/td&gt;</p>
<p>&lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-Example_7" title="wikilink">Example
7</a>&lt;/td&gt; &lt;td&gt;Single 3D BbarBrick element (inclined by 4
degrees), subjected to sinusoidal base shaking&lt;/td&gt;
&lt;/tr&gt;</p>
<p>&lt;tr&gt; &lt;td colspan=2 align=center &gt;&lt;b&gt;Material in
saturated, undrained elastic-plastic state (coupled with
FluidSolidPorous Material)&lt;/b&gt;&lt;/td&gt;</p>
<p>&lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-Example_8" title="wikilink">Example
8</a>&lt;/td&gt; &lt;td&gt;Single quadrilateral element, subjected to
sinusoidal base shaking&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-Example_9" title="wikilink">Example
9</a>&lt;/td&gt;</p>
<p>&lt;td&gt;Single quadrilateral element, subjected to monotonic
pushover&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-Example_10" title="wikilink">Example
10</a>&lt;/td&gt; &lt;td&gt;Single quadrilateral element (inclined by 4
degrees), subjected to msinusoidal base shaking&lt;/td&gt; &lt;/tr&gt;
&lt;tr&gt;</p>
<p>&lt;td&gt;<a href="PressureDependMultiYield-Example_11"
title="wikilink">Example 11</a>&lt;/td&gt; &lt;td&gt;Single 3D BbarBrick
element, subjected to sinusoidal base shaking&lt;/td&gt; &lt;/tr&gt;
&lt;tr&gt; &lt;td&gt;<a href="PressureDependMultiYield-Example_12"
title="wikilink">Example 12</a>&lt;/td&gt; &lt;td&gt;Single 3D BbarBrick
element (inclined by 4 degrees), subjected to sinusoidal base
shaking&lt;/td&gt; &lt;/tr&gt;</p>
<p>&lt;tr&gt; &lt;td&gt;<a href="PressureDependMultiYield--Example_13"
title="wikilink">Example 13</a>&lt;/td&gt; &lt;td&gt;A column of
quadrilateral element (inclined by 4 degrees), subjected to sinusoidal
base shaking&lt;/td&gt; &lt;/tr&gt;</p>
<p>&lt;tr&gt; &lt;td colspan=2 align=center &gt;&lt;b&gt;Material in
saturated, undrained elastic-plastic state (with user defined modulus
reduction curve)&lt;/b&gt;&lt;/td&gt; &lt;/tr&gt;</p>
<p>&lt;tr&gt; &lt;td&gt;<a href="PressureDependMultiYield-Example_14"
title="wikilink">Example 14</a>&lt;/td&gt; &lt;td&gt;A column of
quadrilateral element (inclined by 4 degrees), subjected to sinusoidal
base shaking&lt;/td&gt; &lt;/tr&gt;</p>
<p>&lt;tr&gt; &lt;td colspan=2 align=center &gt;&lt;b&gt;Solid-Fluid
fully coupled elements - quadUP element&lt;/b&gt;&lt;/td&gt;
&lt;/tr&gt;</p>
<p>&lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-quadUP_element" title="wikilink">Example
15</a>&lt;/td&gt; &lt;td&gt;A column (2D plane strain quadUP element) of
saturated, undrained Pressure Dependent material (inclined by 4
degrees), subjected to sinusoidal base shaking&lt;/td&gt;
&lt;/tr&gt;</p>
<p>&lt;/table&gt;</p>
<p>Code Developed by: <span style="color:blue"> UC San Diego (Dr.
Zhaohui Yang)</span>:</p>
<hr />
<p>UC San Diego Soil Model: </p>

 # PressureIndependMultiYield

<p><strong>PressureIndependMultiYield</strong> material is an
elastic-plastic material in which plasticity exhibits only in the
deviatoric stress-strain response. The volumetric stress-strain response
is linear-elastic and is independent of the deviatoric response. This
material is implemented to simulate monotonic or cyclic response of
materials whose shear behavior is insensitive to the confinement change.
Such materials include, for example, organic soils or clay under fast
(undrained) loading conditions.</p>
<p>During the application of gravity load (and static loads if any),
material behavior is linear elastic. In the subsequent dynamic (fast)
loading phase(s), the stress-strain response is elastic-plastic (see
MATERIAL STAGE UPDATE below). Plasticity is formulated based on the
multi-surface (nested surfaces) concept, with an associative flow rule.
The yield surfaces are of the Von Mises type.</p>
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
<td><p><strong>nDmaterial PressureIndependMultiYield $tag $nd $rho
$refShearModul $refBulkModul $cohesi $peakShearStra &lt;$frictionAng=0.
$refPress=100. $pressDependCoe=0. $noYieldSurf=20 &lt;$r1 $Gs1 …&gt;
&gt;</strong></p></td>
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
<td><p><strong>$cohesi (c)</strong></p></td>
<td><p>Apparent cohesion at zero effective confinement.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$peakShearStra
(&amp;gamma;&lt;sub&gt;max&lt;/sub&gt;)</strong></p></td>
<td><p>An octahedral shear strain at which the maximum shear strength is
reached, specified at a reference mean effective confining pressure
refPress of p’&lt;sub&gt;r&lt;/sub&gt; (see below).</p></td>
</tr>
<tr class="even">
<td><p><strong>$frictionAng (&amp;Phi;)</strong></p></td>
<td><p>Friction angle at peak shear strength in degrees, optional
(default is 0.0).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$refPress (p’&lt;sub&gt;r&lt;/sub&gt;)</strong></p></td>
<td><p>Reference mean effective confining pressure at which Gr, Br, and
&amp;gamma;&lt;sub&gt;max&lt;/sub&gt; are defined, optional (default is
100. kPa).</p></td>
</tr>
<tr class="even">
<td><p><strong>$pressDependCoe (d)</strong></p></td>
<td><p>A positive constant defining variations of G and B as a function
of instantaneous effective confinement p’(default is 0.0)::</p>
<figure>
<img src="PreDep_pressDepCoe.png‎" title="PreDep_pressDepCoe.png‎"
alt="PreDep_pressDepCoe.png‎" />
<figcaption aria-hidden="true">PreDep_pressDepCoe.png‎</figcaption>
</figure>
<p><strong>If &amp;Phi;=0, d is reset to 0.0.</strong></p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">noYieldSurf</code></td>
<td><p>Number of yield surfaces, optional (must be less than 40, default
is 20). The surfaces are generated based on the hyperbolic relation
defined in Note 2 below.</p></td>
</tr>
<tr class="even">
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
</tbody>
</table>
<p><strong>NOTE:</strong></p>
<p>1. The friction angle &amp;Phi; and cohesion c define the variation
of peak (octahedral) shear strength &amp;tau;&lt;sub&gt;f&lt;/sub&gt; as
a function of current effective confinement
p’&lt;sub&gt;i&lt;/sub&gt;:</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<img src="PreIndep_octTauStrength.png‎"
title="fig:PreIndep_octTauStrength.png‎"
alt="PreIndep_octTauStrength.png‎" />
</dd>
</dl>
</dd>
</dl>
<p>2. Automatic surface generation: at a constant confinement p’, the
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
<img src="PreIndep_TauStrength2.png‎"
title="fig:PreIndep_TauStrength2.png‎" alt="PreIndep_TauStrength2.png‎" />
</dd>
</dl>
</dd>
</dl>
<p>3. (User defined surfaces) The user specified friction angle
&amp;Phi; = 0. cohesion c will be ignored. Instead, c is defined by
c=sqrt(3)*&amp;sigma;&lt;sub&gt;m&lt;/sub&gt;/2, where
&amp;sigma;&lt;sub&gt;m&lt;/sub&gt; is the product of the last modulus
and strain pair in the modulus reduction curve. Therefore, it is
important to adjust the backbone curve so as to render an appropriate
c.</p>
<p>If the user specifies &amp;Phi; &gt; 0, this &amp;Phi; will be
ignored. Instead, &amp;Phi;is defined as follows:</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<img src="PreIndep_sinPhi.png‎" title="fig:PreIndep_sinPhi.png‎"
alt="PreIndep_sinPhi.png‎" />
</dd>
</dl>
</dd>
</dl>
<p>If the resulting &amp;Phi; &lt;0, we set &amp;Phi;=0 and
c=sqrt(3)*&amp;sigma;&lt;sub&gt;m&lt;/sub&gt;/2.</p>
<p>Also remember that improper modulus reduction curves can result in
strain softening response (negative tangent shear modulus), which is not
allowed in the current model formulation. Finally, note that the
backbone curve varies with confinement, although the variation is small
within commonly interested confinement ranges. Backbone curves at
different confinements can be obtained using the OpenSees element
recorder facility (see OUTPUT INTERFACE above).</p>
<p>4. SUGGESTED PARAMETER VALUES</p>
<p>For user convenience, a table is provided below as a quick reference
for selecting parameter values. However, use of this table should be of
great caution, and other information should be incorporated wherever
possible.</p>
<table>
<tbody>
<tr class="odd">
<td><p>Parameters</p></td>
<td><p>Soft Clay</p></td>
<td><p>Medium Clay</p></td>
<td><p>Stiff Clay</p></td>
</tr>
<tr class="even">
<td><p>rho</p></td>
<td><p>1.3 ton/m&lt;sup&gt;3&lt;/sup&gt; or</p>
<p>1.217x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
<td><p>1.5 ton/m&lt;sup&gt;3&lt;/sup&gt; or</p>
<p>1.404x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
<td><p>1.8 ton/m&lt;sup&gt;3&lt;/sup&gt; or</p>
<p>1.685x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
</tr>
<tr class="odd">
<td><p>refShearModul</p></td>
<td><p>1.3x10&lt;sup&gt;4&lt;/sup&gt; kPa or
1.885x10&lt;sup&gt;3&lt;/sup&gt; psi</p></td>
<td><p>6.0x10&lt;sup&gt;4&lt;/sup&gt; kPa or
8.702x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>1.5x10&lt;sup&gt;5&lt;/sup&gt; kPa or
2.176x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
</tr>
<tr class="even">
<td><p>refBulkModu</p></td>
<td><p>6.5x10&lt;sup&gt;4&lt;/sup&gt; kPa or
9.427x10&lt;sup&gt;3&lt;/sup&gt; psi</p></td>
<td><p>3.0x10&lt;sup&gt;5&lt;/sup&gt; kPa or
4.351x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>7.5x10&lt;sup&gt;5&lt;/sup&gt; kPa or
1.088x10&lt;sup&gt;5&lt;/sup&gt; psi</p></td>
</tr>
<tr class="odd">
<td><p>cohesi</p></td>
<td><p>18 kPa or 2.611 psi</p></td>
<td><p>37 kPa or 5.366 psi</p></td>
<td><p>75 kPa or 10.878 psi</p></td>
</tr>
<tr class="even">
<td><p>peakShearStra (at p’&lt;sub&gt;r&lt;/sub&gt;=80 kPa or 11.6
psi)</p></td>
<td><p>0.1</p></td>
<td><p>0.1</p></td>
<td><p>0.1</p></td>
</tr>
<tr class="odd">
<td><p>frictionAng</p></td>
<td><p>0</p></td>
<td><p>0</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p>pressDependCoe</p></td>
<td><p>0</p></td>
<td><p>0</p></td>
<td><p>0</p></td>
</tr>
</tbody>
</table>
<h2 id="pressure_independent_material_examples"><strong>Pressure
Independent Material Examples:</strong></h2>
<p>&lt;table border=1 width=800&gt; &lt;tr&gt; &lt;td colspan=2
align=center &gt;&lt;b&gt;Material in elastic state&lt;/b&gt;&lt;/td&gt;
&lt;/tr&gt; &lt;tr&gt; &lt;td width=90&gt;<a
href="PressureIndependentMultiYield-Example_1" title="wikilink">Example
1</a> &lt;/td&gt;</p>
<p>&lt;td&gt;Single 2D plane-strain quadrilateral element, subjected to
sinusoidal base shaking&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureIndependentMultiYield-Example_2" title="wikilink">Example
2</a>&lt;/td&gt; &lt;td&gt;Single 2D quadrilateral element, subjected to
monotonic pushover (<a
href="http://cyclic.ucsd.edu/opensees/newEnglishUnits/Elastic%20Pressure%20Independent%20Wet%20Level%20Pushover/index.htm">English
units version</a>)&lt;/td&gt; &lt;/tr&gt;</p>
<p>&lt;/table&gt;</p>
<p>Code Developed by: <span style="color:blue"> UC San Diego (Dr.
Zhaohui Yang)</span>:</p>
<hr />
<p>UC San Diego Soil Model: </p>

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
(McKenna and Fenves 2001)<sup><a href="Soil_Models_References"
title="wikilink">&reg;</a></sup>: "<strong>stress</strong>",
"<strong>strain</strong>", "<strong>backbone</strong>", or
"<strong>tangent</strong>".</p>
<p>For 2D problems, the stress output follows this order:
&sigma;<sub>xx</sub>,
&sigma;<sub>yy</sub>,
&sigma;<sub>zz</sub>,
&sigma;<sub>xy</sub>, &eta;<sub>r</sub>,
where &eta;<sub>r</sub> is the ratio between the shear
(deviatoric) stress and peak shear strength at the current confinement
(0&lt;=&eta;<sub>r</sub>&lt;=1.0). The strain output
follows this order: &epsilon;<sub>xx</sub>,
&epsilon;<sub>yy</sub>,
&gamma;<sub>xy</sub>.</p>
<p>For 3D problems, the stress output follows this order:
&sigma;<sub>xx</sub>,
&sigma;<sub>yy</sub>,
&sigma;<sub>zz</sub>,
&sigma;<sub>xy</sub>,
&sigma;<sub>yz</sub>,
&sigma;<sub>zx</sub>, &eta;<sub>r</sub>,
and the strain output follows this order:
&epsilon;<sub>xx</sub>,
&epsilon;<sub>yy</sub>,
&epsilon;<sub>zz</sub>,
&gamma;<sub>xy</sub>,
&gamma;<sub>yz</sub>,
&gamma;<sub>zx</sub>.</p>

The "<strong>backbone</strong>" option records (secant) shear modulus
reduction curves at one or more given confinements. The specific
recorder command is as follows:
```tcl
recorder Element -ele $eleNum -file $fName -dT $deltaT material $GaussNum backbone $p1 < $p2 … >
```
where p1, p2, … are the confinements at which modulus reduction
curves are recorded. In the output file, corresponding to each given
confinement there are two columns: shear strain &gamma; and secant
modulus G<sub>s</sub>. The number of rows equals the number
of yield surfaces.

```tcl
nDMaterial PressureDependMultiYield $tag $nd $rho
        $refShearModul $refBulkModul $frictionAng $peakShearStra $refPress
        $pressDependCoe $PTAng $contrac $dilat1 $dilat2 $liquefac1 $liquefac2
        $liquefac3 < $noYieldSurf=20 < $r1 $Gs1 … > $e=0.6 $cs1=0.9
        $cs2=0.02 $cs3=0.7 $pa=101 < $c=0.3 > >
```

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
<td><p><strong>`refShearModul`
(G<sub>r</sub>)</strong></p></td>
<td><p>Reference low-strain shear modulus, specified at a reference mean
effective confining pressure refPress of p’<sub>r</sub> (see
below).</p></td>
</tr>
<tr class="odd">
<td><p><strong>`refBulkModul`
(B<sub>r</sub>)</strong></p></td>
<td><p>Reference bulk modulus, specified at a reference mean effective
confining pressure refPress of p’<sub>r</sub> (see
below).</p></td>
</tr>
<tr class="even">
<td><p><strong>`frictionAng` (&Phi;)</strong></p></td>
<td><p>Friction angle at peak shear strength, in degrees.</p></td>
</tr>
<tr class="odd">
<td><p><strong>`peakShearStra`
(&gamma;<sub>max</sub>)</strong></p></td>
<td><p>An octahedral shear strain at which the maximum shear strength is
reached, specified at a reference mean effective confining pressure
refPress of p’<sub>r</sub> (see below). Octahedral shear
strain is defined as:</p>
<figure>
<img src="/OpenSeesRT/contrib/static/PreDep_OctGamma.png"
alt="PreDep_OctGamma.png" />
<figcaption aria-hidden="true">PreDep_OctGamma.png‎</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p><strong>`refPress` (p’<sub>r</sub>)</strong></p></td>
<td><p>Reference mean effective confining pressure at which Gr, Br, and
&gamma;<sub>max</sub> are defined.</p></td>
</tr>
<tr class="odd">
<td><p><strong>`pressDependCoe` (d)</strong></p></td>
<td><p>A positive constant defining variations of G and B as a function
of instantaneous effective confinement p’:</p>
<figure>
<img src="/OpenSeesRT/contrib/static/PreDep_pressDepCoe.png" alt="PreDep_pressDepCoe.png" />
<figcaption aria-hidden="true">PreDep_pressDepCoe.png</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p><strong>`PTAng`
(&Phi;<sub>PT</sub>)</strong></p></td>
<td><p>Phase transformation angle, in degrees.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">contrac</code></td>
<td><p>A non-negative constant defining the rate of shear-induced volume
decrease (contraction) or pore pressure buildup. A larger value
corresponds to faster contraction rate.</p></td>
</tr>
<tr class="even">
<td><p><strong>`dilat1`, `dilat2`</strong></p></td>
<td><p>Non-negative constants defining the rate of shear-induced volume
increase (dilation). Larger values correspond to stronger dilation
rate.</p></td>
</tr>
<tr class="odd">
<td><p><strong>`liquefac1`, `liquefac2`, `liquefac3`</strong></p></td>
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
&gamma;<sub>b</sub> accumulated at each loading phase
under biased shear loading conditions, as
&gamma;<sub>b</sub>=liquefac2 x liquefac3. Typically,
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
<td><p><strong>`r`, `Gs`</strong></p></td>
<td><p>Instead of automatic surfaces generation (Note 2), <strong>you
can define yield surfaces directly based on desired shear modulus
reduction curve.</strong> To do so, add a minus sign in front of
noYieldSurf, then provide noYieldSurf pairs of shear strain
(&gamma;) and modulus ratio (G<sub>s</sub>) values. For
example, to define 10 surfaces: …
-10&gamma;<sub>1</sub>G<sub>s1</sub> …
&gamma;<sub>10</sub>G<sub>s10</sub> …</p>
<p>See Note 3 below for some important notes.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">e</code></td>
<td><p>Initial void ratio, optional (default is 0.6).</p></td>
</tr>
<tr class="odd">
<td><p><strong>`cs1`, `cs2`, `cs3`, `pa`</strong></p></td>
<td><p>Parameters defining a straight critical-state line
e<sub>c</sub> in e-p’ space. If `cs3=0`,</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
e<sub>c</sub> = cs1-cs2 log(p'/p<sub>a</sub>)
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
e<sub>c</sub> =
cs1-cs2(p'/p<sub>a</sub>)<sup>cs3</sup>
</dd>
</dl>
</dd>
</dl>
<p>where p<sub>a</sub> is atmospheric pressure for
normalization (typically 101 kPa in SI units, or 14.65 psi in English
units). All four constants are optional (default values: cs1=0.9,
cs2=0.02, cs3=0.7, p<sub>a</sub> =101 kPa).</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">c</code></td>
<td><p>Numerical constant (default value = 0.3 kPa)</p></td>
</tr>
</tbody>
</table>

<p><strong>NOTE:</strong></p>

1. The friction angle &Phi; defines the variation of peak
  (octahedral) shear strength &tau;<sub>f</sub> as a
  function of current effective confinement p’:
  <dl>
  <dt></dt>
  <dd>
  <dl>
  <dt></dt>
  <dd>
  <img src="/OpenSeesRT/contrib/static/PreDep_octTauStrength.png"
  title="fig:PreDep_octTauStrength.png" alt="PreDep_octTauStrength.png" />
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
  <img src="/OpenSeesRT/contrib/static/PreDep_octTau.png" />
  </dd>
  </dl>
  </dd>
  </dl>
2. (Automatic surface generation) At a constant confinement p’, the
  shear stress &tau;(octahedral) - shear strain &gamma;
  (octahedral) nonlinearity is defined by a hyperbolic curve (backbone
  curve):
  <dl>
  <dt></dt>
  <dd>
  <dl>
  <dt></dt>
  <dd>
  <img src="/OpenSeesRT/contrib/static/PreDep_Tau.png" title="fig:PreDep_Tau.png"
  alt="PreDep_Tau.png" />
  </dd>
  </dl>
  </dd>
  </dl>
  <p>where &gamma;<sub>r</sub> satisfies the following
  equation at p’<sub>r</sub>:</p>
  <dl>
  <dt></dt>
  <dd>
  <dl>
  <dt></dt>
  <dd>
  <img src="/OpenSeesRT/contrib/static/PreDep_TauStrength.png" alt="PreDep_TauStrength.png" />
  </dd>
  </dl>
  </dd>
  </dl>
3. (User defined surfaces) The user specified friction angle
  &Phi; is ignored. Instead, &Phi; is defined as follows:
  <dl>
  <dt></dt>
  <dd>
  <dl>
  <dt></dt>
  <dd>
  <img src="/OpenSeesRT/contrib/static/PreDep_sinPhi.png" alt="PreDep_sinPhi.png" />
  </dd>
  </dl>
  </dd>
  </dl>
  <p>where &sigma;<sub>m</sub> is the product of the last
  modulus and strain pair in the modulus reduction curve. Therefore, it is
  important to adjust the backbone curve so as to render an appropriate
  &Phi;. If the resulting &Phi; is smaller than the phase
  transformation angle &Phi;<sub>PT</sub>,
  &Phi;<sub>PT</sub> is set equal to &Phi;. Also
  remember that improper modulus reduction curves can result in strain
  softening response (negative tangent shear modulus), which is not
  allowed in the current model formulation. Finally, note that the
  backbone curve varies with confinement, although the variations are
  small within commonly interested confinement ranges. Backbone curves at
  different confinements can be obtained using the OpenSees element
  recorder facility (see OUTPUT INTERFACE above).

4. The last five optional parameters are needed when critical-state
  response (flow liquefaction) is anticipated. Upon reaching the
  critical-state line, material dilatancy is set to zero.

5. SUGGESTED PARAMETER VALUES

   For user convenience, a table is provided below as a quick reference
   for selecting parameter values. However, use of this table should be of
   great caution, and other information should be incorporated wherever
   possible.

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
   <td><p>1.7 ton/m<sup>3</sup> or
   1.59x10<sup>-4</sup>
   (lbf)(s<sup>2</sup>)/in<sup>4</sup></p></td>
   <td><p>1.9 ton/m<sup>3</sup> or</p>
   <p>1.778x10<sup>-4</sup>
   (lbf)(s<sup>2</sup>)/in<sup>4</sup></p></td>
   <td><p>2.0 ton/m<sup>3</sup> or</p>
   <p>1.872x10<sup>-4</sup>
   (lbf)(s<sup>2</sup>)/in<sup>4</sup></p></td>
   <td><p>2.1 ton/m<sup>3</sup> or</p>
   <p>1.965x10<sup>-4</sup>
   (lbf)(s<sup>2</sup>)/in<sup>4</sup></p></td>
   </tr>
   <tr class="odd">
   <td><p>refShearModul (at p’<sub>r</sub>=80 kPa or 11.6
   psi)</p></td>
   <td><p>5.5x10<sup>4</sup> kPa or
   7.977x10<sup>3</sup> psi</p></td>
   <td><p>7.5x10<sup>4</sup> kPa or
   1.088x10<sup>4</sup> psi</p></td>
   <td><p>1.0x10<sup>5</sup> kPa or
   1.45x10<sup>4</sup> psi</p></td>
   <td><p>1.3x10<sup>5</sup> kPa or
   1.885x10<sup>4</sup> psi</p></td>
   </tr>
   <tr class="even">
   <td><p>refBulkModu (at p’<sub>r</sub>=80 kPa or 11.6
   psi)</p></td>
   <td><p>1.5x10<sup>5</sup> kPa or
   2.176x10<sup>4</sup> psi</p></td>
   <td><p>2.0x10<sup>5</sup> kPa or
   2.9x10<sup>4</sup> psi</p></td>
   <td><p>3.0x10<sup>5</sup> kPa or
   4.351x10<sup>4</sup> psi</p></td>
   <td><p>3.9x10<sup>5</sup> kPa or
   5.656x10<sup>4</sup> psi</p></td>
   </tr>
   <tr class="odd">
   <td><p>frictionAng</p></td>
   <td><p>29</p></td>
   <td><p>33</p></td>
   <td><p>37</p></td>
   <td><p>40</p></td>
   </tr>
   <tr class="even">
   <td><p>peakShearStra (at p’<sub>r</sub>=80 kPa or 11.6
   psi)</p></td>
   <td><p>0.1</p></td>
   <td><p>0.1</p></td>
   <td><p>0.1</p></td>
   <td><p>0.1</p></td>
   </tr>
   <tr class="odd">
   <td><p>refPress (p’<sub>r</sub>)</p></td>
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

<h2 id="pressure_dependent_material_examples">Pressure Dependent Material Examples:</h2>
<table border=1 width=800> <tr> <td colspan=2
align=center ><b>Material in elastic, drained (or dry)
state</b></td></p>
<p></tr> <tr> <td width=90><a href="PressureDependMultiYield-Example_1" title="wikilink">Example
1</a></td> <td>Single quadrilateral element, subjected to
sinusoidal base shaking</td> </tr> <tr> <td><a
href="PressureDependMultiYield-Example_2" title="wikilink">Example
2</a></td></p>
<p><td>Single quadrilateral element, subjected to monotonic
pushover (<a
href="http://cyclic.ucsd.edu/opensees/newEnglishUnits/Elastic%20Pressure%20Dependent%20Dry%20Level%20Pushover/index.htm">English
units version</a>)</td> </tr></p>
<p><tr> <td colspan=2 align=center ><b>Material in
drained (or dry), elastic-plastic state</b></td> </tr>
<tr></p>
<p><td><a href="PressureDependMultiYield-Example_3"
title="wikilink">Example 3</a> </td> <td>Single
quadrilateral element, subjected to sinusoidal base shaking</td>
</tr> <tr> <td><a
href="PressureDependMultiYield-Example_4" title="wikilink">Example
4</a></td> <td>Single quadrilateral element (inclined by 4
degrees), subjected to sinusoidal base shaking</td>
</tr></p>
<p><tr> <td><a href="PressureDependMultiYield-Example_5"
title="wikilink">Example 5</a></td> <td>Single quadrilateral
element, subjected to monotonic pushover</td> </tr>
<tr> <td><a href="PressureDependMultiYield-Example_6"
title="wikilink">Example 6</a></td> <td>Single 3D BbarBrick
element, subjected to sinusoidal base shaking</td></p>
<p></tr> <tr> <td><a
href="PressureDependMultiYield-Example_7" title="wikilink">Example
7</a></td> <td>Single 3D BbarBrick element (inclined by 4
degrees), subjected to sinusoidal base shaking</td>
</tr></p>
<p><tr> <td colspan=2 align=center ><b>Material in
saturated, undrained elastic-plastic state (coupled with
FluidSolidPorous Material)</b></td></p>
<p></tr> <tr> <td><a
href="PressureDependMultiYield-Example_8" title="wikilink">Example
8</a></td> <td>Single quadrilateral element, subjected to
sinusoidal base shaking</td> </tr> <tr> <td><a
href="PressureDependMultiYield-Example_9" title="wikilink">Example
9</a></td></p>
<p><td>Single quadrilateral element, subjected to monotonic
pushover</td> </tr> <tr> <td><a
href="PressureDependMultiYield-Example_10" title="wikilink">Example
10</a></td> <td>Single quadrilateral element (inclined by 4
degrees), subjected to msinusoidal base shaking</td> </tr>
<tr></p>
<p><td><a href="PressureDependMultiYield-Example_11"
title="wikilink">Example 11</a></td> <td>Single 3D BbarBrick
element, subjected to sinusoidal base shaking</td> </tr>
<tr> <td><a href="PressureDependMultiYield-Example_12"
title="wikilink">Example 12</a></td> <td>Single 3D BbarBrick
element (inclined by 4 degrees), subjected to sinusoidal base
shaking</td> </tr></p>
<p><tr> <td><a href="PressureDependMultiYield--Example_13"
title="wikilink">Example 13</a></td> <td>A column of
quadrilateral element (inclined by 4 degrees), subjected to sinusoidal
base shaking</td> </tr></p>
<p><tr> <td colspan=2 align=center ><b>Material in
saturated, undrained elastic-plastic state (with user defined modulus
reduction curve)</b></td> </tr></p>
<p><tr> <td><a href="PressureDependMultiYield-Example_14"
title="wikilink">Example 14</a></td> <td>A column of
quadrilateral element (inclined by 4 degrees), subjected to sinusoidal
base shaking</td> </tr></p>
<p><tr> <td colspan=2 align=center ><b>Solid-Fluid
fully coupled elements - quadUP element</b></td>
</tr></p>
<p><tr> <td><a
href="PressureDependMultiYield-quadUP_element" title="wikilink">Example
15</a></td> <td>A column (2D plane strain quadUP element) of
saturated, undrained Pressure Dependent material (inclined by 4
degrees), subjected to sinusoidal base shaking</td>
</tr></p>
<p></table></p>

<p>Code Developed by: <span style="color:blue"> UC San Diego (Dr.
Zhaohui Yang)</span>:</p>
<hr />
<p>UC San Diego Soil Model: </p>


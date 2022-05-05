 # ConfinedConcrete01

<p>This command is used to construct an uniaxial material
object of confined concrete in according to the work of
Braga, Gigliotti and Laterza (2006). The confined concrete
model (BGLmodel) has not tensile strength and degraded linear
unloading/reloading stiffness as proposed by Karsan and Jirsa
(1969). The BGL model accounts for confinement effects due to
different arrangements of transverse reinforcement and/or
external strengthening such as steel jackets or FRP wraps. The
confinement effect along the column is described as well. In
order to obtain th ecompressive envelope curve a non linear
approach is performed at each increment of column axial
strain.The sougth curve is obtained crossing different
stress‐strain relationships, each of which corresponding to a
different level of confinement. Currently, the Attard and
Setunge’s model is implemented in calculating each active curve
of the confined concrete. IMPORTANT: the units to be used are MPa,
mm.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>uniaxialMaterial ConfinedConcrete01 $tag $secType $fpc
$Ec (&lt;-epscu $epscu&gt; OR &lt;-gamma $gamma&gt;) (&lt;-nu $nu&gt; OR
&lt;-varub&gt; OR &lt;-varnoub&gt;) $L1 ($L2) ($L3) $phis $S $fyh $Es0
$haRatio $mu $phiLon &lt;-internal $phisi $Si $fyhi $Es0i $haRatioi
$mui&gt; &lt;-wrap $cover $Am $Sw $fuil $Es0w&gt; &lt;-gravel&gt;
&lt;-silica&gt; &lt;-tol $tol&gt; &lt;-maxNumIter $maxNumIter&gt;
&lt;-epscuLimit $epscuLimit&gt; &lt;-stRatio
$stRatio&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>integer tag identifying material.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">secType</code></td>
<td><p>tag for the transverse reinforcement configuration. See NOTE
1.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fpc</code></td>
<td><p>unconfined cylindrical strength of concrete specimen.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ec</code></td>
<td><p>initial elastic modulus of unconfined concrete.</p></td>
</tr>
<tr class="odd">
<td><p><strong>&lt;-epscu $epscu&gt; OR &lt;-gamma
$gamma&gt;</strong></p></td>
<td><p>confined concrete ultimate strain. See NOTE 2.</p></td>
</tr>
<tr class="even">
<td><p><strong>&lt;-nu $nu&gt; OR &lt;-varub&gt; OR
&lt;-varnoub&gt;</strong></p></td>
<td><p>Poisson's Ratio. See NOTE 3.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$L1</strong></p></td>
<td><p>length/diameter of square/circular core section measured respect
to the hoop center line.</p></td>
</tr>
<tr class="even">
<td><p><strong>($L2), ($L3)</strong></p></td>
<td><p>additional dimensions when multiple hoops are being used. See
NOTE 4.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">phis</code></td>
<td><p>hoop diameter. If section arrangement has multiple hoops it
refers to the external hoop.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">S</code></td>
<td><p>hoop spacing.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fyh</code></td>
<td><p>yielding strength of the hoop steel.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Es0</code></td>
<td><p>elastic modulus of the hoop steel.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">haRatio</code></td>
<td><p>hardening ratio of the hoop steel.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">mu</code></td>
<td><p>ductility factor of the hoop steel.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">phiLon</code></td>
<td><p>diameter of longitudinal bars.</p></td>
</tr>
<tr class="even">
<td><p><strong>&lt;-internal $phisi $Si $fyhi $Es0i $haRatioi
$mui&gt;</strong></p></td>
<td><p>optional parameters for defining the internal transverse
reinforcement. If they are not specified they will be assumed equal to
the external ones (for S2, S3, S4a, S4b and S5 typed).</p></td>
</tr>
<tr class="odd">
<td><p><strong>&lt;-wrap $cover $Am $Sw $ful $Es0w&gt;</strong></p></td>
<td><p>optional parameters required when section is strengthened with
FRP wraps. See NOTE 5.</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<p>1) The following section types are available:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>S1</strong></p></td>
<td><p>square section with S1 type of transverse reinforcement with or
without external FRP wrapping;</p></td>
</tr>
<tr class="even">
<td><p><strong>S2</strong></p></td>
<td><p>square section with S2 type of transverse reinforcement with or
without external FRP wrapping;</p></td>
</tr>
<tr class="odd">
<td><p><strong>S3</strong></p></td>
<td><p>square section with S3 type of transverse reinforcement with or
without external FRP wrapping;</p></td>
</tr>
<tr class="even">
<td><p><strong>S4a</strong></p></td>
<td><p>square section with S4a type of transverse reinforcement with or
without external FRP wrapping;</p></td>
</tr>
<tr class="odd">
<td><p><strong>S4b</strong></p></td>
<td><p>square section with S4b type of transverse reinforcement with or
without external FRP wrapping;</p></td>
</tr>
<tr class="even">
<td><p><strong>S5</strong></p></td>
<td><p>square section with S5 type of transverse reinforcement with or
without external FRP wrapping;</p></td>
</tr>
<tr class="odd">
<td><p><strong>C</strong></p></td>
<td><p>circular section with or without external FRP wrapping;</p></td>
</tr>
<tr class="even">
<td><p><strong>R</strong></p></td>
<td><p>rectangular section with or without external FRP
wrapping.</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/SectionTypes.png" title="SectionTypes.png" width="300"
alt="SectionTypes.png" />
<figcaption aria-hidden="true">SectionTypes.png</figcaption>
</figure>
<p>2) The confined concrete ultimate strain is defined using
<strong>-epscu</strong> or <strong>-gamma</strong>. When
<strong>-gamma</strong> option is specified, <strong>$gamma</strong> is
the ratio of the strength corresponding to ultimate strain to the peak
strength of the confined concrete stress-strain curve. If
<strong>$gamma</strong> cannot be achieved in the range [0,
<strong>$epscuLimit</strong>] then <strong>$epscuLimit</strong>
(optional, default: 0.05) will be assumed as ultimate strain.</p>
<p>3) Poisson's Ratio is specified by one of these 3 methods: a)
providing <strong>$nu</strong> using the <strong>-nu</strong> option. b)
using the <strong>-varUB</strong> option in which Poisson’s ratio is
defined as a function of axial strain by means of the expression
proposed by Braga et al. (2006) with the upper bound equal to 0.5; or c)
using the <strong>-varNoUB</strong> option in which case Poisson’s ratio
is defined as a function of axial strain by means of the expression
proposed by Braga et al. (2006) without any upper bound.</p>
<p>4) <strong>$L1</strong> (2l), <strong>$L2</strong> (a) and
<strong>$L3</strong> (b) are required when either S4a or S4b section
types is used. <strong>$L1</strong> (2d) and <strong>$L2</strong> (2c)
must be used for rectangular section.</p>
<p>5) When external stengthening is used must be specified the following
parameters:</p>
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">cover</code></td>
<td><p>cover thickness measured from the outer line of hoop.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Am</code></td>
<td><p>total area of FRP wraps (number of layers x wrap thickness x wrap
width).</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Sw</code></td>
<td><p>spacing of FRP wraps (if continuous wraps are used the spacing is
equal to the wrap width).</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ful</code></td>
<td><p>ultimate strength of FRP wraps.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Es0w</code></td>
<td><p>elastic modulus of FRP wraps.</p></td>
</tr>
</tbody>
</table>
<p>6) Stresses and strains can be defined either as positive
or as negative values. All commands are not case
sensitive.</p>
<p>EXAMPLES:</p>
<p><strong>Square section reinforced by simple transverse hoop
and by additional FRP wraps (Section S1)</strong></p>
<figure>
<img src="/OpenSeesRT/contrib/static/S1.png" title="S1.png" width="500" alt="S1.png" />
<figcaption aria-hidden="true">S1.png</figcaption>
</figure>
<p><em>Section S1</em></p>
<p>&lt;source lang="tcl"&gt;</p>
<ol>
<li>uniaxialMaterial ConfinedConcrete01 $tag $secType $fpc $Ec -epscu
$epscu $nu $L1 $phis $S $fyh $Es0 $haRatio $mu $phiLon -stRatio
$stRatio</li>
</ol>
<p>uniaxialMaterial ConfinedConcrete01 1 S1 -30.0 26081.0 -epscu -0.03
-varub 300.0 10.0 100.0 300.0 206000.0 0.0 1000.0 16.0 -stRatio 0.85
&lt;/source&gt;</p>
<p><em>Section S1 strengthened by additional FRP wraps</em> &lt;source
lang="tcl"&gt;</p>
<ol>
<li>uniaxialMaterial ConfinedConcrete01 $tag $secType $fpc $Ec -epscu
$epscu $nu $L1 $phis $S $fyh $Es0 $haRatio $mu phiLon $cover $Am $Sw
$ful $Es0w -stRatio $stRatio</li>
</ol>
<p>uniaxialMaterial ConfinedConcrete01 1 S1 -30.0 26081.0 -epscu -0.03
-varub 300.0 10.0 100.0 300.0 206000.0 0.0 1000.0 16.0 -wrap 30.0 51.0
100.0 3900.0 230000.0 -stRatio 0.85 &lt;/source&gt;</p>
<p><strong>Square section reinforced by multiple transverse hoop
and by additional FRP wraps (Section S4a)</strong></p>
<figure>
<img src="/OpenSeesRT/contrib/static/S4a.png" title="S4a.png" width="500" alt="S4a.png" />
<figcaption aria-hidden="true">S4a.png</figcaption>
</figure>
<p><em>Section S4a</em> &lt;source lang="tcl"&gt;</p>
<ol>
<li>uniaxialMaterial ConfinedConcrete01 $tag $secType $fpc $Ec -epscu
$epscu $nu $L1 $L2 $L3 $phis $S $fyh $Es0 $haRatio $mu $phiLon -stRatio
$stRatio</li>
</ol>
<p>uniaxialMaterial ConfinedConcrete01 1 S4a -30.0 26081.0 -epscu -0.03
-varUB 300.0 200.0 100.0 10.0 100.0 300.0 206000.0 0.0 1000.0 16.0
-stRatio 0.85 &lt;/source&gt;</p>
<p><em>Section S4a strengthened by additional FRP wraps</em> &lt;source
lang="tcl"&gt;</p>
<ol>
<li>uniaxialMaterial ConfinedConcrete01 $tag $secType $fpc $Ec -epscu
$epscu $nu $L1 $L2 $L3 $phis $S $fyh $Es0 $haRatio $mu $phiLon $cover
$Am $Sw $ful $Es0w -stRatio $stRatio</li>
</ol>
<p>uniaxialMaterial ConfinedConcrete01 1 S4a -30.0 26081.0 -epscu -0.03
-varUB 300.0 200.0 100.0 10.0 100.0 300.0 206000.0 0.0 1000.0 16.0 -wrap
30.0 51.0 100.0 3900.0 230000.0 -stRatio 0.85 &lt;/source&gt;</p>
<p><strong>Rectangular section reinforced by simple transverse
hoop and by additional FRP wraps (Section R)</strong></p>
<figure>
<img src="/OpenSeesRT/contrib/static/R.png" title="R.png" width="500" alt="R.png" />
<figcaption aria-hidden="true">R.png</figcaption>
</figure>
<p><em>Section R</em> &lt;source lang="tcl"&gt;</p>
<ol>
<li>uniaxialMaterial ConfinedConcrete01 $tag $secType $fpc $Ec -epscu
$epscu $nu $L1 $L2 $phis $S $fyh $Es0 $haRatio $mu $phiLon -stRatio
$stRatio</li>
</ol>
<p>uniaxialMaterial ConfinedConcrete01 1 R -30.0 26081.0 -epscu -0.03
-varUB 500.0 300.0 10.0 100.0 300.0 206000.0 0.0 1000.0 16.0 -stRatio
0.85 &lt;/source&gt;</p>
<p><em>Section R strengthened by additional FRP wraps</em> &lt;source
lang="tcl"&gt;</p>
<ol>
<li>uniaxialMaterial ConfinedConcrete01 $tag $secType $fpc $Ec -epscu
$epscu $nu $L1 $L2 $phis $S $fyh $Es0 $haRatio $mu $phiLon $cover $Am
$Sw $ful $Es0w -stRatio $stRatio</li>
</ol>
<p>uniaxialMaterial ConfinedConcrete01 1 R -30.0 26081.0 -epscu -0.03
-varUB 500.0 300.0 10.0 100.0 300.0 206000.0 0.0 1000.0 16.0 -wrap 30.0
51.0 100.0 3900.0 230000.0 -stRatio 0.85 &lt;/source&gt;</p>
<hr />
<p>REFEERENCES:</p>
<ol>
<li>Attard, M. M., Setunge, S., 1996. “Stress-strain relationship of
confined and unconfined concrete”. Material Journal ACI, 93(5),
432-444</li>
<li>Braga, F., Gigliotti, R., Laterza, M., 2006. “Analytical
stress-strain relationship for concrete confined by steel stirrups
and/or FRP jackets”. Journal of Structural Engineering ASCE, 132(9),
1402-1416.</li>
<li>D’Amato M., February 2009. “Analytical models for non linear
analysis of RC structures: confined concrete and bond-slips of
longitudinal bars”. Doctoral Thesis. University of Basilicata, Potenza,
Italy.</li>
<li>D'Amato, M., Braga, F., Gigliotti, R., Kunnath S., Laterza, M.,
2012. “A numerical general-purpose confinement model for non-linear
analysis of R/C members”. Computers and Structures Journal, Elsevier,
Vol. 102-103, 64-75.</li>
<li>Karsan, I. D., Jirsa, J. O., 1969. “Behavior of concrete under
compressive loadings”, Journal of Structural Division ASCE, 95(12),
2543-2563.</li>
</ol>
<hr />
<p>Code Developed by: <span style="color:blue"> Michele D'Amato,
University of Basilicata, Italy </span></p>

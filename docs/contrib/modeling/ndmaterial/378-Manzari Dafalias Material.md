# Manzari Dafalias Material

<p>This command is used to construct a multi-dimensional
Manzari-Dafalias(2004) material.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDmaterial ManzariDafalias $matTag $G0 $nu $e_init $Mc $c
$lambda_c $e0 $ksi $P_atm $m $h0 $ch $nb $A0 $nd $z_max $cz
$Den</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$G0</strong></p></td>
<td><p>shear modulus constant</p></td>
</tr>
<tr class="odd">
<td><p><strong>$nu</strong></p></td>
<td><p>poisson ratio</p></td>
</tr>
<tr class="even">
<td><p><strong>$e_init</strong></p></td>
<td><p>initial void ratio</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Mc</strong></p></td>
<td><p>critical state stress ratio</p></td>
</tr>
<tr class="even">
<td><p><strong>$c</strong></p></td>
<td><p>ratio of critical state stress ratio in extension and
compression</p></td>
</tr>
<tr class="odd">
<td><p><strong>$lambda_c</strong></p></td>
<td><p>critical state line constant</p></td>
</tr>
<tr class="even">
<td><p><strong>$e0</strong></p></td>
<td><p>critical void ratio at p = 0</p></td>
</tr>
<tr class="odd">
<td><p><strong>$ksi</strong></p></td>
<td><p>critical state line constant</p></td>
</tr>
<tr class="even">
<td><p><strong>$P_atm</strong></p></td>
<td><p>atmospheric pressure</p></td>
</tr>
<tr class="odd">
<td><p><strong>$m</strong></p></td>
<td><p>yield surface constant (radius of yield surface in stress ratio
space)</p></td>
</tr>
<tr class="even">
<td><p><strong>$h0</strong></p></td>
<td><p>constant parameter</p></td>
</tr>
<tr class="odd">
<td><p><strong>$ch</strong></p></td>
<td><p>constant parameter</p></td>
</tr>
<tr class="even">
<td><p><strong>$nb</strong></p></td>
<td><p>bounding surface parameter, $nb &amp;ge; 0</p></td>
</tr>
<tr class="odd">
<td><p><strong>$A0</strong></p></td>
<td><p>dilatancy parameter</p></td>
</tr>
<tr class="even">
<td><p><strong>$nd</strong></p></td>
<td><p>dilatancy surface parameter $nd &amp;ge; 0</p></td>
</tr>
<tr class="odd">
<td><p><strong>$z_max</strong></p></td>
<td><p>fabric-dilatancy tensor parameter</p></td>
</tr>
<tr class="even">
<td><p><strong>$cz</strong></p></td>
<td><p>fabric-dilatancy tensor parameter</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Den</strong></p></td>
<td><p>mass density of the material</p></td>
</tr>
</tbody>
</table>
<p>The material formulations for the Manzari-Dafalias object are
"ThreeDimensional" and "PlaneStrain"</p>
<hr />
<p>Code Developed by: <span style="color:blue">Alborz Ghofrani, <a
href="http://www.ce.washington.edu/people/faculty/bios/arduino_p.html">Pedro
Arduino, U Washington</a></span></p>
<hr />
<h2 id="notes">Notes</h2>
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
<h2 id="theory">Theory</h2>
<p>&lt;math&gt; p = \frac{1}{3} \mathrm{tr}(\mathbf{\sigma})
&lt;/math&gt;</p>
<p>&lt;math&gt; \mathbf{s} = \mathrm{dev} (\mathbf{\sigma}) =
\mathbf{\sigma} - \frac{1}{3} p \mathbf{1} &lt;/math&gt;</p>
<h3 id="elasticity">Elasticity</h3>
<p>Elastic moduli are considered to be functions of p and current void
ratio:</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; G = G_0
p_{atm}\frac{\left(2.97-e\right)^2}{1+e}\left(\frac{p}{p_{atm}}\right)^{1/2}
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

$$K = \frac{2(1+\nu)}{3(1-2\nu)} G $$

</dd>
</dl>
</dd>
</dl>
<p>The elastic stress-strain relationship is:</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; d\mathbf{e}^\mathrm{e} = \frac{d\mathbf{s}}{2G}
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
&lt;math&gt; d\varepsilon^\mathrm{e}_v = \frac{dp}{K}
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<h3 id="critical_state_line">Critical State Line</h3>
<p>A power relationship is assumed for the critical state line:</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>

$$e_c = e_0 - \lambda_c\left(\frac{p_c}{p_{atm}}\right)^\xi
$$

</dd>
</dl>
</dd>
</dl>
<p>where $e_0$ is the void ratio at &lt;math&gt;
p_c = 0 &lt;/math&gt; and $\lambda_c $ and
$\xi $ constants.</p>
<h3 id="yield_surface">Yield Surface</h3>
<p>Yield surface is a stress-ratio dependent surface in this model and
is defined as</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; \left\| \mathbf{s} - p \mathbf{\alpha} \right\| -
\sqrt\frac{2}{3}pm = 0 &lt;/math&gt;
</dd>
</dl>
</dd>
</dl>
<p>with $\mathbf{\alpha} $ being the deviatoric
back stress-ratio.</p>
<h3 id="plastic_strain_increment">Plastic Strain Increment</h3>
<p>The increment of the plastic strain tensor is given by</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; d\mathbf{\varepsilon}^p = \langle L \rangle \mathbf{R}
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
&lt;math&gt; \mathbf{R} = \mathbf{R'} + \frac{1}{3} D \mathbf{1}
&lt;/math&gt;
</dd>
</dl>
</dd>
</dl>
<p>therefore</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; d\mathbf{e}^p = \langle L \rangle \mathbf{R'}&lt;/math&gt;
and $d\varepsilon^p_v = \langle L \rangle D $
</dd>
</dl>
</dd>
</dl>
<p>The hardening modulus in this model is defined as</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; K_p = \frac{2}{3} p h (\mathbf{\alpha}^b_{\theta} -
\mathbf{\alpha}): \mathbf{n}
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt; where $\mathbf{n}$ is the
deviatoric part of the gradient to yield surface.</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; \mathbf{\alpha}^b_{\theta} = \sqrt{\frac{2}{3}}
\left[g(\theta,c) M_c exp(-n^b\Psi) - m\right] \mathbf{n}
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;, $\Psi$ being the state
parameter.</p>
<p>the hardening parameter $h $ is defined
as</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; h =
\frac{b_0}{(\mathbf{\alpha}-\mathbf{\alpha_{in}}):\mathbf{n}}
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;, $\mathbf{\alpha_{in}}$ is the
value of $\mathbf{\alpha}$ at initiation of
loading cycle.</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>

$$b_0 = G_0 h_0 (1-c_h e)
\left(\frac{p}{p_{atm}}\right)^{-1/2} $$

</dd>
</dl>
</dd>
</dl>
<p>Also the dilation parameters are defined as</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; D = A_d (\mathbf{\alpha}^d_{\theta}-\mathbf{\alpha}) :
\mathbf{n}
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
&lt;math&gt; \mathbf{\alpha}^d_{\theta} = \sqrt{\frac{2}{3}}
\left[g(\theta,c) M_c exp(n^d\Psi) - m\right] \mathbf{n}
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
&lt;math&gt; A_d = A_0 (1+\langle \mathbf{z : n}\rangle) &lt;/math&gt;,
where $\mathbf{z} $ is the fabric tensor.
</dd>
</dl>
</dd>
</dl>
<p>The evolution of fabric and the back stress-ratio tensors are defined
as</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>

$$d\mathbf{z} = - c_z \langle -d\varepsilon^p_v \rangle
(z_{max}\mathbf{n}+\mathbf{z}) $$

</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
&lt;math&gt; d\mathbf{\alpha} = \langle L \rangle (2/3) h
(\mathbf{\alpha}^b_{\theta} - \mathbf{\alpha})
</dd>
</dl>
</dd>
</dl>
<p>&lt;/math&gt;</p>
<h2 id="example">Example</h2>
<p>This example, provides an undrained confined triaxial compression
test using one 8-node SSPBrickUP element and ManzariDafalias material
model.</p>
<p>&lt;source lang="tcl"&gt;</p>
<ol>
<li>HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
#</li>
<li>3D Undrained Conventional Triaxial Compression Test Using One
Element #</li>
<li>University of Washington, Department of Civil and Environmental Eng
#</li>
<li>Geotechnical Eng Group, A. Ghofrani, P. Arduino - Dec 2013 #</li>
<li>Basic units are m, Ton(metric), s #</li>
<li>HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
#</li>
</ol>
<p>wipe</p>
<ol>
<li>------------------------ #</li>
<li>Test Specific parameters #</li>
<li>------------------------ #</li>
<li>Confinement Stress</li>
</ol>
<p>set pConf -300.0</p>
<ol>
<li>Deviatoric strain</li>
</ol>
<p>set devDisp -0.3</p>
<ol>
<li>Permeablity</li>
</ol>
<p>set perm 1.0e-10</p>
<ol>
<li>Initial void ratio</li>
</ol>
<p>set vR 0.8</p>
<ol>
<li>Rayleigh damping parameter</li>
</ol>
<p>set damp 0.1 set omega1 0.0157 set omega2 64.123 set a1 [expr
2.0*$damp/($omega1+$omega2)] set a0 [expr $a1*$omega1*$omega2]</p>
<ol>
<li>HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH</li>
<li>HHHHHHHHHHHHHHHHHHHHHHHHHHHCreate
ModelHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH</li>
<li>HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH</li>
</ol>
<ol>
<li>Create a 3D model with 4 Degrees of Freedom</li>
</ol>
<p>model BasicBuilder -ndm 3 -ndf 4</p>
<ol>
<li>Create nodes</li>
</ol>
<p>node 1 1.0 0.0 0.0 node 2 1.0 1.0 0.0 node 3 0.0 1.0 0.0 node 4 0.0
0.0 0.0 node 5 1.0 0.0 1.0 node 6 1.0 1.0 1.0 node 7 0.0 1.0 1.0 node 8
0.0 0.0 1.0</p>
<ol>
<li>Create Fixities</li>
</ol>
<p>fix 1 0 1 1 1 fix 2 0 0 1 1 fix 3 1 0 1 1 fix 4 1 1 1 1 fix 5 0 1 0 1
fix 6 0 0 0 1 fix 7 1 0 0 1 fix 8 1 1 0 1</p>
<ol>
<li>Create material</li>
<li>ManzariDafalias tag G0 nu e_init Mc c lambda_c e0 ksi P_atm m h0 ch
nb A0 nd z_max cz Den</li>
</ol>
<p>nDMaterial ManzariDafalias 1 125 0.05 $vR 1.25 0.712 0.019 0.934 0.7
100 0.01 7.05 0.968 1.1 0.704 3.5 4 600 1.42</p>
<ol>
<li>Create element</li>
<li>SSPbrickUP tag i j k l m n p q matTag fBulk fDen k1 k2 k3 void alpha
&lt;b1 b2 b3&gt;</li>
</ol>
<p>element SSPbrickUP 1 1 2 3 4 5 6 7 8 1 2.2e6 1.0 $perm $perm $perm
$vR 1.5e-9</p>
<ol>
<li>Create recorders</li>
</ol>
<p>recorder Node -file disp.out -time -nodeRange 1 8 -dof 1 2 3 disp
recorder Node -file press.out -time -nodeRange 1 8 -dof 4 vel recorder
Element -file stress.out -time stress recorder Element -file strain.out
-time strain recorder Element -file alpha.out -time alpha recorder
Element -file fabric.out -time fabric</p>
<ol>
<li>Create analysis</li>
</ol>
<p>constraints Penalty 1.0e18 1.0e18 test NormDispIncr 1.0e-5 20 1
algorithm Newton numberer RCM system BandGeneral integrator Newmark 0.5
0.25 rayleigh $a0 0. $a1 0.0 analysis Transient</p>
<ol>
<li>Apply confinement pressure</li>
</ol>
<p>set pNode [expr $pConf / 4.0] pattern Plain 1 {Series -time {0 10000
1e10} -values {0 1 1} -factor 1} { load 1 $pNode 0.0 0.0 0.0 load 2
$pNode $pNode 0.0 0.0 load 3 0.0 $pNode 0.0 0.0 load 4 0.0 0.0 0.0 0.0
load 5 $pNode 0.0 $pNode 0.0 load 6 $pNode $pNode $pNode 0.0 load 7 0.0
$pNode $pNode 0.0 load 8 0.0 0.0 $pNode 0.0 } analyze 100 100</p>
<ol>
<li>Let the model rest and waves damp out</li>
</ol>
<p>analyze 50 100</p>
<ol>
<li>Close drainage valves</li>
</ol>
<p>for {set x 1} {$x&lt;9} {incr x} { remove sp $x 4 } analyze 50
100</p>
<ol>
<li>Read vertical displacement of top plane</li>
</ol>
<p>set vertDisp [nodeDisp 5 3]</p>
<ol>
<li>Apply deviatoric strain</li>
</ol>
<p>set lValues [list 1 [expr 1+$devDisp/$vertDisp] [expr
1+$devDisp/$vertDisp]] set ts "{Series -time {20000 1020000 10020000}
-values {$lValues} -factor 1}"</p>
<ol>
<li>loading object deviator stress</li>
</ol>
<p>eval "pattern Plain 2 $ts { sp 5 3 $vertDisp sp 6 3 $vertDisp sp 7 3
$vertDisp sp 8 3 $vertDisp }"</p>
<ol>
<li>Set number and length of (pseudo)time steps</li>
</ol>
<p>set dT 100 set numStep 10000</p>
<ol>
<li>Analyze and use substepping if needed</li>
</ol>
<p>set remStep $numStep set success 0 proc subStepAnalyze {dT subStep} {
if {$subStep &gt; 10} { return -10 } for {set i 1} {$i &lt; 3} {incr i}
{ puts "Try dT = $dT" set success [analyze 1 $dT] if {$success != 0} {
set success [subStepAnalyze [expr $dT/2.0] [expr $subStep+1]] if
{$success == -10} { puts "Did not converge." return success } } else {
if {$i==1} { puts "Substep $subStep : Left side converged with dT = $dT"
} else { puts "Substep $subStep : Right side converged with dT = $dT" }
} } return success }</p>
<p>puts "Start analysis" set startT [clock seconds]</p>
<p>while {$success != -10} { set subStep 0 set success [analyze $remStep
$dT] if {$success == 0} { puts "Analysis Finished" break } else { set
curTime [getTime] puts "Analysis failed at $curTime . Try substepping."
set success [subStepAnalyze [expr $dT/2.0] [incr subStep]] set curStep
[expr int(($curTime-20000)/$dT + 1)] set remStep [expr
int($numStep-$curStep)] puts "Current step: $curStep , Remaining steps:
$remStep" } } set endT [clock seconds] puts "loading analysis execution
time: [expr $endT-$startT] seconds."</p>
<p>wipe &lt;/source&gt;</p>
<h2 id="references">References</h2>
<p>Dafalias YF, Manzari MT. "Simple plasticity sand model accounting for
fabric change effects". Journal of Engineering Mechanics 2004</p>

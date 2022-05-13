# PressureDependMultiYield-Example 2

<table>
<tbody>
<tr class="odd">
<td><p>&lt;center&gt;<strong>Elastic Pressure Dependent Dry Level
Pushover</strong>&lt;/center&gt;</p></td>
</tr>
</tbody>
</table>
<h2 id="input_file">Input File</h2>
<p>&lt;syntaxhighlight lang="tcl"&gt;</p>
<ol>
<li>Created by Zhaohui Yang (zhyang@ucsd.edu)</li>
<li>elastic pressure dependent material</li>
<li>plane strain, single element,</li>
<li>push over analysis (Applied load linearly increases with time),</li>
<li>SI units (m, s, KN, ton)</li>
<li></li>
<li>4 3</li>
<li>------- --&gt; F (loads applied to node 3)</li>
<li>| |</li>
<li>| |</li>
<li>| |</li>
<li>1-------2 (nodes 1 and 2 fixed)</li>
<li>^ ^</li>
</ol>
<p>wipe</p>
<ol>
<li></li>
<li>some user defined variables</li>
<li></li>
</ol>
<p>set massDen 2.000 ;# mass density set massProportionalDamping 0.0 ;
set stiffnessProportionalDamping 0.001 ; set fangle 31.4 ;#friction
angle set ptangle 26.5 ;#phase transformation angle set E1 90000.0
;#Young's modulus set poisson1 0.40 ; set G [expr $E1/(2*(1+$poisson1))]
; set B [expr $E1/(3*(1-2*$poisson1))] ; set press 0 ;# isotropic
consolidation pressure on quad element(s) set loadIncr 1 ;# Static shear
load set period 2 ;# Period of applied sinusoidal load set deltaT 0.01
;# time step for analysis set numSteps 2000 ;# Number of analysis steps
set gamma 0.5 ;# Newmark integration parameter set unitWeightX 0.0
;#unit weight in X direction set unitWeightY [expr -9.81*($massDen)]
;#unit weight in Y direction</p>
<ol>
<li><ol>
<li></li>
</ol></li>
<li>create the ModelBuilder</li>
</ol>
<p>model basic -ndm 2 -ndf 2</p>
<ol>
<li>define material and properties</li>
</ol>
<p>nDMaterial PressureDependMultiYield 2 2 $massDen $G $B $fangle .1 80
0.5 \ $ptangle 0.17 0.4 10 10 0.015 1.0 nDMaterial FluidSolidPorous 1 2
2 2.2e6</p>
<ol>
<li>define the nodes</li>
</ol>
<p>node 1 0.0 0.0 node 2 1.0 0.0 node 3 1.0 1.0 node 4 0.0 1.0</p>
<ol>
<li>define the element thick material maTag press density gravity</li>
</ol>
<p>element quad 1 1 2 3 4 1.0 "PlaneStrain" 2 $press 0.0 $unitWeightX
$unitWeightY</p>
<p>updateMaterialStage -material 2 -stage 0</p>
<ol>
<li>fix the base in vertical direction</li>
</ol>
<p>fix 1 1 1 fix 2 1 1</p>
<ol>
<li>tie nodes 3 and 4</li>
</ol>
<p>equalDOF 3 4 1 2</p>
<ol>
<li><ol>
<li></li>
</ol></li>
<li>GRAVITY APPLICATION (elastic behavior)</li>
<li>create the SOE, ConstraintHandler, Integrator, Algorithm and
Numberer</li>
</ol>
<p>system ProfileSPD test NormDispIncr 1.e-12 25 0 constraints
Transformation integrator LoadControl 1 1 1 1 algorithm Newton numberer
RCM analysis Static</p>
<ol>
<li>analyze</li>
</ol>
<p>analyze 2</p>
<ol>
<li>switch the material to elastic pressure dependent</li>
</ol>
<p>updateMaterialStage -material 2 -stage 2</p>
<ol>
<li>analyze</li>
</ol>
<p>analyze 1</p>
<ol>
<li><ol>
<li></li>
</ol></li>
<li>NOW APPLY LOADING SEQUENCE AND ANALYZE</li>
</ol>
<ol>
<li>rezero time</li>
</ol>
<p>setTime 0.0 wipeAnalysis</p>
<ol>
<li>create a LoadPattern with a Linear time series</li>
</ol>
<p>pattern Plain 1 Linear { load 3 $loadIncr 0.0 ;#load applied in x
direction }</p>
<ol>
<li>create the Analysis</li>
</ol>
<p>constraints Transformation ; # Penalty 1.0e18 1.0e18 ;# test
NormDispIncr 1.e-12 25 0 algorithm Newton numberer RCM system ProfileSPD
rayleigh $massProportionalDamping 0.0 $stiffnessProportionalDamping 0.
integrator Newmark $gamma [expr pow($gamma+0.5, 2)/4] analysis
VariableTransient</p>
<ol>
<li>create the recorder</li>
</ol>
<p>recorder Node -file disp.out -time -node 1 2 3 4 -dof 1 2 -dT 0.01
disp recorder Node -file acce.out -time -node 1 2 3 4 -dof 1 2 -dT 0.01
accel recorder Element -ele 1 -time -file stress1.out -dT 0.01 material
1 stress recorder Element -ele 1 -time -file strain1.out -dT 0.01
material 1 strain recorder Element -ele 1 -time -file stress3.out -dT
0.01 material 3 stress recorder Element -ele 1 -time -file strain3.out
-dT 0.01 material 3 strain</p>
<ol>
<li>analyze</li>
</ol>
<p>set startT [clock seconds] analyze $numSteps $deltaT [expr
$deltaT/100] $deltaT 10 set endT [clock seconds] puts "Execution time:
[expr $endT-$startT] seconds."</p>
<p>wipe #flush ouput stream</p>
<p>&lt;/syntaxhighlight&gt;</p>
<h2 id="matlab_plotting_file">MATLAB Plotting File</h2>
<p>&lt;syntaxhighlight lang="matlab"&gt; clear all;</p>
<p>a1=load('acce.out'); d1=load('disp.out'); s1=load('stress1.out');
e1=load('strain1.out'); s5=load('stress3.out');
e5=load('strain3.out');</p>
<p>fs=[0.5, 0.2, 4, 6];</p>
<p>%integration point 1 p-q po=(s1(:,2)+s1(:,3)+s1(:,4))/3; for
i=1:size(s1,1) qo(i)=(s1(i,2)-s1(i,3))^2 + (s1(i,3)-s1(i,4))^2
+(s1(i,2)-s1(i,4))^2 + 6.0* s1(i,5)^2;
qo(i)=sign(s1(i,5))*1/3.0*qo(i)^0.5; end figure(1); clf; %integration
point 1 stress-strain subplot(2,1,1), plot(e1(:,4),s1(:,5),'r'); title
('Integration point 1 shear stress \tau_x_y VS. shear strain
\epsilon_x_y'); xLabel('Shear strain \epsilon_x_y'); yLabel('Shear
stress \tau_x_y (kPa)');</p>
<p>subplot(2,1,2), plot(-po,qo,'r'); title ('Integration point 1
confinement p VS. deviatoric q relation'); xLabel('confinement p
(kPa)'); yLabel('q (kPa)'); set(gcf,'paperposition',fs);
saveas(gcf,'SS_PQ1','jpg');</p>
<p>%integration point 3 p-q po=(s5(:,2)+s5(:,3)+s5(:,4))/3; for
i=1:size(s5,1) qo(i)=(s5(i,2)-s5(i,3))^2 + (s5(i,3)-s5(i,4))^2
+(s5(i,2)-s5(i,4))^2 + 6.0* s5(i,5)^2;
qo(i)=sign(s5(i,5))*1/3.0*qo(i)^0.5; end</p>
<p>figure(4); clf; %integration point 3 stress-strain subplot(2,1,1),
plot(e5(:,4),s5(:,5),'r'); title ('Integration point 3 shear stress
\tau_x_y VS. shear strain \epsilon_x_y'); xLabel('Shear strain
\epsilon_x_y'); yLabel('Shear stress \tau_x_y (kPa)');</p>
<p>subplot(2,1,2), plot(-po,qo,'r'); title ('Integration point 3
confinement p VS. deviatoric q relation'); xLabel('confinement p
(kPa)'); yLabel('q (kPa)'); set(gcf,'paperposition',fs);
saveas(gcf,'SS_PQ5','jpg');</p>
<p>figure(2); clf; %node 3 displacement relative to node 1
subplot(2,1,1),plot(d1(:,1),d1(:,6),'r'); title ('Lateral displacement
at element top'); xLabel('Time (s)'); yLabel('Displacement (m)');
set(gcf,'paperposition',fs); saveas(gcf,'D','jpg');</p>
<p>&lt;/syntaxhighlight&gt;</p>
<h2 id="displacement_output_file">Displacement Output File</h2>
<figure>
<img src="/OpenSeesRT/contrib/static/PD_Ex9Disp.png" title="PD_Ex9Disp.png" alt="PD_Ex9Disp.png" />
<figcaption aria-hidden="true">PD_Ex9Disp.png</figcaption>
</figure>
<h2 id="stress_strain_output_file">Stress-Strain Output File</h2>
<figure>
<img src="/OpenSeesRT/contrib/static/PD_Ex9SS_PQ13.png" title="PD_Ex9SS_PQ13.png"
alt="PD_Ex9SS_PQ13.png" />
<figcaption aria-hidden="true">PD_Ex9SS_PQ13.png</figcaption>
</figure>
<hr />
<p>Return to: </p>

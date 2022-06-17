# PressureDependMultiYield02-Example 2

<table>
<tbody>
<tr class="odd">
<td><p>&lt;center&gt;<strong>Solid-fluid fully coupled (u-p) 8-node
brick element: saturated soil element with pressure dependent material,
subjected to 1D sinusoidal base shaking</strong>&lt;/center&gt;</p></td>
</tr>
</tbody>
</table>
<h2 id="input_file">Input File</h2>

```tcl
# single BrickUP element with pressure dependent material.
# subjected to 1D sinusoidal base shaking


# Written by Jinchi Lu and Zhaohui Yang (May 2004)

<p>wipe set friction 31. ;#friction angle set phaseTransform 26. ;#phase
transformation angle set G1 9.e4 ;
set B1 22.e4 ;
set gamma 0.600 ;#
Newmark integration parameter</p>
<p>set dt 0.01 ;# time step for analysis, does not have to be the same
as accDt. set numSteps 2500 ;# number of time steps set rhoS 1.80 ;#
saturated mass density set rhoF 1.00 ;# fluid mass density</p>
<p>set Bfluid 2.2e6 ;# fluid shear modulus set perm 1.e-5 ;#permeability
(m/s) set accGravity 9.81 ;#acceleration of gravity set perm [expr $perm/$accGravity/$rhoF] ;# actual value used in computation set matTag
1 ;# material tag</p>
<p>set accMul 1 ;# acceleration multiplier set pi 3.1415926535 ; set
inclination 0;</p>
<p>set massProportionalDamping 0.0 ; set
InitStiffnessProportionalDamping 0.002;</p>
<p>set gravityX [expr $accGravity*sin($inclination/180.0*$pi)] ;#
gravity acceleration in X direction set gravityY 0.0 ;# gravity
acceleration in Y direction set gravityZ [expr -$accGravity*cos($inclination/180.0*$pi)] ;# gravity acceleration in Z
direction</p>
set ndm 3 ;# space dimension
model BasicBuilder -ndm $ndm -ndf 4
<p>nDMaterial PressureDependMultiYield02 $matTag $ndm $rhoS $G1 $B1
$friction 0.1 80 0.5 \ $phaseTransform 0.067 0.23 0.06 0.27</p>
<p>node 1 0.00000 0.0000 0.00000
node 2 0.00000 0.0000 1.00000
node 3 0.00000 1.0000 0.00000
node 4 0.00000 1.0000 1.00000
node 5 1.00000 0.0000 0.00000
node 6 1.00000 0.0000 1.00000
node 7 1.00000 1.0000 0.00000
node 8 1.00000 1.0000 1.00000
<p>element brickUP 1 1 5 7 3 2 6 8 4 $matTag $Bfluid $rhoF $perm $perm
$perm $gravityX $gravityY $gravityZ</p>
updateMaterialStage -material $matTag -stage 0
<p>fix 1 1 1 1 0
fix 2 0 1 0 1
fix 3 1 1 1 0
fix 4 0 1 0 1
fix 5 1 1 1 0
fix 6 0 1 0 1
fix 7 1 1 1 0
fix 8 0 1 0 1</p>

# equalDOF
# tied nodes around

equalDOF 2 4 1 3 equalDOF 2 6 1 3 equalDOF 2 8 1 3
<p>set nodeList {} for {set i 1} {$i &lt;= 8 } {incr i 1} { lappend
nodeList $i }</p>
<p>set elementList {} for {set i 1} {$i &lt;= 1 } {incr i 1} { lappend
elementList $i }</p>

# GRAVITY APPLICATION (elastic behavior)
<li>create the SOE, ConstraintHandler, Integrator, Algorithm and
Numberer</li>

<p>numberer Plain system ProfileSPD test NormDispIncr 1.0e-8 20 1
algorithm KrylovNewton constraints Penalty 1.e18 1.e18 set nw 1.5
integrator Newmark $nw [expr pow($nw+0.5, 2)/4] analysis Transient</p>
analyze 10 5.e0

# switch the material to plastic

updateMaterialStage -material $matTag -stage 1
analyze 10 5.e1
<p>setTime 0.0 ;# reset time, otherwise reference time is not zero for
time history analysis wipeAnalysis</p>

#
# create recorders ##############################
#

<p>eval "recorder Node -file disp -time -node $nodeList -dof 1 2 3 -dT 0.01 disp"
eval "recorder Node -file acc -time -node $nodeList -dof 1 2 3 -dT 0.01 accel"
eval "recorder Node -file pwp -time -node $nodeList -dof 4 -dT 0.01 vel"
eval "recorder Element -ele $elementList -time -file stress1 -dT 0.01 material 1 stress"
eval "recorder Element -ele $elementList -time -file strain1 -dT 0.01 material 1 strain" eval
"recorder Element -ele $elementList -time -file stress3 -dT 0.01 material 3 stress"
eval "recorder Element -ele $elementList -time -file strain3 -dT 0.01 material 3 strain"
eval "recorder Element -ele $elementList -time -file stress5 -dT 0.01 material 5 stress" eval
"recorder Element -ele $elementList -time -file strain5 -dT 0.01 material 5 strain"</p>

<li><ol>
<li>create dynamic time history analysis ##################</li>
</ol></li>

<p>pattern UniformExcitation 1 1 -accel "Sine 0 10 1 -factor $accMul"
integrator Newmark $gamma [expr pow($gamma+0.5, 2)/4] rayleigh
$massProportionalDamping 0.0 $InitStiffnessProportionalDamping 0.0
constraints Penalty 1.e18 1.e18 ;# can't combine with test NormUnbalance
test NormDispIncr 1.0e-3 25 0 ;# can't combine with constraints
Lagrange</p>

<li>algorithm Newton ;# tengent is updated at each iteration</li>

<p>algorithm KrylovNewton ;# system ProfileSPD ;# Use sparse solver.
Next numberer is better to be Plain. numberer Plain ;# method to map
between between equation numbers of DOFs analysis VariableTransient ;#
splitting time step requires VariableTransient</p>

#
# perform the Analysis and record time used #############
#

set startT [clock seconds] 
analyze $numSteps $dt [expr $dt/64] $dt 15
set endT [clock seconds] 
puts "Execution time: [expr $endT-$startT] seconds." 
```



<h2 id="matlab_plotting_file">MATLAB Plotting File</h2>


```matlab
 clear all;</p>
<p>a1=load('acc'); d1=load('disp'); p1=load('pwp'); s1=load('stress1');
e1=load('strain1'); s5=load('stress3'); e5=load('strain3');
s9=load('stress5'); e9=load('strain5');</p>
<p>fs=[0.5, 0.2, 4, 6]; fs2=[0.5, 0.2, 4, 3]; accMul = 2;</p>
<p>%integration point 1 p-q po=(s1(:,2)+s1(:,3)+s1(:,4))/3; for
i=1:size(s1,1) qo(i)=(s1(i,2)-s1(i,3))^2 + (s1(i,3)-s1(i,4))^2
+(s1(i,2)-s1(i,4))^2 + 6.0* (s1(i,5)^2 +s1(i,6)^2+s1(i,7)^2) ;
qo(i)=sign(s1(i,7))*1/3.0*qo(i)^0.5; end</p>
<p>figure(1); close 1; figure(1); %integration point 1 stress-strain
subplot(2,1,1), plot(e1(:,7),s1(:,7),'r'); title ('shear stress \tau_x_z
VS. shear strain \epsilon_x_z at integration point 1'); xLabel('Shear
strain \epsilon_x_z'); yLabel('Shear stress \tau_x_z (kPa)');
subplot(2,1,2), plot(-po,qo,'r'); title ('confinement p VS. deviatoric
stress q at integration point 1'); xLabel('confinement p (kPa)');
yLabel('q (kPa)'); set(gcf,'paperposition',fs);
saveas(gcf,'SS_PQ_p1','jpg');</p>
<p>%integration point 5 p-q po=(s5(:,2)+s5(:,3)+s5(:,4))/3; for
i=1:size(s5,1) qo(i)=(s5(i,2)-s5(i,3))^2 + (s5(i,3)-s5(i,4))^2
+(s5(i,2)-s5(i,4))^2 + 6.0*( s5(i,5)^2 + s5(i,6)^2 + s5(i,7)^2);
qo(i)=sign(s5(i,7))*1/3.0*qo(i)^0.5; end</p>
<p>figure(5); close 5; figure(5); %integration point 5 stress-strain
subplot(2,1,1), plot(e5(:,7),s5(:,7),'r'); title ('shear stress \tau_x_z
VS. shear strain \epsilon_x_z at integration point 3'); xLabel('Shear
strain \epsilon_x_z'); yLabel('Shear stress \tau_x_z (kPa)');
subplot(2,1,2), plot(-po,qo,'r'); title ('confinement p VS. deviatoric
stress q at integration point 3'); xLabel('confinement p (kPa)');
yLabel('q (kPa)'); set(gcf,'paperposition',fs);
saveas(gcf,'SS_PQ_p3','jpg');</p>
<p>%integration point 9 p-q po=(s9(:,2)+s9(:,3)+s9(:,4))/3; for
i=1:size(s1,1) qo(i)=(s9(i,2)-s9(i,3))^2 + (s9(i,3)-s9(i,4))^2
+(s9(i,2)-s9(i,4))^2 + 6.0*( s9(i,5)^2 + s9(i,6)^2 + s9(i,7)^2);
qo(i)=sign(s9(i,7))*1/3.0*qo(i)^0.5; end</p>
<p>figure(6); close 6; figure(6); %integration point 9 stress-strain
subplot(2,1,1), plot(e9(:,7),s9(:,7),'r'); title ('shear stress \tau_x_z
VS. shear strain \epsilon_x_z at integration point 5'); xLabel('Shear
strain \epsilon_x_z'); yLabel('Shear stress \tau_x_z (kPa)');
subplot(2,1,2), plot(-po,qo,'r'); title ('confinement p VS. deviatoric
stress q at integration point 5'); xLabel('confinement p (kPa)');
yLabel('q (kPa)'); set(gcf,'paperposition',fs);
saveas(gcf,'SS_PQ_p5','jpg');</p>
<p>figure(2); close 2; figure(2); %node 3 displacement relative to node
1 plot(d1(:,1),d1(:,5)); title ('Lateral displacement at element top');
xLabel('Time (s)'); yLabel('Displacement (m)');
set(gcf,'paperposition',fs2); saveas(gcf,'Disp','jpg');</p>
<p>s=accMul*sin(0:pi/50:20*pi); s=[s';zeros(3000,1)];
s1=interp1(0:0.01:40,s,a1(:,1));</p>
<p>figure(3); close 3; figure(3); %node acceleration a =
plot(a1(:,1),s1+a1(:,5),'r'); title ('Lateral acceleration at element
top'); xLabel('Time (s)'); yLabel('Acceleration (m/s^2)');
set(gcf,'paperposition',fs2); saveas(gcf,'Acc','jpg');</p>
<p>figure(4); close 4; figure(4); a=plot(p1(:,1),p1(:,2)); title ('Pore
pressure at base'); xLabel('Time (s)'); yLabel('Pore pressure (kPa)');
set(gcf,'paperposition',fs2); saveas(gcf,'EPWP','jpg');</p>
<p>
```

<h2 id="displacement_output_file">Displacement Output File</h2>
<figure>
<img src="PD02_Ex24Disp.jpg" title="PD02_Ex24Disp.jpg"
alt="PD02_Ex24Disp.jpg" />
<figcaption aria-hidden="true">PD02_Ex24Disp.jpg</figcaption>
</figure>
<h2 id="stress_strain_output_file_integration_point_1">Stress-Strain
Output File (integration point 1)</h2>
<figure>
<img src="PD02_Ex24SS_PQ1.jpg" title="PD02_Ex24SS_PQ1.jpg"
alt="PD02_Ex24SS_PQ1.jpg" />
<figcaption aria-hidden="true">PD02_Ex24SS_PQ1.jpg</figcaption>
</figure>
<h2 id="stress_strain_output_file_integration_point_3">Stress-Strain
Output File (integration point 3)</h2>
<figure>
<img src="PD02_Ex24SS_PQ3.jpg" title="PD02_Ex24SS_PQ3.jpg"
alt="PD02_Ex24SS_PQ3.jpg" />
<figcaption aria-hidden="true">PD02_Ex24SS_PQ3.jpg</figcaption>
</figure>
<h2 id="stress_strain_output_file_integration_point_5">Stress-Strain
Output File (integration point 5)</h2>
<figure>
<img src="PD02_Ex24SS_PQ5.jpg" title="PD02_Ex24SS_PQ5.jpg"
alt="PD02_Ex24SS_PQ5.jpg" />
<figcaption aria-hidden="true">PD02_Ex24SS_PQ5.jpg</figcaption>
</figure>
<h2 id="excess_pore_pressure_output_file">Excess Pore Pressure Output
File</h2>
<figure>
<img src="PD02_Ex24EPP.jpg" title="PD02_Ex24EPP.jpg"
alt="PD02_Ex24EPP.jpg" />
<figcaption aria-hidden="true">PD02_Ex24EPP.jpg</figcaption>
</figure>
<h2 id="acceleration_output_file">Acceleration Output File</h2>
<figure>
<img src="PD02_Ex24Accel.jpg" title="PD02_Ex24Accel.jpg"
alt="PD02_Ex24Accel.jpg" />
<figcaption aria-hidden="true">PD02_Ex24Accel.jpg</figcaption>
</figure>
<hr />
Return to: 

# PressureDependMultiYield02-Example 1

<table>
<tbody>
<tr class="odd">
<td><p>&lt;center&gt;<strong>Solid-fluid fully coupled (u-p)
plane-strain 9-4 noded element: saturated soil element with pressure
dependent material, subjected to 1D sinusoidal base
shaking</strong>&lt;/center&gt;</p></td>
</tr>
</tbody>
</table>
<h2 id="input_file">Input File</h2>
<p>&lt;syntaxhighlight lang="tcl"&gt;</p>
<ol>
<li>Written by Jinchi Lu and Zhaohui Yang (May 2004)</li>
</ol>
<p>wipe set matOpt 1 ;# 1 = pressure depend;</p>
<dl>
<dt># 2 = pressure independ;</dt>

</dl>
<p>set fmass 1 ;# fluid mass density set smass 2.0 ;# saturated soil
mass density set G 9.0e4 set B 2.2e5 set bulk 2.2e6 ;#fluid-solid
combined bulk modulus set vperm 5.e-6 ;#vertical permeability (m/s) set
hperm [expr $vperm] ;#horizontal permeability (m/s)</p>
<p>set accGravity 9.81 ;#acceleration of gravity set vperm [expr
$vperm/$accGravity/$fmass] ;#actual value used in computation set hperm
[expr $hperm/$accGravity/$fmass] ;#actual value used in computation set
loadBias 0.0 ;# Static shear load, in percentage</p>
<dl>
<dt># of gravity load (=sin(inclination angle))</dt>

</dl>
<p>set accMul 2. ;# acc. multiplier set period 1.0 ;# Period for applied
Sine wave set deltaT 0.01 ;# time step for analysis set numSteps 2500 ;#
number of time steps set gamma 0.6 ;# Newmark integration parameter</p>
<p>set massProportionalDamping 0. ; set InitStiffnessProportionalDamping
0.002;</p>
<ol>
<li><ol>
<li></li>
</ol></li>
<li>BUILD MODEL</li>
</ol>
<ol>
<li>create the ModelBuilder</li>
</ol>
<p>model basic -ndm 2 -ndf 3 node 1 0 0 node 2 2.5 0 node 3 2.5 2 node 4
0 2</p>
<p>fix 1 1 1 0 fix 2 1 1 0 fix 3 0 0 1 fix 4 0 0 1 equalDOF 3 4 1 2</p>
<p>model basic -ndm 2 -ndf 2 node 5 1.25 0. node 6 2.5 1 node 7 1.25 2
node 8 0 1 node 9 1.25 1</p>
<p>fix 5 1 1 equalDOF 3 7 1 2 equalDOF 6 8 1 2 equalDOF 6 9 1 2</p>
<p>set gravY [expr -$accGravity] ;#calc. gravity set gravX [expr
-$gravY*$loadBias]</p>
<ol>
<li>define material and properties</li>
</ol>
<p>switch $matOpt { 1 { nDMaterial PressureDependMultiYield02 1 2 1.8 $G
$B 32 .1 80 0.5\ 26. 0.067 0.23 0.06 0.27 } 2 { nDMaterial
PressureIndependMultiYield 2 2 1.8 4.e4 2.e5 40 .1 } }</p>
<ol>
<li>ele# thick maTag bulk mDensity perm1 perm2 gravity</li>
</ol>
<p>element 9_4_QuadUP 1 1 2 3 4 5 6 7 8 9 1.0 1 $bulk $fmass $hperm
$vperm $gravX $gravY</p>
<ol>
<li>set material to elastic for gravity loading</li>
</ol>
<p>updateMaterialStage -material $matOpt -stage 0</p>
<ol>
<li>recorder for nodal variables along the vertical center line.</li>
</ol>
<p>set SnodeList {} for {set i 0} {$i &lt; 9} {incr i 1} { lappend
SnodeList [expr $i+1] }</p>
<p>set FnodeList {} for {set i 0} {$i &lt; 4} {incr i 1} { lappend
FnodeList [expr $i+1] }</p>
<ol>
<li><ol>
<li></li>
</ol></li>
<li>GRAVITY APPLICATION (elastic behavior)</li>
</ol>
<ol>
<li>create the SOE, ConstraintHandler, Integrator, Algorithm and
Numberer</li>
</ol>
<p>numberer RCM system ProfileSPD test NormDispIncr 1.0e-8 30 0
algorithm KrylovNewton constraints Penalty 1.e18 1.e18 set nw 1.5 set
nw2 [expr pow($nw+0.5, 2)/4] integrator Newmark $nw $nw2 analysis
Transient</p>
<p>analyze 10 5e3</p>
<p>updateMaterialStage -material $matOpt -stage 1</p>
<p>analyze 100 1.e0</p>
<ol>
<li>rezero time</li>
</ol>
<p>wipeAnalysis setTime 0.0</p>
<ol>
<li><ol>
<li></li>
</ol></li>
<li>NOW APPLY LOADING SEQUENCE AND ANALYZE (plastic)</li>
</ol>
<ol>
<li>base input motion</li>
</ol>
<p>pattern UniformExcitation 1 1 -accel "Sine 0. 10. $period -factor
$accMul"</p>
<p>eval "recorder Node -file disp -time -node $SnodeList -dof 1 2 -dT
$deltaT disp" eval "recorder Node -file pwp -time -node $FnodeList -dof
3 -dT $deltaT vel" eval "recorder Node -file acc -time -node $SnodeList
-dof 1 2 -dT $deltaT accel" recorder Element -ele 1 -time -file stress1
-dT $deltaT material 1 stress recorder Element -ele 1 -time -file
strain1 -dT $deltaT material 1 strain recorder Element -ele 1 -time
-file stress5 -dT $deltaT material 5 stress recorder Element -ele 1
-time -file strain5 -dT $deltaT material 5 strain recorder Element -ele
1 -time -file stress9 -dT $deltaT material 9 stress recorder Element
-ele 1 -time -file strain9 -dT $deltaT material 9 strain</p>
<p>constraints Penalty 1.e18 1.e18 test NormDispIncr 1.e-4 25 0 numberer
RCM algorithm KrylovNewton system ProfileSPD integrator Newmark $gamma
[expr pow($gamma+0.5, 2)/4] rayleigh $massProportionalDamping 0.0
$InitStiffnessProportionalDamping 0.0 analysis VariableTransient</p>
<p>set startT [clock seconds] analyze $numSteps $deltaT [expr
$deltaT/100] $deltaT 15 set endT [clock seconds] puts "Execution time:
[expr $endT-$startT] seconds."</p>
<p>wipe #flush ouput stream &lt;/syntaxhighlight&gt;</p>
<h2 id="matlab_plotting_file">MATLAB Plotting File</h2>
<p>&lt;syntaxhighlight lang="matlab"&gt; clear all;</p>
<p>a1=load('acc'); d1=load('disp'); p1=load('pwp'); s1=load('stress1');
e1=load('strain1'); s5=load('stress5'); e5=load('strain5');
s9=load('stress9'); e9=load('strain9');</p>
<p>fs=[0.5, 0.2, 4, 6]; fs2=[0.5, 0.2, 4, 3]; accMul = 2;</p>
<p>%integration point 1 p-q po=(s1(:,2)+s1(:,3)+s1(:,4))/3; for
i=1:size(s1,1) qo(i)=(s1(i,2)-s1(i,3))^2 + (s1(i,3)-s1(i,4))^2
+(s1(i,2)-s1(i,4))^2 + 6.0* s1(i,5)^2;
qo(i)=sign(s1(i,5))*1/3.0*qo(i)^0.5; end</p>
<p>figure(1); close 1; figure(1); %integration point 1 stress-strain
subplot(2,1,1), plot(e1(:,4),s1(:,5),'r'); title ('shear stress \tau_x_y
VS. shear strain \epsilon_x_y at integration point 1'); xLabel('Shear
strain \epsilon_x_y'); yLabel('Shear stress \tau_x_y (kPa)');
subplot(2,1,2), plot(-po,qo,'r'); title ('confinement p VS. deviatoric
stress q at integration point 1'); xLabel('confinement p (kPa)');
yLabel('q (kPa)'); set(gcf,'paperposition',fs);
saveas(gcf,'SS_PQ_p1','jpg');</p>
<p>%integration point 5 p-q po=(s5(:,2)+s5(:,3)+s5(:,4))/3; for
i=1:size(s5,1) qo(i)=(s5(i,2)-s5(i,3))^2 + (s5(i,3)-s5(i,4))^2
+(s5(i,2)-s5(i,4))^2 + 6.0* s5(i,5)^2;
qo(i)=sign(s5(i,5))*1/3.0*qo(i)^0.5; end</p>
<p>figure(5); close 5; figure(5); %integration point 5 stress-strain
subplot(2,1,1), plot(e5(:,4),s5(:,5),'r'); title ('shear stress \tau_x_y
VS. shear strain \epsilon_x_y at integration point 5'); xLabel('Shear
strain \epsilon_x_y'); yLabel('Shear stress \tau_x_y (kPa)');
subplot(2,1,2), plot(-po,qo,'r'); title ('confinement p VS. deviatoric
stress q at integration point 5'); xLabel('confinement p (kPa)');
yLabel('q (kPa)'); set(gcf,'paperposition',fs);
saveas(gcf,'SS_PQ_p5','jpg');</p>
<p>%integration point 9 p-q po=(s9(:,2)+s9(:,3)+s9(:,4))/3; for
i=1:size(s1,1) qo(i)=(s9(i,2)-s9(i,3))^2 + (s9(i,3)-s9(i,4))^2
+(s9(i,2)-s9(i,4))^2 + 6.0* s9(i,5)^2;
qo(i)=sign(s9(i,5))*1/3.0*qo(i)^0.5; end</p>
<p>figure(6); close 6; figure(6); %integration point 9 stress-strain
subplot(2,1,1), plot(e9(:,4),s9(:,5),'r'); title ('shear stress \tau_x_y
VS. shear strain \epsilon_x_y at integration point 9'); xLabel('Shear
strain \epsilon_x_y'); yLabel('Shear stress \tau_x_y (kPa)');
subplot(2,1,2), plot(-po,qo,'r'); title ('confinement p VS. deviatoric
stress q at integration point 9'); xLabel('confinement p (kPa)');
yLabel('q (kPa)'); set(gcf,'paperposition',fs);
saveas(gcf,'SS_PQ_p9','jpg');</p>
<p>figure(2); close 2; figure(2); %node 3 displacement relative to node
1 plot(d1(:,1),d1(:,6)); title ('Lateral displacement at element top');
xLabel('Time (s)'); yLabel('Displacement (m)');
set(gcf,'paperposition',fs2); saveas(gcf,'Disp','jpg');</p>
<p>s=accMul*sin(0:pi/50:20*pi); s=[s';zeros(3000,1)];
s1=interp1(0:0.01:40,s,a1(:,1));</p>
<p>figure(3); close 3; figure(3); %node acceleration a =
plot(a1(:,1),s1+a1(:,6),'r'); title ('Lateral acceleration at element
top'); xLabel('Time (s)'); yLabel('Acceleration (m/s^2)');
set(gcf,'paperposition',fs2); saveas(gcf,'Acc','jpg');</p>
<p>figure(4); close 4; figure(4); a=plot(p1(:,1),p1(:,2)); title ('Pore
pressure at base'); xLabel('Time (s)'); yLabel('Pore pressure (kPa)');
set(gcf,'paperposition',fs2); saveas(gcf,'EPWP','jpg');</p>
<p>&lt;/syntaxhighlight&gt;</p>
<h2 id="displacement_output_file">Displacement Output File</h2>
<figure>
<img src="PD02_Ex23Disp.jpg" title="PD02_Ex23Disp.jpg"
alt="PD02_Ex23Disp.jpg" />
<figcaption aria-hidden="true">PD02_Ex23Disp.jpg</figcaption>
</figure>
<h2 id="stress_strain_output_file_integration_point_1">Stress-Strain
Output File (integration point 1)</h2>
<figure>
<img src="PD02_Ex23SS_PQ1.jpg" title="PD02_Ex23SS_PQ1.jpg"
alt="PD02_Ex23SS_PQ1.jpg" />
<figcaption aria-hidden="true">PD02_Ex23SS_PQ1.jpg</figcaption>
</figure>
<h2 id="stress_strain_output_file_integration_point_5">Stress-Strain
Output File (integration point 5)</h2>
<figure>
<img src="PD02_Ex23SS_PQ5.jpg" title="PD02_Ex23SS_PQ5.jpg"
alt="PD02_Ex23SS_PQ5.jpg" />
<figcaption aria-hidden="true">PD02_Ex23SS_PQ5.jpg</figcaption>
</figure>
<h2 id="stress_strain_output_file_integration_point_9">Stress-Strain
Output File (integration point 9)</h2>
<figure>
<img src="PD02_Ex23SS_PQ9.jpg" title="PD02_Ex23SS_PQ9.jpg"
alt="PD02_Ex23SS_PQ9.jpg" />
<figcaption aria-hidden="true">PD02_Ex23SS_PQ9.jpg</figcaption>
</figure>
<h2 id="excess_pore_pressure_output_file">Excess Pore Pressure Output
File</h2>
<figure>
<img src="PD02_Ex23EPP.jpg" title="PD02_Ex23EPP.jpg"
alt="PD02_Ex23EPP.jpg" />
<figcaption aria-hidden="true">PD02_Ex23EPP.jpg</figcaption>
</figure>
<h2 id="acceleration_output_file">Acceleration Output File</h2>
<figure>
<img src="PD02_Ex23Accel.jpg" title="PD02_Ex23Accel.jpg"
alt="PD02_Ex23Accel.jpg" />
<figcaption aria-hidden="true">PD02_Ex23Accel.jpg</figcaption>
</figure>
<hr />
<p>Return to: </p>

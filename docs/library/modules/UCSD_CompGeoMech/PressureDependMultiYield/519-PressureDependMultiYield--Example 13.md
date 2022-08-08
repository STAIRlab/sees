# PressureDependMultiYield--Example 13

<table>
<tbody>
<tr class="odd">
<td><p>&lt;center&gt;<strong>Inclined (4 degrees), saturated, undrained
soil column with pressure dependent
material</strong>&lt;/center&gt;</p></td>
</tr>
</tbody>
</table>
<h2 id="input_file">Input File</h2>

```tcl

# Created by Zhaohui Yang (zhyang@ucsd.edu)
# 
# plane strain, shear-beam type mesh with single material,
# dynamic analysis, SI units (m, s, KN, ton)
# input motion may be from a file, or a sinusoidal wave.
# 

wipe

# 
# some user defined variables
# 

<p>set matOpt 1 ;# 1 = drained, pressure depend; 2 = undrained, pressure
depend;</p>
<dl>
<dt># 3 = undrained, pressure independ; 4 = elastic</dt>

</dl>
<p>set mass 2.0 ;# saturated mass density set fmass 1.0 ;# fluid mass
density set G 6.e4 ;
set B 2.4e5 ;
set press 0. ;# isotropic
consolidation pressure on quad element(s) set accMul 2. ;# acc.
multiplier (m/s/s) set accNam myACC ;# acc. file name if imposed motion
is read from file</p>
<dl>
<dt># - YOU MUST CHANGE IT TO THE RIGHT NAME</dt>

</dl>
<p>set accDt 0.0166 ;# dt for input acc. set loadBias .07 ;# Static
shear load, in percentage of gravity load (=sin(inclination)) set period
1.0 ;# Period if imposed motion is Sine wave set deltaT 0.01 ;# time
step for analysis, does not have to be the same as accDt. set numSteps
2000 ;# number of time steps set gamma 0.6 ;# Newmark integration
parameter</p>
<p>set massProportionalDamping 0.0 ; set
InitStiffnessProportionalDamping 0.002;</p>
<p>set numXele 1 ;# number of elements in x (H) direction set numYele 10
;# number of elements in y (V) direction set xSize 1.0 ;# x direction
element size set ySize 1.0 ;# y direction element size</p>

<li><ol>
# 
</ol></li>
# BUILD MODEL


# create the ModelBuilder

model basic -ndm 2 -ndf 2

# define material and properties

<p>switch $matOpt { 1 { nDMaterial PressureDependMultiYield 1 2 $mass $G
$B 31.4 .1 80 0.5 \
        26.5 0.17 0.4 10 10 0.015 1.0 updateMaterialStage
-material 1 -stage 0</p>
<p>set gravY [expr -9.81*$mass] ;#gravity set gravX [expr -$gravY*$loadBias] } 2 { nDMaterial PressureDependMultiYield 1 2 $mass
$G $B 31.4 .1 80 0.5 \
        26.5 0.17 0.4 10 10 0.015 1.0 nDMaterial
FluidSolidPorous 2 2 1 2.2e6</p>
<p>set gravY [expr -9.81*($mass-$fmass)] ;# buoyant unit weight set
gravX [expr -$gravY*$loadBias] } 3 { nDMaterial
PressureIndependMultiYield 1 2 $mass 4.e4 2.e5 20 .1 nDMaterial
FluidSolidPorous 3 2 1 2.2e6</p>
<p>updateMaterialStage -material 1 -stage 0 updateMaterialStage
-material 3 -stage 0</p>
<p>set gravY [expr -9.81*($mass-fmass)] ;# buoyant unit weight set gravX [expr -$gravY*$loadBias] } 4 { nDMaterial ElasticIsotropic 4 2000 0.3
$mass set gravY [expr -9.81*$mass] ;#gravity set gravX [expr -$gravY*$loadBias] } }</p>

# define the nodes

set numXnode [expr $numXele+1] set numYnode [expr $numYele+1]
<p>for {set i 1} {$i &lt;= $numXnode} {incr i 1} { for {set j 1} {$j
&lt;= $numYnode} {incr j 1} { set xdim [expr ($i-1)*$xSize] set ydim [expr ($j-1)*$ySize] set nodeNum [expr $i + ($j-1)*$numXnode] node
$nodeNum $xdim $ydim } }</p>

# define elements

<p>for {set i 1} {$i &lt;= $numXele} {incr i 1} { for {set j 1} {$j
&lt;= $numYele} {incr j 1} { set eleNum [expr $i + ($j-1)*$numXele] set
n1 [expr $i + ($j-1)*$numXnode] set n2 [expr $i + ($j-1)*$numXnode + 1]
set n4 [expr $i + $j*$numXnode + 1] set n3 [expr $i + $j*$numXnode]</p>

# thick material maTag press density gravity

<p>element quad $eleNum $n1 $n2 $n4 $n3 1.0 "PlaneStrain" $matOpt $press
0.0 $gravX $gravY } }</p>
<p>updateMaterialStage -material 1 -stage 0 updateMaterialStage
-material 2 -stage 0</p>

# fix the base

<p>for {set i 1} {$i &lt;= $numXnode} {incr i 1} { fix $i 1 1 }</p>

# tie two lateral sides

<p>for {set i 1} {$i &lt; $numYnode} {incr i 1} { set nodeNum1 [expr $i*$numXnode + 1] set nodeNum2 [expr ($i+1)*$numXnode] equalDOF
$nodeNum1 $nodeNum2 1 2 }</p>

<li><ol>
# 
</ol></li>
# GRAVITY APPLICATION (elastic behavior)


<li>create the SOE, ConstraintHandler, Integrator, Algorithm and
Numberer</li>

<p>system ProfileSPD 
test NormDispIncr 1.e-5 10 0 algorithm
ModifiedNewton constraints Transformation integrator LoadControl 1 1 1 1
numberer RCM</p>

# create the Analysis

analysis Static
analyze 2

# switch material stage from elastic (gravity) to plastic

<p>switch $matOpt { 1 { updateMaterialStage -material 1 -stage 1
updateMaterials -material 1 bulkModulus [expr $G*2/3.] } 2 {
updateMaterialStage -material 1 -stage 1 updateMaterialStage -material 2
-stage 1 updateMaterials -material 1 bulkModulus [expr $G*2/3.] } 3 {
updateMaterialStage -material 1 -stage 1 updateMaterialStage -material 3
-stage 1 } 4 ;# do nothing }</p>

<li><ol>
# 
</ol></li>
# NOW APPLY LOADING SEQUENCE AND ANALYZE (plastic)


# rezero time

setTime 0.0 wipeAnalysis

# 
# Sinusoidal motion, comment next line if using input motion file

<p>pattern UniformExcitation 1 1 -accel "Sine 0 10 $period -factor $accMul"</p>

# decomment next line if using input motion file
<li>pattern UniformExcitation 1 1 -accel "Series -factor $accMul -filePath $accNam -dt $accDt"</li>


# recorder for nodal displacement along the vertical center line.

<p>set nodeList {} for {set i 0} {$i &lt; $numYnode} {incr i 1} {
lappend nodeList [expr $numXnode/2 + $i*$numXnode] }
eval "recorder Node -file disp -time -node $nodeList -dof 1 2 -dT $deltaT disp" eval
"recorder Node -file acc -time -node $nodeList -dof 1 2 -dT $deltaT accel"</p>

# recorder for element output along the vertical center line.

<p>set name1 "stress";
set name2 "strain";
set name3 "press" for {set i
1} {$i &lt; $numYnode} {incr i 1} { set ele [expr $numXele-$numXele/2+($i-1)*$numXele] set name11 [join [list $name1 $i]
{}] set name22 [join [list $name2 $i] {}] set name33 [join [list $name3
$i] {}] recorder Element -ele $ele -time -file $name11 material 1 stress
recorder Element -ele $ele -time -file $name22 material 1 strain if {
$matOpt == 2 || $matOpt == 3 } { ;#excess pore pressure ouput recorder
Element -ele $ele -time -file $name33 material 1 pressure } }</p>
<p>constraints Transformation test NormDispIncr 1.e-4 10 0 numberer RCM
algorithm Newton system ProfileSPD rayleigh $massProportionalDamping 0.0
$InitStiffnessProportionalDamping 0. integrator Newmark $gamma [expr pow($gamma+0.5, 2)/4] analysis VariableTransient</p>

# analyze

<p>set startT [clock seconds] analyze $numSteps $deltaT [expr $deltaT/100] $deltaT 5 set endT [clock seconds] puts "Execution time: [expr $endT-$startT] seconds."</p>
<p>wipe #flush ouput stream 
```

<h2 id="matlab_plotting_file">MATLAB Plotting File</h2>

```matlab
 clear all;</p>
<p>a1=load('acc'); d1=load('disp'); p1=load('press1');
s1=load('stress1'); e1=load('strain1'); p6=load('press6');
s5=load('stress5'); e5=load('strain5'); p10=load('press10');
s9=load('stress9'); e9=load('strain9');</p>
<p>fs=[0.5, 0.2, 4, 6]; accMul = 2;</p>
<p>%integration point 1 p-q po=(s1(:,2)+s1(:,3)+s1(:,4))/3; for
i=1:size(s1,1) qo(i)=(s1(i,2)-s1(i,3))^2 + (s1(i,3)-s1(i,4))^2
+(s1(i,2)-s1(i,4))^2 + 6.0* s1(i,5)^2;
qo(i)=sign(s1(i,5))*1/3.0*qo(i)^0.5; end</p>
<p>figure(1); close 1; figure(1); %integration point 1 stress-strain
subplot(2,1,1), plot(e1(:,4),s1(:,5),'r'); title ('shear stress \tau_x_y
VS. shear strain \epsilon_x_y at 10 m depth'); xLabel('Shear strain
\epsilon_x_y'); yLabel('Shear stress \tau_x_y (kPa)'); subplot(2,1,2),
plot(-po,qo,'r'); title ('confinement p VS. deviatoric stress q at 10 m
depth'); xLabel('confinement p (kPa)'); yLabel('q (kPa)');
set(gcf,'paperposition',fs); saveas(gcf,'SS_PQ_10m','jpg');</p>
<p>%integration point 5 p-q po=(s5(:,2)+s5(:,3)+s5(:,4))/3; for
i=1:size(s5,1) qo(i)=(s5(i,2)-s5(i,3))^2 + (s5(i,3)-s5(i,4))^2
+(s5(i,2)-s5(i,4))^2 + 6.0* s5(i,5)^2;
qo(i)=sign(s5(i,5))*1/3.0*qo(i)^0.5; end</p>
<p>figure(5); close 5; figure(5); %integration point 5 stress-strain
subplot(2,1,1), plot(e5(:,4),s5(:,5),'r'); title ('shear stress \tau_x_y
VS. shear strain \epsilon_x_y at 6 m depth'); xLabel('Shear strain
\epsilon_x_y'); yLabel('Shear stress \tau_x_y (kPa)'); subplot(2,1,2),
plot(-po,qo,'r'); title ('confinement p VS. deviatoric stress q at 6 m
depth'); xLabel('confinement p (kPa)'); yLabel('q (kPa)');
set(gcf,'paperposition',fs); saveas(gcf,'SS_PQ_6m','jpg');</p>
<p>%integration point 9 p-q po=(s9(:,2)+s9(:,3)+s9(:,4))/3; for
i=1:size(s1,1) qo(i)=(s9(i,2)-s9(i,3))^2 + (s9(i,3)-s9(i,4))^2
+(s9(i,2)-s9(i,4))^2 + 6.0* s9(i,5)^2;
qo(i)=sign(s9(i,5))*1/3.0*qo(i)^0.5; end</p>
<p>figure(6); close 6; figure(6); %integration point 9 stress-strain
subplot(2,1,1), plot(e9(:,4),s9(:,5),'r'); title ('shear stress \tau_x_y
VS. shear strain \epsilon_x_y at 2 m depth'); xLabel('Shear strain
\epsilon_x_y'); yLabel('Shear stress \tau_x_y (kPa)'); subplot(2,1,2),
plot(-po,qo,'r'); title ('confinement p VS. deviatoric stress q at 2 m
depth'); xLabel('confinement p (kPa)'); yLabel('q (kPa)');
set(gcf,'paperposition',fs); saveas(gcf,'SS_PQ_2m','jpg');</p>
<p>figure(2); close 2; figure(2); %node 3 displacement relative to node
1 subplot(2,1,1),a=plot(d1(:,1),d1(:,8),'r'); hold on
subplot(2,1,1),b=plot(d1(:,1),d1(:,14),'g'); hold on
subplot(2,1,1),c=plot(d1(:,1),d1(:,22),'b'); title ('Lateral
displacement wrt base'); xLabel('Time (s)'); yLabel('Displacement (m)');
legend([a,b,c],'8m depth','4m depth', 'Surface',2)
set(gcf,'paperposition',fs); saveas(gcf,'Disp','jpg');</p>
<p>s=accMul*sin(0:pi/50:20*pi); s=[s';zeros(1000,1)];
s1=interp1(0:0.01:20,s,a1(:,1));</p>
<p>figure(3); close 3; figure(3); %node acceleration
subplot(3,1,1),a=plot(a1(:,1),s1+a1(:,22),'r'); legend(a,'at
surface',4); title ('Lateral acceleration'); xLabel('Time (s)');
yLabel('Acceleration (m/s^2)');
subplot(3,1,2),a=plot(a1(:,1),s1+a1(:,14),'r'); legend(a,'4 m depth',4);
xLabel('Time (s)'); yLabel('Acceleration (m/s^2)');
subplot(3,1,3),a=plot(a1(:,1),s1+a1(:,8),'r'); legend(a,'8 m depth',4);
xLabel('Time (s)'); yLabel('Acceleration (m/s^2)');
set(gcf,'paperposition',fs); saveas(gcf,'Acc','jpg');</p>
<p>figure(4); close 4; figure(4); %integration point 1 excess pore water
pressure subplot(3,1,1),a=plot(p10(:,1),-p10(:,2),'r'); legend(a,'1 m
depth',4); title ('Excess pore pressure'); xLabel('Time (s)');
yLabel('Excess pore pressure (kPa)');
subplot(3,1,2),a=plot(p6(:,1),-p6(:,2),'r'); legend(a,'5 m depth',4);
xLabel('Time (s)'); yLabel('Excess pore pressure (kPa)');
subplot(3,1,3),a=plot(p1(:,1),-p1(:,2),'r'); legend(a,'10 m depth',4);
xLabel('Time (s)'); yLabel('Excess pore pressure (kPa)');
set(gcf,'paperposition',fs); saveas(gcf,'EPWP','jpg');</p>
<p>
```

<h2 id="displacement_output_file">Displacement Output File</h2>
<figure>
<img src="PD_Ex20Disp.jpg" title="PD_Ex20Disp.jpg"
alt="PD_Ex20Disp.jpg" />
<figcaption aria-hidden="true">PD_Ex20Disp.jpg</figcaption>
</figure>
<h2 id="stress_strain_output_file_2_m_depth">Stress-Strain Output File
(2 m depth)</h2>
<figure>
<img src="PD_Ex20SS_PQ2m.jpg" title="PD_Ex20SS_PQ2m.jpg"
alt="PD_Ex20SS_PQ2m.jpg" />
<figcaption aria-hidden="true">PD_Ex20SS_PQ2m.jpg</figcaption>
</figure>
<h2 id="stress_strain_output_file_6_m_depth">Stress-Strain Output File
(6 m depth)</h2>
<figure>
<img src="PD_Ex20SS_PQ6m.jpg" title="PD_Ex20SS_PQ6m.jpg"
alt="PD_Ex20SS_PQ6m.jpg" />
<figcaption aria-hidden="true">PD_Ex20SS_PQ6m.jpg</figcaption>
</figure>
<h2 id="stress_strain_output_file_10_m_depth">Stress-Strain Output File
(10 m depth)</h2>
<figure>
<img src="PD_Ex20SS_PQ10m.jpg" title="PD_Ex20SS_PQ10m.jpg"
alt="PD_Ex20SS_PQ10m.jpg" />
<figcaption aria-hidden="true">PD_Ex20SS_PQ10m.jpg</figcaption>
</figure>
<h2 id="excess_pore_pressure_output_file">Excess Pore Pressure Output
File</h2>
<figure>
<img src="PD_Ex20EPP.jpg" title="PD_Ex20EPP.jpg" alt="PD_Ex20EPP.jpg" />
<figcaption aria-hidden="true">PD_Ex20EPP.jpg</figcaption>
</figure>
<h2 id="acceleration_output_file">Acceleration Output File</h2>
<figure>
<img src="PD_Ex20Accel.jpg" title="PD_Ex20Accel.jpg"
alt="PD_Ex20Accel.jpg" />
<figcaption aria-hidden="true">PD_Ex20Accel.jpg</figcaption>
</figure>
<hr />
Return to: 

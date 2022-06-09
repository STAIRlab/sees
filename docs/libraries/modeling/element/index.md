# Element Command

<hr />

<p>NOTE:</p>
<p>The valid queries to any element when creating an ElementRecorder are
documented in the NOTES section for each element.</p>

<p>The following contain information about eleType? and the args
required for each of the available element types:</p>


<ul>
<li>Truss Elements
 <ul>
  <li><a href="Truss" >Truss Element</a></li>
  <li><a href="Corotational_Truss" >Corotational
 Truss Element</a></li>
 </ul>
</li>

<li>Beam-Column Elements
 <ul>
 <li><a href="ElasticBeamColumn" >Elastic Beam Column</a></li>
 <li><a href="ModElasticBeamColumn"
 >Elastic Beam Column Element with Stiffness
 Modifiers</a></li>
 <li><a href="Elastic_Timoshenko_Beam_Column"
 >Elastic Timoshenko Beam Column Element</a></li>
 <li><a href="Beam_With_Hinges" >Beam With Hinges
 Element</a></li>
 
 <li><a href="Displacement-Based_Beam-Column"
 >Displacement-Based Beam-Column Element</a></li>
 
 <li><a href="Force-Based_Beam-Column"
 >Force-Based Beam-Column Element</a></li>
 
 <li><a
 href="Flexure-Shear_Interaction_Displacement-Based_Beam-Column"
 >Flexure-Shear Interaction Displacement-Based Beam-Column Element</a></li>
 
 <li><a href="MVLEM">MVLEM</a> - Multiple-Vertical-Line-Element-Model for RC Walls</li>
 
 <li><a href="SFI_MVLEM">SFI_MVLEM</a> - Cyclic Shear-Flexure Interaction Model for RC Walls</li>
 </ul>

<li>Zero-Length Elements
<ul>
<li><a href="zeroLength" >zeroLength</a></li>

<li><a href="zeroLengthND" >zeroLengthND</a></li>

<li><a href="zeroLengthSection">zeroLengthSection Element</a></li>

<li><a href="CoupledZeroLength">CoupledZeroLength</a></li>

<li><a href="zeroLengthContact">zeroLengthContact</a></li>

<li><a href="zeroLengthContactNTS2D">zeroLengthContactNTS2D</a></li>

<li><a href="zeroLengthInterface2D">zeroLengthInterface2D</a></li>

<li><a href="zeroLengthImpact3D">zeroLengthImpact3D</a></li>
</ul></li>


<li>Joint Elements
<ul>
<li><a href="BeamColumnJoint" >BeamColumnJoint
Element</a></li>
<li><a href="ElasticTubularJoint"
>ElasticTubularJoint Element</a></li>
<li><a href="Joint2D" >Joint2D Element</a></li>
</ul></li>
</ul>
<ul>
<li>Link Elements
<ul>
<li><a href="Two_Node_Link" >Two Node Link Element</a></li>
</ul></li>

<li>Bearing Elements
<ul>
<li><a href="Elastomeric_Bearing_(Plasticity)">Elastomeric Bearing (Plasticity)</a></li>

<li><a href="Elastomeric_Bearing_(Bouc-Wen)">Elastomeric Bearing (Bouc-Wen)</a></li>

<li><a href="Flat_Slider_Bearing" >Flat Slider Bearing</a></li>

<li><a href="Single_Friction_Pendulum_Bearing">Single Friction Pendulum Bearing</a></li>

<li><a href="Triple_Friction_Pendulum_Bearing" >TFP</a></li>

<li><a href="Triple_Friction_Pendulum" >Triple Friction Pendulum</a></li>

<li><a href="MultipleShearSpring">MultipleShearSpring</a></li>

<li><a href="KikuchiBearing" >KikuchiBearing</a></li>

<li><a href="YamamotoBiaxialHDR">YamamotoBiaxialHDR Element</a></li>
<li><a href="ElastomericX" >ElastomericX</a></li>
<li><a href="LeadRubberX" >LeadRubberX</a></li>
<li><a href="HDR" >HDR</a></li>
<li><a href="RJ-Watson_EQS_Bearing" >RJ-Watson EQS Bearing Element</a></li>
<li><a href="FPBearingPTV" >FPBearingPTV</a></li>
</ul></li>

<li>Quadrilateral Elements
<ul>
<li><a href="Quad" >Quad Element</a></li>
<li><a href="Shell" >Shell Element</a></li>
<li><a href="ShellDKGQ" >ShellDKGQ</a></li>
<li><a href="ShellNLDKGQ" >ShellNLDKGQ</a></li>
<li><a href="ShellNL" >ShellNL</a></li>
<li><a href="Bbar_Plane_Strain_Quadrilateral" >Bbar Plane Strain Quadrilateral Element</a></li>
<li><a href="Enhanced_Strain_Quadrilateral" >Enhanced Strain Quadrilateral Element</a></li>
<li><a href="SSPquad" >SSPquad Element</a></li>
</ul></li>

<li>Triangular Elements
<ul>
<li><a href="Tri31" >Tri31 Element</a></li>
<li><a href="ShellDKGT" >ShellDKGT</a></li>
<li><a href="ShellNLDKGT" >ShellNLDKGT</a></li>
</ul></li>

<li>Brick Elements
<ul>
<li><a href="Standard_Brick" >Standard Brick</a></li>
<li><a href="Bbar_Brick" >Bbar Brick</a></li>
<li><a href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/734.htm">Twenty Node Brick</a></li>
<li><a href="Twenty_Seven_Node_Brick" >Twenty Seven Node Brick</a></li>
<li><a href="SSPbrick" >SSPbrick</a></li>
</ul></li>

<li>Tetrahedron Elements
<ul>
<li><a href="FourNodeTetrahedron" >FourNodeTetrahedron</a></li>
</ul></li>


<li>u-p Elements
<ul>
<li>UC San Diego u-p element (saturated soil)
<ul>
<li><a href="Four_Node_Quad_u-p" >Four Node Quad u-p</a></li>
<li><a href="Brick_u-p" >Brick u-p</a></li>
<li><a href="bbarQuad_u-p" >bbarQuad u-p</a></li>
<li><a href="bbarBrick_u-p" >bbarBrick u-p</a></li>
<li><a href="Nine_Four_Node_Quad_u-p" >Nine Four Node Quad u-p</a></li>
<li><a href="Twenty_Eight_Node_Brick_u-p">Twenty Eight Node Brick u-p</a></li>
</ul></li>

<li><a href="Twenty_Node_Brick_u-p" >Twenty Node Brick u-p</a></li>
<li><a href="Brick_Large_Displacement_u-p">Brick Large Displacement u-p</a></li>
<li><a href="SSPquadUP" >SSPquadUP</a></li>
<li><a href="SSPbrickUP" >SSPbrickUP</a></li>
</ul></li>

<li>Contact Elements
<ul>
<li><a href="SimpleContact2D" >SimpleContact2D</a></li>
<li><a href="SimpleContact3D" >SimpleContact3D</a></li>
<li><a href="BeamContact2D" >BeamContact2D</a></li>
<li><a href="BeamContact3D" >BeamContact3D</a></li>
<li><a href="BeamEndContact3D" >BeamEndContact3D</a></li>
<li><a href="zeroLengthImpact3D">zeroLengthImpact3D</a></li>
</ul></li>


<li>Cable Elements
<ul>
<li><a href="CatenaryCableElement" >CatenaryCable
</a></li>
</ul></li>

<li>Misc.
<ul>
<li><a href="ShallowFoundationGen"
>ShallowFoundationGen</a></li>
<li><a href="SurfaceLoad" >SurfaceLoad
Element</a></li>
<li><a href="VS3D4" >VS3D4</a></li>
<li><a href="AC3D8" >AC3D8</a></li>
<li><a href="ASI3D8" >ASI3D8</a></li>
<li><a href="AV3D4" >AV3D4</a></li>
</ul></li>
</ul>

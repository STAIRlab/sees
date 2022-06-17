# NDMaterial Library

This command is used to construct an `NDMaterial`
object which represents the stress-strain relationship at the
gauss-point of a continuum element.

<hr />

<p>NOTE:</p>

The valid queries to any uniaxial material when creating an
`ElementRecorder` are `"strain"`, and `"stress"`. Some materials have
additional queries to which they will respond. These are documented in
the NOTES section for those materials.


## Wrappers

See Prof. Scott's post [here](https://portwooddigital.com/2020/07/11/theres-a-wrapper-for-that/)

- `InitStressNDMaterial`
- `BeamFiberMaterial`
- `PlateFromPlaneStressMaterial` wrapper adds linear-elastic shear behavior to a plane stress material in order to get the plate fiber stress condition.

<ul>
<li><a href="Elastic_Isotropic_Material" title="wikilink">Elastic
Isotropic Material</a></li>
<li><a href="Elastic_Orthotropic_Material" title="wikilink">Elastic
Orthotropic Material</a></li>
<li><a href="J2_Plasticity_Material" title="wikilink">J2 Plasticity</a></li>
<li><a href="Drucker_Prager" title="wikilink"> Drucker Prager</a></li>
<li><a href="Damage2p" title="wikilink"> Concrete Damage Model</a></li>
<li><a href="Plane_Stress_Material" title="wikilink">Plane Stress Material</a></li>
<li><a href="Plane_Strain_Material" title="wikilink">Plane Strain Material</a></li>
<li><a href="MCP" title="wikilink"> Multi Axial Cyclic Plasticity</a></li>
<li><a href="Bounding_Cam_Clay" title="wikilink"> Bounding Surface Cam Clay Material</a></li>
<li><a href="Plate_Fiber_Material" title="wikilink">Plate Fiber</a></li>
<li><a href="Plane_Stress_Concrete_Materials" title="wikilink">Plane Stress Concrete Materials</a></li>
<li><a href="FSAM_-_2D_RC_Panel_Constitutive_Behavior" >FSAM - 2D RC Panel Constitutive Behavior</a></li>


<li>Tsinghua Sand Models
  <ul>
  <li><a href="CycLiqCP_Material_(Cyclic_ElasticPlasticity)"
  title="wikilink">CycLiqCP Material (Cyclic ElasticPlasticity)</a></li>
  <li><a href="CycLiqCPSP_Material" title="wikilink">CycLiqCPSP</a></li>
  </ul>
</li>

<li><a href="Manzari_Dafalias_Material" title="wikilink">Manzari Dafalias Material</a></li>
<li><a href="J2CyclicBoundingSurface_Material" title="wikilink">J2CyclicBoundingSurface Material</a></li>
<li><a href="PM4Sand_Material" title="wikilink">PM4Sand</a></li>
<li><a href="PM4Silt_Material_(Beta)" title="wikilink">PM4Silt Material (Beta)</a></li>
<li><a href="Stress_Density_Material" title="wikilink">Stress Density</a></li>

<li>Materials for Modeling Concrete Walls
<ul>
  <li><a
  href="http://www.luxinzheng.net/download/OpenSEES/En_THUShell_OpenSEES.htm">PlaneStressUserMaterial</a></li>
  <li><a
  href="http://www.luxinzheng.net/download/OpenSEES/En_THUShell_OpenSEES.htm">PlateFromPlaneStress</a></li>
  <li><a
  href="http://www.luxinzheng.net/download/OpenSEES/En_THUShell_OpenSEES.htm">PlateRebar</a></li>
  <li><a
  href="http://www.luxinzheng.net/download/OpenSEES/En_THUShell_OpenSEES.htm">LayeredShell</a></li>
  </ul>
</li>

<li>Contact Materials for 2D and 3D
  <ul>
  <li><a href="ContactMaterial2D" >ContactMaterial2D</a></li>
  <li><a href="ContactMaterial3D" >ContactMaterial3D</a></li>
  </ul></li>
  <li>Wrapper material for Initial State Analysis
  <ul>
  <li><a href="InitialStateAnalysisWrapper" >InitialStateAnalysisWrapper</a></li>
  </ul>
</li>


<li>UC San Diego soil models (Linear/Nonlinear, dry/drained/undrained
soil response under general 2D/3D static/cyclic loading conditions
(please visit <a href="http://soilquake.net/opensees">UCSD</a> for examples)
<ul>
<li><a href="PressureIndependMultiYield_Material" >PressureIndependMultiYield Material</a></li>
<li><a href="PressureDependMultiYield_Material" >PressureDependMultiYield Material</a></li>
<li><a href="PressureDependMultiYield02_Material" >PressureDependMultiYield02 Material</a></li>
<li><a href="PressureDependMultiYield03_Material" >PressureDependMultiYield03 Material</a></li>
</ul></li>
<li>UC San Diego Saturated Undrained soil
<ul>
<li><a href="FluidSolidPorousMaterial" >FluidSolidPorousMaterial</a></li>
</ul></li>
<li>Misc.
<ul>
<li><a href="AcousticMedium" title="wikilink">AcousticMedium</a></li>
</ul></li>
<li>Steel &amp;amp; Reinforcing-Steel Materials
<ul>
<li><a href="UVCmultiaxial_(Updated_Voce-Chaboche)" >UVCmultiaxial (Updated Voce-Chaboche)</a></li>
<li><a href="UVCplanestress_(Updated_Voce-Chaboche)" >UVCplanestress (Updated Voce-Chaboche)</a></li>
</ul></li>
</ul>

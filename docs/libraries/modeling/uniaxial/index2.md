# UniaxialMaterial Command

This command is used to construct a UniaxialMaterial object which
represents uniaxial stress-strain (or force-deformation) relationships.

``` tcl
uniaxialMaterial matType? matTag? arg1?...
```

<hr />
<p>
The type of material created and the additional arguments required
depends on the <strong>matType?</strong> provided in the command.
</p>
<p>
NOTE:
</p>
<p>
The valid queries to any uniaxial material when creating an
ElementRecorder are ‘strain,’ ‘stress,’ and ‘tangent.’ Some materials
have additional queries to which they will respond. These are documented
in the NOTES section for those materials.
</p>
<p>
The following contain information about matType? and the args required
for each of the available material types:
</p>
<p>
\</noinclude>
</p>
<ul>
<li>
Steel & Reinforcing-Steel Materials
<ul>
<li>
<a href="Steel01_Material">Steel01 Material</a>
</li>
<li>
<a
href="Steel02_Material_--_Giuffré-Menegotto-Pinto_Model_with_Isotropic_Strain_Hardening"
>Steel02 Material – Giuffré-Menegotto-Pinto Model with Isotropic Strain
Hardening</a>
</li>
<li>
<a href="Steel4_Material">Steel4 Material</a>
</li>
<li>
<a href="Hysteretic_Material">Hysteretic </a>
</li>
<li>
<a href="Reinforcing_Steel_Material">Reinforcing Steel Material</a>
</li>
<li>
<a href="DoddRestrepo"> Dodd Restrepo</a>
</li>
<li>
<a href="RambergOsgoodSteel_Material"
>RambergOsgoodSteel Material</a>
</li>
<li>
<a
href="SteelMPF_-_Menegotto_and_Pinto_(1973)_Model_Extended_by_Filippou_et_al._(1983)"
>SteelMPF - Menegotto and Pinto (1973) Model Extended by Filippou et
al. (1983)</a>
</li>
<li>
<a href="UVCuniaxial_(Updated_Voce-Chaboche)"
>UVCuniaxial (Updated Voce-Chaboche)</a>
</li>
</ul>
</li>
<li>
Concrete Materials
<ul>
<li>
<a href="Concrete01_Material_--_Zero_Tensile_Strength"
>Concrete01 Material – Zero Tensile Strength</a>
</li>
<li>
<a href="Concrete02_Material_--_Linear_Tension_Softening"
>Concrete02 Material – Linear Tension Softening</a>
</li>
<li>
<a href="Concrete04_Material_--_Popovics_Concrete_Material"
>Concrete04 Material – Popovics Concrete </a>
</li>
<li>
<a href="Concrete06_Material"
>Concrete06 </a>
</li>
<li>
<a href="Concrete07_-_Chang_&amp;amp;_Mander’s_1994_Concrete_Model"
>Concrete07 - Chang &amp; Mander’s 1994 Concrete Model</a>
</li>
<li>
<a href="Concrete01_Material_With_Stuff_in_the_Cracks"
>Concrete01 Material With Stuff in the Cracks</a>
</li>
<li>
<a href="ConfinedConcrete01_Material"
>ConfinedConcrete01 Material</a>
</li>
<li>
<a href="ConcreteD">ConcreteD</a>
</li>
<li>
<a href="FRPConfinedConcrete"
>FRPConfinedConcrete</a>
</li>
<li>
<a href="ConcreteCM_-_Complete_Concrete_Model_by_Chang_and_Mander_(1994)"
>ConcreteCM - Complete Concrete Model by Chang and Mander (1994)</a>
</li>
</ul>
</li>
<li>
Some Standard Uniaxial Materials
<ul>
<li>
<a href="Elastic_Uniaxial_Material"
>Elastic Uniaxial Material</a>
</li>
<li>
<a href="Elastic-Perfectly_Plastic_Material"
>Elastic-Perfectly Plastic Material</a>
</li>
<li>
<a href="Elastic-Perfectly_Plastic_Gap_Material"
>Elastic-Perfectly Plastic Gap Material</a>
</li>
<li>
<a href="Elastic-No_Tension_Material"
>Elastic-No Tension Material</a>
</li>
<li>
<a href="Parallel_Material">Parallel </a>
</li>
<li>
<a href="Series_Material">Series Material</a>
</li>
</ul>
</li>
<li>
Other Uniaxial Materials
<ul>
<li>
<a href="CastFuse_Material">CastFuse </a>
</li>
<li>
<a href="ViscousDamper_Material">ViscousDamper </a>
</li>
<li>
<a href="BilinearOilDamper_Material"
>BilinearOilDamper Material</a>
</li>
<li>
<a
href="Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Bilinear_Hysteretic_Response_(Bilin_Material)"
>Modified Ibarra-Medina-Krawinkler Deterioration Model with Bilinear
Hysteretic Response (Bilin Material)</a>
</li>
<li>
<a
href="Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Peak-Oriented_Hysteretic_Response_(ModIMKPeakOriented_Material)"
>Modified Ibarra-Medina-Krawinkler Deterioration Model with
Peak-Oriented Hysteretic Response (ModIMKPeakOriented Material)</a>
</li>
<li>
<a href="Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Pinched_Hysteretic_Response_(ModIMKPinching_Material)"
    >Modified Ibarra-Medina-Krawinkler Deterioration Model with Pinched
Hysteretic Response (ModIMKPinching Material)</a>
</li>
<li>
<a href="SAWS_Material">SAWS Material</a>
</li>
<li>
<a href="BARSLIP_Material">BARSLIP</a>
</li>
<li>
<a href="Bond_SP01">Bond_SP01 - - Strain Penetration Model for Fully
Anchored Steel Reinforcing Bars</a>
</li>
<li>
<a href="Fatigue_Material">Fatigue</a>
</li>
<li>
<a href="Hardening_Material">Hardening</a>
</li>
<li>
<a href="Impact_Material">Impact Material</a>
</li>
<li>
<a href="Hyperbolic_Gap_Material">Hyperbolic Gap</a>
</li>
<li>
<a href="Limit_State_Material">Limit State</a>
</li>
<li>
<a href="MinMax_Material">MinMax Material</a>
</li>
<li>
<a href="ElasticBilin_Material">ElasticBilin</a>
</li>
<li>
<a href="ElasticMultiLinear_Material">ElasticMultiLinear Material</a>
</li>
<li>
<a href="MultiLinear_Material">MultiLinear Material</a>
</li>
<li>
<a href="Initial_Strain_Material">Initial Strain Material</a>
</li>
<li>
<a href="Initial_Stress_Material">Initial Stress Material</a>
</li>
<li>
<a href="PathIndependent_Material">PathIndependent Material</a>
</li>
<li>
<a href="Pinching4_Material">Pinching4 Material</a>
</li>
<li>
<a href="Engineered_Cementitious_Composites_Material">Engineered
Cementitious Composites Material</a>
</li>
<li>
<a href="SelfCentering_Material">SelfCentering Material</a>
</li>
<li>
<a href="Viscous_Material">Viscous Material</a>
</li>
<li>
<a href="BoucWen_Material">BoucWen Material</a>
</li>
<li>
<a href="BWBN_Material">BWBN Material</a> (Pinching Hysteretic Bouc-Wen
Material)
</li>
<li>
PyTzQz uniaxial materials for p-y, t-z and q-z elements for modeling
soil-structure interaction through the piles in a structural foundation
<ul>
<li>
<a href="PySimple1_Material">PySimple1 Material</a>
</li>
<li>
<a href="TzSimple1_Material">TzSimple1 Material</a>
</li>
<li>
<a href="QzSimple1_Material">QzSimple1 Material</a>
</li>
<li>
<a href="PyLiq1_Material">PyLiq1 Material</a>
</li>
<li>
<a href="TzLiq1_Material">TzLiq1 Material</a>
</li>
<li>
<a
  href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1257.htm">PySimple1Gen
Command</a>
</li>
<li>
<a
  href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1261.htm">TzSimple1Gen
Command</a>
</li>
</ul>
</li>
<li>
<a href="KikuchiAikenHDR_Material">KikuchiAikenHDR Material</a>
</li>
<li>
<a href="KikuchiAikenLRB_Material">KikuchiAikenLRB Material</a>
</li>
<li>
<a href="AxialSp_Material">AxialSp Material</a>
</li>
<li>
<a href="AxialSpHD_Material">AxialSpHD Material</a>
</li>
<li>
<a href="Pinching_Limit_State_Material">Pinching Limit State
Material</a>
</li>
<li>
<a href="CFSWSWP"> CFSWSWP Wood-Sheathed Cold-Formed Steel Shear Wall
Panel</a>
</li>
<li>
<a href="CFSSSWP"> CFSSSWP Steel-Sheathed Cold-formed Steel Shear Wall
Panel</a>
</li>
</ul>
</li>
</ul>

# UniaxialMaterial Command

<p>&lt;noinclude&gt;This command is used to construct a UniaxialMaterial
object which represents uniaxial stress-strain (or force-deformation)
relationships.</p>

```tcl
uniaxialMaterial matType? matTag? arg1?
        ...
```

<hr />
<p>The type of material created and the additional arguments required
depends on the <strong>matType?</strong> provided in the command.</p>
<p>NOTE:</p>
<p>The valid queries to any uniaxial material when creating an
ElementRecorder are 'strain,' 'stress,' and 'tangent.' Some materials
have additional queries to which they will respond. These are documented
in the NOTES section for those materials.</p>
<p>The following contain information about matType? and the args
required for each of the available material types:</p>
<p>&lt;/noinclude&gt;</p>
<ul>
<li>Steel &amp;amp; Reinforcing-Steel Materials
<ul>
<li><a href="Steel01_Material" title="wikilink">Steel01
Material</a></li>
<li><a
href="Steel02_Material_--_Giuffré-Menegotto-Pinto_Model_with_Isotropic_Strain_Hardening"
title="wikilink">Steel02 Material -- Giuffré-Menegotto-Pinto Model with
Isotropic Strain Hardening</a></li>
<li><a href="Steel4_Material" title="wikilink">Steel4 Material</a></li>
<li><a href="Hysteretic_Material" title="wikilink">Hysteretic
Material</a></li>
<li><a href="Reinforcing_Steel_Material" title="wikilink">Reinforcing
Steel Material</a></li>
<li><a href="DoddRestrepo" title="wikilink"> Dodd Restrepo</a></li>
<li><a href="RambergOsgoodSteel_Material"
title="wikilink">RambergOsgoodSteel Material</a></li>
<li><a
href="SteelMPF_-_Menegotto_and_Pinto_(1973)_Model_Extended_by_Filippou_et_al._(1983)"
title="wikilink">SteelMPF - Menegotto and Pinto (1973) Model Extended by
Filippou et al. (1983)</a></li>
<li><a href="UVCuniaxial_(Updated_Voce-Chaboche)"
title="wikilink">UVCuniaxial (Updated Voce-Chaboche)</a></li>
</ul></li>
<li>Concrete Materials
<ul>
<li><a href="Concrete01_Material_--_Zero_Tensile_Strength"
title="wikilink">Concrete01 Material -- Zero Tensile Strength</a></li>
<li><a href="Concrete02_Material_--_Linear_Tension_Softening"
title="wikilink">Concrete02 Material -- Linear Tension
Softening</a></li>
<li><a href="Concrete04_Material_--_Popovics_Concrete_Material"
title="wikilink">Concrete04 Material -- Popovics Concrete
Material</a></li>
<li><a href="Concrete06_Material" title="wikilink">Concrete06
Material</a></li>
<li><a href="Concrete07_-_Chang_&amp;amp;_Mander’s_1994_Concrete_Model"
title="wikilink">Concrete07 - Chang &amp;amp; Mander’s 1994 Concrete
Model</a></li>
<li><a href="Concrete01_Material_With_Stuff_in_the_Cracks"
title="wikilink">Concrete01 Material With Stuff in the Cracks</a></li>
<li><a href="ConfinedConcrete01_Material"
title="wikilink">ConfinedConcrete01 Material</a></li>
<li><a href="ConcreteD" title="wikilink">ConcreteD</a></li>
<li><a href="FRPConfinedConcrete"
title="wikilink">FRPConfinedConcrete</a></li>
<li><a
href="ConcreteCM_-_Complete_Concrete_Model_by_Chang_and_Mander_(1994)"
title="wikilink">ConcreteCM - Complete Concrete Model by Chang and
Mander (1994)</a></li>
</ul></li>
<li>Some Standard Uniaxial Materials
<ul>
<li><a href="Elastic_Uniaxial_Material" title="wikilink">Elastic
Uniaxial Material</a></li>
<li><a href="Elastic-Perfectly_Plastic_Material"
title="wikilink">Elastic-Perfectly Plastic Material</a></li>
<li><a href="Elastic-Perfectly_Plastic_Gap_Material"
title="wikilink">Elastic-Perfectly Plastic Gap Material</a></li>
<li><a href="Elastic-No_Tension_Material" title="wikilink">Elastic-No
Tension Material</a></li>
<li><a href="Parallel_Material" title="wikilink">Parallel
Material</a></li>
<li><a href="Series_Material" title="wikilink">Series Material</a></li>
</ul></li>
<li>Other Uniaxial Materials
<ul>
<li><a href="CastFuse_Material" title="wikilink">CastFuse
Material</a></li>
<li><a href="ViscousDamper_Material" title="wikilink">ViscousDamper
Material</a></li>
<li><a href="BilinearOilDamper_Material"
title="wikilink">BilinearOilDamper Material</a></li>
<li><a
href="Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Bilinear_Hysteretic_Response_(Bilin_Material)"
title="wikilink">Modified Ibarra-Medina-Krawinkler Deterioration Model
with Bilinear Hysteretic Response (Bilin Material)</a></li>
<li><a
href="Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Peak-Oriented_Hysteretic_Response_(ModIMKPeakOriented_Material)"
title="wikilink">Modified Ibarra-Medina-Krawinkler Deterioration Model
with Peak-Oriented Hysteretic Response (ModIMKPeakOriented
Material)</a></li>
<li><a
href="Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Pinched_Hysteretic_Response_(ModIMKPinching_Material)"
title="wikilink">Modified Ibarra-Medina-Krawinkler Deterioration Model
with Pinched Hysteretic Response (ModIMKPinching Material)</a></li>
<li><a href="SAWS_Material" title="wikilink">SAWS Material</a></li>
<li><a href="BARSLIP_Material" title="wikilink">BARSLIP
Material</a></li>
<li><a
href="Bond_SP01_-_-_Strain_Penetration_Model_for_Fully_Anchored_Steel_Reinforcing_Bars"
title="wikilink">Bond_SP01 - - Strain Penetration Model for Fully
Anchored Steel Reinforcing Bars</a></li>
<li><a href="Fatigue_Material" title="wikilink">Fatigue
Material</a></li>
<li><a href="Hardening_Material" title="wikilink">Hardening
Material</a></li>
<li><a href="Impact_Material" title="wikilink">Impact Material</a></li>
<li><a href="Hyperbolic_Gap_Material" title="wikilink">Hyperbolic Gap
Material</a></li>
<li><a href="Limit_State_Material" title="wikilink">Limit State
Material</a></li>
<li><a href="MinMax_Material" title="wikilink">MinMax Material</a></li>
<li><a href="ElasticBilin_Material" title="wikilink">ElasticBilin
Material</a></li>
<li><a href="ElasticMultiLinear_Material"
title="wikilink">ElasticMultiLinear Material</a></li>
<li><a href="MultiLinear_Material" title="wikilink">MultiLinear
Material</a></li>
<li><a href="Initial_Strain_Material" title="wikilink">Initial Strain
Material</a></li>
<li><a href="Initial_Stress_Material" title="wikilink">Initial Stress
Material</a></li>
<li><a href="PathIndependent_Material" title="wikilink">PathIndependent
Material</a></li>
<li><a href="Pinching4_Material" title="wikilink">Pinching4
Material</a></li>
<li><a href="Engineered_Cementitious_Composites_Material"
title="wikilink">Engineered Cementitious Composites Material</a></li>
<li><a href="SelfCentering_Material" title="wikilink">SelfCentering
Material</a></li>
<li><a href="Viscous_Material" title="wikilink">Viscous
Material</a></li>
<li><a href="BoucWen_Material" title="wikilink">BoucWen
Material</a></li>
<li><a href="BWBN_Material" title="wikilink">BWBN Material</a> (Pinching
Hysteretic Bouc-Wen Material)</li>
<li>PyTzQz uniaxial materials for p-y, t-z and q-z elements for modeling
soil-structure interaction through the piles in a structural foundation
<ul>
<li><a href="PySimple1_Material" title="wikilink">PySimple1
Material</a></li>
<li><a href="TzSimple1_Material" title="wikilink">TzSimple1
Material</a></li>
<li><a href="QzSimple1_Material" title="wikilink">QzSimple1
Material</a></li>
<li><a href="PyLiq1_Material" title="wikilink">PyLiq1 Material</a></li>
<li><a href="TzLiq1_Material" title="wikilink">TzLiq1 Material</a></li>
<li><a
href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1257.htm">PySimple1Gen
Command</a></li>
<li><a
href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1261.htm">TzSimple1Gen
Command</a></li>
</ul></li>
<li><a href="KikuchiAikenHDR_Material" title="wikilink">KikuchiAikenHDR
Material</a></li>
<li><a href="KikuchiAikenLRB_Material" title="wikilink">KikuchiAikenLRB
Material</a></li>
<li><a href="AxialSp_Material" title="wikilink">AxialSp
Material</a></li>
<li><a href="AxialSpHD_Material" title="wikilink">AxialSpHD
Material</a></li>
<li><a href="Pinching_Limit_State_Material" title="wikilink">Pinching
Limit State Material</a></li>
<li><a href="CFSWSWP" title="wikilink"> CFSWSWP Wood-Sheathed
Cold-Formed Steel Shear Wall Panel</a></li>
<li><a href="CFSSSWP" title="wikilink"> CFSSSWP Steel-Sheathed
Cold-formed Steel Shear Wall Panel</a></li>
</ul></li>
</ul>

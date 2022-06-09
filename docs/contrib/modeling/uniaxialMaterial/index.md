# UniaxialMaterial Library

This command is used to construct a `UniaxialMaterial`
object which represents uniaxial stress-strain (or force-deformation)
relationships.

<hr />

<p>NOTE:</p>
<p>The valid queries to any uniaxial material when creating an
ElementRecorder are `strain`, `stress`, and `tangent`. Some materials
have additional queries to which they will respond. These are documented
in the NOTES section for those materials.</p>

<p>The following contain information about matType? and the args
required for each of the available material types:</p>


### General-Purpose Materials

#### Elastic / Path-Independent
<ul>
<li><a href="Elastic_Uniaxial_Material">Elastic</a></li>
<li><a href="Elastic-No_Tension_Material">Elastic-No Tension</a></li>
<li><a href="ElasticBilin_Material">ElasticBilin</a></li>
<li><a href="ElasticMultiLinear_Material">ElasticMultiLinear</a></li>
<li><a href="PathIndependent_Material">PathIndependent</a></li>
</ul>

#### Inelastic
<ul>
<li><a href="MultiLinear_Material">MultiLinear</a></li>
<li><a href="Elastic-Perfectly_Plastic_Gap">Elastic-Perfectly Plastic Gap</a></li>
<li><a href="Pinching4_Material">Pinching4</a></li>
</ul>

### Standard Rate-Independent Materials

These models are formulated and implemented according to well-established
principles and algorithms.

<ul>
<li><a href="ElasticPP">ElasticPP</a> Elastic-perfectly plastic</li>
<li><a href="Hardening_Material">Hardening</a></li>
</ul>

### Standard Rate-Dependent Materials

<ul>
<li><a href="Viscous_Material">Viscous</a></li>
<li><a href="ViscousDamper_Material">ViscousDamper
</a></li>
</ul>


### Metallic 

<dl>
<dt><a href="Steel01">Steel01</a></dt>
<dt><a href="Steel02">Steel02</a></dt>
   <dd>Giuffré-Menegotto-Pinto Model with Isotropic Strain Hardening</dd>

<dt><a href="Steel4">Steel4</a></dt>
   <dd></dd>
<dt><a href="Hysteretic_Material">Hysteretic</a></dt>
   <dd></dd>
<dt><a href="Reinforcing_Steel_Material">ReinforcingSteel</a></dt>
   <dd></dd>
<dt><a href="DoddRestrepo">Dodd Restrepo</a></dt>
   <dd></dd>
<dt><a href="RambergOsgoodSteel">RambergOsgoodSteel</a></dt>
   <dd></dd>

<dt><a href="SteelMPF">SteelMPF</a></dt>
   <dd>Menegotto and Pinto (1973) model Extended by Filippou et al. (1983)</dd>

<dt><a href="UVCuniaxial_(Updated_Voce-Chaboche)">UVCuniaxial</a></dt>
   <dd>Updated Voce-Chaboche</dd>
</dl>


### Concrete

<dl>
<dt><a href="Concrete01">Concrete01</a></dt>
  <dd>Hognestad's concrete curve with zero tensile strength</dd>

<dt><a href="Concrete02">Concrete02</a></dt>
  <dd>Concrete01 with linear tension softening</dd>

<dt><a href="Concrete04">Concrete04</a></dt>
  <dd>Popovics concrete curve</dd>

<dt><a href="Concrete06">Concrete06</a></dt>
  <dd>
  </dd>

<dt><a href="Concrete07">Concrete07</a></dt>
  <dd>Chang &amp; Mander’s 1994 Concrete Model</dd>

<dt><a href="ConfinedConcrete01">ConfinedConcrete01</a></dt>
  <dd>
  </dd>

<dt><a href="ConcreteD">ConcreteD</a></dt>
  <dd>
  </dd>

<dt><a href="FRPConfinedConcrete">FRPConfinedConcrete</a></dt>
  <dd>
  </dd>

<dt><a href="ConcreteCM">ConcreteCM</a></dt>
  <dd>Complete Concrete Model by Chang and Mander (1994)</dd>

</dl>

### Bouc-Wen Models

<ul>
<li>BoucWenOriginal</li>
<li>DegradingPinchedBW</li>
<li>BoucWenInfill</li>
<li><a href="BoucWen_Material">BoucWen</a></li>
<li><a href="BWBN_Material">BWBN</a> Pinching Hysteretic Bouc-Wen Material</li>
</ul>

### Wrappers

<ul>
<li><a href="Parallel_Material">Parallel</a></li>
<li><a href="Series_Material">Series</a></li>
<li><a href="Initial_Strain_Material">Initial Strain</a></li>
<li><a href="Initial_Stress_Material">Initial Stress</a></li>
<li><a href="Fatigue_Material">Fatigue</a></li>
<li><a href="MinMax_Material">MinMax</a></li>
</ul>


### Other Uniaxial Materials

<ul>
<li><a href="Concrete01WithSITC">Concrete01WithSITC</a>
Concrete Material With Stuff in the Cracks</li>

<li><a href="ModIMKBilin/">ModIMKBilin</a>
Modified Ibarra-Medina-Krawinkler Deterioration Model with Bilinear Hysteretic Response (Bilin)
</li>

<li><a href="ModIMKPeakOriented/">ModIMKPeakOriented</a>
Modified Ibarra-Medina-Krawinkler Deterioration Model with Peak-Oriented Hysteretic Response
</li>

<li><a href="ModIMKPinching">ModIMKPinching</a>
Modified Ibarra-Medina-Krawinkler Deterioration Model with Pinched Hysteretic Response
</li>

<li><a href="CastFuse">CastFuse</a></li>
<li><a href="BilinearOilDamper">BilinearOilDamper</a></li>
<li><a href="SAWS_Material">SAWS</a></li>
<li><a href="BARSLIP_Material">BARSLIP</a></li>
<li><a href="Bond_SP01">Bond_SP01</a>
Strain Penetration Model for Fully Anchored Steel Reinforcing Bars
</li>

<li><a href="Impact_Material">Impact</a></li>
<li><a href="Hyperbolic_Gap_Material">HyperbolicGap</a></li>

<li><a href="Limit_State_Material">Limit State</a></li>
<li><a href="Pinching_Limit_State_Material">Pinching Limit State</a></li>

<li><a href="Engineered_Cementitious_Composites_Material">Engineered Cementitious Composites</a></li>


<li><a href="KikuchiAikenHDR_Material">KikuchiAikenHDR</a></li>
<li><a href="KikuchiAikenLRB_Material">KikuchiAikenLRB</a></li>
<li><a href="AxialSp_Material">AxialSp</a></li>
<li><a href="AxialSpHD_Material">AxialSpHD</a></li>
<li><a href="CFSWSWP">CFSWSWP</a> Wood-Sheathed Cold-Formed Steel Shear Wall Panel </li>
<li><a href="CFSSSWP">CFSSSWP</a> Steel-Sheathed Cold-formed Steel Shear Wall Panel</li>

<li><a href="SelfCentering_Material">SelfCentering</a> uniaxial self-centering (flag-shaped) material object with optional non-recoverable slip behaviour and an optional stiffness increase at high strains (bearing behaviour).</li>
</ul>

### PyTzQz uniaxial soil materials 

for p-y, t-z and q-z elements for modeling soil-structure interaction through the piles in a structural foundation
<ul>
  <li><a href="PySimple1">PySimple1</a></li>
  <li><a href="TzSimple1">TzSimple1</a></li>
  <li><a href="QzSimple1">QzSimple1</a></li>
  <li><a href="PyLiq1">PyLiq1</a></li>
  <li><a href="TzLiq1">TzLiq1</a></li>
  <li><a
    href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1257.htm">PySimple1Gen Command</a></li>
  <li><a
    href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/1261.htm">TzSimple1Gen Command</a></li>
</ul>



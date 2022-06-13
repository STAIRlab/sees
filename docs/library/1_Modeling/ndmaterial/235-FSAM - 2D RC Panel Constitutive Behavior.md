# FSAM - 2D RC Panel Constitutive Behavior

<p>This command is used to construct a nDMaterial <strong>FSAM</strong>
(Fixed-Strut-Angle-Model, Figure 1, Kolozvari et al., 2015), which is a
plane-stress constitutive model for simulating the behavior of RC panel
elements under generalized, in-plane, reversed-cyclic loading conditions
(Ulugtekin, 2010; Orakcal et al., 2012). In the <strong>FSAM</strong>
constitutive model, the strain fields acting on concrete and reinforcing
steel components of a RC panel are assumed to be equal to each other,
implying perfect bond assumption between concrete and reinforcing steel
bars. While the reinforcing steel bars develop uniaxial stresses under
strains in their longitudinal direction, the behavior of concrete is
defined using stress-strain relationships in biaxial directions, the
orientation of which is governed by the state of cracking in concrete.
Although the concrete stress-strain relationship used in the
<strong>FSAM</strong> is fundamentally uniaxial in nature, it also
incorporates biaxial softening effects including compression softening
and biaxial damage. For transfer of shear stresses across the cracks, a
friction-based elasto-plastic shear aggregate interlock model is
adopted, together with a linear elastic model for representing dowel
action on the reinforcing steel bars (Kolozvari, 2013). Note that
<strong>FSAM</strong> constitutive model is implemented to be used with
Shear-Flexure Interaction model for RC walls (<a
href="http://opensees.berkeley.edu/wiki/index.php/SFI_MVLEM_-_Cyclic_Shear-Flexure_Interaction_Model_for_RC_Walls"><strong>SFI_MVLEM</strong></a>),
but it could be also used elsewhere.</p>
<p><strong>Source:</strong>
/usr/local/cvs/OpenSees/SRC/material/nD/reinforcedConcretePlaneStress/</p>
<figure>
<img src="/OpenSeesRT/contrib/static/FSAM_1.png"
title="Figure 1. FSAM for Converting In-Plane Strains to In-Plane Smeared Stresses on a RC Panel Element"
width="500"
alt="Figure 1. FSAM for Converting In-Plane Strains to In-Plane Smeared Stresses on a RC Panel Element" />
<figcaption aria-hidden="true">Figure 1. FSAM for Converting In-Plane
Strains to In-Plane Smeared Stresses on a RC Panel Element</figcaption>
</figure>
<hr />
<p><strong>Input Format:</strong></p>

```tcl
nDMaterial FSAM $mattag $rho $sX $sY $conc $rouX $rouY
        $nu $alfadow
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">mattag</code></td>
<td><p>Unique nDMaterial tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>Material density</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">sX</code></td>
<td><p>Tag of uniaxialMaterial simulating horizontal (x)
reinforcement</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sY</code></td>
<td><p>Tag of uniaxialMaterial simulating vertical (y)
reinforcement</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">conc</code></td>
<td><p>Tag of uniaxialMaterial&lt;sup
class="superscript">1</sup&gt; simulating concrete</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rouX</code></td>
<td><p>Reinforcing ratio in horizontal (x) direction (rouX = A&lt;sub
class="subscript">s,x</sub>/A&lt;sub
class="subscript">gross,x</sub>)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rouY</code></td>
<td><p>Reinforcing ratio in vertical (y) direction (rouY = A&lt;sub
class="subscript">s,y</sub>/A&lt;sub
class="subscript">gross,y</sub>)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">nu</code></td>
<td><p>Concrete friction coefficient (0.0 &lt; nu &lt; 1.5)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">alfadow</code></td>
<td><p>Stiffness coefficient of reinforcement dowel action (0.0 &lt;
alfadow &lt; 0.05)</p></td>
</tr>
</tbody>
</table>

<p><sup class="superscript">1</sup>nDMaterial
<strong>FSAM</strong> shall be used with uniaxialMaterial <a
href="http://opensees.berkeley.edu/wiki/index.php/ConcreteCM_-_Complete_Concrete_Model_by_Chang_and_Mander_(1994)"><strong>ConcreteCM</strong></a></p>
<p>Recommended values for parameter of a shear resisting mechanism
(<strong>nu</strong> and <strong>alfadow</strong>, Figure 2) are
provided above. Details about the sensitivity of analytical predictions
using <a
href="http://opensees.berkeley.edu/wiki/index.php/SFI_MVLEM_-_Cyclic_Shear-Flexure_Interaction_Model_for_RC_Walls"><strong>SFI_MVLEM</strong></a>
element to changes in these parameters are presented by Kolozvari
(2013).</p>
<hr />
<p><strong>Material Recorders:</strong></p>
<p>The following output is available from the <strong>FSAM</strong> RC
panel model:</p>

<table>
<tbody>
<tr class="odd">
<td><p><strong>panel_strain</strong></p></td>
<td><p>Strains ε<sub class="subscript">x</sub>, ε<sub
class="subscript">y</sub>, &gamma;<sub
class="subscript">xy</sub> (Figure 1)</p></td>
</tr>
<tr class="even">
<td><p><strong>panel_stress</strong></p></td>
<td><p>Resulting panel stresses σ<sub
class="subscript">x</sub>, σ<sub
class="subscript">y</sub>, &tau;<sub
class="subscript">xy</sub> (concrete and steel, Figure
1)</p></td>
</tr>
<tr class="odd">
<td><p><strong>panel_stress_concrete</strong></p></td>
<td><p>Resulting panel concrete stresses σ<sub
class="subscript">xc</sub>, σ<sub
class="subscript">yc</sub>, &tau;<sub
class="subscript">xyc</sub> (Figure 2b)</p></td>
</tr>
<tr class="even">
<td><p><strong>panel_stress_steel</strong></p></td>
<td><p>Resulting panel steel stresses σ<sub
class="subscript">xs</sub>, σ<sub
class="subscript">ys</sub>, &tau;<sub
class="subscript">xys</sub> (Figure 2e)</p></td>
</tr>
<tr class="odd">
<td><p><strong>strain_stress_steelX</strong></p></td>
<td><p>Uniaxial strain and stress of horizontal reinforcement ε<sub
class="subscript">x</sub>, σ<sub
class="subscript">xxs</sub> (Figure 2f)</p></td>
</tr>
<tr class="even">
<td><p><strong>strain_stress_steelY</strong></p></td>
<td><p>Uniaxial strain and stress of vertical reinforcement ε<sub
class="subscript">y</sub>, σ<sub
class="subscript">yys</sub> (Figure 2f)</p></td>
</tr>
<tr class="odd">
<td><p><strong>strain_stress_concrete1</strong></p></td>
<td><p>Uniaxial strain and stress of concrete strut 1 ε<sub
class="subscript">c1</sub>, σ<sub
class="subscript">c1</sub> (Figure 2c)</p></td>
</tr>
<tr class="even">
<td><p><strong>strain_stress_concrete2</strong></p></td>
<td><p>Uniaxial strain and stress of concrete strut 2 ε<sub
class="subscript">c2</sub>, σ<sub
class="subscript">c2</sub> (Figure 2c)</p></td>
</tr>
<tr class="odd">
<td><p><strong>strain_stress_interlock1</strong></p></td>
<td><p>Shear strain and stress in concrete along crack 1 ε<sub
class="subscript">cr1</sub>, &tau;<sub
class="subscript">cr1</sub> (Figure 2d)</p></td>
</tr>
<tr class="even">
<td><p><strong>strain_stress_interlock2</strong></p></td>
<td><p>Shear strain and stress in concrete along crack 2 ε<sub
class="subscript">cr2</sub>, &tau;<sub
class="subscript">cr2</sub> (Figure 2d)</p></td>
</tr>
<tr class="odd">
<td><p><strong>cracking_angles</strong></p></td>
<td><p>Orientation of concrete cracks</p></td>
</tr>
</tbody>
</table>

<p>Note that recorders for a RC panel (marco-fiber) are invoked as <a
href="http://opensees.berkeley.edu/wiki/index.php/SFI_MVLEM_-_Cyclic_Shear-Flexure_Interaction_Model_for_RC_Walls"><strong>SFI_MVLEM</strong></a>
element recorders using command <strong>RCPanel</strong> and one of the
desired commands listed above. Currently, it is possible to output
values only for one macro-fiber within one or multiple elements.</p>
<hr />

## Examples

```tcl
nDMaterial FSAM 1 0.0 1 2 4 0.0073 0.0606 0.1 0.01
recorder Element -file MVLEM_panel_strain.out -time -ele 1 RCPanel 1 panel_strain
```

<figure>
<img src="/OpenSeesRT/contrib/static/FSAM_2a.png"
title="Figure 2. Behavior and Input/Output Parameters of the FSAM Constitutive Model"
width="1000"
alt="Figure 2. Behavior and Input/Output Parameters of the FSAM Constitutive Model" />
<figcaption aria-hidden="true">Figure 2. Behavior and Input/Output
 Parameters of the FSAM Constitutive Model</figcaption>
</figure>

<hr />

## References
1) Kolozvari K., Orakcal K., and Wallace J. W. (2015). "Shear-Flexure
  Interaction Modeling of reinforced Concrete Structural Walls and Columns
  under Reversed Cyclic Loading", Pacific Earthquake Engineering Research
  Center, University of California, Berkeley, <a
  href="http://peer.berkeley.edu/publications/peer_reports/reports_2015/webPEER-2015-12-kolozvari.pdf">PEER Report No. 2015/12</a>

2) Kolozvari K. (2013). “Analytical Modeling of Cyclic Shear-Flexure
  Interaction in Reinforced Concrete Structural Walls”, PhD Dissertation,
  University of California, Los Angeles.

3) Orakcal K., Massone L.M., and Ulugtekin D. (2012). “Constitutive
  Modeling of Reinforced Concrete Panel Behavior under Cyclic Loading”,
  Proceedings, 15th World Conference on Earthquake Engineering, Lisbon,
  Portugal.

4) Ulugtekin D. (2010). “Analytical Modeling of Reinforced Concrete
  Panel Elements under Reversed Cyclic Loadings”, M.S. Thesis, Bogazici
  University, Istanbul, Turkey.

<p><strong>Code developed by:</strong></p>
<p><a href="mailto:kkolozvari@fullerton.edu"><span style="color:blue"> Kristijan Kolozvari</span>
<span style="color:black"></a>, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal<span style="color:black">, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> Leonardo Massone<span style="color:black">, University of Chile, Santiago</p>
<p><span style="color:blue"> John Wallace<span style="color:black">, Univeristy of California, Los Angeles</p>


# ConcretewBeta

<p>&emsp;&emsp;This command is used to construct a uniaxial
concrete material object that explicitly considers for the effect of
normal (to the axis where the material object is used) strain to the
behavior of the concrete in compression. The compressive stress-strain
envelope, up to the peak compressive strength(unconfined or confined) is
based on the Fujii concrete model (Hoshikuma et al. 1997). The material
has two options regarding the strength degradation in tension: (a)
tri-linear or (b) nonlinear [based on the tension stiffening relation of
Stevens et al (1991)]. The softening behavior in compression is
tri-linear.</p>
<p>&emsp;&emsp;The model accounts for the effect of normal
tensile strains on the concrete compressive behavior when used with the
<strong><a href="Truss2_Element" title="wikilink"> Truss2</a></strong>
or <strong><a href="CorotTruss2_Element" title="wikilink">
CorotTruss2</a></strong> elements. See the <strong><a
href="Truss2_Element" title="wikilink"> Truss2 Element</a></strong> for
description of how the normal strain is computed. The instantaneous
stress is $\beta f$ where $f$ is the
computed stress and $\beta$ is the compressive stress reduction
factor which depends on the normal tensile strain,
$\epsilon_n$. The relation between
$\epsilon_n$ and $\beta$ (see the <strong><a
href="#Biaxial_Behavior" title="wikilink">Biaxial Behavior
Section</a></strong>) is tri-linear. Default values result in
$\beta$ = 1.</p>
<p>See the <strong><a href="#Examples" title="wikilink">Examples
Section</a></strong> for the use of this material model in truss models
for planar RC walls and a beam-truss model for a non-planar wall loaded
biaxially.</p>
<dl>
<dt></dt>
<dd>

<dl>
<dt></dt>
<dd>
<a href="File:BeyerTUB_point770.jpg"
title="wikilink" alt="RC C-shaped wall">Reinforced
concrete wall with a C-shaped section subject to multi-axial loading,
described in <a href="#Examples" title="wikilink">the examples</a>.</a>
</dd>
</dl>
</dd>
</dl>

```tcl
uniaxialMaterial ConcretewBeta $matTag $fpc $ec0 $fcint
        $ecint $fcres $ecres $ft $ftint $etint $ftres $etres 
        < -lambda $lambda > 
        < -alpha $alpha > < -beta $bint $ebint $bres $ebres > 
        < -M $M > < -E $Ec >
        < -conf $fcc $ecc >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fpc</code></td>
<td><p>peak unconfined concrete compressive strength*</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ec0</code></td>
<td><p>compressive strain corresponding to unconfined concrete
compressive strength*</p></td>
</tr>
<tr class="even">
<td><p><code>fcint, ecint</code></p></td>
<td><p>intermediate stress-strain point for compression post-peak
envelope*</p></td>
</tr>
<tr class="odd">
<td><p><code>fcres, ecres</code></p></td>
<td><p>residual stress-strain point for compression post-peak
envelope*</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ftint</code></td>
<td><p>tensile strength of concrete</p></td>
</tr>
<tr class="odd">
<td><p><code>ftint, etint</code></p></td>
<td><p>intermediate stress-strain point for tension softening
envelope</p></td>
</tr>
<tr class="even">
<td><p><code>ftres, etres</code></p></td>
<td><p>residual stress-strain point for tension softening
envelope</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Optional:</p></td>
<td></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">lambda</code></td>
<td><p>controls the path of unloading from compression strain (default 0.5)</p>
</td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>controls the path of unloading from tensile strain (default 1)</p>
</td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">bint ebint</code></p></td>
<td><p>intermediate $\beta$-strain point for for biaxial effect
(default 1 and 0, respectively)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">bres ebres</code></p></td>
<td><p>residual &beta;-strain point for for biaxial effect (default
1 and 0, respectively)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">M</code></td>
<td><p>factor for Stevens et al. (1991) tension stiffening (default 0;
see Note 2)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ec</code></td>
<td><p>initial stiffness (default
2*<code class="tcl-variable">fpc</code>/<code class="tcl-variable">ec0</code>; see Note 3)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">fcc ecc</code></p></td>
<td><p>confined concrete peak compressive stress and corresponding
strain* (see Eq. 1)</p></td>
</tr>
</tbody>
</table>


### Notes

- Parameters of concrete in compression should be specified as
  negative values.
- For non-zero <code class="tcl-variable">M</code>, the tension stiffening behavior
  will govern the post-peak tension envelope. Tri-linear tension softening
  parameters <code>ftint, etint, ftres, etres</code> will have no
  effect, but dummy values must be specified.
- Value of <code class="tcl-variable">Ec</code> must be between
  <code class="tcl-variable">fpc</code>/<code class="tcl-variable">ec0</code> and
  2*<code class="tcl-variable">fpc</code>/<code class="tcl-variable">ec0</code> otherwise the closest
  value will be assigned.

<h2 id="implementation">Implementation</h2>

<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<img src="/OpenSeesRT/contrib/static/ConcwBeta_Eq1a.png" >
<a href="File:ConcwBeta_Eq1a.png" title="wikilink">thumb|upright=2.5|Equation 1.</a>
</dd>
<dd>

$$
\boldsymbol{E} \boldsymbol{u}= \texttt{ lambda } \cdot\left(\frac{f}{\varepsilon}\right)+(1- \texttt{ lambda }) \cdot \texttt{Ec}
$$

</dd>
<dd>
<img src="/OpenSeesRT/contrib/static/ConcwBeta_Eq3.png" >
<a href="File:ConcwBeta_Eq3.png" title="wikilink">thumb|upright=1.8|Equation 3.</a>
</dd>
</dl>
</dd>
</dl>
<h3 id="uniaxial_behavior">Uniaxial Behavior</h3>
<p>&emsp;&emsp;Figure 1 shows the compression and tension
envelopes and the input parameters. The confined concrete envelope is
defined by Equation 1 up to strain <code class="tcl-variable">ecc</code>. The default
values of `fcc` and `ecc` are equal to
<code class="tcl-variable">fpc</code> and <code class="tcl-variable">ec0</code>, respectively, for an an
unconfined behavior. Following this region, the compression envelope is
tri-linear and passes through the points (<code class="tcl-variable">ecint</code>,
<code class="tcl-variable">fcint</code>) and (<code class="tcl-variable">ecres</code>,
<code class="tcl-variable">fcres</code>) in that order. For compression strains larger
than <code class="tcl-variable">ecres</code>, the residual stress is
<code class="tcl-variable">fcres</code>.

&emsp;&emsp;For compression strain, the slope of the
unloading branch is defined by Equation 2. After reaching zero stress,
the material reloads linearly to the point with the largest tensile
strain that occurred before.

<p>&emsp;&emsp;The tension envelope is linear until it reaches
<code class="tcl-variable">ft</code>. If the tension stiffening parameter
<code class="tcl-variable">M</code> is not specified, the tension envelope after
reaching <code class="tcl-variable">ft</code> is tri-linear and passes through the
points (<code class="tcl-variable">etint</code>, <code class="tcl-variable">ftint</code>) and
(<code class="tcl-variable">etres</code>, <code class="tcl-variable">ftres</code>) in that order. For
tensile strains larger than <code class="tcl-variable">etres</code>, the residual stress
is <code class="tcl-variable">fcres</code>.</p>
<p>&emsp;&emsp;If <code class="tcl-variable">M</code> is specified, the
nonlinear tension stiffening behavior defined by Equation 3. It is
suggested that <code class="tcl-variable">M</code> = (75
mm)*$\rho_\ell$/<em>d<sub>b</sub></em>
where $\rho_\ell$ is the steel ratio in
the direction parallel to the material direction and
<em>d<sub>b</sub></em> is the bar diameter in mm.</p>
<p>&emsp;&emsp;The material unloads from tension strain using a
slope of <code class="tcl-variable">Ec</code>. After reaching zero stress, the material
targets the point (0, -<code class="tcl-variable">alpha</code>*<code class="tcl-variable">ft</code>).
Thereafter, the material loads linearly to the point where the peak
compressive strain previously occurred. In the case where the slope
leading to this target point is less than that for the point (0,
-<code class="tcl-variable">alpha</code>*<code class="tcl-variable">ft</code>), the material reloads
directly to the point where peak compressive strain occurred.</p>

<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="File:ConcwBeta_Fig1b.gif"
title="wikilink">thumb|center|upright=4.0|alt=ConcretewBeta Figure 1
|Figure 1. ConcretewBeta material model behavior based on specified
input parameters</a>
</dd>
</dl>
</dd>
</dl>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="File:ConcwBeta_Fig2b.gif"
title="wikilink">thumb|upright=2.0|alt=ConcretewBeta Figure 2 |Figure 2.
Relation between the concrete compressive stress reduction factor,
$\beta$, and normal tensile strain,
$\epsilon_n$</a>

</dd>
</dl>
</dd>
</dl>

<h3 id="biaxial_behavior">Biaxial Behavior</h3>
<p>&emsp;&emsp;The ConcretewBeta material model accounts for the
biaxial strain field on the concrete compressive behavior when used in
conjunction with the <strong><a href="Truss2_Element" title="wikilink">
Truss2</a></strong> element. The <strong><a href="Truss2_Element"
title="wikilink"> Truss2</a></strong> element computes the strain normal
to the direction of the element (see <strong><a href="Truss2_Element"
title="wikilink"> Truss2 Element</a></strong>).</p>
<p>&emsp;&emsp;Figure 2 shows the relationship between concrete
compressive stress reduction factor, $\beta$, and the normal
tensile strain, $\epsilon_n$. For compressive
stresses, the instantaneous stress value computed by the material is
$\beta f_c$ where
$f_c$ is the compressive stress given by
the uniaxial behavior described above. For positive (tensile) stress,
$\beta = 1$. For compressive stress, the
$\beta - \epsilon_n$ relationship
is tri-linear and passes through the points (0,1),
(<code class="tcl-variable">ebint</code>, <code class="tcl-variable">bint</code>), and
(<code class="tcl-variable">ebres</code>, <code class="tcl-variable">bres</code>) in that order. For
normal tensile strains larger than <code class="tcl-variable">ebres</code>,
$\beta$ = <code class="tcl-variable">bres</code>.</p>

<h2 id="examples">Examples</h2>
<h3
id="story_rc_core_wall_buildings_conventional_fixed_base_video_rocking_wall_video_and_base_isolation_with_rocking_wall_video">20-story
RC core wall buildings: conventional fixed-base (<strong><a
href="http://youtu.be/r14GDOB9tgY">video</a></strong>), rocking wall
(<strong><a href="http://youtu.be/DmEwyWwcRP4">video</a></strong>), and
base isolation with rocking wall (<strong><a
href="http://youtu.be/FBj-mNos8gU">video</a></strong>)</h3>
<p><a href="Image:20story_samplePic2.png" title="wikilink">1200px
|alt=20-story core walls</a></p>
<h3
id="story_coupled_wall_specimen_with_diagonal_tension_failure_see_video_of_the_simulation">5-story
coupled wall specimen with diagonal tension failure, see: <strong><a
href="http://youtu.be/a26aZiU5RgY">Video of the
simulation</a></strong></h3>
<figure>
<img src="/OpenSeesRT/contrib/static/5story_samplePic.png" title="5story_samplePic.png" width="800"
alt="5story_samplePic.png" />
<figcaption aria-hidden="true">5story_samplePic.png</figcaption>
</figure>

<h3
id="see_truss_model___mestyanek_1986_squat_rc_wall_and_video_of_the_simulation">See:
<strong><a href="Truss_Model_Example_-_Mestyanek_Squat_Wall"
title="wikilink"> Truss Model - Mestyanek (1986) Squat RC
Wall</a></strong> and <strong><a
href="http://youtu.be/lQpzwHF_Z94">Video of the
simulation</a></strong></h3>

<figure>
<img src="/OpenSeesRT/contrib/static/Mestyanek_resultsPlot2.png" title="Mestyanek_resultsPlot2.png"
width="800" alt="Mestyanek_resultsPlot2.png" />
<figcaption aria-hidden="true">Mestyanek_resultsPlot2.png</figcaption>
</figure>

<h3
id="see_beam_truss_model___beyer_et_al._2008_rc_wall_and_video_of_the_simulation">See:
<strong><a href="Beam-truss_Model_Example_-_C-shaped_RC_Wall"
title="wikilink"> Beam-truss Model - Beyer et al. (2008) RC
Wall</a></strong> and <strong><a
href="http://youtu.be/9O9Mev62Ilw">Video of the
simulation</a></strong></h3>

<figure>
<img src="/OpenSeesRT/contrib/static/BeyerWall_fig2.png" title="BeyerWall_fig2.png" width="800"
alt="BeyerWall_fig2.png" />
<figcaption aria-hidden="true">BeyerWall_fig2.png</figcaption>
</figure>

<h3
id="see_truss_model___massone_sanchez_2005_squat_rc_wall_and_video_of_the_simulation">See:
<strong><a href="Truss_Model_Example_-_Squat_RC_Wall" title="wikilink">
Truss Model - Massone Sanchez (2005) Squat RC Wall</a></strong> and
<strong><a href="http://youtu.be/aq7r4HMAmvc">Video of the
simulation</a></strong></h3>
<figure>
<img src="/OpenSeesRT/contrib/static/MassoneWall_displ1a.jpg" title="MassoneWall_displ1a.jpg"
width="400" alt="MassoneWall_displ1a.jpg" />
<figcaption aria-hidden="true">MassoneWall_displ1a.jpg</figcaption>
</figure>

<h2 id="references">References</h2>
<p>Lu, Y., Panagiotou, M, and Koutromanos, I. (2014). "Three-dimensional
beam-truss model for reinforced concrete walls and slabs subjected to
cyclic static or dynamic loading." Report PEER 2014/18, Pacific
Earthquake Engineering Research Center, University of California,
Berkeley, Berkeley, CA.</p>
<p>Lu, Y. and Panagiotou, M. (2014). “Earthquake Damage Resistant
Multistory Buildings at Near Fault Regions using Base Isolation and
Rocking Core Walls.” 1st Huixian International Forum on Earthquake
Engineering for Young Researchers, August 16-19, Harbin, China.</p>
<p>Lu, Y., and Panagiotou, M. (2014). “Three-Dimensional Nonlinear
Cyclic Beam-Truss Model for Reinforced Concrete Non-Planar Walls.”
Journal of Structural Engineering, 140 (3), DOI:
10.1061/(ASCE)ST.1943-541X.0000852.</p>
<p>Panagiotou, M., Restrepo, J.I., Schoettler, M., and Kim G. (2012).
"Nonlinear cyclic truss model for reinforced concrete walls." ACI
Structural Journal, 109(2), 205-214.</p>
<p>Beyer, K., Dazio, A., and Priestley, M. J. N.(2008). "Quasi-Static
Cyclic Tests of Two U-Shaped Reinforced Concrete Walls." Journal of
Earthquake Engineering, 12:7, 1023-1053.</p>
<p>Hoshikuma, J., Kawashima, K., Nagaya, K., and Taylor, A. W. (1997).
“Stress-strain model for confined reinforced concrete in bridge piers.”
Journal of Structural Engineering, 123(5), 624-633.</p>
<p>Massone Sanchez, L. M. (2006). “RC Wall Shear—Flexure Interaction:
Analytical and Experimental Responses.” PhD thesis, University of
California, Los Angeles, Los Angeles, CA, 398 pp.</p>
<p>Mestyanek, J. M. (1986). "The earthquake resistance of reinforced
concrete structural walls of limited ductility." ME thesis. University
of Canterbury.</p>
<p>Stevens, N. J., Uzumeri, S. M., Collins, M. P., and Will, T. G.
(1991). “Constitutive model for reinforced concrete finite element
analysis.” ACI Structural Journal, 88(1), 49-59.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Yuan Lu, UC
Berkeley </span> and <span style="color:blue"> Marios
Panagiotou, UC Berkeley </span></p>

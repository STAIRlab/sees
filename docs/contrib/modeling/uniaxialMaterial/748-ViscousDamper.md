# ViscousDamper

<p>This command is used to construct a ViscousDamper material, which
represents the <a
href="http://en.wikipedia.org/wiki/Maxwell_material">Maxwell Model</a>
(linear spring and nonlinear dashpot in series). The ViscousDamper
material simulates the hysteretic response of nonlinear viscous dampers.
An adaptive iterative algorithm has been implemented and validated to
solve numerically the constitutive equations within a nonlinear viscous
damper with a high-precision accuracy.</p>

```tcl
uniaxialMaterial ViscousDamper $matTag $K $Cd $alpha
        < $LGap > < $NM $RelTol $AbsTol $MaxHalf >
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">K</code></td>
<td><p>Elastic stiffness of linear spring to model the axial flexibility
of a viscous damper (e.g. combined stiffness of the supporting brace and
internal damper portion)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Cd</code></td>
<td><p>Damping coefficient</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>Velocity exponent</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">LGap</code></td>
<td><p>Gap length to simulate the gap length due to the pin
tolerance</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">NM</code></td>
<td><p>Employed adaptive numerical algorithm (default value NM = 1; 1 =
Dormand-Prince54, 2=6th order Adams-Bashforth-Moulton, 3=modified
Rosenbrock Triple)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">RelTol</code></td>
<td><p>Tolerance for absolute relative error control of the adaptive
iterative algorithm (default value 10^-6)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">AbsTol</code></td>
<td><p>Tolerance for absolute error control of adaptive iterative
algorithm (default value 10^-10)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">MaxHalf</code></td>
<td><p>Maximum number of sub-step iterations within an integration step
(default value 15)</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>
<hr />

## Examples


1. Input parameters:

   Assume a viscous damper with axial stiffness K=300.0kN/mm,
   damping coefficient `Cd=280.3kN`(s/mm)<sup>0.3</sup>, and
   exponent a=0.30.

   The input parameters for the material should be as
   follows:

   ```tcl
   uniaxialMaterial ViscousDamper 1 300 280.3 0.30
   ```

   Using these properties, Figure 1 shows the hysteretic response of
   this damper for sinusoidal displacement increments of 12, 24 and 36mm
   and a frequency f = 0.5Hz.

   The sensitivity of the viscous damper with respect to its
   velocity exponent is shown in Figures 2 to 4 for the following set of
   parameters:

  <figure>
  <img src="/OpenSeesRT/contrib/static/Fig2_ViscousDampers.png"
  title=" Viscous Damper with various input parameter variations"
  width="850"
  alt=" Viscous Damper with various input parameter variations" />
  <figcaption aria-hidden="true"> Viscous Damper with various input
  parameter variations</figcaption>
  </figure>


<strong><em><a
href="http://opensees.berkeley.edu/wiki/index.php/Dynamic_Analyses_of_1-Story_Moment_Frame_with_Viscous_Dampers">2. Single story single bay frame with viscous damper</a></em></strong>

<hr />

## References

<table>
<tbody>
<tr class="odd">
<td><p><strong>[1]</strong></p></td>
<td><p>Akcelyan, S., Lignos, D. G., Hikino, T., and Nakashima, M.
(2016). “Evaluation of simplified and state-of-the-art analysis
procedures for steel frame buildings equipped with supplemental damping
devices based on E-Defense full-scale shake table tests.” Journal of
Structural Engineering, 142(6), 04016024. <a
href="http://ascelibrary.org/doi/ref/10.1061/%28ASCE%29ST.1943-541X.0001474">1</a></p></td>
</tr>
<tr class="even">
<td><p><strong>[2]</strong></p></td>
<td><p>Akcelyan, S., Lignos, D. G., Hikino, T. (2018). “Adaptive
Numerical Method Algorithms for Nonlinear Viscous and Bilinear Oil
Damper Models Subjected to Dynamic Loading.” Soil Dynamics and
Earthquake Engineering, 113, 488-502. <a
href="http://doi.org/10.1016/j.soildyn.2018.06.021">2</a>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>[3]</strong></p></td>
<td><p>Akcelyan, S. (2017). "Seismic retrofit of existing steel tall
buildings with supplemental damping devices." Ph.D. Dissertation, McGill
University, Canada.</p></td>
</tr>
<tr class="even">
<td><p><strong>[4]</strong></p></td>
<td><p>Oohara, K., and Kasai, K. (2002), “Time-History Analysis Models
for Nonlinear Viscous Dampers”, Proc. Structural Engineers World
Congress (SEWC), Yokohama, JAPAN, CD-ROM, T2-2-b-3 (in
Japanese).</p></td>
</tr>
<tr class="odd">
<td><p><strong>[5]</strong></p></td>
<td><p>Kasai K, Oohara K. “Algorithm and Computer Code To Simulate
Response of Nonlinear Viscous Damper” Passively Controlled Structure
Symposium 2001, Yokohama, Japan (in Japanese).</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<p>Code Developed and Implemented by : <span style="color:blue">
<strong><em><a href="http://sarvenakcelyan.com">Sarven
Akcelyan</a><strong><em>&amp;</em></strong><a
href="http://dimitrios-lignos.research.mcgill.ca/PLignos.html">Prof.
Dimitrios G. Lignos</a></em></strong>, (McGill University)
</span></p>


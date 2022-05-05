# Damage2p

<p>This command is used to construct a three-dimensional material object
that has a Drucker-Prager plasticity model coupled with a two-parameter
damage model.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDMaterial Damage2p $matTag $fcc &lt;-fct $fct&gt; &lt;-E
$E&gt; &lt;-ni $ni&gt; &lt;-Gt $Gt&gt; &lt;-Gc $Gc&gt; &lt;-rho_bar
$rho_bar&gt; &lt;-H $H&gt; &lt;-theta $theta&gt; &lt;-tangent
$tangent&gt;</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$fcc</strong></p></td>
<td><p>concrete compressive strength</p></td>
</tr>
<tr class="odd">
<td><p><strong>$fct</strong></p></td>
<td><p>optional concrete tensile strength</p></td>
</tr>
<tr class="even">
<td><p><strong>$E</strong></p></td>
<td><p>optional Young modulus</p></td>
</tr>
<tr class="odd">
<td><p><strong>$ni</strong></p></td>
<td><p>optional Poisson coefficient</p></td>
</tr>
<tr class="even">
<td><p><strong>$Gt</strong></p></td>
<td><p>optional tension fracture energy density</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Gc</strong></p></td>
<td><p>optional compression fracture energy density</p></td>
</tr>
<tr class="even">
<td><p><strong>$rho_bar</strong></p></td>
<td><p>ptional parameter of plastic volume change</p></td>
</tr>
<tr class="odd">
<td><p><strong>$H</strong></p></td>
<td><p>optional linear hardening parameter for plasticity</p></td>
</tr>
<tr class="even">
<td><p><strong>$theta</strong></p></td>
<td><p>optional ratio between isotropic and kinematic hardening</p></td>
</tr>
<tr class="odd">
<td><p><strong>$tangent</strong></p></td>
<td><p>optional integer to choose the computational stiffness
matrix</p></td>
</tr>
</tbody>
</table>
<p>The material formulations for the Damage2p object are
"ThreeDimensional" and "PlaneStrain"</p>
<h2 id="notes">NOTES</h2>
<p>1. Admissible values: The input parameters vary as follows:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>$fcc</strong></p></td>
<td><p>negative real value (positive input is changed in sign
automatically)</p></td>
</tr>
<tr class="even">
<td><p><strong>$fct</strong></p></td>
<td><p>positive real value (for concrete like materials is less than
$fcc)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Gt</strong></p></td>
<td><p>positive real value (integral of the stress-strain envelope in
tension)</p></td>
</tr>
<tr class="even">
<td><p><strong>$Gc</strong></p></td>
<td><p>positive real value (integral of the stress-strain envelope after
the peak in compression)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$rhoBar</strong></p></td>
<td><p>positive real value 0=rhoBar&lt;sqrt(2/3)</p></td>
</tr>
<tr class="even">
<td><p><strong>$H</strong></p></td>
<td><p>positive real value (usually less than $E)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$theta</strong></p></td>
<td><p>positive real value 0=$theta=1 (with: 0 hardening kinematic only
and 1 hardening isotropic only</p></td>
</tr>
<tr class="even">
<td><p><strong>$tangent</strong></p></td>
<td><p>0: computational tangent; 1: damaged secant stiffness (hint: in
case of strong nonlinearities use it with Krylov-Newton
algorithm)</p></td>
</tr>
</tbody>
</table>
<p>2. Default values: The Damage2p object hve the following defualt
parameters:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>$fct</strong></p></td>
<td><p>= 0.1*abs(fcc)</p></td>
</tr>
<tr class="even">
<td><p><strong>$E</strong></p></td>
<td><p>= 4750*sqrt(abs(fcc)) if abs(fcc)&lt;2000 because fcc is assumed
in MPa (see ACI 318)</p>
<p>= 57000*sqrt(abs(fcc)) if abs(fcc)&gt;2000 because fcc is assumed in
psi (see ACI 318)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$ni</strong>'</p></td>
<td><p>= 0.15 (from comparison with tests by Kupfer Hilsdorf Rusch
1969)</p></td>
</tr>
<tr class="even">
<td><p><strong>'$Gt</strong></p></td>
<td><p>= 1840*fct*fct/E (from comparison with tests by Gopalaratnam and
Shah 1985)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Gc</strong></p></td>
<td><p>= 6250*fcc*fcc/E (from comparison with tests by Karsan and Jirsa
1969)</p></td>
</tr>
<tr class="even">
<td><p><strong>$rhoBar</strong></p></td>
<td><p>= 0.2 (from comparison with tests by Kupfer Hilsdorf Rusch
1969)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$H</strong></p></td>
<td><p>= 0.25*E (from comparison with tests by Karsan and Jirsa 1969 and
Gopalaratnam and Shah 1985)</p></td>
</tr>
<tr class="even">
<td><p><strong>'$theta</strong></p></td>
<td><p>= 0.5 (from comparison with tests by Karsan and Jirsa 1969 and
Gopalaratnam and Shah 1985)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$tangent</strong></p></td>
<td><p>= 0</p></td>
</tr>
</tbody>
</table>
<h2 id="development_team">Development Team</h2>
<p>This code has been Developed by: &lt;span
style="color:blue"&gt;Leopoldo Tesser - Dept. DICEA - Univeristy of
Padua - Italy</span>,</p>
<p>contact: <span style="color:blue">leopoldo.tesser AT
dicea.unipd.it</span></p>
<h2 id="references">References</h2>
<p>Tesser L.,"Efficient 3-D plastic damage model for cyclic inelastic
analysis of concrete structures", Report of the University of Padua,
Italy, 2012. (soon available at paduareserach.cab.unipd.it)</p>
<p>Petek K.A., "Development and application of mixed beam-solid models
for analysis of soil-pile interaction problems", Ph.D. dissertation,
Univerisity of Washington, USA, 2006</p>

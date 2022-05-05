 # Impact

<p>This command is used to construct an impact material object</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>uniaxialMaterial ImpactMaterial $matTag $K1 $K2 $δy
$gap</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$K1</strong></p></td>
<td><p>initial stiffness</p></td>
</tr>
<tr class="odd">
<td><p><strong>$K2</strong></p></td>
<td><p>secondary stiffness</p></td>
</tr>
<tr class="even">
<td><p><strong>$δy</strong></p></td>
<td><p>yield displacement</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">gap</code></td>
<td><p>initial gap*</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<p>This material is implemented as a compression-only gap material.
Delta_y and gap should be input as negative values.</p>
<p>DESCRIPTION:</p>
<p>This material is based on an approximation to the Hertz contact model
proposed by Muthukumar (See REFERENCES below). The energy dissipated
during impact is:</p>
<p>E = kh * δm^(n+1) * (1-e^2) / (N+1)</p>
<p>where kh is the impact stiffness parameter, with a typical value of
EA/L or 25,000 k-in.-3/2; n is typically taken as 3/2 for the exponent
associated with the Hertz power rule; e is the coefficient of
restitution, with typical values from 0.6-0.8; and δm is the maximum
penetration during the pounding event. The effective stiffness, Keff,
is:</p>
<p>Keff = kh * sqrt(δm)</p>
<p>The yield displacement is:</p>
<p>δy = a * δm</p>
<p>where a is typically taken as 0.1. The initial stiffness, K1, and
secondary stiffness, K2, are then selected such that the Impact model
dissipates an amount of energy during a pounding event that is
consistent with the associated energy dissipated in the Hertz model.</p>
<p>K1 = Keff + E / (a*δm^2)</p>
<p>K2 = Keff - E / ((1-a)*δm^2)</p>
<p>Response of Impact Material during a pounding event.</p>
<figure>
<img src="ImpactA.gif" title="ImpactA.gif" alt="ImpactA.gif" />
<figcaption aria-hidden="true">ImpactA.gif</figcaption>
</figure>
<p>Response of Impact Material for displacement cycles of increasing
amplitude.</p>
<figure>
<img src="ImpactB.gif" title="ImpactB.gif" alt="ImpactB.gif" />
<figcaption aria-hidden="true">ImpactB.gif</figcaption>
</figure>
<p>EXAMPLE:</p>
<p>REFERENCES:</p>
<p>Muthukumar, S., and DesRoches, R. (2006). “A Hertz Contact Model with
Non-linear Damping for Pounding Simulation.” Earthquake Engineering and
Structural Dynamics, 35, 811-828.</p>
<p>Muthukumar, S. (2003). “A Contact Element Approach with Hysteresis
Damping for the Analysis and Design of Pounding in Bridges.” PhD Thesis,
Georgia Institute of Technology. <a
href="http://smartech.gatech.edu/">http://smartech.gatech.edu/</a></p>
<p>Nielson, B. (2005). “Analytical Fragility Curves for Highway Bridges
in Moderate Seismic Zones.” PhD Thesis, Georgia Institute of Technology.
<a
href="http://smartech.gatech.edu/">http://smartech.gatech.edu/</a></p>
<hr />
<p>Code Developed by: <span style="color:blue"> Mathew Dryden, UC
Berkeley </span></p>

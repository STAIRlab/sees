# BarSlip

<p>This command is used to construct a uniaxial material that simulates
the bar force versus slip response of a reinforcing bar anchored in a
beam-column joint. The model exhibits degradation under cyclic loading.
Cyclic degradation of strength and stiffness occurs in three ways:
unloading stiffness degradation, reloading stiffness degradation,
strength degradation.</p>

```tcl
uniaxialMaterial BarSlip $matTag $fc $fy $Es $fu $Eh $db
        $ld $nb $depth $height 
        < $ancLratio > 
        $bsFlag $type 
        < $damage $unit >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>unique material object integer tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fc</code></td>
<td><p>positive floating point value defining the compressive strength
of the concrete in which the reinforcing bar is anchored</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fy</code></td>
<td><p>positive floating point value defining the yield strength of the
reinforcing steel</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Es</code></td>
<td><p>floating point value defining the modulus of elasticity of the
reinforcing steel</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fu</code></td>
<td><p>positive floating point value defining the ultimate strength of
the reinforcing steel</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Eh</code></td>
<td><p>floating point value defining the hardening modulus of the
reinforcing steel</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ld</code></td>
<td><p>floating point value defining the development length of the
reinforcing steel</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">db</code></td>
<td><p>point value defining the diameter of reinforcing steel</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nb</code></td>
<td><p>an integer defining the number of anchored bars</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">depth</code></td>
<td><p>floating point value defining the dimension of the member (beam
or column) perpendicular to the dimension of the plane of the
paper</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">height</code></td>
<td><p>floating point value defining the height of the flexural member,
perpendicular to direction in which the reinforcing steel is placed, but
in the plane of the paper</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ancLratio</code></td>
<td><p>floating point value defining the ratio of anchorage length used
for the reinforcing bar to the dimension of the joint in the direction
of the reinforcing bar (optional, default: 1.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">bsFlag</code></td>
<td><p>string indicating relative bond strength for the anchored
reinforcing bar (options: "Strong" or "Weak")</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">type</code></td>
<td><p>string indicating where the reinforcing bar is placed. (options:
"beamtop", "beambot" or "column")</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">damage</code></td>
<td><p>string indicating type of damage:whether there is full damage in
the material or no damage (optional, options: "Damage", "NoDamage" ;
default: Damage)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">unit</code></td>
<td><p>string indicating the type of unit system used (optional,
options: "psi", "MPa", "Pa", "psf", "ksi", "ksf") (default: "psi" /
"MPa")*</p></td>
</tr>
</tbody>
</table>
<p>NOTES</p>
<ul>
<li>Model Characteristics:</li>
</ul>
<p>The uniaxial material model uses the Pinching4 material model (Ref.
Pinching4 material model). The response envelope for the bar-slip
springs does not represent strength deterioration, but once the slip
demand exceeds 3mm (0.12 in), strength deterioration due to cyclic
loading initiates. As a result the bond-slip springs always exhibit
positive stiffness, but strength deterioration upon reloading to a
previously observed slip demand. Reloading and Unloading Stiffness
deterioration are also simulated.

The damage index for unloading and reloading stiffness degradation is
evaluated the same say as the Pinching4 material (ref. Pinching4
material doc.) but the index for strength degradation is specified
as</p>
<p>With degradation model parameters gF*. It should be noted in here
that the deterioration parameters for unloading, reloading stiffness and
strength degradation cannot be modified by the user and are defined to
represent observed behavior.</p>
<ul>
<li>The model includes predefined bond strengths, so there is the
necessity to include in Units in this material model. For default one
can specify units in psi (i.e. pounds/inch2) or in MPa (i.e. N/mm2). The
code detects units in psi if the compressive strength of concrete is
greater than 1000 otherwise it takes it as MPa system. The optional
variable `unit` will help the user to specify other different types of
unit systems according to one's choice, but currently it is limited to
the unit systems as specified above. The user should also take care to
specify the units of length in the corresponding matching units. (note:
Pa = N/m2; ksf = kilo-pound/ft2)</li>
</ul>

<hr />

<p>Code Developed by: <span style="color:blue"> Nilanjan Mitra,
CalPoly State University </span></p>

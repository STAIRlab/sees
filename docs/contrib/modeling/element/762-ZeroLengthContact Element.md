# ZeroLengthContact Element

<p>This command is used to construct a zeroLengthContact2D element or a
zeroLengthContact3D element, which are Node-to-node frictional contact
element used in two dimensional analysis and three dimensional
analysis:</p>
<p>2d analysis:</p>

```tcl
element zeroLengthContact2D $eleTag $cNode $rNode $Kn $Kt
        $mu -normal $Nx $Ny
```
<p>3d analysis:</p>

```tcl
element zeroLengthContact3D $eleTag $cNode $rNode $Kn $Kt
        $mu $c $dir
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">cNode</code></td>
<td><p>Constrained node tag</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rNode</code></td>
<td><p>Retained node tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Kn</code></td>
<td><p>Penalty in normal direction</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Kt</code></td>
<td><p>Penalty in tangential direction</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">mu</code></td>
<td><p>friction coefficient</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">c</code></td>
<td><p>cohesion (not available in 2D)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dir</code></td>
<td><p>Direction flag of the contact plane (3D), it can be:</p>
<p>1 Out normal of the retained plane pointing to +X direction</p>
<p>2 Out normal of the retained plane pointing to +Y direction</p>
<p>3 Out normal of the retained plane pointing to +Z direction</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/ZeroLengthContact2.png" title="ZeroLengthContact2.png"
alt="ZeroLengthContact2.png" />
<figcaption aria-hidden="true">ZeroLengthContact2.png</figcaption>
</figure>
<p>NOTES:</p>
<ol>
<li>The contact element is node-to-node contact. Contact occurs between
two contact nodes when they come close. The relation follows
Mohr-coulomb law: T = $mu * N + $c, where T is tangential force and N is
normal force across the interface. $mu is friction coefficient and $c is
total cohesion (summed over the effective area of contact nodes)</li>
<li>The contact node pair in node-to-node contact element is termed
"retained node" and "constrained node", respectively.
Retained/constrained plane is the contact plane which the
retrained/constrained node belongs to. The discrimination is made solely
for contact detection purpose. User need to specify the corresponding
out normal of the master plane, and this direction is assumed to be
unchanged during analysis. For simplicity, 3D contact only allows 3
options to specify the directions of the contact plane. The convention
is: out normal of master plane always points to positive axial direction
(+X or +Y, or +Z)</li>
<li>For 2D contact, constrained nodes and retained nodes must be 2 DOF.
For 3D contact, constrained nodes and retained nodes must be 3 DOF.</li>
<li>The resulted tangent from the contact element is
<strong>NON-SYMMETRIC</strong>. Switch to non-symmetric matrix
solver.</li>
</ol>
<hr />

## Examples

<p>Gang Wang to provide a smart example!</p>
<hr />
<p>REFERENCES:</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Gang Wang,
Geomatrix</span></p>

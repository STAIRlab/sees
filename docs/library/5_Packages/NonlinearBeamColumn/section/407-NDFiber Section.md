# NDFiber Section

This commnand allows the user to construct an NDFiberSection object.
Each NDFiberSection object is composed of NDFibers, with each fiber
containing an NDMaterial, an area and a location (y,z). The
NDFiberSection works for 2D and 3D frame elements and it queries the
NDMaterial of each fiber for its axial and shear stresses. In 2D, stress
components 11 and 12 are obtained from each fiber in order to provide
stress resultants for axial force, bending moment, and shear (N, Mz, and
Vy). Stress components 11, 12, and 13 lead to all six stress resultants
in 3D (N, Mz, Vy, My, Vz, and T).

The `NDFiberSection` works with any `NDMaterial` via wrapper classes that
perform static condensation of the stress vector down to the 11, 12, and
13 components, or via concrete NDMaterial subclasses that implement the
appropriate fiber stress conditions.

The command to generate NDFiberSection object contains in <strong>{
}</strong> the commands to generate all the fibers in the object. To
construct an NDFiberSection and populate it, the following command is
used:

<table>
<tbody>
<tr class="odd">
<td><p><strong>section NDFiber $secTag {</strong></p></td>
</tr>
<tr class="even">
<td><p><strong><a href="fiber_Command" title="wikilink">
fiber</a>...</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong><a href="patch_Command" title="wikilink">
patch</a>...</strong></p></td>
</tr>
<tr class="even">
<td><p><strong><a href="layer_Command" title="wikilink">
layer</a>...</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>...</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>}</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">secTag</code></p></td>
<td><p>unique tag among all sections</p></td>
</tr>
<tr class="even">
<td><p><strong><a href="fiber_Command" title="wikilink">
fiber</a>...</strong></p></td>
<td><p>command to generate a single fiber.</p></td>
</tr>
<tr class="odd">
<td><p><strong><a href="patch_Command" title="wikilink">
patch</a>...</strong></p></td>
<td><p>command to generate a number of fibers over a geometric
cross-section</p></td>
</tr>
<tr class="even">
<td><p><strong><a href="layer_Command" title="wikilink">
layer</a>...</strong></p></td>
<td><p>command to generate a row of fibers along a
geometric-arc</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<p>NOTES:</p>
<ol>
<li>The command to generate an NDFiberSection contains in <strong>{
    }</strong> the commands to generate all the fibers in the section.</li>
<li>The patch and layer commands can be used to generate multiple fibers
    in a single command.</li>
<li>In an element recorder you can ask an NDFiberSection for its
    `deformations`, `forces`, `forceAndDeformation`, `fiber $fiberNum
    $matArg1 ..`, `fiber $yLoc $zLoc $matTag $matArg1 `</li>
</ol>
<hr />

```plantuml
NDFiberSection o- NDFiber
```

<hr />
<p>Code Developed by: <span style="color:blue"> Michael H. Scott, Oregon State University </span></p>

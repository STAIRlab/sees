# Fiber Section

This commnand allows the user to construct a FiberSection object.
Each FiberSection object is composed of Fibers, with each fiber
containing a `UniaxialMaterial`, an area and a location ($y$,$z$). The command
to generate FiberSection object contains in <strong>{ }</strong> the
commands to generate all the fibers in the object. To construct a
FiberSection and populate it, the following command is used:

<table>
<tbody>
<tr class="odd">
<td><p><strong>section Fiber $secTag &lt;-GJ $GJ&gt; {</strong></p></td>
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
<td><p>unique tag among sections</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">GJ</code></p></td>
<td><p>linear-elastic torsional stiffness assigned to the section
(optional, default = no torsional stiffness)</p></td>
</tr>
<tr class="odd">
<td><p><strong><a href="fiber_Command" title="wikilink">
fiber</a>...</strong></p></td>
<td><p>command to generate a single fiber</p></td>
</tr>
<tr class="even">
<td><p><strong><a href="patch_Command" title="wikilink">
patch</a>...</strong></p></td>
<td><p>command to generate a number of fibers over a geometric
cross-section</p></td>
</tr>
<tr class="odd">
<td><p><strong><a href="layer_Command" title="wikilink">
layer</a>...</strong></p></td>
<td><p>command to generate a row of fibers along a
geometric-arc</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<p>NOTES:</p>
<ol>
<li>The command to generate a FiberSection contains in <strong>{ }</strong> 
  the commands to generate all the fibers in the section.</li>
<li>The patch and layer commands can be used to generate multiple fibers
  in a single command.</li>
<li>In an element recorder you can ask a FiberSection for its
  `deformations`, `forces`, `forceAndDeformation`, `fiber $fiberNum $matArg1 ..`, 
  `fiber $yLoc $zLoc $matTag $matArg1 `</li>
</ol>
<hr />
<p>&lt;uml&gt; FiberSection o- Fiber &lt;/uml&gt;</p>
<hr />

<p>Code developed by: <span style="color:blue"> Michael H. Scott, Oregon State University </span></p>


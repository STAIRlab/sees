# ZeroLengthImpact3D

<p>This command constructs a node-to-node zero-length contact element in
3D space to simulate the impact/pounding and friction phenomena.</p>

```tcl
element zeroLengthImpact3D $tag $cNode $rNode $direction
        $initGap $frictionRatio $Kt $Kn $Kn2 $Delta_y
        $cohesion
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>Unique element object tag</p></td>
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
<td><code class="parameter-table-variable">direction</code></td>
<td><p>1 if out-normal vector of master plane points to +X direction</p>
<p>2 if out-normal vector of master plane points to +Y direction</p>
<p>3 if out-normal vector of master plane points to +Z
direction</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">initGap</code></td>
<td><p>Initial gap between retained plane and constrained plane</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">frictionRatio</code></td>
<td><p>Friction ratio in two tangential directions (parallel to retained
and constrained planes)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Kt</code></td>
<td><p>Penalty in two tangential directions</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Kn</code></td>
<td><p>Penalty in normal direction (normal to retained and constrained
planes)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Kn2</strong></p></td>
<td><p>Penalty in normal direction after yielding based on Hertz impact
model</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Delta_y</code></td>
<td><p>Yield deformation based on Hertz impact model</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">cohesion</code></td>
<td><p>Cohesion, if no cohesion, it is zero</p></td>
</tr>
</tbody>
</table>
<hr />
<p>NOTES:</p>
<ol>
<li>This element has been developed on top of the “zeroLengthContact3D”.
All the notes available in <a href="ZeroLengthContact_Element"
title="wikilink"> “zeroLengthContact3D” wiki page </a> would apply to
this element as well. It includes the definition of retained and
constrained nodes, the number of degrees of freedom in the domain,
etc.</li>
<li>Regarding the number of degrees of freedom (DOF), the end nodes of
this element should be defined in 3DOF domain. For getting information
on how to use 3DOF and 6DOF domain together, please refer to OpenSees
documentation and forums or see the zip file provided in the EXAMPLES
section below.</li>
<li>This element adds the capabilities of <a href="Impact_Material"
title="wikilink"> “ImpactMaterial” </a> to <a
href="ZeroLengthContact_Element" title="wikilink">
“zeroLengthContact3D.” </a></li>
<li>For simulating a surface-to-surface contact, the element can be
defined for connecting the nodes on constrained surface to the nodes on
retained surface.</li>
<li>The element was found to be fast-converging and eliminating the need
for extra elements and nodes in the modeling process.</li>
</ol>
<hr />
<p>EXAMPLES:</p>
<ol>
<li>The following zip file contains an example script and the
corresponding input cyclic displacement: <embed
src="Example_script_2.zip" title="Example_script_2.zip" /></li>
<li>The following zip file contains an example script on how to use 6DOF
domain and 3DOF domain together: <embed
src="Example_script_6DOF_3DOF.zip"
title="Example_script_6DOF_3DOF.zip" /></li>
</ol>
<p>&lt;!--</p>
<hr />
<p>SAMPLE COMMAND (example scripts are available at bottom of this
page):</p>
<p>&lt;source lang="Tcl"&gt;</p>
<p>&lt;/source&gt; --&gt;</p>
<hr />
<p>REFERENCES:</p>
<p><a href="ZeroLengthContact_Element" title="wikilink">
zeroLengthContact3D </a> , <a href="Impact_Material" title="wikilink">
ImpactMaterial </a></p>
<hr />
<p>CODE DEVELOPED BY:</p>
<dl>
<dt></dt>
<dd>
<span style="color:blue"> Dr. Arash E. Zaghi and Majid Cashany at
University of Connecticut (UConn) </span>
</dd>
</dl>
<hr />
<p>APPLICATIONS:</p>
<ol>
<li>This element has been employed to simulate the bridge hinges
including superstructure-abutment interaction at the University of
Connecticut (UConn) and University of Nevada, Reno (UNR).</li>
<li>It has been implemented in non-structural systems like suspended
ceilings, simulating the impact/pounding and friction phenomena.</li>
</ol>
<p>&lt;!-- After running the example script, the following hysteresis
loop is resulted in normal direction under cyclic excitation:</p>
<p><img src="/OpenSeesRT/contrib/static/_HysteresisLoop.png" title="_HysteresisLoop.png"
alt="_HysteresisLoop.png" /> --&gt;</p>

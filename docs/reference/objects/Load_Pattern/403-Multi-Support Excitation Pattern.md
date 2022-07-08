# Multi-Support Excitation Pattern

<p>The Multi-Support pattern allows similar or different prescribed
ground motions to be input at various supports in the structure. In
OpenSees, the prescribed motion is applied using single-point
constraints, the single-point constraints taking their constraint value
from user created ground motions.</p>

```plantuml
abstract class TimeSeries 
LoadPattern <|-- MultipleSupportExcitation 
MultipleSupportExcitation o- GroundMotion
MultipleSupportExcitation o- ImposedMotionSP 
ImposedMotionSP --- GroundMotion 
SP_Constraint <|-- ImposedMotionSP 
GroundMotion o- TimeSeries 
```


<p>The command to generate a multi-support excitation contains in
<strong>{ }</strong> the commands to generate all the ground motions and
the single-point constraints in the pattern. The command is as
follows:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>pattern MultipleSupport $patternTag {</strong></p></td>
</tr>
<tr class="even">
<td><p><strong><a href="groundMotion_Command" title="wikilink">
groundMotion</a>...</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong><a href="imposedMotion_Command" title="wikilink">
imposedMotion</a>...</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>...</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>}</strong></p></td>
</tr>
</tbody>
</table>

<p>NOTES:</p>
<ol>
<li>The results for the responses at the nodes are the ABSOLUTE values,
and not relative values as in the case of a UniformExciatation.</li>
<li>The non-homogeneous single point constraints require an appropriate
choice of constraint handler.</li>
</ol>
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">patternTag</code></p></td>
<td><p>unique tag among load patterns</p></td>
</tr>
<tr class="even">
<td><p><strong><a href="groundMotion_Command" title="wikilink">
groundMotion</a>...</strong></p></td>
<td><p>command to generate a ground motion</p></td>
</tr>
<tr class="odd">
<td><p><strong><a href="imposedMotion_Command" title="wikilink">
imposedMotion</a> ...</strong></p></td>
<td><p>command to generate an imposed motion</p></td>
</tr>
</tbody>
</table>

<hr />

<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

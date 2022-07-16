# Plain Loading


This commnand allows the user to construct a LoadPattern object. Each
plain load pattern is associated with a <a href="Time_Series_Command"
title="wikilink"> TimeSeries</a> object and can contain multiple
NodalLoads, ElementalLoads and SP_Constraint objects. The command to
generate LoadPattern object contains in <strong>{ }</strong> the
commands to generate all the loads and the single-point constraints in
the pattern. To construct a load pattern and populate it, the following
command is used:

::: {apidoc="opensees.pattern.Plain"}
:::

<table>
<tbody>
<tr class="odd">
<td><p><strong>pattern Plain $patternTag $tsTag &lt;-fact $cFactor&gt;
{</strong></p></td>
</tr>
<tr class="even">
<td><p><strong><a href="nodalLoad_Command" title="wikilink">
load</a>...</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong><a href="eleLoad_Command" title="wikilink">
eleLoad</a>...</strong></p></td>
</tr>
<tr class="even">
<td><p><strong><a href="sp_Command" title="wikilink">
sp</a>...</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>...</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>}</strong></p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">patternTag</code></p></td>
<td><p>unique tag among load patterns</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">tsTag</code></p></td>
<td><p>the tag of the time series to be used in the load
pattern</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">cFactor</code></p></td>
<td><p>constant factor (optional, default=1.0)</p></td>
</tr>
<tr class="even">
<td><p><strong><a href="nodalLoad_Command" title="wikilink">
load</a>...</strong></p></td>
<td><p>command to nodal load</p></td>
</tr>
<tr class="odd">
<td><p><strong><a href="eleLoad_Command" title="wikilink"> eleLoad</a>
...</strong></p></td>
<td><p>command to generate elemental load</p></td>
</tr>
<tr class="even">
<td><p><strong><a href="sp_Command" title="wikilink"> sp</a>
...</strong></p></td>
<td><p>command to generate single-point constraint</p></td>
</tr>
</tbody>
</table>

<hr />

<p>NOTES:</p>
<ol>
<li>The command to generate a `LoadPattern` contains in <strong>{
}</strong> the commands to generate all the loads and single-point
constraints..</li>
</ol>

<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

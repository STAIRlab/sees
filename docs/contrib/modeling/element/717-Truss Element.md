# Truss Element

<p>This command is used to construct a truss element object. There are
two ways to construct a truss element object:</p>
<p>One way is to specify an area and a UniaxialMaterial identifier:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element truss $eleTag $iNode $jNode $A $matTag &lt;-rho
$rho&gt; &lt;-cMass $cFlag&gt; &lt;-doRayleigh
$rFlag&gt;</strong></p></td>
</tr>
</tbody>
</table>
<p>the other is to specify a Section identifier:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element trussSection $eleTag $iNode $jNode $secTag
&lt;-rho $rho&gt; &lt;-cMass $cFlag&gt; &lt;-doRayleigh
$rFlag&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">A</code></td>
<td><p>cross-sectional area of element</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tag associated with previously-defined UniaxialMaterial</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">secTag</code></td>
<td><p>tag associated with previously-defined Section</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>mass per unit length, optional, default = 0.0</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">cFlag</code></td>
<td><p>consistent mass flag, optional, default = 0</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>cFlag = 0 lumped mass matrix (default)</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>cFlag = 1 consistent mass matrix</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rFlag</code></td>
<td><p>Rayleigh damping flag, optional, default = 0</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>rFlag = 0 NO RAYLEIGH DAMPING (default)</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>rFlag = 1 include Rayleigh damping</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<ol>
<li>The truss element DOES NOT include geometric nonlinearities, even
when used with beam-columns utilizing P-Delta or Corotational
transformations.</li>
<li>When constructed with a UniaxialMaterial object, the truss element
considers strain-rate effects, and is thus suitable for use as a damping
element.</li>
<li>The valid queries to a truss element when creating an
ElementRecorder object are 'axialForce,' 'forces,' 'localForce',
deformations,' 'material matArg1 matArg2...,' 'section sectArg1
sectArg2...' There will be more queries after the interface for the
methods involved have been developed further.</li>
<li>For backward compatibility the command <em>'element truss $eleTag
$iNode $jNode $secTag</em> will still work and produce a TrussSection
element.</li>
<li>There was an inconsistency in the way damping was treated between
element types before version 2.2.0. Before 2.2.0, a Truss DID NOT
INCLUDE Rayleigh damping, a TrussSection did. By default they both
<strong>DO NOT</strong> now include Rayleigh damping by default.</li>
</ol>
<p>EXAMPLE:</p>
<p>element truss 1 2 4 5.5 9; # truss element with tag 1 added between
nodes 2 and 4 with area 5.5 that uses material 9</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

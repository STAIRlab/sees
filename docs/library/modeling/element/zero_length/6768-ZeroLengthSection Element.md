# ZeroLengthSection

<p>This command is used to construct a zero length element object, which
is defined by two nodes at the same location. The nodes are connected by
a single section object to represent the force-deformation relationship
for the element.</p>

```tcl
element zeroLengthSection $eleTag $iNode $jNode $secTag
        < -orient $x1 $x2 $x3 $yp1 $yp2 $yp3 > < -doRayleigh $rFlag >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">iNode jNode</code></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">secTag</code></td>
<td><p>tag associated with previously-defined Section object</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">x1 x2 x3</code></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">yp1 yp2 yp3</code></p></td>
<td><p>vector components in global coordinates defining vector yp which
lies in the local x-y plane for the element. (optional)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rFlag</code></td>
<td><p>optional, default = 1</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>rFlag = 0 no Rayleigh damping</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>rFlag = 1 include Rayleigh damping (default)</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<ol>
<li>If the optional orientation vectors are not specified, the local
element axes coincide with the global axes. Otherwise the local z-axis
is defined by the cross product between the vectors `x` and `yp` vectors
specified on the command line.</li>

<li>The section force-deformation response represented by section string
`P` acts along the element local $x$-axis, and the response for code `Vy`
along the local $y$-axis. The other modes of section response follow from
this orientation.</li>

<li>The valid queries to a zero-length element when creating an
ElementRecorder object are `force,` `deformation,` `stiff,` and `section
$secArg1 secArg2 ...`.</li>
</ol>

## Examples

Truss tag 1 between nodes 2 and 4 usinga type 6 section:
```tcl
element zeroLengthSection 1 2 4 6;
```

Element tag 1 between nodes 1 and 2 defined with section 1. Local direction x,
perpendicular to element section, is aligned with the global Y axis and
the vector yp is aligned with the negative global Z axis:
```tcl
element zeroLengthSection 1 1 2 1 -orient 0 1 0 0 0 -1; 
```

<hr />
<p>Code developed by: <span style="color:blue"> Michael Scott, Oregon State University. </span></p>

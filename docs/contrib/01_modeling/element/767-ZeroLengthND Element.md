# ZeroLengthND Element

<p>This command is used to construct a zeroLengthND element object,
which is defined by two nodes at the same location. The nodes are
connected by a single NDMaterial object to represent the
force-deformation relationship for the element.</p>

```tcl
element zeroLengthND $eleTag $iNode $jNode $matTag
        &lt;$uniTag&gt; &lt;-orient $x1 $x2 $x3 $yp1 $yp2
        $yp3&gt;
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
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tag associated with previously-defined ndMaterial object</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">uniTag</code></td>
<td><p>ag associated with previously-defined UniaxialMaterial object
which may be used to represent uncoupled behavior orthogonal to the
plane of the NDmaterial response. SEE NOTES 2 and 3.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">x1 x2 x3</code></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">yp1 yp2 yp3</code></p></td>
<td><p>vector components in global coordinates defining vector yp which
lies in the local x-y plane for the element. (optional)</p></td>
</tr>
</tbody>
</table>
<p>NOTE:</p>
<ol>
<li>The zeroLengthND element only represents translational response
between its nodes</li>
<li>If the NDMaterial object is of order two, the response lies in the
element local x-y plane and the UniaxialMaterial object may be used to
represent the uncoupled behavior orthogonal to this plane, i.e. along
the local z-axis.</li>
<li>If the NDMaterial object is of order three, the response is along
each of the element local exes.</li>
<li>If the optional orientation vectors are not specified, the local
element axes coincide with the global axes. Otherwise the local z-axis
is defined by the cross product between the vectors x and yp vectors
specified on the command line.</li>
<li>The valid queries to a zero-length element when creating an
ElementRecorder object are 'force', 'deformation', and 'material matArg1
matArg2 ...'</li>
</ol>

## Examples

<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott,
Oregon State University. </span></p>

# ZeroLengthND Element

<p>This command is used to construct a zeroLengthND element object,
which is defined by two nodes at the same location. The nodes are
connected by a single NDMaterial object to represent the
force-deformation relationship for the element.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element zeroLengthND $eleTag $iNode $jNode $matTag
&lt;$uniTag&gt; &lt;-orient $x1 $x2 $x3 $yp1 $yp2
$yp3&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$eleTag</strong></p></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>tag associated with previously-defined ndMaterial object</p></td>
</tr>
<tr class="even">
<td><p><strong>$uniTag</strong></p></td>
<td><p>ag associated with previously-defined UniaxialMaterial object
which may be used to represent uncoupled behavior orthogonal to the
plane of the NDmaterial response. SEE NOTES 2 and 3.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$x1 $x2 $x3</strong></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="even">
<td><p><strong>$yp1 $yp2 $yp3</strong></p></td>
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
<p>EXAMPLE:</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott,
Oregon State University. </span></p>

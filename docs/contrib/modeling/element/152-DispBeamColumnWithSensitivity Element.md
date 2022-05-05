# DispBeamColumnWithSensitivity Element

<dl>
<dt></dt>
<dd>
This command is used to construct a 2-D or 3-D distributed-plasticity
displacement-based beam-column (frame) element.
</dd>
</dl>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element dispBeamColumnWithSensitivity $eleTag $iNode
$jNode $numIntgrPts $secTag $transfTag &lt;integration
method&gt;</strong></p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>integer tag identifying an existing parameter.</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>end nodes.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">numIntgrPts</code></td>
<td><p>number of integration points along the element.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">secTag</code></td>
<td><p>identifier for previously-defined section object.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">transfTag</code></td>
<td><p>identifier for previously-defined coordinate-transformation
(CrdTransf) object.</p></td>
</tr>
<tr class="even">
<td><p><strong>integration method</strong></p></td>
<td><p>optional (available options = ‘Lobatto’ or ‘Legendre’, default =
‘Legendre’).</p></td>
</tr>
</tbody>
</table>
<hr />
<dl>
<dt></dt>
<dd>
Currently, there are no sensitivity parameters in the
‘dispBeamColumnWithSensitivity’ element command.
</dd>
</dl>

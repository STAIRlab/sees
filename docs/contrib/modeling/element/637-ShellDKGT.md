# ShellDKGT

<p>This command is used to construct a ShellDKGT element object, which
is a triangular shell element based on the theory of generalized
conforming element.</p>

```tcl
element ShellDKGT $eleTag $iNode $jNode $kNode
        $secTag
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode $kNode</strong></p></td>
<td><p>three nodes defining element boundaries, input in clockwise or
counter-clockwise order around the element.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>tag associated with previously-defined SectionForceDeformation
object.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">secTag</code></td>
<td><p>currently can be a PlateFiberSection, a
ElasticMembranePlateSection and a LayeredShell section</p></td>
</tr>
</tbody>
</table>
<hr />
<p>Code Developed by : <span style="color:blue"> Shuhao Zhang,
Tsinghua University, and Prof. Xinzheng Lu, Tsinghua University
</span></p>

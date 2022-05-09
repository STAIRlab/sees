# ShellDKGQ

<p>This command is used to construct a ShellDKGQ element object, which
is a quadrilateral shell element based on the theory of generalized
conforming element.</p>

```tcl
element ShellDKGQ $eleTag $iNode $jNode $kNode $lNode
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
<td><p><code class="parameter-table-variable">iNode jNode kNode lNode</code></p></td>
<td><p>four nodes defining element boundaries, input in clockwise or
counter-clockwise order around the element.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">secTag</code></td>
<td><p>tag associated with previously-defined SectionForceDeformation
object. Currently can be a PlateFiberSection, a
ElasticMembranePlateSection and a LayeredShell section</p></td>
</tr>
</tbody>
</table>
<hr />
<p>Code Developed by : <span style="color:blue"> Lisha Wang,
Tsinghua University, Prof. Xinzheng Lu, Tsinghua University, Linlin Xie,
Tsinghua University, Prof. Song Cen, Tsinghua University and Prof. Quan
Gu, Xiamen University </span></p>

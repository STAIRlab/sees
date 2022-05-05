# BbarBrickWithSensitivity Element

<dl>
<dt></dt>
<dd>
This command is used to construct an eight-node 3D brick element object
based on a trilinear isoparametric formulation.
</dd>
</dl>

```tcl
element bbarBrickWithSensitivity $eleTag $node1 $node2
        $node3 $node4 $node5 $node6 $node7 $node8 $matTag
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$eleTag</strong></p></td>
<td><p>unique element object tag.</p></td>
</tr>
<tr class="even">
<td><p><strong>$node1 - $node8</strong></p></td>
<td><p>eight nodes defining element boundaries (numbered as shown in the
figure below).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>tag associated with previously-defined nDMaterial
object.</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="_Numbering_of_nodes_for_the_B-bar_brick_element.jpg"
title="_Numbering_of_nodes_for_the_B-bar_brick_element.jpg"
alt="_Numbering_of_nodes_for_the_B-bar_brick_element.jpg" />
<figcaption
aria-hidden="true">_Numbering_of_nodes_for_the_B-bar_brick_element.jpg</figcaption>
</figure>
<hr />
<dl>
<dt></dt>
<dd>
Currently, there are no sensitivity parameters in the
‘bbarBrickWithSensitivity’ element command.
</dd>
</dl>

# Plate Fiber Wrapper

This command is used to construct a plate-fiber material wrapper
which converts any three-dimensional material into a plate fiber
material (by static condensation) appropriate for shell analysis.

```tcl
nDMaterial PlateFiber $matTag $threeDTag
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">threeDTag</code></td>
<td><p>material tag for a previously-defined three-dimensional
material</p></td>
</tr>
</tbody>
</table>


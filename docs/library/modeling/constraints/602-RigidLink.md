# RigidLink

This command is used to construct a single MP_Constraint object.

:::{apidoc="opensees.constraint.RigidLink"}
```tcl
rigidLink $type $rNodeTag $cNodeTag
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">type</code></p></td>
<td><p>string-based argument for rigid-link type:</p></td>
</tr>
<tr class="even">
<td></td>
<td><p><strong>bar</strong> only the translational degree-of-freedom
will be constrained to be exactly the same as those at the retained
node</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p><strong>beam</strong> both the translational and rotational
degrees of freedom are constrained.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">rNodeTag</code></p></td>
<td><p>integer tag identifying the retained node</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">cNodeTag</code></p></td>
<td><p>integer tag identifying the constrained node</p></td>
</tr>
</tbody>
</table>
:::

NOTE: The constraint object constructed for the beam option assumes
small rotations

## Examples

connect node 3 to node 2 via a rigid link-beam.

```tcl
rigidLink beam 2 3; 
```

## References
<p>Cook, R.D., Malkus, D.S., Plesha, M. E., and Witt, R. J., "Concepts
and Applications of Finite Element Analysis," 4th edition, John Wiley
and Sons publishers, 2002.</p>

<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

# Broyden

This command is used to construct a Broyden algorithm object for
general unsymmetric systems which performs successive rank-one updates
of the tangent at the first iteration of the current time step.


```tcl
algorithm Broyden < $count >
```

<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">count</code></p></td>
<td><p>number of iterations within a time step until a new tangent is
formed</p></td>
</tr>
</tbody>
</table>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

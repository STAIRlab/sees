# Secant Newton

This command is used to construct a `SecantNewton` algorithm object
which uses the two-term update to accelerate the convergence of the
modified newton method. The command is of the following form:

```tcl
algorithm SecantNewton < -iterate $tangIter >
        < -increment $tangIncr > < -maxDim $maxDim >
```

<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">tangIter</code></p></td>
<td><p>tangent to iterate on, options are current, initial, noTangent.
default is current.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">tangIncr</code></p></td>
<td><p>tangent to increment on, options are current, initial, noTangent.
default is current</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">maxDim</code></p></td>
<td><p>max number of iterations until the tangent is reformed and
acceleration restarts (default = 3)</p></td>
</tr>
</tbody>
</table>
<hr />

## Notes

The default "cut-out" values recommended by Crisfield ($R_1=3.5$,
$R_2=0.3$) are used.

<hr />

## References
<p>Crisfield, M.A. "Non-linear Finite Element Analysis of Solids and
Structures", Vol. 1, Wiley, 1991.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Michael Scott,
Oregon State University </span></p>

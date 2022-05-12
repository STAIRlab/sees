# Secant Newton Algorithm

<p>This command is used to construct a SecantNewton algorithm object
which uses the two-term update to accelerate the convergence of the
modified newton method. The command is of the following form:</p>

```tcl
algorithm SecantNewton &lt;-iterate $tangIter&gt;
        &lt;-increment $tangIncr&gt; &lt;-maxDim $maxDim&gt;
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
<p>NOTES:</p>
<p>The default "cut-out" values recommended by Crisfield (R1=3.5,
R2=0.3) are used.</p>
<hr />
<p>REFERENCES:</p>
<p>Crisfield, M.A. "Non-linear Finite Element Analysis of Solids and
Structures", Vol. 1, Wiley, 1991.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Michael Scott,
Oregon State University </span></p>

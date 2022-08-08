# Fix

## FixX command

<p>This command is used to construct multiple homogeneous single-point
boundary constraints for all nodes whose x-coordinate lies within a
specified distance from a specified coordinate.</p>

```tcl
fixX $xCoordinate (ndf $ConstrValues) &lt;-tol $tol&gt;
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">xCoordinate</code></p></td>
<td><p>x-coordinate of nodes to be constrained</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">constrValues</code></p></td>
<td><p>ndf constraint values (0 or 1) corresponding to the ndf
degrees-of-freedom.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p><strong>0</strong> unconstrained (or free)</p></td>
</tr>
<tr class="even">
<td></td>
<td><p><strong>1</strong> constrained (or fixed)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">tol</code></p></td>
<td><p>user-defined tolerance (optional, default = 1e-10)</p></td>
</tr>
</tbody>
</table>

### Examples

  fixX 0.0 1 1 1 1 1 1; # fully restrain all nodes in y-z plane at origin (x=0.0)

## FixY command

<p>This command is used to construct multiple homogeneous single-point
boundary constraints for all nodes whose y-coordinate lies within a
specified distance from a specified coordinate.</p>

```tcl
fixY $yCoordinate (ndf $ConstrValues) &lt;-tol $tol&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">yCoordinate</code></p></td>
<td><p>y-coordinate of nodes to be constrained</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">constrValues</code></p></td>
<td><p>ndf constraint values (0 or 1) corresponding to the ndf
degrees-of-freedom.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p><strong>0</strong> unconstrained (or free)</p></td>
</tr>
<tr class="even">
<td></td>
<td><p><strong>1</strong> constrained (or fixed)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">tol</code></p></td>
<td><p>user-defined tolerance (optional, default = 1e-10)</p></td>
</tr>
</tbody>
</table>

### Examples

<p>fixY 0.0 1 1 1 1 1 1; # fully restrain all nodes in x=z plane at origin (y=0.0)</p>


## FixZ command

<p>This command is used to construct multiple homogeneous single-point
boundary constraints for all nodes whose z-coordinate lies within a
specified distance from a specified coordinate.</p>

```tcl
fixZ $zCoordinate (ndf $ConstrValues) &lt;-tol
        $tol&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">zCordinate</code></p></td>
<td><p>z-coordinate of nodes to be constrained</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">constrValues</code></p></td>
<td><p>ndf constraint values (0 or 1) corresponding to the ndf
degrees-of-freedom.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p><strong>0</strong> unconstrained (or free)</p></td>
</tr>
<tr class="even">
<td></td>
<td><p><strong>1</strong> constrained (or fixed)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">tol</code></p></td>
<td><p>user-defined tolerance (optional, default = 1e-10)</p></td>
</tr>
</tbody>
</table>

### Examples

<p>fixZ 0.0 1 1 1 1 1 1; # fully restrain all nodes in x-y plane at
origin (z=0.0)</p>

## Fix command

<p>This command is used to construct single-point homogeneous boundary
constraints.</p>

```tcl
fix $nodeTag (ndf $constrValues)
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">nodeTag</code></p></td>
<td><p>integer tag identifying the node to be constrained</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">constrValues</code></p></td>
<td><p>ndf constraint values (0 or 1) corresponding to the ndf
degrees-of-freedom.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p><strong>0</strong> unconstrained (or free)</p></td>
</tr>
<tr class="even">
<td></td>
<td><p><strong>1</strong> constrained (or fixed)</p></td>
</tr>
</tbody>
</table>

### Examples
```tcl
fix 1 1 1 1 1 1 1; # node 1: fully fixed
fix 2 0 1 0 0 1 0 # node 2: homogeneous constraints (movement = 0) at dof 2 and 5 only.
```
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

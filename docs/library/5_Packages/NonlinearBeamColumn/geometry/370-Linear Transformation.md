# Linear

<p>This command is used to construct a linear coordinate transformation
(LinearCrdTransf) object, which performs a linear geometric
transformation of beam stiffness and resisting force from the basic
system to the global-coordinate system.</p>
<p>For a two-dimensional problem:</p>

```tcl
geomTransf Linear $transfTag < -jntOffset $dXi $dYi $dXj $dYj >
```
<p>For a three-dimensional problem:</p>

```tcl
geomTransf Linear $transfTag $vecxzX $vecxzY $vecxzZ
        < -jntOffset $dXi $dYi $dZi $dXj $dYj $dZj >
```

<hr />

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">transfTag</code></td>
<td><p>integer tag identifying transformation</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">vecxzX vecxzY vecxzZ</code></p></td>
<td><p>$X$, $Y$, and $Z$ components of `vecxz`, the vector used to define the
local x-z plane of the local-coordinate system. The local y-axis is
defined by taking the cross product of the `vecxz` vector and the
x-axis.

These components are specified in the global-coordinate system $X$,$Y$,$Z$
and define a vector that is in a plane parallel to the $x-z$ plane of the
local-coordinate system.</p>
<p>These items need to be specified for the three-dimensional
problem.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">dXi dYi dZi</code></p></td>
<td><p>joint offset values -- offsets specified with respect to the
global coordinate system for element-end node i (optional, the number of
arguments depends on the dimensions of the current model).</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">dXj dYj dZj</code></p></td>
<td><p>joint offset values -- offsets specified with respect to the
global coordinate system for element-end node j (optional, the number of
arguments depends on the dimensions of the current model).</p></td>
</tr>
</tbody>
</table>

## Examples

<figure>
<img src="/OpenSeesRT/contrib/static/ElementCrossSection.png" alt="ElementCrossSection.png" />
<figcaption aria-hidden="true">Element cross section</figcaption>
</figure>

<figure>
  <img src="/OpenSeesRT/contrib/static/ElementOrientation.png" alt="ElementOrientation.png" />
  <figcaption aria-hidden="true">Element orientation</figcaption>
</figure>

<figure>
  <img src="/OpenSeesRT/contrib/static/ElementVectors.png" alt="ElementVectors.png" />
  <figcaption aria-hidden="true">Element vectors</figcaption>
</figure>

```tcl
# Element 1 : tag 1 : vecxZ = zaxis

geomTransf Linear 1 0 0 -1

# Element 2 : tag 2 : vecxZ = y axis

geomTransf Linear 2 0 1 0

# If there was a rigid offset at the top of element 1:

geomTransf Linear 1 0 0 -1 -jntOffset 0.0 0.0 0.0 0.0 -$Offset 0.0
```

<p>Code Developed by: <span style="color:blue"> Remo Magalhaes de Souza
</span></p>

<p>Images Developed by: <span style="color:blue"> Silvia Mazzoni
</span></p>

# MultiLinear

<p>This command is used to construct a uniaxial multilinear material
object.</p>

:::{apidoc="opensees.uniaxial.Multilinear"}
:::

```tcl
uniaxialMaterial MultiLinear $matTag $u1 $f1 $u2 $f2 $u3
        $f3 $u4 $f4 ...
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">u1 f1</code></p></td>
<td><p>strain and stress (or deformation &amp; force) at first point of
the envelope</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">u2 f2</code></p></td>
<td><p>strain and stress (or deformation &amp; force) at second point of
the envelope</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">u3 f3</code></p></td>
<td><p>strain and stress (or deformation &amp; force) at third point of
the envelope</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">u4 f4</code></p></td>
<td><p>strain and stress (or deformation &amp; force) at fourth point of
the envelope</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/MultiLinear_Material2.png" title="MultiLinear_Material2.png"
alt="MultiLinear_Material2.png" />
<figcaption aria-hidden="true">MultiLinear_Material2.png</figcaption>
</figure>
<p>MultiLinear Material -- Hysteretic Behavior</p>

<hr />

<p>Code Developed by: <span style="color:blue"> Frank Mckenna, UC Berkeley </span></p>
<p>Images Developed by: <span style="color:blue"> Vesna Terzic</span></p>

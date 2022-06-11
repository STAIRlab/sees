# Series

<p>This command is used to construct a series material object made up of
an arbitrary number of previously-constructed UniaxialMaterial
objects.</p>

```tcl
uniaxialMaterial Series $matTag $tag1 $tag2...
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><code>tag1 tag2 ...</code></p></td>
<td><p>identification tags of materials making up the material
model</p></td>
</tr>
</tbody>
</table>

<p>The series material is represented graphically: <img
src="/OpenSeesRT/contrib/static/SeriesMaterial.gif" title="SeriesMaterial.gif"
alt="SeriesMaterial.gif" /></p>

<p>In a series model, stresses are equal and strains and flexibilities
are additive: <img src="/OpenSeesRT/contrib/static/SeriesMaterialExample.gif"
title="SeriesMaterialExample.gif" alt="SeriesMaterialExample.gif" /></p>
<hr />
<p>Code Developed by: <span style="color:blue"> Micheal Scott,
Oregon State University</span></p>
<p>Images Developed by: <span style="color:blue"> Silvia Mazzoni
</span></p>


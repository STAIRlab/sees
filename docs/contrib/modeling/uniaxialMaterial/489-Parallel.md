# Parallel

<p>This command is used to construct a parallel material object made up
of an arbitrary number of previously-constructed UniaxialMaterial
objects.</p>

```tcl
uniaxialMaterial Parallel $matTag $tag1 $tag2 ...
        < -factors $fact1 $fact2 ... >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code>tag1 tag2 ...</code></td>
<td><p>identification tags of materials making up the material
model</p></td>
</tr>
<tr class="odd">
<td><p><code>fact1 fact2 ...</code></p></td>
<td><p>factors to create a linear combination of the specified
materials. Factors can be negative to subtract one material from an
other. (optional, default = 1.0)</p></td>
</tr>
</tbody>
</table>

The parallel material is represented graphically: 

<img
src="/OpenSeesRT/contrib/static/ParallelMaterial.gif" title="ParallelMaterial.gif"
alt="ParallelMaterial.gif" />

<p>In a parallel model, strains are equal and stresses and stiffnesses
are additive: <img src="/OpenSeesRT/contrib/static/ParallelMaterialExample.gif"
title="ParallelMaterialExample.gif"
alt="ParallelMaterialExample.gif" /></p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
<p>Images Developed by: <span style="color:blue"> Silvia Mazzoni
</span></p>


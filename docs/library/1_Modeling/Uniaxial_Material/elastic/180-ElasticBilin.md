# ElasticBilin

<p>This command is used to construct an elastic bilinear uniaxial
material object. Unlike all other bilinear materials, the unloading
curve follows the loading curve exactly.</p>

:::{apidoc="opensees.uniaxial.ElasticBilin"}
```tcl
uniaxialMaterial ElasticBilin $matTag $EP1 $EP2 $epsP2
        < $EN1 $EN2 $epsN2 >
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">EP1</code></p></td>
<td><p>tangent in tension for stains: 0 &lt;= strains &lt;=
<code>epsP2</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">EP2</code></p></td>
<td><p>tangent when material in tension with strains 
<code>epsP2</code></p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">epsP2</code></p></td>
<td><p>strain at which material changes tangent in tension.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">EN1</code></p></td>
<td><p>optional, default = <code>EP1</code>. tangent in compression for stains: 0
&lt; strains &lt;= <code>epsN2</code></p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">EN2</code></p></td>
<td><p>optional, default = <code>EP2</code>. tangent in compression with strains
&lt; $epsN2</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">epsN2</code></p></td>
<td><p>optional, default = -epsP2. strain at which material changes
tangent in compression.</p></td>
</tr>
</tbody>
</table>
:::
<figure>
<img src="/OpenSeesRT/contrib/static/ElasticPP.gif" title="ElasticPP.gif" alt="ElasticPP.gif" />
<figcaption aria-hidden="true">ElasticPP.gif</figcaption>
</figure>
<p>NOTE:</p>
<p>eps0 can not be controlled. It is always zero.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

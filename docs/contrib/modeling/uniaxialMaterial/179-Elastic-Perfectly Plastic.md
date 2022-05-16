# Elastic-Perfectly Plastic

<p>This command is used to construct an elastic perfectly-plastic
uniaxial material object.</p>

```tcl
uniaxialMaterial ElasticPP $matTag $E $epsyP < $epsyN $eps0 >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E</code></td>
<td><p>tangent</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsyP</code></td>
<td><p>strain or deformation at which material reaches plastic state in
tension</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">epsyN</code></td>
<td><p>strain or deformation at which material reaches plastic state in
compression.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>(optional, default is tension value)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">eps0</code></td>
<td><p>initial strain (optional, default: zero)</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/ElasticPP.gif" title="ElasticPP.gif" alt="ElasticPP.gif" />
<figcaption aria-hidden="true">ElasticPP.gif</figcaption>
</figure>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

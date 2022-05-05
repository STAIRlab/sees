# Elastic-Perfectly Plastic Material

<p>This command is used to construct an elastic perfectly-plastic
uniaxial material object.</p>

```tcl
uniaxialMaterial ElasticPP $matTag $E $epsyP &lt;$epsyN
        $eps0&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$E</strong></p></td>
<td><p>tangent</p></td>
</tr>
<tr class="odd">
<td><p><strong>$epsyP</strong></p></td>
<td><p>strain or deformation at which material reaches plastic state in
tension</p></td>
</tr>
<tr class="even">
<td><p><strong>$epsyN</strong></p></td>
<td><p>strain or deformation at which material reaches plastic state in
compression.</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>(optional, default is tension value)</p></td>
</tr>
<tr class="even">
<td><p><strong>$eps0</strong></p></td>
<td><p>initial strain (optional, default: zero)</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="ElasticPP.gif" title="ElasticPP.gif" alt="ElasticPP.gif" />
<figcaption aria-hidden="true">ElasticPP.gif</figcaption>
</figure>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

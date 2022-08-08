# FluidSolidPorousMaterial

<strong>FluidSolidPorousMaterial</strong> couples the responses of
two phases: fluid and solid. The fluid phase response is only volumetric
and linear elastic. The solid phase can be any NDMaterial. This material
is developed to simulate the response of saturated porous media under
fully undrained condition.

<p>OUTPUT INTERFACE:</p>
The following information may be extracted for this material at given
integration point, using the OpenSees Element Recorder facility (McKenna
and Fenves 2001): <strong>"stress"</strong>, <strong>"strain"</strong>,
<strong>"tangent"</strong>, or <strong>"pressure"</strong>. The
<strong>"pressure"</strong> option records excess pore pressure and
excess pore pressure ratio at a given material integration point.

```tcl
nDMaterial FluidSolidPorousMaterial $tag $nd $soilMatTag
        $combinedBulkModul < $pa=101 >
```
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">Tag</code></td>
<td><p>A positive integer uniquely identifying the element among all
elements</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">nd</code></td>
<td><p>Number of dimensions, 2 for plane-strain, and 3 for general 3D
analysis.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">soilMatTag</code></td>
<td><p>The material number for the solid phase material (previously
defined).</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">combinBulkModul</code></td>
<td><p>Combined undrained bulk modulus B<sub>c</sub>
relating changes in pore pressure and volumetric strain, may be
approximated by:</p>
<p>B<sub>c</sub> &amp;asymp; B<sub>f</sub>
/n</p>
<p>where B<sub>f</sub> is the bulk modulus of fluid phase
(2.2x10<sup>6</sup> kPa (or 3.191x10<sup>5</sup>
psi) for water), and n the initial porosity.</p></td>
</tr>
<tr class="odd">
<td><p><strong>`p`<sub>a</sub></strong></p></td>
<td><p>Optional atmospheric pressure for normalization (typically 101
kPa in SI units, or 14.65 psi in English units)</p></td>
</tr>
</tbody>
</table>

## Notes
1. Buoyant unit weight (total unit weight - fluid unit weight) should
   be used in definition of the finite elements composed of a
   <strong>FluidSolidPorousMaterial</strong>.
2. During the application of gravity (elastic) load, the fluid phase
   does not contribute to the material response.

<h2 id="fluid_solid_porous_material_examples"><strong>Fluid Solid Porous
Material Examples:</strong></h2>
<table border=1 width=800>
<tr><td colspan=2 align="center"><b>Pressure Dependent Material in saturated, undrained elastic-plastic state
(coupled with FluidSolidPorous Material)</b></td></p>
<p></tr> <tr> <td><a
href="PressureDependMultiYield-Example_8" title="wikilink">Example
1</a></td> <td>Single quadrilateral element, subjected to
sinusoidal base shaking</td> </tr> <tr> <td><a
href="PressureDependMultiYield-Example_9" title="wikilink">Example
2</a></td></p>
<p><td>Single quadrilateral element, subjected to monotonic
pushover</td> </tr> <tr> <td><a
href="PressureDependMultiYield-Example_10" title="wikilink">Example
3</a></td> <td>Single quadrilateral element (inclined by 4
degrees), subjected to msinusoidal base shaking</td> </tr>
<tr></p>
<p><td><a href="PressureDependMultiYield-Example_11"
title="wikilink">Example 4</a></td> <td>Single 3D BbarBrick
element, subjected to sinusoidal base shaking</td> </tr>
<tr> <td><a href="PressureDependMultiYield-Example_12"
title="wikilink">Example 5</a></td> <td>Single 3D BbarBrick
element (inclined by 4 degrees), subjected to sinusoidal base
shaking</td> </tr></p>
<p><tr> <td><a href="PressureDependMultiYield--Example_13"
title="wikilink">Example 6</a></td> <td>A column of
quadrilateral element (inclined by 4 degrees), subjected to sinusoidal
base shaking</td> </tr></p>
</table>

<hr />
<p>Code developed by: <span style="color:blue"> UC San Diego (Dr. Zhaohui Yang)</span>:</p>



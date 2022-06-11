# FluidSolidPorousMaterial

<p><strong>FluidSolidPorousMaterial</strong> couples the responses of
two phases: fluid and solid. The fluid phase response is only volumetric
and linear elastic. The solid phase can be any NDMaterial. This material
is developed to simulate the response of saturated porous media under
fully undrained condition.</p>
<p>OUTPUT INTERFACE:</p>
<p>The following information may be extracted for this material at given
integration point, using the OpenSees Element Recorder facility (McKenna
and Fenves 2001): <strong>"stress"</strong>, <strong>"strain"</strong>,
<strong>"tangent"</strong>, or <strong>"pressure"</strong>. The
<strong>"pressure"</strong> option records excess pore pressure and
excess pore pressure ratio at a given material integration point.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDMaterial FluidSolidPorousMaterial $tag $nd $soilMatTag
$combinedBulkModul &lt;$pa=101&gt;</strong></p></td>
</tr>
</tbody>
</table>
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
<td><p>Combined undrained bulk modulus B&lt;sub&gt;c&lt;/sub&gt;
relating changes in pore pressure and volumetric strain, may be
approximated by:</p>
<p>B&lt;sub&gt;c&lt;/sub&gt; &amp;asymp; B&lt;sub&gt;f&lt;/sub&gt;
/n</p>
<p>where B&lt;sub&gt;f&lt;/sub&gt; is the bulk modulus of fluid phase
(2.2x10&lt;sup&gt;6&lt;/sup&gt; kPa (or 3.191x10&lt;sup&gt;5&lt;/sup&gt;
psi) for water), and n the initial porosity.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$p&lt;sub&gt;a&lt;/sub&gt;</strong></p></td>
<td><p>Optional atmospheric pressure for normalization (typically 101
kPa in SI units, or 14.65 psi in English units)</p></td>
</tr>
</tbody>
</table>
<p><strong>NOTE:</strong></p>
<p>1. Buoyant unit weight (total unit weight - fluid unit weight) should
be used in definition of the finite elements composed of a
<strong>FluidSolidPorousMaterial</strong>.</p>
<p>2. During the application of gravity (elastic) load, the fluid phase
does not contribute to the material response.</p>
<h2 id="fluid_solid_porous_material_examples"><strong>Fluid Solid Porous
Material Examples:</strong></h2>
<p>&lt;table border=1 width=800&gt;</p>
<p>&lt;tr&gt; &lt;td colspan=2 align=center &gt;&lt;b&gt;Pressure
Dependent Material in saturated, undrained elastic-plastic state
(coupled with FluidSolidPorous Material)&lt;/b&gt;&lt;/td&gt;</p>
<p>&lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-Example_8" title="wikilink">Example
1</a>&lt;/td&gt; &lt;td&gt;Single quadrilateral element, subjected to
sinusoidal base shaking&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-Example_9" title="wikilink">Example
2</a>&lt;/td&gt;</p>
<p>&lt;td&gt;Single quadrilateral element, subjected to monotonic
pushover&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield-Example_10" title="wikilink">Example
3</a>&lt;/td&gt; &lt;td&gt;Single quadrilateral element (inclined by 4
degrees), subjected to msinusoidal base shaking&lt;/td&gt; &lt;/tr&gt;
&lt;tr&gt;</p>
<p>&lt;td&gt;<a href="PressureDependMultiYield-Example_11"
title="wikilink">Example 4</a>&lt;/td&gt; &lt;td&gt;Single 3D BbarBrick
element, subjected to sinusoidal base shaking&lt;/td&gt; &lt;/tr&gt;
&lt;tr&gt; &lt;td&gt;<a href="PressureDependMultiYield-Example_12"
title="wikilink">Example 5</a>&lt;/td&gt; &lt;td&gt;Single 3D BbarBrick
element (inclined by 4 degrees), subjected to sinusoidal base
shaking&lt;/td&gt; &lt;/tr&gt;</p>
<p>&lt;tr&gt; &lt;td&gt;<a href="PressureDependMultiYield--Example_13"
title="wikilink">Example 6</a>&lt;/td&gt; &lt;td&gt;A column of
quadrilateral element (inclined by 4 degrees), subjected to sinusoidal
base shaking&lt;/td&gt; &lt;/tr&gt;</p>
<p>&lt;/table&gt;</p>
<p>Code Developed by: <span style="color:blue"> UC San Diego (Dr.
Zhaohui Yang)</span>:</p>
<hr />
<p>UC San Diego Soil Model: </p>

 # TzLiq1

<p>The command constructs a uniaxial t-z material that incorporates
liquefaction effects. This t z material is used with a zeroLength
element to connect a pile (beam-column element) to a 2 D plane-strain FE
mesh. The t-z material obtains the average mean effective stress (which
decreases with increasing excess pore pressure) from two specified soil
elements. Currently, the implementation requires that the specified soil
elements consist of FluidSolidPorousMaterials in FourNodeQuad
elements.</p>

```tcl
uniaxialMaterial TzLiq1 $matTag $tzType $tult $z50 $c
        $ele1 $ele2
```
<p>OR</p>

```tcl
uniaxialMaterial TzLiq1 $matTag $tzType $tult $z50 $c
        -timeSeries $seriesTag
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">soilType</code></td>
<td><p>soilType = 1 Backbone of t-z curve approximates Reese and O'Neill
(1987).</p>
<p>soilType = 2 Backbone of t-z curve approximates Mosher (1984)
relation.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">tult</code></td>
<td><p>Ultimate capacity of the t-z material. SEE NOTE 1.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Z50</code></p></td>
<td><p>Displacement at which 50% of tult is mobilized in monotonic
loading.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">c</code></td>
<td><p>The viscous damping term (dashpot) on the far-field (elastic)
component of the displacement rate (velocity).</p></td>
</tr>
<tr class="even">
<td><p><strong>$ele1 $ele2</strong></p></td>
<td><p>are the eleTag (element numbers) for the two solid elements from
which PyLiq1 will obtain mean effective stresses and excess pore
pressures</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">seriesTag</code></td>
<td><p>Alternatively, mean effective stress can be supplied by a time
series by specifying the text string -timeSeries and the tag of the
seriesm $seriesTag.</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<ol>
<li>The argument tult is the ultimate capacity of the t-z material. Note
that “t” or “tult” are shear</li>
</ol>
<p>stresses [force per unit area of pile surface] in common design
equations, but are both loads for this uniaxialMaterial [i.e., shear
stress times the tributary area of the pile].</p>
<ol>
<li>Nonzero c values are used to represent radiation damping
effects</li>
<li>To model the effects of liquefaction with TzLiq1, it is necessary to
use the material stage updating command:</li>
</ol>
<p>&lt;pre&gt; updateMaterialStage -material matNum -stage sNum
&lt;/pre&gt;</p>
<p>where the argument matNum is the material number (for TzLiq1) and the
argument sNum is the desired stage (valid values are 0 &amp; 1). With
sNum=0, the TzLiq1 behavior will be independent of any pore pressure in
the specified solidElem’s. When updateMaterialStage first sets sNum=1,
TzLiq1 will obtain the average mean effective stress in the two
solidElem’s and treat it as the initial consolidation stress prior to
undrained loading. Thereafter, the behavior of TzLiq1 will depend on the
mean effective stress (and hence excess pore pressures) in the
solidElem’s. The default value of sNum is 0 (i.e., sNum=0 if
updateMaterialStage is not called). Note that the updateMaterialStage
command is used with some soil material models, and that sNum=0
generally corresponds to the application of gravity loads (e.g., elastic
behavior with no excess pore pressure development) and sNum=1 generally
corresponds to undrained loading (e.g., plastic behavior with excess
pore pressures development).</p>
<p>The analysis for gravity loading cannot use the "algorithm Linear"
command because the relevant soil materials do not currently work
properly with this command. Instead, the "algorithm Newton" or some
other option must be used.</p>
<p>TzLiq1 inherits TzSimple1 and modifies its response based on the mean
effective stresses (and hence excess pore pressures) in the specified
solid soil elements. The logic and implementation are the same as for
how PyLiq1 inherits and modifies PySimple1. Therefore, the reader is
referred to the documentation of PyLiq1 for details.</p>

## Examples

<p>REFERENCES:</p>
<p>"Seismic Soil-pile-strcture interaction experiments and analysis",
Boulanger, R.W., Curras, C.J., Kutter, B.L., Wilson, D.W., and Abghari,
A. (1990). Jornal of Geotechnical and Geoenvironmental Engineering,
ASCS, 125(9):750-759.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Ross Boulanger, UC
Davis </span></p>

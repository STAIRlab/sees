# ElasticTubularJoint Element

<p>This command is used to construct an ElasticTubularJoint element
object, which models joint flexibility of tubular joints in two
dimensional analysis of any structure having tubular joints.</p>

```tcl
element ElasticTubularJoint $Tag $iNode $jNode
        $Brace_Diameter $Brace_Angle $E $Chord_Diameter $Chord_Thickness
        $Chord_Angle
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">Tag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">iNode</code></td>
<td><p>first end node- it is always located on the chord axis</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">jNode</code></td>
<td><p>second end node - it is always located on the chord wall</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Brace_Diameter</code></td>
<td><p>outer diameter of brace</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Brace_Angle</code></td>
<td><p>angle between brace and chord axis 0 &lt; Brace_Angle &lt;
90</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E</code></td>
<td><p>Young's Modulus</p></td>
</tr>
<tr class="odd">
<td><p><strong>$ Chord_Diameter</strong></p></td>
<td><p>outer diameter of chord</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Chord_Thickness</code></td>
<td><p>thickness of chord</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Chord_Angle</code></td>
<td><p>angle between chord axis and global x-axis 0 &lt; Chord_Angle
&lt; 180</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>EXAMPLE:</p>
<p>element ElasticTubularJoint 1 1 2 0.25 45 210E+09 0.5 0.016 45 #
Tubular joint having tag 1 which interconnects nodes 1 and 2; brace
diameter is 25cm; intersection angle is 45 degrees; Young's modulus of
the material used is 210e9; outer diameter and thickness of the chord
are 50 cm and 1.6 cm respectively; angle between chord axis and global
horizontal axis is 45 degrees.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> M. Kia and P.
Alanjari, Sharif University of Technology and K. N. Toosi University of
Technology, Tehran, Iran. </span></p>

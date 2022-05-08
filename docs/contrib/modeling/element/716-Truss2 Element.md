# Truss2 Element

<p>This command is used to construct a Truss2 or CorotTruss2 element
object, a biaxial truss element designed to be used in conjunction with
the <strong><a href="ConcretewBeta_Material" title="wikilink">
ConcretewBeta</a></strong> material for accounting for biaxial effects
in a uniaxial element.</p>
<p>Truss:</p>

```tcl
element Truss2 $eleTag $iNode $jNode $mGNode $nGNode $A
        $matTag &lt;-rho $rho&gt; &lt;-rayleigh $rflag&gt;
```
<p>Corotational Truss:</p>

```tcl
element CorotTruss2 $eleTag $iNode $jNode $mGNode $nGNode
        $A $matTag &lt;-rho $rho&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>end nodes of the truss element</p></td>
</tr>
<tr class="odd">
<td><p><strong>$mGNode $nGNode</strong></p></td>
<td><p>end nodes for the zero-stiffness gauge element</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">A</code></td>
<td><p>cross-sectional area of truss element</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tag of material used (see Note 1)</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>Optional:</p></td>
<td></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>mass per unit length, as in the <strong><a href="Truss_Element"
title="wikilink"> Truss</a></strong> and <strong><a
href="Corotational_Truss_Element" title="wikilink">
CorotTruss</a></strong> Elements (default = 0.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rFlag</code></td>
<td><p>flag for Rayleigh damping, as in the <strong><a
href="Truss_Element" title="wikilink"> Truss</a></strong> Element
(default = 0; see Note 2)</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<p>(1) If the material used does not use biaxial effects, the element
will behave like the uniaxial counterpart (<strong><a
href="Truss_Element" title="wikilink">Truss</a></strong> or <strong><a
href="Corotational_Truss_Element" title="wikilink">
CorotTruss</a></strong>). For the <strong><a
href="ConcretewBeta_Material" title="wikilink">
ConcretewBeta</a></strong> material, the normal strain will be passed to
the material to be used in calculation of the material response.</p>
<p>(2) Consistent with the implementation of the <strong><a
href="Truss_Element" title="wikilink"> Truss</a></strong> element, the
Truss2 element does not include Rayleigh damping by default. Rayleigh
damping can be included by using the -rayleigh option with
<code class="tcl-variable">rFlag</code> = 1.</p>
<p>However, like the <strong><a href="Corotational_Truss_Element"
title="wikilink"> CorotTruss</a></strong> element, the CorotTruss2
element includes the Rayleigh damping by default so the -rayleigh option
is not available to the CorotTruss2 element.</p>
<p>(3) At this time, there is no trussSection equivalent implementation
of these biaxial trusses.</p>
<h2 id="implementation">Implementation</h2>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="File:Truss2_Eq1.png"
title="wikilink">thumb|upright=1.5|Equation 1.</a>
</dd>
</dl>
</dd>
</dl>
<p>The above figure shows the layout of the truss and zero-stiffness
gauge elements that make up the Truss2 Element object. The truss element
part behaves identically to the <strong><a href="Truss_Element"
title="wikilink"> Truss</a></strong> Element object (or the <strong><a
href="Corotational_Truss_Element" title="wikilink">
CorotTruss</a></strong> Element object for the case of CorotTruss2).</p>
<p>The zero-stiffness gauge element is used to measure the strain in the
direction of the gauge. The strain in the direction normal to the truss
element is described by Equation 1, where
<em>&amp;epsilon;&lt;sub&gt;truss&lt;/sub&gt;</em> is the strain
calculated in the truss element,
<em>&amp;epsilon;&lt;sub&gt;gauge&lt;/sub&gt;</em> is the strain
calculated in the gauge element, and
<em>&amp;theta;&lt;sub&gt;g&lt;/sub&gt;</em> is the angle between the
truss and gauge elements. It is suggested to make
<em>&amp;theta;&lt;sub&gt;g&lt;/sub&gt;</em> as close to 90&amp;deg; as
possible.</p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
<a href="File:Truss2_Fig1.png"
title="wikilink">thumb|center|upright=2.5|alt=Truss2 Figure 1 |Figure 1.
Truss2 truss and gauge element layout based on input node values.</a>
</dd>
</dl>
</dd>
</dl>
<h2 id="references">References</h2>
<p>Lu, Y., and Panagiotou, M. (2013). “Three-Dimensional Nonlinear
Cyclic Beam-Truss Model for Reinforced Concrete Non-Planar Walls.”
Journal of Structural Engineering, published online.</p>
<p>Panagiotou, M., Restrepo, J.I., Schoettler, M., and Kim G. (2012).
"Nonlinear cyclic truss model for reinforced concrete walls." ACI
Structural Journal, 109(2), 205-214.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Yuan Lu, UC
Berkeley </span> and <span style="color:blue"> Marios
Panagiotou, UC Berkeley </span></p>

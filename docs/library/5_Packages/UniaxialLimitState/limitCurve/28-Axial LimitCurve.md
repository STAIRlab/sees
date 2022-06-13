# Axial LimitCurve

<p>This command is used to construct an axial limit curve object that is
used to define the point of axial failure for a LimitStateMaterial
object. Point of axial failure based on model from Chapter 3 of PEER
2003/01 report. After axial failure the response of LimitStateMaterial
is forced to follow axial limit curve.</p>

```tcl
limitCurve Axial $curveTag $eleTag $Fsw $Kdeg $Fres
        $defType $forType &lt;$ndI $ndJ $dof $perpDirn
        $delta&gt;
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">curveTag</code></td>
<td><p>unique LimitCurve tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>integer element tag for the associated beam-column
element</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Fsw</code></td>
<td><p>floating point value describing the amount of transverse
reinforcement &lt;math&gt;(F_{sw} =
\frac{A_{st}f_{yt}d_c}{s})&lt;/math&gt;</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Kdeg</code></td>
<td><p>floating point value for the slope of the third branch in the
post-failure backbone, assumed to be negative (see Figure 4-6)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Fres</code></td>
<td><p>floating point value for the residual force capacity of the
post-failure backbone (see Figure 4-6)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">defType</code></td>
<td><p>integer flag for type of deformation defining the abscissa of the
limit curve</p>
<p>1 = maximum beam-column chord rotations</p>
<p>2 = drift based on displacment of nodes ndI and ndJ</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">forType</code></td>
<td><p>nteger flag for type of force defining the ordinate of the limit
curve. See NOTES 1.</p>
<p>0 = force in associated limit state material</p>
<p>1 = shear in beam-column element</p>
<p>2 = axial load in beam-column element</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ndI</code></td>
<td><p>nteger node tag for the first associated node (normally node I of
$eleTag beam-column element)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ndJ</code></td>
<td><p>integer node tag for the second associated node (normally node J
of $eleTag beam-column element)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dof</code></td>
<td><p>nodal degree of freedom to monitor for drift. See NOTES
2</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">perpDirn</code></td>
<td><p>perpendicular global direction from which length is determined to
compute drift. See Notes 2.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">delta</code></td>
<td><p>drift (floating point value) used to shift axial limit
curve</p></td>
</tr>
</tbody>
</table>
<p>NOTES:</p>
<ol>
<li>Options 1 and 2 assume no member loads</li>
<li>1 = X, 2 = Y, 3 = Z</li>
</ol>
<hr />

## Examples

<p>&lt;tcl&gt;CenterColAxialSpring.tcl&lt;/tcl&gt;</p>
<hr />
<p>DESCRIPTION:</p>
<p>Modeling Failures in Existing Reinforced Concrete Columns by Ken
Elwood: <a href="file:ElwoodCJCE2004.pdf"
title="wikilink">file:ElwoodCJCE2004.pdf</a></p>
<hr />
## References
<p>Elwood, K.J and Moehle, J.P., "Shake Table Tests and Analystical
Studies on the Gravity Load Collapse of Reinforced Concrete Frames",
Pacific Earthquake Engineering Research Center, University of
California, Berkeley, CA. PEER 2003/01.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Ken Elwood,
University of British Columbia</span></p>

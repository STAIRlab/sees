 # CastFuse

<p>This command is used to construct a CastFuse uniaxial material. The
CastFuse material simulates the hysteretic response a cast yielding fuse
(CSF) for concentrically braced frames. The details of a CSF-brace are
discussed in Gray et al. [1,2]. Isotropic hardening is modeled with the
rules developed by Filippou et al. [3].</p>

```tcl
uniaxialMaterial Cast $matTag $n $bo $h $fy $E $L $b $Ro
        $cR1 $cR2 &lt;$a1 $a2 $a3 $a4&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">n</code></td>
<td><p>Number of yield fingers of the CSF-brace</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">bo</code></td>
<td><p>Width of an individual yielding finger at its base of the
CSF-brace</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">h</code></td>
<td><p>Thickness of an individual yielding finger</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fy</code></td>
<td><p>Yield strength of the steel material of the yielding
finger</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E</code></td>
<td><p>Modulus of elasticity of the steel material of the yielding
finger</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">L</code></td>
<td><p>Height of an individual yielding finger</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">b</code></td>
<td><p>Strain hardening ratio</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Ro</code></td>
<td><p>Parameter that controls the Bauschinger effect. Recommended
Values for $Ro=between 10 to 30</p></td>
</tr>
<tr class="even">
<td><p><strong>$cR1</strong></p></td>
<td><p>Parameter that controls the Bauschinger effect. Recommended Value
$cR1=0.925</p></td>
</tr>
<tr class="odd">
<td><p><strong>$cR2</strong></p></td>
<td><p>Parameter that controls the Bauschinger effect. Recommended Value
$cR2=0.150</p></td>
</tr>
<tr class="even">
<td><p><strong>$a1</strong></p></td>
<td><p>isotropic hardening parameter, increase of compression yield
envelope as proportion of yield strength after a plastic deformation of
$a2*(P&lt;sub&gt;p&lt;/sub&gt;/K&lt;sub&gt;p&lt;/sub&gt;)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$a2</strong></p></td>
<td><p>isotropic hardening parameter (see explanation under $a1).
(optional default = 1.0)</p></td>
</tr>
<tr class="even">
<td><p><strong>$a3</strong></p></td>
<td><p>isotropic hardening parameter, increase of tension yield envelope
as proportion of yield strength after a plastic deformation of
$a4*(P&lt;sub&gt;p&lt;/sub&gt;/K&lt;sub&gt;p&lt;/sub&gt;)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$a4</strong></p></td>
<td><p>isotropic hardening parameter (see explanation under $a3).
(optional default = 1.0)</p></td>
</tr>
</tbody>
</table>
<hr />
<table>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><p>Gray et al. [1] showed that the monotonic backbone curve of a
CSF-brace with known properties (n, b&lt;sub&gt;o&lt;/sub&gt;, h, L, fy,
E) after yielding can be expressed as a close-form solution that is
given by,</p></td>
</tr>
<tr class="odd">
<td><p>P = P&lt;sub&gt;p&lt;/sub&gt;/cos(2d/L), in which d is the axial
deformation of the brace at increment i and P&lt;sub&gt;p&lt;/sub&gt; is
the yield strength of the CSF-brace and is given by the following
expression</p></td>
</tr>
<tr class="even">
<td><p>P&lt;sub&gt;p&lt;/sub&gt; =
nb&lt;sub&gt;o&lt;/sub&gt;h&lt;sup&gt;2&lt;/sup&gt;f&lt;sub&gt;y&lt;/sub&gt;/4L</p></td>
</tr>
<tr class="odd">
<td><p>The elastic stiffness of the CSF-brace is given by,</p></td>
</tr>
<tr class="even">
<td><p>K&lt;sub&gt;p&lt;/sub&gt; =
nb&lt;sub&gt;o&lt;/sub&gt;Eh&lt;sup&gt;3&lt;/sup&gt;f&lt;sub&gt;y&lt;/sub&gt;/6L&lt;sup&gt;3&lt;/sup&gt;</p></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>Examples:</strong></p>
<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
</tbody>
</table>
<hr />
<p><strong>References</strong>:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>[1]</strong></p></td>
<td><p>Gray, M.G., Christopoulos, C., Packer, J.A., (2010). "Cast Steel
Yielding Fuse for Concentrically Braced Frames," Proceedings of the 9th
U.S. National and 10th Canadian Conference on Earthquake Engineering,
July 25-29, 2010, Toronto, Ontario, Canada, paper No. 595.</p></td>
</tr>
<tr class="even">
<td><p><strong>[2]</strong></p></td>
<td><p>Gray, M.G., Christopoulos, C., Packer, J.A., Lignos, D.G. (2012).
"Development, Validation and Modeling of the New Cast Steel Yielding
Brace System,” Proceedings ASCE Structures Congress, March 29th-31st,
Chicago, IL, USA, SEI institute.</p></td>
</tr>
<tr class="odd">
<td><p><strong>[3]</strong></p></td>
<td><p>Filippou, F. C., Popov, E. P., Bertero, V. V. (1983). "Effects of
Bond Deterioration on Hysteretic Behavior of Reinforced Concrete
Joints," Report EERC 83-19, Earthquake Engineering Research Center,
University of California, Berkeley.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Code Developed by : <span style="color:blue"> by Dr. Dimitrios
G. Lignos, (McGill University) </span></p>

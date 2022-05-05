# SAWS Material

<p>This file contains the class definition for SAWSMaterial.
SAWSMaterial provides the implementation of a one-dimensional hysteretic
model develeped as part of the CUREe Caltech wood frame project.</p>

```tcl
uniaxialMaterial SAWS $tag $F0 $FI $DU $S0 $R1 $R2 $R3
        $R4 $alph $beta
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><strong>$matTag</strong></p></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><p><strong>$F0</strong></p></td>
<td><p>Intercept strength of the shear wall spring element for the
asymtotic line to the envelope curve F0 &gt; FI &gt; 0</p></td>
</tr>
<tr class="odd">
<td><p><strong>$FI</strong></p></td>
<td><p>Intercept strength of the spring element for the pinching branch
of the hysteretic curve. (FI &gt; 0).</p></td>
</tr>
<tr class="even">
<td><p><strong>$DU</strong></p></td>
<td><p>Spring element displacement at ultimate load. (DU &gt;
0).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$S0</strong></p></td>
<td><p>Initial stiffness of the shear wall spring element (S0 &gt;
0).</p></td>
</tr>
<tr class="even">
<td><p><strong>$R1</strong></p></td>
<td><p>Stiffness ratio of the asymptotic line to the spring element
envelope curve. The slope of this line is R1 S0. (0 &lt; R1 &lt;
1.0).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$R2</strong></p></td>
<td><p>Stiffness ratio of the descending branch of the spring element
envelope curve. The slope of this line is R2 S0. ( R2 &lt; 0).</p></td>
</tr>
<tr class="even">
<td><p><strong>$R3</strong></p></td>
<td><p>Stiffness ratio of the unloading branch off the spring element
envelope curve. The slope of this line is R3 S0. ( R3 1).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$R4</strong></p></td>
<td><p>Stiffness ratio of the pinching branch for the spring element.
The slope of this line is R4 S0. ( R4 &gt; 0).</p></td>
</tr>
<tr class="even">
<td><p><strong>$alpha</strong></p></td>
<td><p>Stiffness degradation parameter for the shear wall spring
element. (ALPHA &gt; 0).</p></td>
</tr>
<tr class="odd">
<td><p><strong>$beta</strong></p></td>
<td><p>Stiffness degradation parameter for the spring element. (BETA
&gt; 0).</p></td>
</tr>
</tbody>
</table>
<h2 id="notes">Notes:</h2>
<p>Refer to the figure below for more information, and the reference
provided at the end of this page for complete details about modeling
assumptions.</p>
<figure>
<img src="FolzFigure.gif" title="FolzFigure.gif" alt="FolzFigure.gif" />
<figcaption aria-hidden="true">FolzFigure.gif</figcaption>
</figure>
<h2 id="example_files">Example Files:</h2>
<p><em>Click to download files</em></p>
<p><a href="Media:Test.tcl" title="wikilink">Media:Test.tcl</a></p>
<p><a href="Media:SAWSZeroLength.tcl"
title="wikilink">Media:SAWSZeroLength.tcl</a></p>
<h2 id="example_hysteresis">Example: Hysteresis</h2>
<figure>
<img src="TestHysteresis.jpg" title="TestHysteresis.jpg" width="700"
alt="TestHysteresis.jpg" />
<figcaption aria-hidden="true">TestHysteresis.jpg</figcaption>
</figure>
<h2 id="references">References</h2>
<p>Reference: Folz, B. and Filiatrault, A. (2001). "SAWS - Version 1.0,
A Computer Program for the Seismic Analysis of Woodframe Structures",
Structural Systems Research Project Report No. SSRP-2001/09, Dept. of
Structural Engineering, UCSD, La Jolla, CA .</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Patxi Uriz,
Exponent </span> (Converted from FORTRAN code originally written
by Bryan Folz)</p>

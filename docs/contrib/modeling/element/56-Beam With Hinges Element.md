# Beam With Hinges Element

<p>This command is used to construct a forceBeamColumn element object,
which is based on the non-iterative (or iterative) flexibility
formulation. The locations and weights of the element integration points
are based on so-called plastic hinge integration, which allows the user
to specify plastic hinge lenghts at the element ends. Two-point Gauss
integration is used on the element interior while two-point Gauss-Radau
integration is applied over lengths of 4LpI and 4LpJ at the element
ends, viz. "modified Gauss-Radau plastic hinge integration". A total of
six integration points are used in the element state determination (two
for each hinge and two for the interior).</p>
<p>Users may be familiar with the <strong>beamWithHinges</strong>
command format (see below); however, the format shown here allows for
the simple but important case of using a material nonlinear section
model on the element interior. The previous beamWithHinges command
constrained the user to an elastic interior, which often led to
unconservative estimates of the element resisting force when plasticity
spread beyond the plastic hinge regions in to the element interior.</p>
<p>The advantages of this new format over the previous
<strong>beamWithHinges</strong> command are</p>
<ul>
<li>Plasticity can spread beyond the plastic hinge regions</li>
<li>Hinges can form on the element interior, e.g., due to distributed
member loads</li>
</ul>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element forceBeamColumn $eleTag $iNode $jNode $transfTag
"HingeRadau $secTagI $LpI $secTagJ $LpJ $secTagInterior" &lt;-mass
$massDens&gt; &lt;-iter $maxIters $tol&gt;</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><p><strong>$eleTag</strong></p></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>$iNode $jNode</strong></p></td>
<td><p>nodes at element ends I and J, respectively</p></td>
</tr>
<tr class="odd">
<td><p><strong>$secTagI</strong></p></td>
<td><p>identifier for previously-defined section object at end
I</p></td>
</tr>
<tr class="even">
<td><p><strong>$LpI</strong></p></td>
<td><p>plastic hinge length at end I</p></td>
</tr>
<tr class="odd">
<td><p><strong>$secTagJ</strong></p></td>
<td><p>identifier for previously-defined section object at end
J</p></td>
</tr>
<tr class="even">
<td><p><strong>$LpJ</strong></p></td>
<td><p>plastic hinge length at end J</p></td>
</tr>
<tr class="odd">
<td><p><strong>$secTagInterior</strong></p></td>
<td><p>identifier for previously-defined section object on the element
interior (DOES NOT HAVE TO BE ELASTIC, but can be any type of section,
including fiber)</p></td>
</tr>
<tr class="even">
<td><p><strong>$transfTag</strong></p></td>
<td><p>identifier for previously-defined
coordinate-transformation</p></td>
</tr>
<tr class="odd">
<td><p><strong>$maxIters</strong></p></td>
<td><p>maximum number of iterations to undertake to satisfy element
compatibility (optional, default=1)</p></td>
</tr>
<tr class="even">
<td><p><strong>$tol</strong></p></td>
<td><p>tolerance for satisfaction of element compatibility (optional,
default=10-16)</p></td>
</tr>
</tbody>
</table>
<p>NOTE: The keyword <strong>HingeRadau</strong> can be changed to one
of the following in order to use a different hinge integration
approach:</p>
<ul>
<li><strong>HingeRadau</strong> -- two-point Gauss-Radau applied to the
hinge regions over 4LpI and 4LpJ (six element integration points)</li>
<li><strong>HingeRadauTwo</strong> -- two-point Gauss-Radau in the hinge
regions applied over LpI and LpJ (six element integration points)</li>
<li><strong>HingeMidpoint</strong> -- midpoint integration over the
hinge regions (four element integration points)</li>
<li><strong>HingeEndpoint</strong> -- endpoint integration over the
hinge regions (four element integration points)</li>
</ul>
<p>For more information on the behavior, advantages, and disadvantages
of these approaches to plastic hinge integration, see</p>
<p>Scott, M.H. and G.L. Fenves. "<a
href="http://dx.doi.org/10.1061/(ASCE)0733-9445(2006)132:2(244)">Plastic
Hinge Integration Methods for Force-Based Beam-Column Elements</a>",
Journal of Structural Engineering, 132(2):244-252, February 2006.</p>
<p>Scott, M.H. and K.L. Ryan. "<a
href="http://dx.doi.org/10.1193/1.4000136">Moment-Rotation Behavior of
Force-Based Plastic Hinge Elements</a>", Earthquake Spectra,
29(2):597-607, May 2013.</p>
<p>The primary advantages of <strong>HingeRadau</strong> are</p>
<ul>
<li>The user can specify a physically meaningful plastic hinge
length</li>
<li>The largest bending moment is captured at the element ends</li>
<li>The exact numerical solution is recovered for a linear-elastic
prismatic beam</li>
<li>The characteristic length is equal to the user-specified plastic
hinge length when deformations localize at the element ends</li>
</ul>
<p>while the primary disadvantages are</p>
<ul>
<li>The element post-yield response is too flexible for strain-hardening
section response (consider using <strong>HingeRadauTwo</strong>)</li>
<li>The user needs to know the plastic hinge length <em>a priori</em>
(empirical equations are available)</li>
</ul>
<p>NOTE: See the <strong><a href="Force-Based_Beam-Column_Element"
title="wikilink"> forceBeamColumn</a></strong> page for valid recorder
queries.</p>
<hr />
<p>Original command (maintained for backward compatibility)</p>
<p>NOTE: this form of the command forces the element interior to be
linear-elastic, which is not always the best approach.</p>
<p>For 2D:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element beamWithHinges $eleTag $iNode $jNode $secTagI
$Lpi $secTagJ $Lpj $E $A $Iz $transfTag &lt;-mass $massDens&gt;
&lt;-iter $maxIters $tol&gt;</strong></p></td>
</tr>
</tbody>
</table>
<p>For 3D:</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>element beamWithHinges $eleTag $iNode $jNode $secTagI
$Lpi $secTagJ $Lpj $E $A $Iz $Iy $G $J $transfTag &lt;-mass
$massDens&gt; &lt;-iter $maxIters $tol&gt;</strong></p></td>
</tr>
</tbody>
</table>
<p>All inputs are the same as above, with the following additional
inputs, which are used solely to create a "dummy" elastic section at the
two Gauss integration points of the element interior</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>$E</strong></p></td>
<td><p>Youngs modulus elastic portion</p></td>
</tr>
<tr class="even">
<td><p><strong>$A</strong></p></td>
<td><p>Area for elastic portion</p></td>
</tr>
<tr class="odd">
<td><p><strong>$Iz</strong></p></td>
<td><p>second moment of area for elastic portion about local z</p></td>
</tr>
<tr class="even">
<td><p><strong>$Iy</strong></p></td>
<td><p>second moment of area for elastic portion about local y</p></td>
</tr>
<tr class="odd">
<td><p><strong>$G</strong></p></td>
<td><p>torsional moment of inertia of cross section for elastic
portion</p></td>
</tr>
<tr class="even">
<td><p><strong>$J</strong></p></td>
<td><p>Shear Modulus of elastic portion.</p></td>
</tr>
</tbody>
</table>
<hr />
<p>Code maintained by: <a
href="http://web.engr.oregonstate.edu/~mhscott">Michael H. Scott, Oregon
State University</a></p>

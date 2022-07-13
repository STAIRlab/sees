# Bounding Cam Clay

This command is used to construct a multi-dimensional bounding
surface Cam Clay material object after Borja et al. (2001).

> The material formulations for the `BoundingCamClay` object are
> `ThreeDimensional` and `PlaneStrain`


```tcl
nDMaterial BoundingCamClay $matTag $massDensity $C
        $bulkMod $OCR $mu_o $alpha $lambda $h $m
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">massDensity</code></td>
<td><p>mass density</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">C</code></td>
<td><p>ellipsoidal axis ratio (defines shape of ellipsoidal
loading/bounding surfaces)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">bulkMod</code></td>
<td><p>initial bulk modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">OCR</code></td>
<td><p>overconsolidation ratio</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">mu_o</code></td>
<td><p>initial shear modulus</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>pressure-dependency parameter for modulii (greater than or equal
to zero)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">lambda</code></td>
<td><p>soil compressibility index for virgin loading</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">h</code></td>
<td><p>hardening parameter for plastic response inside of bounding
surface (if h = 0, no hardening)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">m</code></td>
<td><p>hardening parameter (exponent) for plastic response inside of
bounding surface (if m = 0, only linear hardening)</p></td>
</tr>
</tbody>
</table>

<hr />

<h2 id="general_information">General Information</h2>
<p>This nDMaterial object provides the bounding surface plasticity model
of Borja et al. (2001) in which the bounding surface model is
represented using modified Cam-Clay theory (Schofield and Wroth 1968).
In addition to the standard capabilities of the Cam-Clay family of
models (e.g., pressure dependence, hardening with plastic volumetric
contraction, softening with plastic dilation, and coupled deviatoric and
volumetric plastic deformation), the Borja et al. (2001) model has been
enhanced to include an anisotropic bounding surface formulation that
allows for consideration of hysteretic behaviour under cyclic loading.
This bounding surface Cam-Clay model is coupled with a nonlinear
hyperelastic model that considered pressure-dependency in the bulk and
shear modulus. The full theory of this model is discussed in great
detail in Borja et al. (2001).</p>
<h3 id="notes">Notes</h3>
<ul>
<li>The ellipsoidal axis ratio parameter $C is defined such that the
ellipsoidal surfaces are C times as wide in the deviatoric direction as
they are along the hydrostatic axis. When $C = 1, the surfaces are
spherical.</li>
</ul>
<ul>
<li>The overconsolidation ratio (input parameter $OCR) defines the
relationship between the loading surface and bounding surface. The
radius of the bounding surface, R, is equal to the product of the OCR
and the radius of the loading surface, r. When the soil is normally
consolidated and $OCR = 1, the bounding and loading surfaces are
coincident and virgin loading will occur.</li>
</ul>
<ul>
<li>When the hyperelastic pressure-dependency parameter (input parameter
$alpha) is set to zero, the elastic shear modulus will be constant with
a value equal to the initial shear modulus (input parameter $mu_o) and
the deviatoric and volumetric responses are uncoupled in the elastic
regime.</li>
</ul>
<ul>
<li>The virgin compressibility parameter (input parameter $lambda)
describes the relationship between the specific volume v = 1 + e and the
logarithm of the mean effective stress (where e is the void ratio). This
is is related to the compression index $C_c$ that describes the
relationship between the void ratio and the logarithm of the mean
effective stress in consolidation testing.</li>
</ul>

<h3 id="usage_examples">Usage Examples</h3>
<p>The following usage example provides the input parameters used in the
single element examples of Borja et al. (2001). The initial bulk modulus
is determined from the initial mean stress desired in the test (in this
case p = 100 kPa) divided by the recompressibilty index kappa = 0.018.
The units of this analysis are kN and m, thus the prescribed initial
shear modulus of 5.4 MPa is input as 5400 kPa. The hardening parameter
$h has the same units as the moduli.</p>

```tcl
set rho 1.8 
set c 1.0 
set bulk 5555.56 
set OCR 1.5 
set mu_o 5.4e3 
set alpha 0.0 
set lambda 0.13 
set h 5.0e3 
set m 1.5 
nDMaterial BoundingCamClay 1 $rho $c $bulk $OCR $mu_o $alpha $lambda $h $m
```

<h3 id="references">References</h3>
<p>Borja, R.I., Lin, C.-H., and Montans, F.J. (2001) 'Cam-Clay
plasticity, Part IV: Implicit integration of anisotropic bounding
surface model with nonlinear hyperelasticity and ellipsoidal loading
function,' <em>Computer Methods in Applied Mechanics and
Engineering,</em> 190(26), 3293-3323, doi:
10.1016/S0045-7825(00)00301-7.</p>
<p>Schofield, A. and Wroth, P. (1968) <em>Critical State Soil
Mechanics,</em> McGraw Hill, New York.</p>
<hr />
<h2 id="example_analysis">Example Analysis</h2>
<p>
```tcl
 
```
</p>

<hr />

<p>Code developed by: <a
href="http://www.civil.canterbury.ac.nz/staff/cmcgann.shtml">Chris McGann</a> &amp; 
<a
href="http://www.ce.washington.edu/people/faculty/faculty.php?id=2">Pedro Arduino</a>, at the University of Washington</p>


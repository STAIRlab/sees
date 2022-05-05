 # PressureDependMultiYield03

<p>(The reference for <strong>PressureDependMultiYield03</strong>
material: Khosravifar, A., Elgamal, A., Lu, J., and Li, J. [2018]. "A 3D
model for earthquake-induced liquefaction triggering and
post-liquefaction response." Soil Dynamics and Earthquake Engineering,
110, 43-52)</p>
<p><strong>PressureDependMultiYield03</strong> is modified from
<strong>PressureDependMultiYield02</strong> material to comply with the
established guidelines on the dependence of liquefaction triggering to
the number of loading cycles, effective overburden stress
(K&amp;sigma;), and static shear stress (K&amp;alpha;). Element drivers
for single element simulations under undrained cyclic, undrained
monotonic, drained cyclic and drained monotonic loading can be <a
href="PDMY03_elementdriver" title="wikilink">downloaded from
here</a>.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDMaterial PressureDependMultiYield03 $tag $nd $rho
$refShearModul $refBulkModul $frictionAng $peakShearStra $refPress
$pressDependCoe $PTAng $mType $ca $cb $cc $cd $ce $da $db $dc
&lt;$noYieldSurf=20 &lt;$r1 $Gs1 …&gt; $liquefac1=1. $liquefac2=0.
$pa=101 &lt;$s0=1.73&gt;&gt;</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><p><strong>$ca, $cb, $cc, $cd, $ce</strong></p></td>
<td><p>Non-negative constants defining the rate of contract or pore
pressure buildup. See Tables 1 and 2 below for more
information.</p></td>
</tr>
<tr class="even">
<td><p><strong>$da, $db, $dc</strong></p></td>
<td><p>A non-negative constant reflecting K&amp;sigma; effect.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$contrac2</strong></p></td>
<td><p>Non-negative constants defining the rate of dilation. See Tables
1 and 2 below for more information.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">mType</code></td>
<td><p>0: Triaxial Compression; 1: Triaxial Extension; 2: Direct
Shear</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">s0</code></td>
<td><p>Numerical constant (default value = 1.73 kPa). See Tables 1 and 2
below for more information.</p></td>
</tr>
<tr class="even">
<td><p><strong>Others</strong></p></td>
<td><p>See PressureDependMultiYield02 material above and Tables 1 and 2
below.</p></td>
</tr>
</tbody>
</table>
<p>Table 1 provides the proposed calibrated input parameters for
<strong>PressureDependMultiYield03</strong> for four different relative
densities. Table 2 provides a brief description for each parameter and
the adopted calibration procedure.</p>
<p>Table 1. Model Input Parameters</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Pdmy03_table1.png" title="Pdmy03_table1.png"
alt="Pdmy03_table1.png" />
<figcaption aria-hidden="true">Pdmy03_table1.png</figcaption>
</figure>
<p><strong>*</strong>These are not input parameters to the constitutive
model, but rather parameters computed during model calibration.</p>
<p>Table 2. Description of Calibration Parameters</p>
<figure>
<img src="/OpenSeesRT/contrib/static/Pdmy03_table2.png" title="Pdmy03_table2.png"
alt="Pdmy03_table2.png" />
<figcaption aria-hidden="true">Pdmy03_table2.png</figcaption>
</figure>
<p>Code Developed by: <span style="color:blue"> UC San Diego (Dr.
Zhaohui Yang)</span>:</p>
<hr />
<p>UC San Diego Soil Model: </p>

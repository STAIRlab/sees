---
description: Uniaxial updated Voce-Chaboche material
...

# UVCuniaxial 

<p>This command is used to construct an Updated Voce-Chaboche (UVC)
material for uniaxial stress states (e.g., beam elements). This material
is a refined version of the classic nonlinear isotropic/kinematic
hardening material model based on the Voce isotropic hardening law and
the Chaboche kinematic hardening law. The UVC model contains an updated
isotropic hardening law, with parameter constraints, to simulate the
permanent decrease in yield stress with initial plastic loading
associated with the discontinuous yielding phenomenon in mild
steels.</p>
<p>Details regarding the model, its implementation, and calibration can
be found in the references cited at the end. The <a
href="https://opensees.berkeley.edu/wiki/index.php/UVCmultiaxial_(Updated_Voce-Chaboche)">multiaxial</a>
(e.g., for solid/brick elements) and <a
href="https://opensees.berkeley.edu/wiki/index.php/UVCplanestress_(Updated_Voce-Chaboche)">plane-stress</a>
(e.g., for quad/plate/shell elements) versions are also available. The
multiaxial and plane-stress implementations have the exact same
hardening rules as this uniaxial model, and only differ in their purpose
and numerical implementation.</p>
<p>Available in OpenSees version 3.1.0+.</p>
<hr />

```tcl
uniaxialMaterial UVCuniaxial $matTag $E $fy $QInf $b
        $DInf $a $N $C1 $gamma1 &lt;$C2 $gamma2 $C3 $gamma3 … $C8
        $gamma8&gt;
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>Integer tag identifying the material.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E</code></td>
<td><p>Elastic modulus of the steel material.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fy</code></td>
<td><p>Initial yield stress of the steel material.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">QInf</code></td>
<td><p>Maximum increase in yield stress due to cyclic hardening
(isotropic hardening).</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">b</code></td>
<td><p>Saturation rate of QInf, b &gt; 0.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">DInf</code></td>
<td><p>Decrease in the initial yield stress, to neglect the model
updates set DInf = 0.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">a</code></td>
<td><p>Saturation rate of DInf, a &gt; 0. If DInf == 0, then a is
arbitrary (but still a &gt; 0).</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">N</code></td>
<td><p>Number of backstresses to define, N &gt;= 1.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">C1</code></p></td>
<td><p>Kinematic hardening parameter associated with backstress
component 1.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">gamma1</code></p></td>
<td><p>Saturation rate of kinematic hardening associated with backstress
component 1.</p></td>
</tr>
<tr class="odd">
<td><p><code>&lt;C2 gamma2 C3 gamma3 ... C8
gamma8&gt;</strong></p></td>
<td><p>Additional backstress parameters, up to 8 may be specified. If C
is specified, then the corresponding gamma must also be specified. Note
that only the first N backstresses will be read by the parser.</p></td>
</tr>
</tbody>
</table>

<hr />

<p><strong>Examples</strong></p>
<p><strong><em>1. Validation with Abaqus:</em></strong></p>
<p>This first example compares the response of the UVC model with the
built-in nonlinear isotropic/kinematic material model in Abaqus v6.14.
For this validation the model updates are neglected by simply setting
DInf = 0.0 and a = 1.0. The model parameters are:</p>
<p>E = 179800 MPa, fy = 318.5 MPa, QInf = 100.7 MPa, b = 8.0, DInf = 0.0
MPa, a = 1.0, C1 = 11608.2 MPa, gamma1 = 145.2, C2 = 1026.3 MPa, gamma2
= 4.7</p>
<p>Figure 1 shows that the UVC implementation in OpenSees agrees with
the built-in Abaqus model to the level of machine precision. Therefore,
you can use the UVC model in place of the nonlinear isotropic/kinematic
hardening material model provided in Abaqus and many other finite
element simulation platforms. The finite element models used to validate
the Abaqus and OpenSees responses can be found at <a
href="https://github.com/ahartloper/UVC_MatMod">https://github.com/ahartloper/UVC_MatMod</a>.</p>

<figure>
 <img src="/OpenSeesRT/contrib/static/UVC_Opensees_valid_s22.png"
title="Figure 1. Validation of UVC model with built-in nonlinear isotropic/kinematic material in Abaqus."
width="400"
alt="Figure 1. Validation of UVC model with built-in nonlinear isotropic/kinematic material in Abaqus." />
<figcaption aria-hidden="true">Figure 1. Validation of UVC model with
built-in nonlinear isotropic/kinematic material in Abaqus.</figcaption>
</figure>

<p><strong><em>2. Comparison with structural steels:</em></strong></p>
<p>The applicability of the UVC material model for structural steels is
demonstrated through two comparisons with experimental data from
uniaxial coupon tests. A comparison with a North American steel, A992
Gr. 50 (nominal fy = 345 MPa), is shown in Figure 2. A comparison with a
European steel, S355J2+N (nominal fy = 355 MPa), is shown in Figure 3.
In both cases the UVC model is able to represent well the initial yield
stress as well as the material behavior in later loading cycles.</p>
<p>The parameters used for the A992 Gr. 50 and S355J2+N steels, along
with other common structural steels, are provided and discussed in the
next section.</p>
<p>
<center>
<div class="gallery" widths=400px heights=300px > 
<a href="File:A992_flange_UVC.png">File:A992_flange_UVC.png</a> | Figure 2.
Comparison of UVC model with uniaxial coupon test data from the A992 Gr.
50 W14X82 flange data set. <a
href="File:S355j2_UVC.png">File:S355j2_UVC.png</a> | Figure 3.
Comparison of UVC model with uniaxial coupon test data from the S355J2+N
25 mm plate data set. 
</div> 
</center>
</p>

<hr />
<p><strong>UVC model parameters for structural steels</strong></p>
<p>Below is a list of UVC model parameters for twelve structural steels
from Reference [1] using two backstresses. These parameters are
applicable for all implementations of the UVC model (uniaxial,
plane-stress, multiaxial).</p>
<p>References [1,3] contain detailed information on the calibration
procedure used to obtain the model parameters. All of the parameters
provided in the table below were obtained by minimizing the total
squared-strain energy across at least five uniaxial coupon tests of
distinct strain histories subject to the constraint that the material
response is non-softening. Therefore, the UVC material model parameters
should be representative of steel material behavior for arbitrarily
imposed strains. Note that although the parameters in this table are
considered representative of a specific sample of each material,
significant variations can exist between different samples of the same
material.</p>
<p>All the parameters in the table are obtained through the UVC model
calibration procedure implemented in the open-source Python package <a
href="https://pypi.org/project/RESSPyLab/">RESSPyLab</a>. The RESSPyLab
package can be used to generate UVC model parameters for other steel
materials if the data is available. Details and examples on the
calibration are provided on the <a
href="https://pypi.org/project/RESSPyLab/">RESSPyLab</a> web page.</p>
<p>Note that the parameters provided in the table below were calibrated
using the true stress-strain definition, i.e., e_true =
ln(1+(L-L_0)/L_0) and s_true = F/A_0 * (1 + (L-L_0)/L_0).</p>


<table>
<tbody><tr>
<th colspan="11">UVC Material Parameters
</th></tr>
<tr>
<td>Material</td>
<td>E</td>
<td>f<sub>y</sub></td>
<td>Q<sub>Inf</sub></td>
<td>b</td>
<td>D<sub>Inf</sub></td>
<td>a</td>
<td>C<sub>1</sub></td>
<td>gamma<sub>1</sub></td>
<td>C<sub>2</sub></td>
<td>gamma<sub>2</sub>
</td></tr>
<tr>
<td>-</td>
<td>[GPa]</td>
<td>[MPa]</td>
<td>[MPa]</td>
<td>-</td>
<td>[MPa]</td>
<td>-</td>
<td>[MPa]</td>
<td>-</td>
<td>[MPa]</td>
<td>-
</td></tr>
<tr>
<td>S355J2+N (25 mm plate)</td>
<td>197.41</td>
<td>338.80</td>
<td>134.34</td>
<td>14.71</td>
<td>133.75</td>
<td>229.25</td>
<td>26242.00</td>
<td>199.04</td>
<td>2445.30</td>
<td>11.66
</td></tr>
<tr>
<td>S355J2+N (50 mm plate)</td>
<td>185.97</td>
<td>332.18</td>
<td>120.48</td>
<td>8.14</td>
<td>93.15</td>
<td>261.75</td>
<td>21102.00</td>
<td>173.60</td>
<td>2300.60</td>
<td>10.42
</td></tr>
<tr>
<td>S355J2+N (HEB500 flange)</td>
<td>192.13</td>
<td>315.04</td>
<td>138.01</td>
<td>11.36</td>
<td>96.16</td>
<td>223.66</td>
<td>18587.84</td>
<td>257.31</td>
<td>1351.98</td>
<td>6.52
</td></tr>
<tr>
<td>S355J2+N (HEB500 web)</td>
<td>199.68</td>
<td>334.94</td>
<td>139.32</td>
<td>14.07</td>
<td>120.33</td>
<td>274.73</td>
<td>28528.03</td>
<td>315.17</td>
<td>2569.45</td>
<td>24.68
</td></tr>
<tr>
<td>S460NL (25 mm plate)</td>
<td>187.61</td>
<td>439.20</td>
<td>97.35</td>
<td>14.02</td>
<td>136.64</td>
<td>226.40</td>
<td>26691.00</td>
<td>188.75</td>
<td>2892.40</td>
<td>10.44
</td></tr>
<tr>
<td>S690QL (25 mm plate)</td>
<td>188.63</td>
<td>685.39</td>
<td>0.11</td>
<td>0.11</td>
<td>132.30</td>
<td>285.15</td>
<td>34575.00</td>
<td>185.16</td>
<td>3154.20</td>
<td>20.14
</td></tr>
<tr>
<td>A992 Gr. 50 (W14X82 web)</td>
<td>210.74</td>
<td>378.83</td>
<td>122.63</td>
<td>19.74</td>
<td>143.49</td>
<td>248.14</td>
<td>31638.00</td>
<td>277.32</td>
<td>1548.60</td>
<td>9.04
</td></tr>
<tr>
<td>A992 Gr. 50 (W14X82 flange)</td>
<td>191.02</td>
<td>373.72</td>
<td>141.47</td>
<td>15.20</td>
<td>135.95</td>
<td>211.16</td>
<td>25621.00</td>
<td>235.12</td>
<td>942.18</td>
<td>3.16
</td></tr>
<tr>
<td>A500 Gr. B (HSS305X16)</td>
<td>191.21</td>
<td>324.09</td>
<td>228.02</td>
<td>0.11</td>
<td>50.41</td>
<td>270.40</td>
<td>17707.00</td>
<td>207.18</td>
<td>1526.20</td>
<td>6.22
</td></tr>
<tr>
<td>BCP325 (22 mm plate)</td>
<td>178.61</td>
<td>368.03</td>
<td>112.25</td>
<td>10.78</td>
<td>105.95</td>
<td>221.92</td>
<td>20104.00</td>
<td>200.43</td>
<td>2203.00</td>
<td>11.76
</td></tr>
<tr>
<td>BCR295 (HSS350X22)</td>
<td>178.74</td>
<td>412.21</td>
<td>0.09</td>
<td>0.09</td>
<td>103.30</td>
<td>212.83</td>
<td>20750.59</td>
<td>225.26</td>
<td>1245.04</td>
<td>2.09
</td></tr>
<tr>
<td>HYP400 (27mm plate)</td>
<td>189.36</td>
<td>454.46</td>
<td>62.63</td>
<td>16.57</td>
<td>109.28</td>
<td>145.74</td>
<td>13860.00</td>
<td>141.61</td>
<td>1031.10</td>
<td>3.53
</td></tr></tbody></table>


<hr />
<p><strong>References</strong>:</p>
<p>Please use Reference [1] when citing the UVC model.</p>
<p><strong>[1]</strong> Hartloper, A. R., de Castro e Sousa A., and
Lignos D.G. "Constitutive Modeling of Structural Steels: Nonlinear
Isotropic/Kinematic Hardening Material Model and its Calibration", <a
href="https://doi.org/10.1061/(ASCE)ST.1943-541X.0002964">https://doi.org/10.1061/(ASCE)ST.1943-541X.0002964</a>.</p>
<p><strong>[2]</strong> Hartloper, A. R., de Castro e Sousa A., and
Lignos D.G. (2019). "Sensitivity of Simulated Steel Column Instabilities
to Plasticity Model Assumptions". 12th Canadian Conference on Earthquake
Engineering, Quebec City, QC, Canada. <a
href="https://infoscience.epfl.ch/record/267788">https://infoscience.epfl.ch/record/267788</a></p>
<p><strong>[3]</strong> Hartloper, A. R., de Castro e Sousa A., and
Lignos D.G. (2019). "A Nonlinear Isotropic/Kinematic Hardening Model for
Materials with Discontinuous Yielding". Report No. 271062, Resilient
Steel Structures Laboratory (RESSLab), EPFL, Lausanne, Switzerland. <a
href="https://infoscience.epfl.ch/record/271062">https://infoscience.epfl.ch/record/271062</a>.</p>
<hr />
<p>Code developed, implemented, and maintained by: 
<span style="color:blue"> Alex Hartloper (EPFL). </span> Issues,
bugs, and feature requests can be opened at the <a
href="https://github.com/ahartloper/UVC_MatMod">github
repository</a>.</p>

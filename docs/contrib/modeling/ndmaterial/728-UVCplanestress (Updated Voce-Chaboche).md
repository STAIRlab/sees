# UVCplanestress (Updated Voce-Chaboche)

<p>This command is used to construct an Updated Voce-Chaboche (UVC)
material for plane-stress stress states (e.g., for quad/plate/shell
elements). This material is a refined version of the classic nonlinear
isotropic/kinematic hardening material model based on the Voce isotropic
hardening law and the Chaboche kinematic hardening law. The UVC model
contains an updated isotropic hardening law, with parameter constraints,
to simulate the permanent decrease in yield stress with initial plastic
loading associated with the discontinuous yielding phenomenon in mild
steels.</p>
<p>Details regarding the model, its implementation, and calibration can
be found in the references cited at the end. The <a
href="https://opensees.berkeley.edu/wiki/index.php/UVCmultiaxial_(Updated_Voce-Chaboche)">multiaxial</a>
(e.g., for solid/brick elements) and <a
href="https://opensees.berkeley.edu/wiki/index.php/UVCuniaxial_(Updated_Voce-Chaboche)">uniaxial</a>
(e.g., for beam elements) versions are also available. The multiaxial
and uniaxial implementations have the exact same hardening rules as this
plane-stress model, and only differ in their purpose and numerical
implementation.</p>
<p>Available in OpenSees version 3.1.0+.</p>
<hr />

```tcl
nDMaterial UVCplanestress $matTag $E $nu $fy $QInf $b
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
<td><code class="parameter-table-variable">nu</code></td>
<td><p>Poisson's ratio for the steel material.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fy</code></td>
<td><p>Initial yield stress of the steel material.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">QInf</code></td>
<td><p>Maximum increase in yield stress due to cyclic hardening
(isotropic hardening).</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">b</code></td>
<td><p>Saturation rate of QInf, b &gt; 0.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">DInf</code></td>
<td><p>Decrease in the initial yield stress, to neglect the model
updates set DInf = 0.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">a</code></td>
<td><p>Saturation rate of DInf, a &gt; 0. If DInf == 0, then a is
arbitrary (but still a &gt; 0).</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">N</code></td>
<td><p>Number of backstresses to define, N &gt;= 1.</p></td>
</tr>
<tr class="even">
<td><p><strong>$C1</strong></p></td>
<td><p>Kinematic hardening parameter associated with backstress
component 1.</p></td>
</tr>
<tr class="odd">
<td><p><strong>$gamma1</strong></p></td>
<td><p>Saturation rate of kinematic hardening associated with backstress
component 1.</p></td>
</tr>
<tr class="even">
<td><p><strong>&lt;$C2 $gamma2 $C3 $gamma3 … $C8
$gamma8&gt;</strong></p></td>
<td><p>Additional backstress parameters, up to 8 may be specified. If C
is specified, then the corresponding gamma must also be specified. Note
that only the first N backstresses will be read by the parser.</p></td>
</tr>
</tbody>
</table>
<hr />
<p><strong>Examples, validation, and UVC model parameters</strong></p>
<p>For the user, the only practical difference between the uniaxial and
multiaxial/plane-stress implementations is the specification of
Poisson's ratio in the list of input parameters.</p>
<p><span style="color:red"> Further information on the UVC model
is centralized at the </span> <strong><a
href="https://opensees.berkeley.edu/wiki/index.php/UVCuniaxial_(Updated_Voce-Chaboche)">UVCuniaxial</a></strong>
web page. On the UVCuniaxial page you will find examples validating the
model, and UVC model parameters for common structural steels that are
applicable for all stress states.</p>
<hr />
<p><strong>References</strong>:</p>
<p>Please use Reference [1] when citing the UVC model.</p>
<p><strong>[1]</strong> Hartloper, A. R., de Castro e Sousa A., and
Lignos D.G. (2019). "Constitutive Modeling of Structural Steels: A
Nonlinear Isotropic/Kinematic Hardening Material Model and its
Calibration", <a
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

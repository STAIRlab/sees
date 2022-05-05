 # BWBN

<p>This command is used to construct a uniaxial Bouc-Wen pinching
hysteretic material object. This material model is an extension of the
original Bouc-Wen model that includes pinching (Baber and Noori (1986)
and Foliente (1995)).</p>

```tcl
uniaxialMaterial BWBN $matTag $alpha $ko $n $gamma $beta
        $Ao $q $zetas $p $Shi $deltaShi $lambda $tol $maxIter
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>ratio of post-yield stiffness to the initial elastic stiffenss
(0&lt; &lt;math&gt;\alpha&lt;/math&gt; &lt;1)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ko</code></td>
<td><p>initial elastic stiffness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">n</code></td>
<td><p>parameter that controls transition from linear to nonlinear range
(as n increases the transition becomes sharper; n is usually grater or
equal to 1)</p></td>
</tr>
<tr class="odd">
<td><p><strong>$gamma $beta</strong></p></td>
<td><p>parameters that control shape of hysteresis loop; depending on
the values of $\gamma$ and
$\beta$ softening, hardening or quasi-linearity
can be simulated (look at the <a
href="http://opensees.berkeley.edu/wiki/index.php/BoucWen_Material">BoucWen
Material</a>)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ao</code></td>
<td><p>parameter that controls tangent stiffness</p></td>
</tr>
<tr class="odd">
<td><p><strong>$q $zetas $p $Shi $deltaShi $lambda</strong></p></td>
<td><p>parameters that control pinching</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">tol</code></td>
<td><p>tolerance</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">maxIter</code></td>
<td><p>maximum iterations</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="BWBN_YSPD.jpg‎" title="BWBN_YSPD.jpg‎" alt="BWBN_YSPD.jpg‎" />
<figcaption aria-hidden="true">BWBN_YSPD.jpg‎</figcaption>
</figure>
<p>Fig. Cyclic force displacement relationship of the YSPDs generated
using the BWBN material model</p>
<hr />
<p>PARAMETER ESTIMATION:</p>
<p><a href="BWBNParameterEstimation"
title="wikilink">BWBNParameterEstimation</a></p>
<hr />
<p>EXAMPLE:</p>
<p><a href="BWBNExample" title="wikilink">BWBNExample</a></p>
<hr />
<p>REFERENCES:</p>
<p><a
href="http://www.sciencedirect.com/science/article/pii/S0141029613003568">Hossain,
M. R., Ashraf, M., &amp; Padgett, J. E. (2013). "Risk-based seismic
performance assessment of Yielding Shear Panel Device." Engineering
Structures, 56, 1570-1579.</a></p>
<p><a
href="http://www.sciencedirect.com/science/article/pii/S0263823112001206">Hossain,
M. R., &amp; Ashraf, M. (2012). "Mathematical modelling of yielding
shear panel device." Thin-Walled Structures, 59, 153-161.</a></p>
<p>Baber, T. T., &amp; Noori, M. N. (1986). "Modeling general hysteresis
behavior and random vibration application." Journal of Vibration
Acoustics Stress and Reliability in Design, 108, 411.</p>
<p>Foliente, G. C. (1995). Hysteresis modeling of wood joints and
structural systems. Journal of Structural Engineering, 121(6),
1013-1022.</p>
<hr />
<p>DEVELOPED BY:</p>
<p><a
href="http://scholar.google.com.au/citations?user=I_li3qkAAAAJ&amp;hl=en&amp;oi=ao">Raquib
Hossain</a>, <a href="http://www.uq.edu.au/">The University of
Queensland (UQ), Australia</a> &amp; <a
href="http://www.buet.ac.bd/">Bangladesh University of Engineering and
Technology (BUET), Bangladesh.</a></p>

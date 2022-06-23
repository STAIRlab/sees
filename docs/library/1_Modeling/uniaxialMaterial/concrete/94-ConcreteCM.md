---
description: Complete Concrete Model by Chang and Mander (1994)
...

# ConcreteCM

This command is used to construct a `UniaxialMaterial`
`ConcreteCM` (Kolozvari et al., 2015), which is a
uniaxial hysteretic constitutive model for concrete developed by Chang
and Mander (1994). This model is a refined, rule-based, generalized, and
non-dimensional constitutive model that allows calibration of the
monotonic and hysteretic material modeling parameters, and can simulate
the hysteretic behavior of confined and unconfined, ordinary and
high-strength concrete, in both cyclic compression and tension (Figure
1). The model addresses important behavioral features, such as
continuous hysteretic behavior under cyclic compression and tension,
progressive stiffness degradation associated with smooth unloading and
reloading curves at increasing strain values, and gradual crack closure
effects. Details of the model are available in the report by Chang and
Mander (1994).

```tcl
uniaxialMaterial ConcreteCM $mattag $fpcc $epcc $Ec $rc
        $xcrn $ft $et $rt $xcrp < -GapClose $gap >
```


<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">mattag</code></td>
<td><p>Unique <em>uniaxialMaterial</em> tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fpcc</code></td>
<td><p>Compressive strength (f'<sub class="subscript">c</sub>)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epcc</code></td>
<td><p>Strain at compressive strength
($\epsilon$'<sub
class="subscript">c</sub>)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Ec</code></td>
<td><p>Initial tangent modulus (E<sub
class="subscript">c</sub>)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rc</code></td>
<td><p>Shape parameter in Tsai’s equation defined for compression
(r<sub class="subscript">c</sub>)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">xcrn</code></td>
<td><p>Non-dimensional critical strain on compression envelope
($\epsilon$<sup
class="superscript">-</sup><sub
class="subscript">cr</sub>, where the envelope curve starts
following a straight line)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ft</code></td>
<td><p>Tensile strength (f<sub
class="subscript">t</sub>)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">et</code></td>
<td><p>Strain at tensile strength
( $\epsilon_\textrm{t}$ )</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rt</code></td>
<td><p>Shape parameter in Tsai’s equation defined for tension (r<sub
class="subscript">t</sub>)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">xcrp</code></td>
<td><p>Non-dimensional critical strain on tension envelope
($\epsilon^+_{cr}$, where the envelope curve starts
following a straight line - large value [e.g., 10000] recommended when
tension stiffening is considered)</p></td>
</tr>
<tr class="odd">
<td><p><strong><-GapClose $gap></strong></p></td>
<td><p><strong>gap</strong> = 0, less gradual gap closure (default);
<strong>gap</strong> = 1, more gradual gap closure</p></td>
</tr>
</tbody>
</table>

<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCM_0.png"
title="Figure 1. Hysteretic Constitutive Model for Concrete by Chang and Mander (1994)"
width="500"
alt="Figure 1. Hysteretic Constitutive Model for Concrete by Chang and Mander (1994)" />
<figcaption aria-hidden="true">Figure 1. Hysteretic Constitutive Model
for Concrete by Chang and Mander (1994)</figcaption>
</figure>

<p>The Chang and Mander (1994) model generates continuous
hysteretic stress-strain relationships with slope continuity for
confined and unconfined concrete in both compression and tension. The
compression envelope curve of the model is defined by the initial
tangent slope, (E<sub class="subscript">c</sub>), the peak
coordinate ($\epsilon^\prime_c$, $f^\prime_c$), a parameter (r<sub class="subscript">c</sub>) from Tsai’s (1988) equation defining
the shape of the envelope curve, and a parameter
($\epsilon$<sup class="superscript">-</sup><sub class="subscript">cr</sub>) to define normalized (with respect
to $\epsilon^\prime_c$) strain where the envelope curve
starts following a straight line, until zero compressive stress is
reached at the spalling strain, $\epsilon_{sp}$. These parameters can be controlled
based on specific experimental results for a refined calibration of the
compression envelope (Figure 2). Chang and Mander (1994) proposed
empirical relationships for parameters $E_c$,
$\epsilon$'<sub class="subscript">c</sub>, and r<sub
class="subscript">c</sub> for unconfined concrete with
compressive strength f'<sub class="subscript">c</sub>, based
on review of previous research. Parameters f'<sub
class="subscript">c</sub>,
$\epsilon$'<sub class="subscript">c</sub>, 
E<sub class="subscript">c</sub>, 
r<sub class="subscript">c</sub>, and
$\epsilon$<sup class="superscript">-</sup><sub class="subscript">cr</sub> 
can also be calibrated to represent
the stress-strain behavior of confined concrete in compression, to
follow the constitutive relationships for confined concrete proposed by
Mander et al (1988) or similar.</p>

<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCM_1.png"
title="Figure 2. Compression and Tension Envelope Curves" width="500"
alt="Figure 2. Compression and Tension Envelope Curves" />
<figcaption aria-hidden="true">Figure 2. Compression and Tension
Envelope Curves</figcaption>
</figure>

The shape of the tension envelope curve in the model is the same as
that of the compression envelope; however, the tension envelope curve is
shifted to a new origin that is based on the unloading strain from the
compression envelope (Figure 2). As well, the strain ductility
experienced previously on the compression envelope is also reflected on
the tension envelope. The parameters associated with the tension
envelope curve include the tensile strength of concrete (f<sub
class="subscript">t</sub>), the monotonic strain at tensile
strength ( $\epsilon_\textrm{t}$ ), a parameter (r<sub
class="subscript">t</sub>) from Tsai’s (1988) equation defining
the shape of the tension envelope curve, and a parameter
($\epsilon$<sup class="superscript">+</sup><sub class="subscript">cr</sub>) 
to define normalized (with respect
to $\epsilon$<sub class="subscript">t</sub>) strain where the tension envelope
curve starts following a straight line, until zero tensile stress is
reached at a strain of $\epsilon$<sub class="subscript">crk</sub>. 
These parameters can also be
controlled and calibrated based on specific experimental results or
empirical relations proposed by other researchers (e.g., Belarbi and
Hsu, 1994) to model the behavior of concrete in tension and the tension
stiffening phenomenon. Concrete experiencing tension stiffening can be
considered not to crack completely; that is, a large value for parameter
$\epsilon$<sup
class="superscript">+</sup><sub
class="subscript">cr</sub> (e.g., 10000) can be defined.

<p>Source: /usr/local/cvs/OpenSees/SRC/material/uniaxial/</p>

<hr />

<p><strong>Input Format:</strong></p>


<hr />
<p><strong>Example:</strong></p>

```tcl
uniaxialMaterial ConcreteCM 1 -6.2 -0.0021 4500 7 1.035 0.30 0.00008 1.2 10000
```

Example of hysteretic stress-strain history generated by the model
code is illustrated in Figure 3.

<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCM_2.png" width="500" alt="Figure 3. Concrete Stress-Strain Behavior" />
<figcaption aria-hidden="true">Figure 3. Concrete Stress-Strain Behavior</figcaption>
</figure>

<hr />
<p><strong>Discussion:</strong></p>
<p>An optional input parameter <strong>gap</strong> is introduced in the
<strong>ConcreteCM</strong> model implemented in OpenSees for providing
the users with the opportunity to control the intensity of gap closure
in the stress-strain behavior of concrete, which in-turn influences the
level of pinching in the lateral load-displacement behavior of a RC
wall. The original Chang and Mander (1994) model adopts a non-zero
tangent stiffness at zero stress level upon unloading from the tension
envelope, which is represented by gap = 1 in
<strong>ConcreteCM</strong>. Using <strong>gap</strong> = 0 (default)
produces less gradual gap closure, since it assumes zero tangent
stiffness at zero stress level upon unloading from the tension envelope,
and is suitable for most analyses. Figure 4 illustrates the effect of
plastic stiffness upon unloading from tension envelope (
E<sup class="superscript">+</sup><sub class="subscript">pl</sub>) on crack 
closure, i.e. use of more gradual (<strong>gap</strong> = 1) or less gradual 
(<strong>gap</strong> = $0$) gap closure. The effect of parameter <strong>gap</strong> on
predictions of flexural behavior of a RC wall is illustrated in Example
1 of <a
href="http://opensees.berkeley.edu/wiki/index.php/MVLEM_-_Multiple-Vertical-Line-Element-Model_for_RC_Walls"><strong>MVLEM</strong></a>
element.</p>
<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCM_3.png"
title="Figure 4. Effect of Plastic Stiffness upon Unloading from Tension Envelope (Epl+) on Crack Closure"
width="500"
alt="Figure 4. Effect of Plastic Stiffness upon Unloading from Tension Envelope (Epl+) on Crack Closure" />
<figcaption aria-hidden="true">Figure 4. Effect of Plastic Stiffness
upon Unloading from Tension Envelope (Epl+) on Crack
Closure</figcaption>
</figure>

Constitutive stress-strain concrete behavior is also implemented in
OpenSees in uniaxialMaterial <a
href="http://opensees.berkeley.edu/wiki/index.php/Concrete07_%E2%80%93_Chang_%26_Mander%E2%80%99s_1994_Concrete_Model"><strong>Cocnrete07</strong></a>.
However, <strong>ConcreteCM</strong> incorporates sophisticated
unloading/reloading rules defined originally by Chang and Mander (1994),
as opposed to <strong>Concrete07</strong> that adopts simplified
hysteretic rules. Comparison between stress-strain response predicted
using <strong>ConcreteCM</strong> and <strong>Concrete07</strong> is
shown in Figure 5.

<figure>
<img src="/OpenSeesRT/contrib/static/ConcreteCMvsConcrete07.png"
title="Figure 5. Comparison of ConcreteCM and Concrete07" width="500"
alt="Figure 5. Comparison of ConcreteCM and Concrete07" />
<figcaption aria-hidden="true">Figure 5. Comparison of ConcreteCM and
Concrete07</figcaption>
</figure>

<hr />

## References

- Belarbi H. and Hsu T.C.C. (1994), “Constitutive Laws of Concrete
  in Tension and Reinforcing Bars Stiffened by Concrete”, ACI Structural
  Journal, V. 91, No. 4, pp. 465-474.
- Chang, G.A. and Mander, J.B. (1994), “Seismic Energy Based Fatigue
  Damage Analysis of Bridge Columns: Part I - Evaluation of Seismic
  Capacity”, NCEER Technical Report No. NCEER-94-0006, State University of
  New York, Buffalo.
- Kolozvari K., Orakcal K., and Wallace J. W. (2015). "Shear-Flexure
  Interaction Modeling of reinforced Concrete Structural Walls and Columns
  under Reversed Cyclic Loading", Pacific Earthquake Engineering Research
  Center, University of California, Berkeley, <a
  href="http://peer.berkeley.edu/publications/peer_reports/reports_2015/webPEER-2015-12-kolozvari.pdf">PEER
  Report No. 2015/12</a>
- Mander J.B., Priestley M.J.N., and Park R. (1988). “Theoretical
  Stress-Strain Model for Confined Concrete”, ASCE Journal of Structural
  Engineering, V. 114, No. 8, pp. 1804-1826.
- Orakcal K.(2004), "Nonlinear Modeling and Analysis of Slender
  Reinforced Concrete Walls", PhD Dissertation, Department of Civil and
  Environmental Engineering, University of California, Los Angeles.
- Tsai W.T. (1988), “Uniaxial Compressional Stress-Strain Relation
  of Concrete”, ASCE Journal of Structural Engineering, V. 114, No. 9, pp.
  2133-2136.

<p><strong>Code developed by:</strong></p>
<p><a href="mailto:kkolozvari@fullerton.edu"><span style="color:blue"> Kristijan Kolozvari</span>
<span style="color:black"></a>, California State University, Fullerton</p>
<p><span style="color:blue"> Kutay Orakcal<span
style="color:black">, Bogazici University, Istanbul, Turkey</p>
<p><span style="color:blue"> John Wallace<span style="color:black">, Univeristy of California, Los Angeles</p>


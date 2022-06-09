
---
title: uniaxial
...

<style>
h1 {
    font-family: var(--md-code-font-family);
    color: var(--md-code-fg-color) !important;
    font-feature-settings: "kern";
}
</style>

# uniaxial



`UniaxialMaterial` object library.

A `UniaxialMaterial` object typically represents a pair of work conjugate
scalars such as axial stress/strain, moment/cuvature, or force/deformation.

<div style="width: 95%; padding-left: 5%">

<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">ElasticSpring</span>(name,<br>&emsp;&emsp;&emsp;elastic_modulus,<br>&emsp;&emsp;&emsp;damp_tangent,<br>&emsp;&emsp;&emsp;negative_modulus,<br>&emsp;&emsp;&emsp;shear_modulus,<br>&emsp;&emsp;&emsp;**kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>E</td><td><code>Num</code></td><td>Young's modulus of elasticity</tr>
<tr><td>eta</td><td><code>Num</code></td><td>damping tangent</tr>
<tr><td>Eneg</td><td><code>Num</code></td><td></tr>
<tr><td>G</td><td><code>Num</code></td><td></tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">Hardening</span>(name, elastic_modulus, sigmaY, H_iso, H_kin, eta, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>E</td><td><code>Num</code></td><td>Young's modulus of elasticity</tr>
<tr><td>sigmaY</td><td><code>Num</code></td><td>yield stress or force</tr>
<tr><td>H_iso</td><td><code>Num</code></td><td>isotropic hardening Modulus</tr>
<tr><td>H_kin</td><td><code>Num</code></td><td>kinematic hardening Modulus</tr>
<tr><td>eta</td><td><code>Num</code></td><td>visco-plastic coefficient (optional, default=0.0)</tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">ElasticPP</span>(name, elastic_modulus, epsyP, epsyN, eps0, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>E</td><td><code>Num</code></td><td>Young's modulus of elasticity</tr>
<tr><td>epsyP</td><td><code>Num</code></td><td>strain or deformation at which material reaches plastic state in tension</tr>
<tr><td>epsyN</td><td><code>Num</code></td><td>strain or deformation at which material reaches plastic state in compression. (optional, default is tension value)</tr>
<tr><td>eps0</td><td><code>Num</code></td><td>initial strain (optional, default: zero)</tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">RambergOsgoodSteel</span>(name, elastic_modulus, fy, a, n, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>E</td><td><code>Num</code></td><td>Young's modulus of elasticity</tr>
<tr><td>fy</td><td><code>Num</code></td><td>yield strength</tr>
<tr><td>a</td><td><code>Num</code></td><td>yield offset parameter</tr>
<tr><td>n</td><td><code>Num</code></td><td></tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">DoddRestrepo</span>(name,<br>&emsp;&emsp;&emsp;Fy,<br>&emsp;&emsp;&emsp;Fsu,<br>&emsp;&emsp;&emsp;esh,<br>&emsp;&emsp;&emsp;esu,<br>&emsp;&emsp;&emsp;elastic_modulus,<br>&emsp;&emsp;&emsp;eshI,<br>&emsp;&emsp;&emsp;fshI,<br>&emsp;&emsp;&emsp;OmegaFac,<br>&emsp;&emsp;&emsp;**kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>Fy</td><td><code>Num</code></td><td>Yield strength</tr>
<tr><td>Fsu</td><td><code>Num</code></td><td>Ultimate tensile strength (UTS)</tr>
<tr><td>esh</td><td><code>Num</code></td><td>Tensile strain at initiation of strain hardening</tr>
<tr><td>esu</td><td><code>Num</code></td><td>Tensile strain at the UTS</tr>
<tr><td>E</td><td><code>Num</code></td><td>Young's modulus of elasticity</tr>
<tr><td>eshI</td><td><code>Num</code></td><td>Tensile strain for a point on strain hardening curve, recommended range of values for eshI: [ (ESU   5esh)/6, (ESU   3esh)/4]</tr>
<tr><td>fshI</td><td><code>Num</code></td><td>Tensile stress at point on strain hardening curve corresponding to eshI</tr>
<tr><td>OmegaFac</td><td><code>Num</code></td><td>Roundedness factor for Bauschinger curve in cycle reversals from the strain hardening curve. Range: [0.75, 1.15]. Largest value tends to near a bilinear Bauschinger curve. Default = 1.0.</tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">Steel02</span>(name, Fy, E0, b, R0, cR1, cR2, a, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>Fy</td><td><code>Num</code></td><td>yield strength</tr>
<tr><td>E0</td><td><code>Num</code></td><td>initial elastic tangent</tr>
<tr><td>b</td><td><code>Num</code></td><td>strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent</tr>
<tr><td>R0</td><td><code>Num</code></td><td></tr>
<tr><td>cR1 = 0.925</td><td><code>Num</code></td><td></tr>
<tr><td>cR2 = 0.15</td><td><code>Num</code></td><td></tr>
<tr><td>a</td><td><code>[a1,a2,a3,a4,sigInit]</code></td><td>isotropic hardening parameters<table>
<tr><td>a1</td><td><code>Num</code></td><td>                       increase of compression yield envelope as proportion                       of yield strength after a plastic strain of `a2∗(Fy/E0)`</tr>
<tr><td>a2 = 1.0</td><td><code>Num</code></td><td>see explanation under `a1`.</tr>
<tr><td>a3</td><td><code>Num</code></td><td>                       increase of tension yield envelope as proportion                       of yield strength after a plastic strain of `a4∗(Fy/E0)`</tr>
<tr><td>a4 = 1.0</td><td><code>Num</code></td><td>see explanation under `a3`.</tr>
<tr><td>sigInit</td><td><code>Num</code></td><td>initial stress</tr>
</table>
</tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">ConfinedConcrete01</span>(name,<br>&emsp;&emsp;&emsp;secType,<br>&emsp;&emsp;&emsp;fpc,<br>&emsp;&emsp;&emsp;elastic_modulus,<br>&emsp;&emsp;&emsp;eps_ult,<br>&emsp;&emsp;&emsp;poisson,<br>&emsp;&emsp;&emsp;L1,<br>&emsp;&emsp;&emsp;L2,<br>&emsp;&emsp;&emsp;L3,<br>&emsp;&emsp;&emsp;phis,<br>&emsp;&emsp;&emsp;S,<br>&emsp;&emsp;&emsp;fyh,<br>&emsp;&emsp;&emsp;Es0,<br>&emsp;&emsp;&emsp;haRatio,<br>&emsp;&emsp;&emsp;mu,<br>&emsp;&emsp;&emsp;phiLon,<br>&emsp;&emsp;&emsp;internals,<br>&emsp;&emsp;&emsp;wrap,<br>&emsp;&emsp;&emsp;gravel,<br>&emsp;&emsp;&emsp;silica,<br>&emsp;&emsp;&emsp;tol,<br>&emsp;&emsp;&emsp;maxNumIter,<br>&emsp;&emsp;&emsp;epscuLimit,<br>&emsp;&emsp;&emsp;stRatio,<br>&emsp;&emsp;&emsp;**kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>secType</td><td><code>Str</code></td><td></tr>
<tr><td>fpc</td><td><code>Num</code></td><td></tr>
<tr><td>E</td><td><code>Num</code></td><td>Young's modulus of elasticity</tr>
<tr><td>eps_ult</td><td><code>Alt</code></td><td></tr>
<tr><td>poisson</td><td><code>Alt</code></td><td></tr>
<tr><td>L1</td><td><code>Num</code></td><td>length/diameter of square/circular core section measured respect to the hoop center line.</tr>
<tr><td>L2</td><td><code>Num</code></td><td>additional dimensions when multiple hoops are being used.</tr>
<tr><td>L3</td><td><code>Num</code></td><td>additional dimensions when multiple hoops are being used.</tr>
<tr><td>phis</td><td><code>Num</code></td><td>hoop diameter. If section arrangement has multiple hoops it refers to the external hoop.</tr>
<tr><td>S</td><td><code>Num</code></td><td>hoop spacing.</tr>
<tr><td>fyh</td><td><code>Num</code></td><td>yielding strength of the hoop steel.</tr>
<tr><td>Es0</td><td><code>Num</code></td><td>elastic modulus of the hoop steel.</tr>
<tr><td>haRatio</td><td><code>Num</code></td><td>hardening ratio of the hoop steel.</tr>
<tr><td>mu</td><td><code>Num</code></td><td>ductility factor of the hoop steel.</tr>
<tr><td>phiLon</td><td><code>Num</code></td><td>diameter of longitudinal bars.</tr>
<tr><td>internals</td><td><code>[phisi,Si,fyhi,Es0i,haRatioi,mui]</code></td><td>optional parameters for defining the internal transverse reinforcement.If they are not specified they will be assumed equal to the external ones (for S2, S3, S4a, S4b and S5 typed).<table>
<tr><td>phisi</td><td><code>Num</code></td><td></tr>
<tr><td>Si</td><td><code>Num</code></td><td></tr>
<tr><td>fyhi</td><td><code>Num</code></td><td></tr>
<tr><td>Es0i</td><td><code>Num</code></td><td></tr>
<tr><td>haRatioi</td><td><code>Num</code></td><td></tr>
<tr><td>mui</td><td><code>Num</code></td><td></tr>
</table>
</tr>
<tr><td>wrap</td><td><code>[cover,Am,Sw,ful,Es0w]</code></td><td><table>
<tr><td>cover</td><td><code>Num</code></td><td>cover thickness measured from the outer line of hoop.</tr>
<tr><td>Am</td><td><code>Num</code></td><td>total area of FRP wraps (number of layers x wrap thickness x wrap width).</tr>
<tr><td>Sw</td><td><code>Num</code></td><td>spacing of FRP wraps (if continuous wraps are used the spacing is equal to the wrap width).</tr>
<tr><td>ful</td><td><code>Num</code></td><td>ultimate strength of FRP wraps.</tr>
<tr><td>Es0w</td><td><code>Num</code></td><td>elastic modulus of FRP wraps.</tr>
</table>
</tr>
<tr><td>gravel</td><td><code>Flg</code></td><td></tr>
<tr><td>silica</td><td><code>Flg</code></td><td></tr>
<tr><td>tol</td><td><code>Num</code></td><td></tr>
<tr><td>maxNumIter</td><td><code>Num</code></td><td></tr>
<tr><td>epscuLimit</td><td><code>Num</code></td><td></tr>
<tr><td>stRatio</td><td><code>Num</code></td><td></tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">Concrete02</span>(name, fpc, epsc0, fpcu, epsU, lamda, ft, Ets, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td>integer tag identifying material</tr>
<tr><td>fpc</td><td><code>Num</code></td><td>concrete compressive strength at 28 days (compression is negative)</tr>
<tr><td>epsc0</td><td><code>Num</code></td><td>concrete strain at maximum strength</tr>
<tr><td>fpcu</td><td><code>Num</code></td><td>concrete crushing strength</tr>
<tr><td>epsU</td><td><code>Num</code></td><td>concrete strain at crushing strength</tr>
<tr><td>lamda</td><td><code>Num</code></td><td>ratio between unloading slope at `epscu` and initial slope</tr>
<tr><td>ft</td><td><code>Num</code></td><td>tensile strength</tr>
<tr><td>Ets</td><td><code>Num</code></td><td>tension softening stiffness (absolute value) (slope of the linear tension softening branch)</tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">Concrete04</span>(name, fc, ec, ecu, Ec, tension, beta, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>fc</td><td><code>Num</code></td><td>floating point values defining concrete compressive strength at 28 days (compression is negative)*</tr>
<tr><td>ec</td><td><code>Num</code></td><td>floating point values defining concrete strain at maximum strength*</tr>
<tr><td>ecu</td><td><code>Num</code></td><td>floating point values defining concrete strain at crushing strength*</tr>
<tr><td>Ec</td><td><code>Num</code></td><td>floating point values defining initial stiffness**</tr>
<tr><td>tension</td><td><code>[fct,et]</code></td><td><table>
<tr><td>fct</td><td><code>Num</code></td><td>floating point value defining the maximum tensile strength of concrete</tr>
<tr><td>et</td><td><code>Num</code></td><td>floating point value defining ultimate tensile strain of concrete</tr>
</table>
</tr>
<tr><td>beta</td><td><code>Num</code></td><td>floating point value defining the exponential curve parameter to define the residual stress (as a factor of $ft) at $etu</tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">Concrete02IS</span>(name, E0, fpc, epsc0, fpcu, epscu, tension, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>E0</td><td><code>Num</code></td><td></tr>
<tr><td>fpc</td><td><code>Num</code></td><td></tr>
<tr><td>epsc0</td><td><code>Num</code></td><td></tr>
<tr><td>fpcu</td><td><code>Num</code></td><td></tr>
<tr><td>epscu</td><td><code>Num</code></td><td></tr>
<tr><td>tension</td><td><code>[rat,ft,Ets]</code></td><td><table>
<tr><td>rat</td><td><code>Num</code></td><td></tr>
<tr><td>ft</td><td><code>Num</code></td><td></tr>
<tr><td>Ets</td><td><code>Num</code></td><td></tr>
</table>
</tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">ConcreteCM</span>(name, fpcc, epcc, Ec, rc, xcrn, ft, et, rt, xcrp, gap, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>fpcc</td><td><code>Num</code></td><td>Compressive strength (f'c)</tr>
<tr><td>epcc</td><td><code>Num</code></td><td>Strain at compressive strength (<math>\epsilon</math>'c)</tr>
<tr><td>Ec</td><td><code>Num</code></td><td>Initial tangent modulus (Ec)</tr>
<tr><td>rc</td><td><code>Num</code></td><td>Shape parameter in Tsai’s equation defined for compression (rc)</tr>
<tr><td>xcrn</td><td><code>Num</code></td><td>Non-dimensional critical strain on compression envelope (<math>\epsilon</math>-cr, where the envelope curve starts following a straight line)</tr>
<tr><td>ft</td><td><code>Num</code></td><td>Tensile strength (ft)</tr>
<tr><td>et</td><td><code>Num</code></td><td>Strain at tensile strength (<math>\epsilon</math>t)</tr>
<tr><td>rt</td><td><code>Num</code></td><td>Shape parameter in Tsai’s equation defined for tension (rt)</tr>
<tr><td>xcrp</td><td><code>Num</code></td><td>Non-dimensional critical strain on tension envelope (<math>\epsilon</math> cr, where the envelope curve starts following a straight line – large value [e.g., 10000] recommended when tension stiffening is considered)</tr>
<tr><td>gap</td><td><code>Int</code></td><td>gap = 0, less gradual gap closure (default); gap = 1, more gradual gap closure</tr>

</tbody>
</table>
<!-- </blockquote> -->

</div>

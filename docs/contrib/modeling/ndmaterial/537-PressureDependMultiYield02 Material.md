# PressureDependMultiYield02

<p><strong>PressureDependMultiYield02</strong> material is modified from
<strong>PressureDependMultiYield</strong> material, with:</p>
<ol>
<li>additional parameters ($contrac3 and $dilat3) to account for
K&amp;sigma; effect,</li>
<li>a parameter to account for the influence of previous dilation
history on subsequent contraction phase ($contrac2), and</li>
<li>modified logic related to permanent shear strain accumulation
($liquefac1 and $liquefac2).</li>
</ol>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDMaterial PressureDependMultiYield02 $tag $nd $rho
$refShearModul $refBulkModul $frictionAng $peakShearStra $refPress
$pressDependCoe $PTAng $contrac1 $contrac3 $dilat1 $dilat3
&lt;$noYieldSurf=20 &lt;$r1 $Gs1 …&gt; $contrac2=5. $dilat2=3.
$liquefac1=1. $liquefac2=0. $e=0.6 $cs1=0.9 $cs2=0.02 $cs3=0.7 $pa=101
&lt;$c=0.1&gt;&gt;</strong></p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">contrac3</code></p></td>
<td><p>A non-negative constant reflecting K&amp;sigma; effect.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">dilat3</code></p></td>
<td><p>A non-negative constant reflecting K&amp;sigma; effect.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">contrac2</code></p></td>
<td><p>A non-negative constant reflecting dilation history on
contraction tendency.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">liquefac1</code></p></td>
<td><p>Damage parameter to define accumulated permanent shear strain as
a function of dilation history. <strong>(Redefined and different from
PressureDependMultiYield material).</strong></p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">liquefac2</code></p></td>
<td><p>Damage parameter to define biased accumulation of permanent shear
strain as a function of load reversal history. <strong>(Redefined and
different from PressureDependMultiYield material).</strong></p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">c</code></td>
<td><p>Numerical constant (default value = 0.1 kPa)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Others</strong></p></td>
<td><p>See PressureDependMultiYield material above.</p></td>
</tr>
</tbody>
</table>
<p><strong>NOTE:</strong></p>
<p>The following values are suggested for the model parameters.</p>
<table>
<tbody>
<tr class="odd">
<td></td>
<td><p>Dr=30%</p></td>
<td><p>Dr=40%</p></td>
<td><p>Dr=50%</p></td>
<td><p>Dr=60%</p></td>
<td><p>Dr=75%</p></td>
</tr>
<tr class="even">
<td><p>rho</p></td>
<td><p>1.7 ton/m&lt;sup&gt;3&lt;/sup&gt; or
1.59x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
<td><p>1.8 ton/m&lt;sup&gt;3&lt;/sup&gt; or
1.685x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
<td><p>1.9 ton/m&lt;sup&gt;3&lt;/sup&gt; or
1.778x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
<td><p>2.0 ton/m&lt;sup&gt;3&lt;/sup&gt; or
1.872x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
<td><p>2.1 ton/m&lt;sup&gt;3&lt;/sup&gt; or
1.965x10&lt;sup&gt;-4&lt;/sup&gt;
(lbf)(s&lt;sup&gt;2&lt;/sup&gt;)/in&lt;sup&gt;4&lt;/sup&gt;</p></td>
</tr>
<tr class="odd">
<td><p>refShearModul (at p’&lt;sub&gt;r&lt;/sub&gt;=80 kPa or 11.6
psi)</p></td>
<td><p>6x10&lt;sup&gt;4&lt;/sup&gt; kPa or
8.702x10&lt;sup&gt;3&lt;/sup&gt; psi</p></td>
<td><p>9x10&lt;sup&gt;4&lt;/sup&gt; kPa or
1.305x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>10x10&lt;sup&gt;4&lt;/sup&gt; kPa or
1.45x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>11x10&lt;sup&gt;4&lt;/sup&gt; kPa or
1.595x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
<td><p>13x10&lt;sup&gt;4&lt;/sup&gt; kPa or
1.885x10&lt;sup&gt;4&lt;/sup&gt; psi</p></td>
</tr>
<tr class="even">
<td><p>refBulkModu (at p’&lt;sub&gt;r&lt;/sub&gt;=80 kPa or 11.6
psi)</p></td>
<td><p>16x10&lt;sup&gt;4&lt;/sup&gt; kPa or
2.321x10&lt;sup&gt;4&lt;/sup&gt; psi
(K&lt;sub&gt;o&lt;/sub&gt;=0.5)</p></td>
<td><p>22x10&lt;sup&gt;4&lt;/sup&gt; kPa or
3.191x10&lt;sup&gt;4&lt;/sup&gt; psi
(K&lt;sub&gt;o&lt;/sub&gt;=0.47)</p></td>
<td><p>23.3x10&lt;sup&gt;4&lt;/sup&gt; kPa or
3.379x10&lt;sup&gt;4&lt;/sup&gt; psi
(K&lt;sub&gt;o&lt;/sub&gt;=0.45)</p></td>
<td><p>24x10&lt;sup&gt;4&lt;/sup&gt; kPa or
3.481x10&lt;sup&gt;4&lt;/sup&gt; psi
(K&lt;sub&gt;o&lt;/sub&gt;=0.43)</p></td>
<td><p>26x10&lt;sup&gt;4&lt;/sup&gt; kPa or
3.771x10&lt;sup&gt;4&lt;/sup&gt; psi
(K&lt;sub&gt;o&lt;/sub&gt;=0.4)</p></td>
</tr>
<tr class="odd">
<td><p>frictionAng</p></td>
<td><p>31</p></td>
<td><p>32</p></td>
<td><p>33.5</p></td>
<td><p>35</p></td>
<td><p>36.5</p></td>
</tr>
<tr class="even">
<td><p>PTAng</p></td>
<td><p>31</p></td>
<td><p>26</p></td>
<td><p>25.5</p></td>
<td><p>26</p></td>
<td><p>26</p></td>
</tr>
<tr class="odd">
<td><p>peakShearStra (at p’&lt;sub&gt;r&lt;/sub&gt;=101 kPa or 14.65
psi)</p></td>
<td><p>&lt;center&gt;0.1&lt;/center&gt;</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>refPress (p’&lt;sub&gt;r&lt;/sub&gt;,)</p></td>
<td><p>&lt;center&gt;101 kPa or 14.65 psi&lt;/center&gt;</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>pressDependCoe</p></td>
<td><p>&lt;center&gt;0.5&lt;/center&gt;</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Contrac1</p></td>
<td><p>0.087</p></td>
<td><p>0.067</p></td>
<td><p>0.045</p></td>
<td><p>0.028</p></td>
<td><p>0.013</p></td>
</tr>
<tr class="odd">
<td><p>Contrac3</p></td>
<td><p>0.18</p></td>
<td><p>0.23</p></td>
<td><p>0.15</p></td>
<td><p>0.05</p></td>
<td><p>0.0</p></td>
</tr>
<tr class="even">
<td><p>dilat1</p></td>
<td><p>0.</p></td>
<td><p>0.06</p></td>
<td><p>0.06</p></td>
<td><p>0.1</p></td>
<td><p>0.3</p></td>
</tr>
<tr class="odd">
<td><p>dilat3</p></td>
<td><p>0.0</p></td>
<td><p>0.27</p></td>
<td><p>0.15</p></td>
<td><p>0.05</p></td>
<td><p>0.0</p></td>
</tr>
<tr class="even">
<td><p>e</p></td>
<td><p>0.85</p></td>
<td><p>0.77</p></td>
<td><p>0.7</p></td>
<td><p>0.65</p></td>
<td><p>0.55</p></td>
</tr>
</tbody>
</table>
<h2
id="pressure_dependent_multiyield02_material_examples"><strong>Pressure
Dependent MultiYield02 Material Examples:</strong></h2>
<p>&lt;table border=1 width=800&gt; &lt;tr&gt; &lt;td&gt;<a
href="PressureDependMultiYield02-Example_1" title="wikilink">Example
1</a>&lt;/td&gt;</p>
<p>&lt;td&gt;Single 2D 9-4 noded element, subjected to sinusoidal base
shaking (PressureDepend02 material)&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt;
&lt;td&gt;<a href="PressureDependMultiYield02-Example_2"
title="wikilink">Example 2</a>&lt;/td&gt; &lt;td&gt;Single 3D brick
element, subjected to sinusoidal base shaking (PressureDepend02
material)&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt;</p>
<p>&lt;td&gt;<a href="PressureDependMultiYield02-Example_3"
title="wikilink">Example 3</a>&lt;/td&gt; &lt;td&gt;Single 3D 20-8 noded
element, subjected to sinusoidal base shaking (PressureDepend02
material)&lt;/td&gt; &lt;/tr&gt; &lt;/table&gt;</p>
<p>Code Developed by: <span style="color:blue"> UC San Diego (Dr.
Zhaohui Yang)</span>:</p>
<hr />
<p>UC San Diego Soil Model: </p>

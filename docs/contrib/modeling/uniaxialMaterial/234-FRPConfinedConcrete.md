# FRPConfinedConcrete

<p>This command is used to construct a uniaxial
Megalooikonomou-Monti-Santini concrete material object with degraded
linear unloading/reloading stiffness according to the work of
Karsan-Jirsa and no tensile strength.</p>

```tcl
uniaxialMaterial FRPConfinedConcrete $matTag $fpc1 $fpc2
        $epsc0 $D $c $Ej $Sj $tj $eju $S $fyl $fyh $dlong $dtrans $Es $vo $k
        $useBuck
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">fpc1</code></p></td>
<td><p>concrete core compressive strength.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">fpc2</code></p></td>
<td><p>concrete cover compressive strength.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">epsc0</code></td>
<td><p>strain corresponding to unconfined concrete strength.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">D</code></td>
<td><p>diameter of the circular section.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">c</code></td>
<td><p>dimension of concrete cover (until the outer edge of steel
stirrups)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Ej</code></td>
<td><p>elastic modulus of the fiber reinforced polymer (FRP)
jacket.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Sj</code></td>
<td><p>clear spacing of the FRP strips - zero if FRP jacket is
continuous.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">tj</code></td>
<td><p>total thickness of the FRP jacket.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">eju</code></td>
<td><p>rupture strain of the FRP jacket from tensile coupons.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">S</code></td>
<td><p>spacing of the steel spiral/stirrups.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fyl</code></td>
<td><p>yielding strength of longitudinal steel bars.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fyh</code></td>
<td><p>yielding strength of the steel spiral/stirrups.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">dlong</code></td>
<td><p>diameter of the longitudinal bars of the circular
section.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">dtrans</code></td>
<td><p>diameter of the steel spiral/stirrups.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Es</code></td>
<td><p>elastic modulus of steel.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">vo</code></td>
<td><p>initial Poisson’s coefficient for concrete.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">k</code></td>
<td><p>reduction factor for the rupture strain of the FRP jacket,
recommended values 0.5-0.8.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">useBuck</code></td>
<td><p>FRP jacket failure criterion due to buckling of longitudinal
compressive steel bars (0 = not include it, 1= to include it).</p></td>
</tr>
</tbody>
</table>
<p><strong>NOTES:</strong></p>
<p>• IMPORTANT: The units of the input parameters should be in MPa, N,
mm.</p>
<p>• Concrete compressive strengths and the corresponding strain should
be input as positive values.</p>
<p>• When rupture of FRP jacket occurs due to dilation of concrete
(lateral concrete strain exceeding reduced rupture strain of FRP
jacket), the analysis is not terminated. Only a message “FRP Rupture” is
plotted on the screen.</p>
<p>• When `useBuck` input parameter is on (equal to 1) and the model's
longitudinal steel buckling conditions are fulfilled, a message
“Initiation of Buckling of Long.Bar under Compression” is plotted on the
screen.</p>
<p>• When rupture of FRP jacket occurs due to its interaction with
buckled longitudinal compressive steel bars, the analysis is not
terminated. Only a message “FRP Rupture due to Buckling of Long.Bar
under compression” is plotted on the screen.</p>

<p><strong>Typical Hysteretic Stress-Strain Relation for
FRPConfinedConcrete.</strong></p>

<figure>
<img src="/OpenSeesRT/contrib/static/Figure_1_.jpg" title="Figure_1_.jpg" width="600"
alt="Figure_1_.jpg" />
<figcaption aria-hidden="true">Figure_1_.jpg</figcaption>
</figure>
<p><strong>EXAMPLES:</strong></p>
<p>Example: Cantilever FRP-Confined Circular Reinforced Concrete Column
under Cyclic Lateral Loading</p>
<p><strong>Cantilever Column Model Definition.</strong></p>
<figure>
<img src="/OpenSeesRT/contrib/static/Figure_2.jpg" width="600"
alt="Figure_2.jpg" />
<figcaption aria-hidden="true">Figure_2.jpg</figcaption>
</figure>

The cantilever column was modeled by a linear beam element with its
stiffness corresponding to flexural yielding and by a fiber element at
the plastic hinge which is used in order to capture the flexural
hysteretic behavior. The length of the fiber element was assumed to be
half of the column’s diameter. A rotational spring at the bottom of the
column represents the longitudinal bar pullout from the footing and was
assumed to have an elastic stiffness. According to FRPConfinedConcrete
model, the averaged response of the two different regions - concrete
core (confined by both the FRP &amp; the existing reinforcement) and
concrete cover (confined only with the FRP wrap) - in the cross-section
allows the assignment of a unique stress-strain law
(FRPConfinedConcrete) to all the concrete fibers/layers of the circular
section.

<p><strong>Input Files:</strong></p>
<p>For Tcl Interpreter: <img src="ExampleFRP.tcl" title="ExampleFRP.tcl"
alt="ExampleFRP.tcl" /></p>


<p><strong>Response of Cantilever FRP-Confined Circular Reinforced
Concrete Column under Cyclic Lateral Loading.</strong></p>
<figure>
<img src="/OpenSeesRT/contrib/static/Figure_3.jpg" width="600" alt="Figure_3.jpg" />
<figcaption aria-hidden="true">Figure 3</figcaption>
</figure>
<hr />

## References
<p>• MEGALOOIKONOMOU K.G., MONTI G., SANTINI S., “Constitutive Model for
Fiber -Reinforced Polymer - and Tie - Confined Concrete”, ACI Structural
Journal, Vol. 109, No. 4, July 2012, pp. 569-578. <a
href="https://doi.org/10.14359/51683876">https://doi.org/10.14359/51683876</a></p>
<p>• KARSAN, I.D., JIRSA, J.O., “Behaviour of concrete under compressive
loadings”, Journal of Structural Division ASCE, Vol. 95, No. 12, 1969,
pp. 2543-2563. <a
href="https://doi.org/10.1061/JSDEAG.0002424">https://doi.org/10.1061/JSDEAG.0002424</a></p>
<p>• MEGALOOIKONOMOU K.G., "Seismic Assessment and Retrofit of
Reinforced Concrete Columns", Cambridge Scholars Publishing, ISBN (10):
1-5275-2785-9, ISBN (13): 978-1-5275-2785-0, 2019, p. 387. <a
href="https://www.cambridgescholars.com/product/978-1-5275-2785-0">https://www.cambridgescholars.com/product/978-1-5275-2785-0</a></p>
<p>• MEGALOOIKONOMOU K.G., MONTI G., "Numerical Modeling of
FRP-Retrofitted Circular RC Columns Including Shear", In Proceedings of:
5th International Conference on Computational Methods in Structural
Dynamics and Earthquake Engineering (COMPDYN 2015), Crete Island,
Greece, May 25 - 27, 2015. <a
href="https://doi.org/10.7712/120115.3663.400">https://doi.org/10.7712/120115.3663.400</a></p>
<p>• MEGALOOIKONOMOU K.G. (2019, December). Modeling the behavior of
shear-critical reinforced concrete columns under lateral loads. Ph.D.
Thesis, Department of Civil and Environmental Engineering, Faculty of
Engineering, University of Cyprus, Nicosia, Cyprus. <a
href="https://doi.org/10.12681/eadd/47504">https://doi.org/10.12681/eadd/47504</a></p>
<p>• GALLARDO - ZAFRA R., KAWASHIMA, K., “Analysis of CFRP RC Bridge
Columns under Lateral Cyclic Loading”, Journal of Earthquake
Engineering, Vol. 13, 2009, pp. 129-154. <a
href="https://doi.org/10.1080/13632460802347455">https://doi.org/10.1080/13632460802347455</a></p>
<hr />
<p><strong>Code developed by:</strong></p>
<p>Dr.-Ing. Konstantinos G. Megalooikonomou, Onassis Foundation Scholar,
University of Cyprus (Webpage: <a
href="https://bigeconomy.gr/en/">https://bigeconomy.gr/en/</a>).</p>

 # Fatigue

<p>The fatigue material uses a modified rainflow cycle counting
algorithm to accumulate damage in a material using Miner’s Rule. Element
stress/strain relationships become zero when fatigue life is
exhausted.</p>

```tcl
uniaxialMaterial Fatigue $matTag $tag &lt;-E0 $E0&gt;
        &lt;-m $m&gt; &lt;-min $min&gt; &lt;-max $max&gt;
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>Unique material object integer tag for the material that is being
wrapped</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">E0</code></td>
<td><p>Value of strain at which one cycle will cause failure (default
0.191)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">m</code></td>
<td><p>Slope of Coffin-Manson curve in log-log space (default
-0.458)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">min</code></td>
<td><p>Global minimum value for strain or deformation (default
-1e16)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">max</code></td>
<td><p>Global maximum value for strain or deformation (default
1e16)</p></td>
</tr>
</tbody>
</table>
<h2 id="description">Description</h2>
<p>This material model accounts for the effects of low cycle fatigue. A
modified rainflow cycle counter has been implemented to track strain
amplitudes. This cycle counter is used in concert with a linear strain
accumulation model (i.e. Miner’s Rule), based on Coffin-Manson log-log
relationships describing low cycle fatigue failure. This material wraps
around another material and does not influence the stress-strain (or
force-deformation) relationship of the parent material.</p>
<p>Once the Fatigue material model reaches a damage level of 1.0, the
force (or stress) of the parent material becomes zero (1.0x10-8 times
the call to the material). If failure is triggered in compression, the
material stress is dropped at the next zero-force crossing (i.e.
compression force never drops to zero).</p>
<p>The Fatigue material assumes that each point is the last point of the
history, and tracks damage with this assumption. If failure is not
triggered, this pseudo-peak is discarded.</p>
<p>The material also has the ability to trigger failure based on a
maximum or minimum strain (i.e. not related to fatigue). The default for
these values is set to very large numbers.</p>
<p>The default values are calibrated parameters from low cycle fatigue
tests of European steel sections Ballio and Castiglioni (1995), for more
information about how material was calibrated, the user is directed to
Uriz (2005).</p>
<p>Valid recorder objects for the material are ‘stress’,’tangent’,
‘strain’, ‘stressStrain’, and ‘damage’. The stress, strain, and tangent
recorder options must be available in the material that you are
wrapping.</p>
<p><strong>NOTE:</strong> Here you can find more information of how to
create 'damage' recorders: <a
href="http://opensees.berkeley.edu/community/viewtopic.php?f=2&amp;t=54193">link</a></p>
<h2 id="example">Example:</h2>
<p><em>Click to Download</em></p>
<p><a href="Media:FatigueExample.tcl"
title="wikilink">Media:FatigueExample.tcl</a></p>
<p><a href="Media:RandomStrainHstory.tcl"
title="wikilink">Media:RandomStrainHstory.tcl</a></p>
<figure>
<img src="/OpenSeesRT/contrib/static/DamageExample.jpg" title="DamageExample.jpg"
alt="DamageExample.jpg" />
<figcaption aria-hidden="true">DamageExample.jpg</figcaption>
</figure>
<h2 id="references">References:</h2>
<p>Uriz, Patxi (2005) “Towards Earthquake Resistant Design of
Concentrically Braced Steel Structures,” Doctoral Dissertation,
Structural Engineering, Mechanics, and Materials, Department of Civil
and Environmental Engineering, University of California, Berkeley,
December 2005</p>
<p>Ballio, G., and Castiglioni, C. A. (1995). "A Unified Approach for
the Design of Steel Structures under Low and/or High Cycle Fatigue."
Journal of Constructional Steel Research, 34, 75-101.</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Patxi Uriz,
Exponent </span></p>

# InitialStateAnalysisWrapper

<p>This command is used to construct an InitialStateAnalysisWrapper
nDMaterial object.</p>

```tcl
nDMaterial InitialStateAnalysisWrapper $matTag $nDMatTag
        $nDim
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique integer tag identifying nDMaterial object</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">nDMatTag</code></td>
<td><p>the tag of the associated nDMaterial object</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">nDim</code></td>
<td><p>number of dimensions (2 for 2D, 3 for 3D)</p></td>
</tr>
</tbody>
</table>
<hr />
<p>The InitialStateAnalysisWrapper nDMaterial allows for the use of the
InitialStateAnalysis command for setting initial conditions. The
InitialStateAnalysisWrapper can be used with any nDMaterial. This
material wrapper allows for the development of an initial stress field
while maintaining the original geometry of the problem. An example
analysis is provided below to demonstrate the use of this material
wrapper object.</p>
<p><strong>NOTES:</strong></p>
<ol>
<li>There are no valid recorder queries for the
InitialStateAnalysisWrapper.</li>
<li>The <em>InitialStateAnalysis off</em> command removes all previously
defined recorders. Two sets of recorders are needed if the results
before and after this command are desired. See the example below for
more.</li>
<li>The InitialStateAnalysisWrapper material is somewhat tricky to use
in dynamic analysis. Sometimes setting the displacement to zero appears
to be interpreted as an initial displacement in subsequent steps,
resulting in undesirable vibrations.</li>
</ol>
<p><strong>EXAMPLES:</strong></p>
<p>InitialStateAnalysisWrapper definition with material tag 1, and
associated nDMaterial tag 2 for a 2D analysis</p>
<p>nDMaterial InitialStateAnalysisWrapper 1 2 2</p>
<hr />
<p>Code Developed by: <span style="color:blue"> Chris McGann,
Pedro Arduino, &amp; Peter Mackenzie-Helnwein, at the University of
Washington </span></p>
<hr />
<p><strong>EXAMPLE ANALYSIS:</strong></p>
<p>The example input file below demonstrates an how the
InitialStateAnalysis command can be used with the
InitialStateAnalysisWrapper to generate a gravitational state of stress
in a single element. As shown below, the use of the InitialStateAnalysis
command necessitates the use of two sets of recorders, one to record
results during the initial state analysis, and one for all subsequent
steps. It is not required to record results during the initial state
analysis, but the example below includes this data to demonstrate the
effect of the InitialStateAnalysis command. At the end of the analysis,
there should be non-zero stress and strain in the element with zero
displacement.</p>
<p>
```tcl
 wipe</p>
<p>model BasicBuilder -ndm 3 -ndf 3</p>
<ol>
<li>create the nodes</li>
</ol>
<p>node 1 1.0 0.0 0.0 node 2 1.0 1.0 0.0 node 3 0.0 1.0 0.0 node 4 0.0
0.0 0.0 node 5 1.0 0.0 1.0 node 6 1.0 1.0 1.0 node 7 0.0 1.0 1.0 node 8
0.0 0.0 1.0</p>
<ol>
<li>boundary conditions</li>
</ol>
<p>fix 1 1 1 1 fix 2 1 1 1 fix 3 1 1 1 fix 4 1 1 1 fix 5 1 1 0 fix 6 1 1
0 fix 7 1 1 0 fix 8 1 1 0</p>
<ol>
<li>define main material obeject</li>
</ol>
<p>nDMaterial ElasticIsotropic 1 25000 0.35</p>
<ol>
<li>define material wrapper</li>
</ol>
<p>nDMaterial InitialStateAnalysisWrapper 2 1 3</p>
<ol>
<li>create the element (NOTE: the material tag associated with this
element is that of the wrapper)</li>
</ol>
<p>element SSPbrick 1 1 2 3 4 5 6 7 8 2 0.0 0.0 -17.0</p>
<ol>
<li>create the pre-gravity recorders</li>
</ol>
<p>set step 0.1</p>
<p>recorder Node -time -file Gdisp.out -dT $step -nodeRange 5 8 -dof 1 2
3 disp recorder Element -ele 1 -time -file Gstress.out -dT $step stress
recorder Element -ele 1 -time -file Gstrain.out -dT $step strain</p>
<ol>
<li>create the gravity analysis</li>
</ol>
<p>integrator LoadControl 0.5 numberer RCM system SparseGeneral
constraints Transformation test NormDispIncr 1e-5 40 1 algorithm Newton
analysis Static</p>
<ol>
<li>turn on the initial state analysis feature</li>
</ol>
<p>InitialStateAnalysis on</p>
<ol>
<li>analyze four steps</li>
</ol>
<p>analyze 4</p>
<ol>
<li>turn off the initial state analysis feature</li>
</ol>
<p>InitialStateAnalysis off</p>
<ol>
<li>create post-gravity recorders</li>
</ol>
<p>recorder Node -time -file disp.out -dT $step -nodeRange 5 8 -dof 1 2
3 disp recorder Element -ele 1 -time -file stress.out -dT $step stress
recorder Element -ele 1 -time -file strain.out -dT $step strain</p>
<ol>
<li>analyze for three steps, should have non-zero stress and strain with
zero displacement</li>
</ol>
<p>analyze 3</p>
<p>wipe 
```
</p>

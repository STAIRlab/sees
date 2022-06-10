---
description: Plane Stress Concrete Materials
...

# ReinforcedConcretePlaneStress

<p><span style="color:red"> WARNING .. AT PRESENT CODE AS
SUBMITTED DOES NOT APPEAR TO WORK .. LOOK AT CONVERGENCE IN
EXAMPLE</span></p>

<p>A number of Reinforced and Prestressed Concrete Plane Stress
Materials are available. The ones on this page have been provided the
University of Houston and are based on the Cyclic Softened Membrane
Model (CSMM). They are capable of modeling the cyclic shear behavior of
prestressed and reinforced concrete membranes.</p>


<hr />

<p>This command is used to construct a Reinforced Concrete Plane Stress
material object based on Rotating Angle Theory with steel along two
directions.</p>

```tcl
nDMaterial ReinforcedConcretePlaneStress matTag? rho? s1?
        s2? c1? c2? angle1? angle2? rou1? rou2? fpc? fy? E0?
        epsc0?
```

<p>This command is used to construct a Reinforced Concrete Plane Stress
material object based on Fixed Angle theory with steel along two
directions.</p>

```tcl
nDMaterial FAReinforcedConcretePlaneStress matTag? rho?
        s1? s2? c1? c2? angle1? angle2? rou1? rou2? fpc? fy? E0?
        epsc0?
```

<p>This command is used to construct a Reinforced Concrete Plane Stress
material object based on Rotating Angle theory with steel along four
directions.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDMaterial RAFourSteelRCPlaneStress matTag? rho?
UniaxiaMatTag1? UniaxiaMatTag2? UniaxiaMatTag3? UniaxiaMatTag4?
UniaxiaMatTag5? UniaxiaMatTag6? angle1? angle2? angle3? angle4? rou1?
rou2? rou3? rou4? fpc? fy? E0? epsc0?</strong></p></td>
</tr>
</tbody>
</table>

<p>This command is used to construct a Reinforced Concrete Plane Stress
material object based on Fixed Angle theory with steel along four
directions.</p>
<table>
<tbody>
<tr class="odd">
<td><p><strong>nDMaterial FAFourSteelRCPlaneStress matTag? rho?
    UniaxiaMatTag1? UniaxiaMatTag2? UniaxiaMatTag3? UniaxiaMatTag4?
    UniaxiaMatTag5? UniaxiaMatTag6? angle1? angle2? angle3? angle4? rou1?
    rou2? rou3? rou4? fpc? fy? E0? epsc0?</strong></p></td>
</tr>
</tbody>
</table>

<p>This command is used to construct a Prestressed Concrete Plane Stress
material object based on Rotating Angle Theory with steel along two
directions.</p>

```tcl
nDMaterial PrestressedConcretePlaneStress matTag? rho?
        t1? s1? c1? c2? angle1? angle2? rou1? rou2? pstrain? fpc? fyT? fy2? E0?
        epsc0?
```

<p>This command is used to construct a Prestressed Concrete Plane Stress
material object based on Fixed Angle theory with steel along two
directions.</p>

```tcl
nDMaterial FAPrestressedConcretePlaneStress matTag? rho?
        t1? s2? c1? c2? angle1? angle2? rou1? rou2? pstrain? fpc? fyT? fy? E0?
        epsc0?
```

<p>This command is used to construct a Prestressed Concrete Plane Stress
material object based on Rotating Angle Theory with steel along four
directions.</p>

```tcl
nDMaterial RAFourSteelPCPlaneStress matTag? rho?
        UniaxiaMatTag1? UniaxiaMatTag2? UniaxiaMatTag3? UniaxiaMatTag4? angle1?
        angle2? rou1? rou2? pstrain? fpc? fyT? fy? E0? epsc0?
```

<p>This command is used to construct a Prestresed Concrete Plane Stress
material object based on Fixed Angle theory with steel along four
directions.</p>

```tcl
nDMaterial FAFourSteelPCPlaneStress matTag? rho? t1? t2?
        s3? s4? c1? c2? angle1? angle2? angle3? angle4? rou1? rou2? rou3? rou4?
        pstrain1? pstrain2? fpc? fyT? fy? E0? epsc0?
```

<hr />

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rho</code></td>
<td><p>material density</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">t1 t2</code></p></td>
<td><p>material tags for uniaxial materials of type
<strong>TendonL01</strong></p></td>
</tr>
<tr class="even">
<td><p><code>s1 s2 ..</code></p></td>
<td><p>material tags for uniaxial materials of type <strong>SteelZ01</strong></p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">c1 c2</code></p></td>
<td><p>material tags for uniaxial materials of type <strong>ConcreteL01, ConcreteZ01</strong></p></td>
</tr>
<tr class="even">
<td><p><code>angle1 angle2 ...</code></p></td>
<td><p>angle of $i$'th (steel or tendon) layer to x coordinate</p></td>
</tr>
<tr class="odd">
<td><p><code>rou1 rou2 ...</code></p></td>
<td><p>steel ratio of the $i$'th layer.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">pstrain1 pstrain2</code></p></td>
<td><p>initial strain in tendons</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fpc</code></td>
<td><p>compressive strength of concrete</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fyT</code></td>
<td><p>yield strength of tendons</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fy</code></td>
<td><p>yield strength of steel</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">E0</code></td>
<td><p>initial stiffness of steel (Young's Modulus)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsc0</code></td>
<td><p>compressive strain of concrete</p></td>
</tr>
</tbody>
</table>

<hr />

<p>A number of special uniaxial materials are needed for these
materials. These materials are created using the following
uniaxialMaterial commands.</p>

```tcl
uniaxialMaterial SteelZ01 tag? fy? E0? fpc? rou? <ac?> <rc?>
```


```tcl
uniaxialMaterial TendonL01 tag? fpy? Eps? fpc? rou? epsp? <ac?> <rc?>
```


```tcl
uniaxialMaterial ConcreteL01 tag? fpc? epsc0?
```


```tcl
uniaxialMaterial ConcreteZ01 tag? fpc? epsc0?
```

<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>unique uniaxial integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fy</code></td>
<td><p>yield strength bare steel</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">E0</code></td>
<td><p>initial stiffness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fpc</code></td>
<td><p>compressive strength of concrete</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsc0</code></td>
<td><p>strain at compressive strength</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rou</code></td>
<td><p>steel ratio</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">epsp</code></td>
<td><p>prestress strain</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ac</code></td>
<td><p>unloading path parameter (default = 1.9)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">rc</code></td>
<td><p>reloading path parameter (default = 10.0)</p></td>
</tr>
</tbody>
</table>
<hr />
<p>EXAMPLE</p>
<p><a href="N_FSW13.tcl" title="wikilink">N_FSW13.tcl</a></p>
<hr />

## References

<p>T.T.C. Hsu and Y.L. Mo, "Unified Theory of Concrete Structures", Wiley, COMING APRIL 2010</p>
<p>Y.L. Mo, J. Zhong, T.T.C. Hsu, "Seismic simulation of RC wall-type
structures",Engineering Structures, 30(11), 3167-3175, 2008.</p>

<hr />

Code developed by:
<span style="color:blue"> A. Laskar</span>, 
<span style="color:blue"> J. Zhong</span>, 
<span style="color:blue"> <a href="http://www.egr.uh.edu/cive/faculty/mo/?e=main">Y.L. Mo</a></span> and 
<span style="color:blue"> <a href="http://www.egr.uh.edu/cive/faculty/hsu/">Thomas T.C. Hsu</a></span>, University of Houston.


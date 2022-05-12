# Cusp

<p>CuSPSolver is a linear sparse system solver based on CUSP Sparse
library for OpenSEES. All the algorithms and the preconditioners
supported by CUSP can be used in this solver. It can be invoked by a
simple statement, which means it is very easy to use. Due to it's
hardware and softawre requirements it is not built into the main
OpenSees executable.</p>
<p>Hardware Requirements: GPU: NVIDIA’s GPU’s with the CUDA™
architecture.</p>
<ul>
<li>The list of CUDA-supported
GPUs：https://developer.nvidia.com/cuda-gpus</li>
</ul>
<p>Software： OS: Windows XP 32/64-bit or later CUDA 5.5 Production
Release CuSP 0.4.0 CuSPSolver package`</p>
<p>Installation Process:</p>
<p>1) Download the CUDA Toolkit 5.5 package from the official website of
NVIDIA (choose the package which is consistent with your OS ), and
install it. NOTE currently we are using CUDA 5.5, even though CUDA is
now at release 6.0 (we will upgrade once CuSP upgrades to 6.0)</p>
<p><a
href="https://developer.nvidia.com/cuda-toolkit-55-archive">https://developer.nvidia.com/cuda-toolkit-55-archive</a></p>
<p>2) Install the CuSP library</p>
<p>download：https://github.com/cusplibrary/cusplibrary</p>
<p>3) Download one of the .dll's we provide based on either your &lt;a
href="<a
href="http://opensees.berkeley.edu/OpenSees/code/cusp/32/CuSPSolver.dll%22%3E">http://opensees.berkeley.edu/OpenSees/code/cusp/32/CuSPSolver.dll"&gt;</a>;
32&lt;/a&gt; or &lt;a href="<a
href="http://opensees.berkeley.edu/OpenSees/code/cusp/64/CuSPSolver.dll%22%3E">http://opensees.berkeley.edu/OpenSees/code/cusp/64/CuSPSolver.dll"&gt;</a>;
64 version of windows.</p>

```tcl
system CuSP -rTol $RTOL -mInt $MINT -pre $PRE -solver
        $SOLVER
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">RTOL</code></p></td>
<td><p>Set the relative tolerance.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">MINT</code></p></td>
<td><p>Set the maximum number of iterations.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">PRE</code></p></td>
<td><p>Set the preconditioner. can be none, diagonal, and ainv</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">SOLVER</code></p></td>
<td><p>Set the iterative solver. can be bicg, bicgstab, cg, and
gmres.</p></td>
</tr>
</tbody>
</table>

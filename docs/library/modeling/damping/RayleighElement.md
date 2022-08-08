# Rayleigh Damping

This command is used to assign damping to all previously-defined
elements and nodes. When using Rayleigh damping in OpenSees, the damping
matrix for an element or node, $D$ is specified as a combination of
stiffness and mass-proportional damping matrices:

$$
D = \alpha_M M + \beta_K K_{t} + \beta_\text{Kinit} K_{0} + \beta_\text{Kcomm} K_{t - 1}
$$

```tcl
setElementRayleighDampingFactors $alphaM $betaK $betaK0 $betaKc
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">alphaM</code></p></td>
<td><p>factor applied to elements or nodes mass matrix</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">betaK</code></p></td>
<td><p>factor applied to elements current stiffness matrix.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">betaKinit</code></p></td>
<td><p>factor applied to elements initial stiffness matrix.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">betaKcomm</code></p></td>
<td><p>factor applied to elements committed stiffness matrix.</p></td>
</tr>
</tbody>
</table>

<p>NOTE:</p>
<ol>
<li>The command overwrites any existing damping coeeficients at the
  Elements and Nodes.</li>

<li>The following paper is something that you should read if you are new
  to the damping and nonlinear analysis. 
  Finley A. Charney, "Unintended Consequences of Modeling Damping in Structures", J. Struct. Engrg.
  Volume 134, Issue 4, pp. 581-592 (April 2008) <a
  href="http://dx.doi.org/10.1061/(ASCE)0733-9445(2008)134:4(581)">DOI</a></li>

<li>Other useful papers to read:
<ol>

<li>Petrini, Lorenza , Maggi, Claudio , Priestley, M. J. Nigel and
  Calvi, G. Michele (2008) "Experimental Verification of Viscous Damping
  Modeling for Inelastic Time History Analyzes", Journal of Earthquake
  Engineering, 12:S1, pp. 125 — 145 <a
  href="http://www.tandfonline.com/doi/abs/10.1080/13632460801925822">DOI</a></li>

<li>Hall, J. F.(2006) "Problems encountered from the use (or misuse) of
  Rayleigh damping," Earthquake Engineering and Structural Dynamic, 35,
  525-545 <a href="http://onlinelibrary.wiley.com/doi/10.1002/eqe.541/abstract">DOI</a></li>
</ol></li>
</ol>

## Examples

<p>rayleigh 0.01 0.02 0.0 0.0</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

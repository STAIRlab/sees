# Newton with Line Search

<p>This command is used to construct a NewtonLineSearch algorithm object
which introduces line search to the <a href="Newton_Algorithm"
title="wikilink"> Newton-Raphson</a> algorithm to solve the nonlinear
residual equation. Line search increases the effectiveness of the Newton
method when convergence is slow due to roughness of the residual. The
command is of the following form:</p>

```tcl
algorithm NewtonLineSearch < -type $typeSearch >
        < -tol $tol > < -maxIter $maxIter > 
        < -minEta $minEta > < -maxEta $maxEta >
```

<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">typeSearch</code></p></td>
<td><p>line search algorithm. optional default is InitialInterpoled.
valid types are:</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>Bisection, Secant, RegulaFalsi, InitialInterpolated</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">tol</code></p></td>
<td><p>tolerance for search. optional, defeulat = 0.8</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">maxIter</code></p></td>
<td><p>max num of iterations to try. optional, default = 10</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">minEta</code></p></td>
<td><p>a min &lt;math&gt;\eta\!&lt;/math&gt; value. optional, default =
0.1</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">maxEta</code></p></td>
<td><p>a max &lt;math&gt;\eta\!&lt;/math&gt; value. optional, default =
10.0</p></td>
</tr>
</tbody>
</table>
<hr />
## References
<p>M.A. Crisfield, "Nonlinear Finite Element Analysis of Solids and
Structures, Volume 1:Essentials", Wiley, 1991.</p>
<hr />

## Theory

<p>The rationale behin line search is that:</p>
<ul>
<li>the direction &lt;math&gt;\Delta U\,\!&lt;/math&gt; found by the <a
href="Newton_Algorithm" title="wikilink"> Newton-Raphson method</a> is
often a good direction, but the step size &lt;math&gt;\parallel\Delta
U\parallel&lt;/math&gt; is not.</li>
<li>It is cheaper to compute the residual for several points along
&lt;math&gt;\Delta U\,\!&lt;/math&gt; rather than form and factor a new
system Jacobian</li>
</ul>
<p>In NewtonLineSearch the regular <a href="Newton_Algorithm"
title="wikilink"> Newton-Raphson method</a> is used to compute the
&lt;math&gt;\Delta U\,\!&lt;/math&gt;, but the update that is used is
modified. The modified update is:</p>

$$ U_{n+1} = U_n + \eta \Delta U\,\!$$


<p>The different line search algorithms use different root finding
methods to obtain &lt;math&gt;\eta\,\!&lt;/math&gt;, a root to the
function $s(\eta)$ defined as:</p>

$$ s(\eta) = \Delta U R(U_{n} + \eta \Delta
U)\,\!$$


<p>with</p>

$$ s_0 = \Delta U R(U_n),\!$$


<h2 id="interpolated_line_search">Interpolated Line Search:</h2>
<p>while (&lt;math&gt;\frac{s_n}{s_0}\!&lt;/math&gt; &gt; $tol
&amp;&amp; count &lt; $maxIter} {</p>

$$ \eta_{n+1} = \frac{\eta_n *s0}{s0 -s_{n+1}}
,\!$$


<p>}</p>
<p>__NOTOC__</p>
<h2 id="regulafalsi_line_search">RegulaFalsi Line Search:</h2>
<p>while (&lt;math&gt;\frac{s_n}{s_0}\!&lt;/math&gt; &gt; $tol
&amp;&amp; count &lt; $maxIter} {</p>

$$ \eta_{n+1} = \eta_U - \frac{s_U*(\eta_L-\eta_U)}{s_L-S_U}
,\!&lt;/math&gt;
</dd>
<dd>
if &lt;math&gt; s_{n+1} * s_L &lt; 0 \Rightarrow \eta_U = \eta_{n+1},
s_U = s_{n+1},\!&lt;/math&gt;
</dd>
<dd>
if &lt;math&gt; s_{n+1} * s_U &lt; 0 \Rightarrow \eta_L = \eta_{n+1},
s_L = s_{n+1},\!$$


<p>}</p>
<h2 id="bisection_line_search">Bisection Line Search:</h2>
<p>while (&lt;math&gt;\frac{s_n}{s_0}\!&lt;/math&gt; &gt; $tol
&amp;&amp; count &lt; $maxIter} {</p>

$$ \eta_{n+1} = \frac{\eta_L - \eta_U}{2.0} ,\!&lt;/math&gt;
</dd>
<dd>
if &lt;math&gt; s_{n+1} * s_L &lt; 0 \Rightarrow \eta_U = \eta_{n+1},
s_U = s_{n+1},\!&lt;/math&gt;
</dd>
<dd>
if &lt;math&gt; s_{n+1} * s_U &lt; 0 \Rightarrow \eta_L = \eta_{n+1},
s_L = s_{n+1},\!$$


<p>}</p>
<h2 id="secant_line_search">Secant Line Search:</h2>
<p>while (&lt;math&gt;\frac{s_n}{s_0}\!&lt;/math&gt; &gt; $tol
&amp;&amp; count &lt; $maxIter} {</p>

$$ \eta_{n+1} = \eta_j -
\frac{s_j*(\eta_{j-1}-\eta_j)}{s_{j-1}-S_j} ,\!&lt;/math&gt;
</dd>
<dd>
if &lt;math&gt; s_{n+1} * s_L &lt; 0 \Rightarrow \eta_U = \eta_{n+1},
s_U = s_{n+1},\!&lt;/math&gt;
</dd>
<dd>
if &lt;math&gt; s_{n+1} * s_U &lt; 0 \Rightarrow \eta_L = \eta_{n+1},
s_L = s_{n+1},\!$$


<p>}</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

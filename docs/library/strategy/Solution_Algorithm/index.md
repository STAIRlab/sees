# Solution Algorithm

The `algorithm` field configures a `SolutionAlgorithm` object, which
determines the sequence of steps taken to solve a non-linear system of
equations.

This object defines the sequence of operations performed by the the `Integrator` and
the `LinearSOE` objects in solving the equilibrium equation $R(U) = 0$
given the current state of the domain at each time step in a direct
integration analysis or load increment in a static analysis.

<hr />

<p>The following algorithms are available:</p>
<ul>
<li><a href="Linear" >Linear</a></li>
<li><a href="Newton" >Newton</a></li>
<li><a href="Newton_with_Line_Search" >Newton with Line Search</a></li>
<li><a href="Modified_Newton" >Modified Newton</a></li>
<li><a href="Krylov-Newton" >Krylov-Newton</a></li>
<li><a href="Secant_Newton" >Secant Newton</a></li>
<li><a href="BFGS" >BFGS</a></li>
<li><a href="Broyden" >Broyden</a></li>
</ul>

# GeneralizedAlpha

$\alpha_F$ and $\alpha_M$ are defined differently than in the paper, we use $\alpha_F = (1-\alpha_f)$ and $\alpha_M=(1-\gamma_m)$ where $\alpha_f$ and $\alpha_m$ are those used in the paper.
Like Newmark and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.

- $\alpha_M = 1.0, \alpha_F = 1.0$ produces the Newmark Method.
- $\alpha_M = 1.0$ corresponds to the HHT method.

The method is second-order accurate provided $\gamma = \tfrac{1}{2} + \alpha_M - \alpha_F$
- The method is unconditionally stable provided $\alpha_M >= \alpha_F >= \tfrac{1}{2}, \beta>=\tfrac{1}{4} +\tfrac{1}{2}(\gamma_M - \gamma_F)$

- $\gamma$ and $\beta$ are optional. The default values ensure the method is unconditionally stable, second order accurate and high frequency dissipation is maximized.
  The defaults are:

  $$\gamma = \tfrac{1}{2} + \gamma_M - \gamma_F$$

  and

$$\beta = \tfrac{1}{4}(1 + \gamma_M - \gamma_F)^2$$


## Theory


The Generalized $\alpha$ method (sometimes called the $\alpha$ method) is a one step implicit method for solving the transient problem which attempts to increase the amount of numerical damping present without degrading the order of accuracy. As with the HHT method, the following Newmark approximations are used:

$$
U_{t+\Delta t} = U_t + \Delta t \dot U_t + [(0.5 - \beta) \Delta t^2] \ddot U_t + [\beta \Delta t^2] \ddot U_{t+\Delta t} \\
\dot U_{t+\Delta t} = \dot U_t + [(1-\gamma)\Delta t] \ddot U_t + [\gamma \Delta t ] \ddot U_{t+\Delta t}
$$

but the time-discrete momentum equation is modified:

$$
R_{t + \alpha_M \Delta t} = F_{t+\Delta t}^\text{ext} - M \ddot U_{t + \alpha_M \Delta t} - C \dot U_{t+\alpha_F \Delta t} - F^\text{int}(U_{t + \alpha_F \Delta t})
$$

where the displacements and velocities at the intermediate point are given by:

$$\mathbf{d}_{t+ \alpha_F \Delta t} = (1 - \alpha_F) U_t + \alpha_F U_{t + \Delta t} \\
\mathbf{v}_{t+\alpha_F \Delta t} = (1-\alpha_F) \dot U_t + \alpha_F \dot U_{t + \Delta t} \\
\mathbf{a}_{t+\alpha_M \Delta t} = (1-\alpha_M) \ddot U_t + \alpha_M \ddot U_{t + \Delta t}$$

Following the methods outlined for Newmarks method, linearization of the nonlinear momentum equation results in the following linear equations:

$$K_{t+\Delta t}^{*i} d U_{t+\Delta t}^{i+1} = R_{t+\Delta t}^i$$

where

$K_{t+\Delta t}^{*i} = \alpha_F K_t + \frac{\alpha_F \gamma}{\beta \Delta t} C_t + \frac{\alpha_M}{\beta \Delta t^2} M$
and

$$
R_{t+\Delta t}^i = F_{t + \Delta t}^\text{ext} - F(U_{t + \alpha F \Delta t}^{i-1})^\text{int} - C \dot U_{t+\alpha F \Delta t}^{i-1} - M \ddot U_{t+ \alpha M \Delta t}^{i-1}
$$

The linear equations are used to solve for $U_{t+\alpha F \Delta t}, \dot U_{t + \alpha F \Delta t} \ddot U_{t+ \alpha M \Delta t}$. Once convergence has been achieved the displacements, velocities and accelerations at time $t + \Delta t$ can be computed.

## REFERENCES

J. Chung, G.M.Hubert. "A Time Integration Algorithm for Structural Dynamics with Improved Numerical Dissipation: The Generalized-$\alpha$ Method" ASME Journal of Applied Mechanics, 60, 371:375, 1993.


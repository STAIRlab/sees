# beamIntegration commands

::: function
beamIntegration(type, tag, \*args)

A wide range of numerical integration options are available in OpenSees
to represent distributed plasticity or non-prismatic section details in
Beam-Column Elements, i.e., across the entire element domain \[0, L\].
:::

Following are beamIntegration types available in the OpenSees:

Integration Methods for Distributed Plasticity. Distributed plasticity
methods permit yielding at any integration point along the element
length.

1.  `Lobatto`{.interpreted-text role="doc"}
2.  `Legendre`{.interpreted-text role="doc"}
3.  `NewtonCotes`{.interpreted-text role="doc"}
4.  `Radau`{.interpreted-text role="doc"}
5.  `Trapezoidal`{.interpreted-text role="doc"}
6.  `CompositeSimpson`{.interpreted-text role="doc"}
7.  `userDefined`{.interpreted-text role="doc"}
8.  `FixedLocation`{.interpreted-text role="doc"}
9.  `LowOrder`{.interpreted-text role="doc"}
10. `MidDistance`{.interpreted-text role="doc"}

::: {.toctree maxdepth="2" hidden=""}
Lobatto Legendre NewtonCotes Radau Trapezoidal CompositeSimpson
userDefined FixedLocation LowOrder MidDistance
:::

Plastic Hinge Integration Methods. Plastic hinge integration methods
confine material yielding to regions of the element of specified length
while the remainder of the element is linear elastic. A summary of
plastic hinge integration methods is found in ([Scott and Fenves
2006]()).

1.  `UserHinge`{.interpreted-text role="doc"}
2.  `HingeMidpoint`{.interpreted-text role="doc"}
3.  `HingeRadau`{.interpreted-text role="doc"}
4.  `HingeRadauTwo`{.interpreted-text role="doc"}
5.  `HingeEndpoint`{.interpreted-text role="doc"}

::: {.toctree maxdepth="2" hidden=""}
UserHinge HingeMidpoint HingeRadau HingeRadauTwo HingeEndpoint
:::

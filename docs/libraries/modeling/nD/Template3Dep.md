# Template Elasto-Plastic Framework {#EPTemplate_commands}

## Yield Surface Command {#YS_Command}

    set ys "-YieldSurfaceType <parameter list>"

This command sets the yield surface variable `ys` to be the specified
type. A list of paramaters can be passed to define the yield surface and
the number of parameters depend on the type of yield surface. Valid
strings for YieldSurfaceType are `DP`, `VM`, `CC`, and `RMC01`, which
are described in the following subsections.

### Drucker-Prager Yield Surface {#dp_ys}

    set ys "-DP"

`DP` stands for Drucker-Prager type, i.e. cone shaped yield surface. In
this case, no parameter needs to be supplied since the slope $\alpha$ is
treated as an internal variable.

### von Mises Yield Surface {#vm_ys}

    set ys "-VM"

`VM` stands for von Mises type, i.e. cylinder shaped yield surface. In
this case, no parameter needs to be supplied since the size of the
cylinder is treated as an internal variable.

### Cam-Clay Yield Surface {#cc_ys}

    set ys "-CC M?"

`CC` stands for Cam-Clay type, i.e. ellipsoid shaped yield surface. For
`CC` type yield surface, the slope of the critical state line in p--q
space, i.e. M, need to be supplied.

### Rounded Mohr-Coulomb (Willam-Warnke) Yield Surface {#rmc01_ys}

    set ys "-RMC01"

`RMC01` stands for rounded Mohr-Coulomb (Willam-Warnke) type, i.e. cone
shaped yield surface. In this case, no parameter needs to be supplied,
this is similar to the Drucker-Prager yield surface.

## Potential Surface Command {#PS_Command}

    set ps "-PotentialSurfaceType <parameter list>"

This command sets the potential surface variable `ps` to be the
specified type. A list of paramaters can be passed to define the
potential surface and the number of parameters depend on the type of
potential surface. Valid strings for PotentialSurfaceType are `DP`,
`VM`, and `CC`, which are described in the following subsections.

### Drucker-Prager Potential Surface {#dp_ps}

    set ps "-DP"

`DP` stands for Drucker-Prager type, i.e. cone shaped potential surface.
In this case, no parameter needs to be supplied since the slope $\alpha$
is treated as an internal variable.

### von Mises Potential Surface {#vm_ps}

    set ps "-VM"

`VM` stands for von Mises type, i.e. cylinder shaped potential surface.
In this case, no parameter needs to be supplied since the size of the
cylinder is treated as an internal variable.

### Cam-Clay Potential Surface {#cc_ps}

    set ps "-CC M?"

`CC` stands for Cam-Clay type, i.e. ellipsoid shaped potential surface.
For `CC` type potential surface, the slope of the critical state line in
p--q space, i.e. M, need to be supplied.

### Rounded Mohr-Coulomb (Willam-Warnke) Potential Surface {#rmc01_ps}

    set ps "-RMC01"

`RMC01` stands for rounded Mohr-Coulomb (Willam-Warnke) type, i.e. cone
shaped Potential surface. In this case, no parameter needs to be
supplied, this is similar to the Drucker-Prager Potential surface.

## Evolution Law Command {#EL_Command}

    set el "-EvolutionLawType <parameter list>"

This command sets the evolution law variable `el` to be the specified
type. A list of paramaters can be passed to define the potential surface
and the number of parameters depend on the type of potential surface.
Valid strings for EvolutionLawType are `Leq`, `NLp`, and ``, which are
described in the following subsections.

### Linear Scalar Evolution Law {#leq_el}

    set el "-Leq a?"

`Leq` stands for Linear Scalar Evolution Law. This hardening rule is
based on the equivalent deviatoric plastic strain $\epsilon_q^{pl}$. In
this case, linear hardening coefficient `a` needs to be supplied. This
hardening rule can be applied to any scalar internal variable, such as
the slope of Drucker--Prager yield surface, the diameter of von Mises
yield surface, and so on.

### Nonlinear Scalar Evolution Law {#nlp_el}

    set el "-NLp e0? lambda? kappa? "

`NLp` stands for Nonlinear Scalar Evolution Law. This hardening rule is
based on the volumetic plastic strain $\epsilon_p^{pl}$. In this case,
parameters including void ration `e0`, `lambda` and `kappa` need to be
supplied. This hardening rule is primarily for the evolution of the tip
stress $p^{'}_{o}$ in Cam-Clay model.

### Linear Tensorial Evolution Law {#LEij}

    set et "-LEij a?"

`LEij` stands for Linear Tensorial Evolution Law. This hardening rule is
based on the plastic strain $\epsilon_{ij}^{pl}$. In this case, linear
hardening coefficient `a` needs to be supplied. This hardening rule can
be applied to any tensorial internal variable, such as the the center
$\alpha_{ij}$ of Drucker--Prager yield surface or von Mises yield
surface, and so on.

### Nonlinear Tensorial Evolution Law (Armstrong-Frederick model ) {#NLEij}

    set et "-NLEij ha? Cr?" 

`NLEij` stands for Nonlinear Tensorial Evolution Law from
Armstrong--Frederick nonlinear model. This kinematic hardening law is
based on the plastic strain $\epsilon_{ij}^{pl}$. In this case,
nonlinear hardening coefficients `ha` and `Cr` need to be supplied. This
hardening rule can be applied to any tensorial internal variable, such
as the the center $\alpha_{ij}$ of Drucker--Prager yield surface or von
Mises yield surface, and so on.

## EPState Command {#ep_Command}

    <set sts "Sxx? Sxy? Sxz? Syx? Syy? Syz? Szx? Szy? Szz?"> 

    set eps "<-NOD nt?> -NOS ns? sc1? sc2? ... <-stressp sts>"

First statement sets the initial stress tensor to variable `sts` (if it
is not stated here, no initial stress by default). Second statement
assigns to the Elasto-Plastic state variable `eps` the specified state
parameters, including number of tensorial internal variables `nt` (if it
is not stated here, $nt=0$ by default), number of scalar internal
variables `ns` and corresponding initial values `sc1`, `sc2`, \..., and
initial stresses defined in `$sts` (if it has been previously defined).

## Template Elasto-Plastic Material Command {#temp_Command}

    nDMaterial Template3Dep mTag? -YS $ys? -PS $ps? -EPS $eps? <-ELS1 $el?> 
    <$-ELT1 et?>

A template elasto-plastic material is constructed using `nDMaterial`
command. The argument `mTag` is used to uniquely identify this
nDMaterial object among nDMaterial objects in the BasicBuilder object.
The other parameters include previously defined yield surface object
`ys`, potential surface object `ps`, elasto-plastic state object `eps`,
scalar evolution law object `el`, and tensorial evolution law object
`et`.

## Examples {#ep_command_Examples}

### von Mises Model

 

::: small
    # Yield surface 
    set ys "-VM"

    # Potential surface
    set ps "-VM"

    # Scalar evolution law: linear hardening coef = 1.0
    set ES1  "-Leq  1.10"

    # EPState
    #______________k=f(Cu)
    set EPS "-NOD 0 -NOS 1 20"#

    # Creating nDMaterial using Template Elastic-Plastic Model
    nDMaterial Template3Dep 1 -YS $ys -PS $ps -EPS $EPS -ELS1 $ES1
:::

<details><summary>Drucker--Prager Model</summary>
```tcl
    # Yield surface 
    set ys "-DP"

    # Potential surface
    set ps "-DP 0.1"

    # Scalar evolution law: linear hardening coef = 1.0
    set ES1  "-Leq  1.10"

    # Initial stress
    set sts "0.10 0 0  0 0.10 0  0 0 0.10"

    # EPState
    #______________alpha___k
    set EPS "-NOD 0 -NOS 2 0.2 0.0 -stressp $sts"
    #
    # where
    #alpha = 2 sin(phi) / (3^0.5) / (3-sin(phi) ), phi is the friction angle
    # and k is the cohesion

    # Creating nDMaterial using Template Elastic-Plastic Model
    nDMaterial Template3Dep 1 -YS $ys -PS $ps -EPS $EPS -ELS1 $ES1
```

</details>
 
<details><summary>Cam-clay Model</summary>

```tcl
    # Yield surface M = 1.2
    set ys "-CC 1.2"

    # Potential surface M = 1.2
    set ps "-CC 1.2"

    # Scalar evolution law___void ratio___Lamda___Kappa 
    set ES1  "-NLp           0.85        0.19   0.06"

    # Initial stress
    set sts "0.10 0 0  0 0.10 0  0 0 0.10"

    #________________po
    set EPS "-NOS 1 200.1 -stressp $sts"

    #
    nDMaterial Template3Dep 1 -YS $ys -PS $ps -EPS $EPS -ELS1 $ES1
```
</details>



# WeakRock 

| |  |
|-----|---------------------------------------------------------------|
| `Kir` | initial slope of the curve, $K_{ir}$
| `pur` | the rock mass ultimate resistance, $p_{ur}$.
| `yrm` | $\texttt{yrm} = k_{rm}B$, $B$ is the shaft diameter, $k_{rm}$ is a constant ranging from 0.0005 to 0.00005 that serves to establish the overall stiffness of the curve.

See page 56 of reference [1] ([link](https://www.dropbox.com/s/h3s9qvvz3pb4tlf/Weak%20Rock%20Reference%20Book.pdf?dl=0)).


For the initial linear portion of the curve

$$p=K_{i r} y \quad \text{for} \quad y \leq y_{A}$$

For the transitional, nonlinear portion

$$
\begin{aligned}
p &=\frac{p_{u r}}{2}\left(\frac{y}{y_{r m}}\right)^{0.25} \text { for } y \geq y_{A}, p \leq p_{\mathrm{ur}} \\
\end{aligned}
$$

and when the ultimate resistance is reached
$$p = p_{u r}$$

```cpp
class WeakRock : public HystereticBackbone {

 public:
  WeakRock(int tag, double kir, double pur, double yrm);

  double getStress(double strain) {
    double yA = pow(pur / (2 * pow(yrm, 0.25) * Kir), 1.333);
    double yu = 16.0 * yrm;

    if (strain < yA) {
      return Kir * strain;
    }

    if (strain < yu) {
      return pur / 2 * pow(strain / yrm, 0.25);
    }

    return pur;
  }

 protected:
 private:
  double Kir;
  double pur;
  double yrm;
};
```

## References

1. National Academies of Sciences, Engineering, and Medicine 2006. *Rock-Socketed Shafts for Highway Structure Foundations.* Washington, DC: The National Academies Press. https://doi.org/10.17226/13975.



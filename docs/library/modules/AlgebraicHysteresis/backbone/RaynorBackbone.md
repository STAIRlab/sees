# Raynor

::: {apidoc="opensees.backbone.Raynor"}
:::


## C++ Interface

```cpp
class RaynorBackbone : public HystereticBackbone
{
 public:
  RaynorBackbone(int tag,double es,double f1,double f2,double epsh,double epsm,double c1,double ey);

  double getStress (double strain)
  {
    double Epsilony = fy/Es;
    double fsh = fy + (Epsilonsh - Epsilony)*Ey;
    if( fabs(strain) <= Epsilony )
      return Es*strain;
    else if( strain> Epsilony && strain<=Epsilonsh )
      return fy+(strain-Epsilony)*Ey;
    else if( strain<-Epsilony && strain>=-Epsilonsh )
      return -fy+(strain+Epsilony)*Ey;
    else if( strain>Epsilonsh && strain<=Epsilonsm )
    {
       return fsu-(fsu-fsh)*pow((Epsilonsm-strain)/(Epsilonsm-Epsilonsh),C1);
    }
    else if( strain<-Epsilonsh && strain>=-Epsilonsm )
    {
      return -fsu+(fsu-fsh)*pow((Epsilonsm+strain)/(Epsilonsm-Epsilonsh),C1);
    }
    else if (strain < -Epsilonsm)
      return -fsu;
    else if (strain > Epsilonsm)
      return fsu;
  }

 private:
  double Es;
  double fy;
  double fsu;
  double Epsilonsh;
  double Epsilonsm;
  double C1;
  double Ey;
};
```

## References

- Raynor, D. J., Lehman, D. L., and Stanton, J. F. 2002. “Bond-slip response of reinforcing bars grouted in ducts.” ACI Struct. J., 995, 568–576.
  [https://doi.org/10.14359/12296](https://doi.org/10.14359/12296)


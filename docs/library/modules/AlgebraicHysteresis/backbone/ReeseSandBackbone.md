# ReeseSand


```cpp
class ReeseSandBackbone : public HystereticBackbone
{
 public:
  ReeseSandBackbone(int tag, double kx, double ym, double pm, double yu, double pu);

  double getStress (double strain)
  {
    int signStrain = (strain > 0.0) ? 1 : -1;

    strain = signStrain*strain;

    double stress = 0.0;

    double m = (pu-pm)/(yu-ym);
    double n = pm/(m*ym);
    double C = pm/pow(ym,1/n);

    double yk = pow(C/kx,n/(n-1));

    if (strain <= yk)
      stress = kx*strain;
    else if (strain <= ym)
      stress = C*pow(strain,1/n);
    else if (strain <= yu)
      stress = pm + m*(strain-ym);
    else
      stress = pu;

    return signStrain*stress;
  }
  
 private:
  double kx;
  double ym;
  double pm;
  double yu;
  double pu;
};
```

Code developed by: <span style="color:blue">MHS</span>
Created: Aug 2000


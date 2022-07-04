# ReeseSoftClay

This file contains the implementation of ReeseSoftClayBackbone.


```cpp
class ReeseSoftClayBackbone : public HystereticBackbone
{
 public:
  ReeseSoftClayBackbone(int tag, double pu, double y50, double n);  

  double getStress (double strain)
  {
    int signStrain = (strain > 0.0) ? 1 : -1;
    strain = signStrain*strain;

    double exp = 1.0/n;
    double fac = pow(2.0,n);

    double minStrain = 0.001*y50;
    double stress;
    if (strain > fac*y50)
      stress = pu;
    else if (strain > minStrain)
      stress = pu*0.5*pow(strain/y50,exp);
    else
      stress = pu*0.5*pow(0.001,exp)/minStrain*strain;

    return signStrain*stress;
  }


 private:
  double pu;
  double y50;
  double n;
};
```

Code developed by: <span style="color:blue">MHS</span>

Created: Aug 2000


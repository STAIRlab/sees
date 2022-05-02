# Raynor

## C++ Interface

```cpp
class RaynorBackbone : public HystereticBackbone
{
 public:
  RaynorBackbone(int tag,double es,double f1,double f2,double epsh,double epsm,double c1,double ey);

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


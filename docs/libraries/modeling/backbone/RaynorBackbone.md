# Raynor

## References

- Raynor, D. J., Lehman, D. L., and Stanton, J. F. 2002. “Bond-slip response of reinforcing bars grouted in ducts.” ACI Struct. J., 995, 568–576.

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


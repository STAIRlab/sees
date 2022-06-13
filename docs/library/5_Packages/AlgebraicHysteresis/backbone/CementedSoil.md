# CementedSoil

the Evans and Duncan (1982) SILT model at
http://www.findapile.com/p-y-curves/p-y-curves-models

```cpp
class CementedSoil : public HystereticBackbone {
 public:
  CementedSoil(int tag, double pM, double pU, double Kpy,
               double z, double b);

  int setVariable(char *argv);
  int getVariable(int varID, double &theValue);

 private:
  double pm;
  double pu;
  double kpy;
  double depth;
  double diameter;
};
```

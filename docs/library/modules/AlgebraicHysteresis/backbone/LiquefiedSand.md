# LiquefiedSand

```tcl
hystereticBackbone LiquefiedSand tag X D
```

| | |
|-------|---------------------------------------------|
|  `X`  | the depth
|  `D`  | the pile diameter between 0.3m and 2.6m
|  `kN` | define the unit kilo Newton
|  `m`  | define the unit meter

[source](https://www.pilegroups.com/single-post/p-y-curve-model-of-liquefied-sand-rollins-et-al-2005)

 
```cpp
class LiquefiedSand : public HystereticBackbone {
 public:
  LiquefiedSand(int tag, double x, double d, double kn, double m);

  double getStress(double strain) {
    double A = 3e-7 * pow(X + 1, 6.05);
    double B = 2.8 * pow(X + 1, 0.11);
    double C = 2.85 * pow(X + 1, -0.41);
    double Pd = 3.81 * log(D) + 5.6;

    if (strain < 0.001 * yu) {
      double k0 = Pd * A * B * C * pow(B * 0.001 * yu, C - 1);
      return k0 * strain;
    }

    if (strain < yu) {
      double P03m = A * pow(B * strain, C);
      if (P03m > 15 * kN / meter) {
        opserr << "WARNING: P0.3m > 15 kN/m\n";
      }
      return Pd * P03m;
    }

    double P03m = A * pow(B * yu, C);
    if (P03m > 15 * kN / meter) {
      opserr << "WARNING: P0.3m > 15 kN/m\n";
    }
    return Pd * P03m;
  }


 private:
  double X;
  double D;
  double kN;
  double meter;
  double yu;
};
```

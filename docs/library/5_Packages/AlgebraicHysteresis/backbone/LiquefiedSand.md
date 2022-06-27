# LiquefiedSand

[source](https://www.pilegroups.com/single-post/p-y-curve-model-of-liquefied-sand-rollins-et-al-2005)

 
```cpp
class LiquefiedSand : public HystereticBackbone {
 public:
  LiquefiedSand(int tag, double x, double d, double kn, double m);

 private:
  double X;
  double D;
  double kN;
  double meter;
  double yu;
};
```

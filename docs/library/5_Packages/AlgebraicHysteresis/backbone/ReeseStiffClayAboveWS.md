# ReeseStiffClayAboveWS

Response of Stiff Clay above the water surface
(https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB94108305.xhtml)
page 336

```tcl
 hystereticBackbone ReeseStiffClayAboveWS tag pu y50
```

| |
|------|----|
| pu   | the ultimate soil resistance per unit length of shaft
| y50  | the deflection at one-half the ultimate soil resistance


## C++ Interface

```cpp
class ReeseStiffClayAboveWS : public HystereticBackbone {
 public:
  ReeseStiffClayAboveWS(int tag, double pu, double y50);
  ReeseStiffClayAboveWS();
  ~ReeseStiffClayAboveWS();

  double getStress(double strain) {
    double yhl = hl * y50;
    if (strain < yhl) {
      return strain * getStress(yhl) / yhl;
    }

    if (strain > 16.0 * y50) {
      return pu;
    }

    return 0.5 * pu * pow(strain / y50, 0.25);
  }

 protected:
 private:
  double pu;
  double y50;
  double hl;
};
```


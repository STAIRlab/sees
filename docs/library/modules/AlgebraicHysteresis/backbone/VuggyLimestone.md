# VuggyLimestone

```tcl
hystereticBackbone VuggyLimestone tag b su
```

|   |  |
|----|----------------------------------|
| `b`  | the pile diameter ($>0$)
| `su` | the shear strength of the rock ($> 0$). |


Response of Stiff Clay above the water surface [@wang1993com624p]
page 348
[source](https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB94108305.xhtml)

```cpp
class VuggyLimestone : public HystereticBackbone {

 public:
  VuggyLimestone(int tag, double b, double su);

  double getStress(double strain) {
    if (strain <= 0.0004 * diameter) {
      return 2000.0 * shearStrength * strain;
    } else if (strain <= 0.0024 * diameter) {
      return 0.8 * diameter * shearStrength +
             100.0 * shearStrength * (strain - 0.0004 * diameter);
    }
    return 0.0;
  }

 protected:
 private:
  double diameter;
  double shearStrength;
};
```

## References

1. Wang, S. T.; Reese, L. C. (1993) *COM624P: Laterally Loaded Pile Analysis Program for the Microcomputer. Version 2.0.*


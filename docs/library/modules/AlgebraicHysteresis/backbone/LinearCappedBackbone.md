# LinearCapped

This file contains the implementation of 
LinearCappedBackbone, which is a linear cap given by a
cap deformation and a slope imposed on a hysteretic backbone.

::: {apidoc="opensees.backbone.LinearCapped"}
:::


Code developed by: <span style="color:blue">MHS</span>

Created: Aug 2000


```cpp
class LinearCappedBackbone : public HystereticBackbone
{
 public:
  LinearCappedBackbone(int tag, HystereticBackbone &backbone,
		       double def, double slope, double resStrength);

  int setVariable(char *argv);
  int getVariable(int varID, double &theValue);
   
 private:
  HystereticBackbone *theBackbone;
  double eCap;
  double sCap;
  double E;
  double eRes;
  double sRes;
};
```

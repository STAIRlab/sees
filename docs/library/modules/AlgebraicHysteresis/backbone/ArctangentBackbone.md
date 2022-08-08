# Arctangent

This file contains the implementation of 
ArctangentBackbone, which is a continuous function given
by $K_1 \operatorname{atan}(K_2*\texttt{strain})$ as developed by Ranzo and Petrangeli (1998)

:::{apidoc="opensees.backbone.Arctangent"}
:::


Code developed by: <span style="color:blue">MHS</span>
Created: Aug 2000


```cpp
class ArctangentBackbone : public HystereticBackbone
{
 public:
  ArctangentBackbone(int tag, double K1, double gammaY, double alpha);
  
  int setVariable(char *argv);
  int getVariable(int varID, double &theValue);
  
 private:
  double K1;
  double K2;
  double gammaY;
  double alpha;
};
```


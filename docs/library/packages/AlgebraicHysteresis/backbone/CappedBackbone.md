# Capped

This file contains the implementation of 
CappedBackbone, which overlays two backbone curves.

Written: MHS
Created: Aug 2000

```
class CappedBackbone : public HystereticBackbone
{
 public:
  CappedBackbone(int tag, HystereticBackbone &backbone, 
                 HystereticBackbone &cap);
  
  int setVariable(char *argv);
  int getVariable(int varID, double &theValue);

 private:
  HystereticBackbone *theBackbone;
  HystereticBackbone *theCap;
  
  double eCap;
};
```

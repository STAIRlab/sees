# Material

Description: This file contains the implementation of 
MaterialBackbone, which treats a uniaxial material as
a hysteretic backbone by removing path dependency, i.e.
commitState is never called on the uniaxial material.

Written: MHS
Created: Aug 2000


```cpp
class MaterialBackbone : public HystereticBackbone
{
 public:
  MaterialBackbone(int tag, UniaxialMaterial &material);
  MaterialBackbone();
  ~MaterialBackbone();
  
  double getStress(double strain);
  double getTangent(double strain);
  double getEnergy(double strain);
  
  double getYieldStrain(void);
  
  HystereticBackbone *getCopy(void);
  
  void Print(OPS_Stream &s, int flag = 0);
  
  int setVariable(char *argv);
  int getVariable(int varID, double &);
  
  int sendSelf(int commitTag, Channel &);
  int recvSelf(int commitTag, Channel &, FEM_ObjectBroker &);
  
 private:
  UniaxialMaterial *theMaterial;
};
```

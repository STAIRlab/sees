# LinearCapped

This file contains the implementation of 
LinearCappedBackbone, which is a linear cap given by a
cap deformation and a slope imposed on a hysteretic backbone.

Written: MHS
Created: Aug 2000


```cpp
class LinearCappedBackbone : public HystereticBackbone
{
 public:
  LinearCappedBackbone(int tag, HystereticBackbone &backbone,
		       double def, double slope, double resStrength);
  LinearCappedBackbone();
  ~LinearCappedBackbone();
  
  
  double getYieldStrain(void);
  
  HystereticBackbone *getCopy(void);
  
  void Print(OPS_Stream &s, int flag = 0);
  
  int setVariable(char *argv);
  int getVariable(int varID, double &theValue);
  
  int sendSelf(int commitTag, Channel &theChannel);  
  int recvSelf(int commitTag, Channel &theChannel, 
	       FEM_ObjectBroker &theBroker);    
  
 protected:
  
 private:
  HystereticBackbone *theBackbone;
  double eCap;
  double sCap;
  double E;
  double eRes;
  double sRes;
};
```

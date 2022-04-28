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
  CappedBackbone();
  ~CappedBackbone();
  
  double getStress(double strain);
  double getTangent(double strain);
  double getEnergy(double strain);
  
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
  HystereticBackbone *theCap;
  
  double eCap;
};
```

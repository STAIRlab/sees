# Trilinear

This file contains the implementation of 
TrilinearBackbone, which is a trilinear backbone

Written: MHS
Created: Aug 2000

```cpp
class TrilinearBackbone : public HystereticBackbone
{
 public:
  TrilinearBackbone(int tag, double e1, double s1, 
		    double e2, double s2, double e3, double s3);
  TrilinearBackbone(int tag, double e1, double s1, 
		    double e2, double s2);
  TrilinearBackbone();
  ~TrilinearBackbone();
  
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
  double E1, E2, E3;
  double e1, e2, e3;
  double s1, s2, s3;
};
```


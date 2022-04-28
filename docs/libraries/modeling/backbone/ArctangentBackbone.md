# Arctangent

This file contains the implementation of 
ArctangentBackbone, which is a continuous function given
by `K1*atan(K2*strain)` as developed by Ranzo and Petrangeli (1998)


Written: MHS
Created: Aug 2000


```cpp
class ArctangentBackbone : public HystereticBackbone
{
 public:
  ArctangentBackbone(int tag, double K1, double gammaY, double alpha);
  ArctangentBackbone();
  ~ArctangentBackbone();
  
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
  double K1;
  double K2;
  double gammaY;
  double alpha;
};
```


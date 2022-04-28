# ReeseSoftClay

Description: This file contains the implementation of 
ReeseSoftClayBackbone.

Written: MHS

Created: Aug 2000


```cpp
class ReeseSoftClayBackbone : public HystereticBackbone
{
 public:
  ReeseSoftClayBackbone(int tag, double pu, double y50, double n);
  ReeseSoftClayBackbone();
  ~ReeseSoftClayBackbone();
  
  
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
  double pu;
  double y50;
  double n;
};
```

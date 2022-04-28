# Mander

This file contains the implementation of 
ManderBackbone, which the concrete backbone function given
by Mander, Priestly, and Park (1988)

Written: MHS
Created: Mar 2001

```cpp
class ManderBackbone : public HystereticBackbone
{
 public:
  ManderBackbone(int tag, double fc, double epsc, double Ec);
  ManderBackbone();
  ~ManderBackbone();


  double getYieldStrain(void);

  HystereticBackbone *getCopy(void);

  void Print(OPS_Stream &s, int flag = 0);

  

  int setVariable(char *argv);
  int getVariable(int varID, double &theValue);
  
  int sendSelf(int commitTag, Channel &theChannel);  
  int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker &theBroker);    

 private:
  double fpc;
  double epsc;
  double Ec;
};
```

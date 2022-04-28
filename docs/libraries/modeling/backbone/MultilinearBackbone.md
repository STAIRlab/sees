# Multilinear

Description: This file contains the implementation of 
MultilinearBackbone, which is a backbone defined by
many points

Written: MHS
Created: Aug 2000

```cpp
class MultilinearBackbone : public HystereticBackbone
{
 public:
  MultilinearBackbone(int tag, int numPoints,
		      const Vector &e, const Vector &s);
  
  MultilinearBackbone();
  ~MultilinearBackbone();
  
  
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
  double *E;
  double *e;
  double *s;
  double *c;
  int numPoints;
};
```


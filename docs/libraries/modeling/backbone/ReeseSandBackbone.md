# ReeseSand

Written: MHS
Created: Aug 2000


```cpp
class ReeseSandBackbone : public HystereticBackbone
{
 public:
  ReeseSandBackbone(int tag, double kx, double ym, double pm,
		    double yu, double pu);
  ReeseSandBackbone();
  ~ReeseSandBackbone();
  
  
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
  double kx;
  double ym;
  double pm;
  double yu;
  double pu;
};
```


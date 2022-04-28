# LiquefiedSand

https://www.pilegroups.com/single-post/p-y-curve-model-of-liquefied-sand-rollins-et-al-2005
 
 
```cpp
class LiquefiedSand : public HystereticBackbone {
 public:
  LiquefiedSand(int tag, double x, double d, double kn, double m);
  LiquefiedSand();
  ~LiquefiedSand();


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
  double X;
  double D;
  double kN;
  double meter;
  double yu;
};
```

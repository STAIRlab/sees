# VuggyLimestone

Response of Stiff Clay above the water surface
(https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB94108305.xhtml)
page 348

```cpp
class VuggyLimestone : public HystereticBackbone {
 public:
  VuggyLimestone(int tag, double b, double su);
  VuggyLimestone();
  ~VuggyLimestone();


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
  double diameter;
  double shearStrength;
};
```


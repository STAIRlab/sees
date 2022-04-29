# ReeseStiffClayAboveWS

Response of Stiff Clay above the water surface
(https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB94108305.xhtml)
page 336

## C++ Interface

```cpp
class ReeseStiffClayAboveWS : public HystereticBackbone {
 public:
  ReeseStiffClayAboveWS(int tag, double pu, double y50);
  ReeseStiffClayAboveWS();
  ~ReeseStiffClayAboveWS();


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
  double hl;
};
```


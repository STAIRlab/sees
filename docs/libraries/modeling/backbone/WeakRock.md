
# WeakRock 

on page 56 of this manual
https://www.dropbox.com/s/h3s9qvvz3pb4tlf/Weak%20Rock%20Reference%20Book.pdf?dl=0

```cpp
class WeakRock : public HystereticBackbone {
 public:
  WeakRock(int tag, double kir, double pur, double yrm);
  WeakRock();
  ~WeakRock();

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
  double Kir;
  double pur;
  double yrm;
};
```


# CementedSoil

/**
 * @brief Cemented Soils - the Evans and Duncan (1982) SILT model at
 * http://www.findapile.com/p-y-curves/p-y-curves-models
 *
 */
```cpp
class CementedSoil : public HystereticBackbone {
 public:
  CementedSoil(int tag, double pM, double pU, double Kpy,
               double z, double b);
  CementedSoil();
  ~CementedSoil();

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
  double pm;
  double pu;
  double kpy;
  double depth;
  double diameter;
};
```

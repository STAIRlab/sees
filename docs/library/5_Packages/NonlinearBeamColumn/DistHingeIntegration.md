# DistHingeIntegration

```cpp
// $Revision: 1.2 $
// $Date: 2006-09-05 22:57:36 $
// $Source: /usr/local/cvs/OpenSees/SRC/element/forceBeamColumn/DistHingeIntegration.h,v $

#include <BeamIntegration.h>

class Matrix;
class ElementalLoad;
class Channel;
class FEM_ObjectBroker;

class DistHingeIntegration : public BeamIntegration
{
 public:
  DistHingeIntegration(double lpI, double lpJ, BeamIntegration &bi);
  DistHingeIntegration();
  ~DistHingeIntegration();
  
  void getSectionLocations(int numSections, double L, double *xi);
  void getSectionWeights(int numSections, double L, double *wt);
  
  BeamIntegration *getCopy(void);

  int sendSelf(int cTag, Channel &theChannel);
  int recvSelf(int cTag, Channel &theChannel, FEM_ObjectBroker &theBroker);

  int setParameter(const char **argv, int argc, Parameter &param);
  int updateParameter(int parameterID, Information &info);
  int activateParameter(int parameterID);

  void Print(OPS_Stream &s, int flag = 0);

  void getLocationsDeriv(int nIP, double L, double dLdh, double *dptsdh);
  void getWeightsDeriv(int nIP, double L, double dLdh, double *dwtsdh);

 private:
  double lpI;
  double lpJ;

  BeamIntegration *beamInt;

  int parameterID;
};
```

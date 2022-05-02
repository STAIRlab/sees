# HystereticBackbone

// Description: This file contains the interface for HystereticBackbone,
// which represents a backbone curve for hysteretic models.
//
// Written: MHS
// Created: Aug 2000
//

```cpp
extern bool OPS_addHystereticBackbone(HystereticBackbone *newComponent);
extern HystereticBackbone *OPS_getHystereticBackbone(int tag);
extern void OPS_clearAllHystereticBackbone(void);

class HystereticBackbone : public TaggedObject, public MovableObject
{
 public:
  HystereticBackbone(int tag, int classTag);
  virtual ~HystereticBackbone();
  
  virtual double getStress(double strain) = 0;
  virtual double getTangent(double strain) = 0;
  virtual double getEnergy(double strain) = 0;
  
  virtual double getYieldStrain(void) = 0;
  
  virtual HystereticBackbone *getCopy(void) = 0;
  
  virtual int setVariable(char *argv);
  virtual int getVariable(int varID, double &theValue);
  
  virtual int setParameter(char **argv, int argc, Information &eleInformation);
  virtual int updateParameter(int responseID, Information &eleInformation);	
  
 protected:
  
 private:
  
};

```


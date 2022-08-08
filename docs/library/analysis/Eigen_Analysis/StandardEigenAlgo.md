# StandardEigenAlgo

// $Revision: 1.2 $
// $Date: 2003-02-14 23:00:41 $
// $Source: /usr/local/cvs/OpenSees/SRC/analysis/algorithm/eigenAlgo/StandardEigenAlgo.h,v $
                                                                        
// Written: MHS
// Created: Oct 2001
//
StandardEigenAlgo is a class which performs a eigen solution algorithm
to solve standard eigenvalue equations. It is not expected that 
this class will have subclasses.

```cpp
#include <EigenAlgorithm.h>

class StandardEigenAlgo : public EigenAlgorithm
{
 public:
  StandardEigenAlgo();
  virtual ~StandardEigenAlgo();
  
  virtual int solveCurrentStep(int numModes);
  
  virtual int sendSelf(int commitTag, Channel &theChannel);
  virtual int recvSelf(int commitTag, Channel &theChannel,
		       FEM_ObjectBroker &theBroker);
  
  virtual void Print(OPS_Stream &s, int flag = 0);
  
 protected:
  
 private:
  
};
```


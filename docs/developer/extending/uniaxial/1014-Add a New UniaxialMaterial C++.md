# Add a New UniaxialMaterial C++

To add a new Uniaxial Material module using the C++ language, the
developer must:

- provide a new C++ subclass of the UniaxialMaterial class
- provide an interface function that will be used to parse the input
  and create the new material.

Unlike the C and Fortran modules, no information about the state of
the model is passed as arguments to the material methods. It is the
responsibility of the material to okeep whatever information it needs.
This information will include both parameters (information needed to
define the material) and state variables or history variables
(information needed by the material to remember it's current state for
the computation of the stress and tangent)

> NOTE: This document assumes the reader is familiar with the C++
> programming language.

<h3 id="uniaxialmaterial_class">UniaxialMaterial Class</h3>

<p>The Uniaxial class itself is an abstract base class. It inherits from
both the `Material` class, which is itself a subclass of `TaggedObject`
class and the MovableObject class. The class has a large number of
methods defined in the interface, not all these methods need to be
included in a new UniaxialMaterial class. The following is the minimal
interface that should be considered:

```cpp
class UniaxialMaterial : public Material
{
  public:
    UniaxialMaterial (int tag, int classTag);
    virtual ~UniaxialMaterial();

    virtual int setTrialStrain (double strain, double strainRate =0) =0;

    virtual double getStrain (void) = 0;
    virtual double getStrainRate (void);
    virtual double getStress (void) = 0;
    virtual double getTangent (void) = 0;
    virtual double getInitialTangent (void) = 0;

    virtual int commitState (void) = 0;
    virtual int revertToLastCommit (void) = 0;
    virtual int revertToStart (void) = 0;

    virtual UniaxialMaterial *getCopy (void) = 0;

    virtual Response *setResponse (const char **argv, int argc,
                                   OPS_Stream &theOutputStream);
    virtual int getResponse (int responseID, Information &matInformation);

    virtual int sendSelf(int commitTag, Channel &theChannel);
    virtual int recvSelf(int commitTag, Channel &theChannel,
                 FEM_ObjectBroker &theBroker);

    virtual void Print(OPS_Stream &s, int flag =0);
};
```

The methods with `=0;` are methods that you must implement for the
class to link successfully with OpenSees. The other classes are
optional.


<h3 id="example___elasticppecpp">Example - ElasticPPecpp</h3>
In the following section we will provide all necessary code to add a
new elastic perfectly plastic material into an OpenSees interpreter.

<h4 id="header">Header</h4>
The header for the new class, which we will call `ElasticPPcpp` is as
follows:
```cpp
#ifndef ElasticPPcpp_h
#define ElasticPPcpp_h

#include <UniaxialMaterial.h>

class ElasticPPcpp : public UniaxialMaterial
{
  public:
    ElasticPPcpp(int tag, double E, double eyp);
    ElasticPPcpp();

    ~ElasticPPcpp();

    int setTrialStrain(double strain, double strainRate = 0.0);
    double getStrain(void);
    double getStress(void);
    double getTangent(void);


    double getInitialTangent(void) {return E;};

    int commitState(void);
    int revertToLastCommit(void);
    int revertToStart(void);

    UniaxialMaterial *getCopy(void);

    int sendSelf(int commitTag, Channel &theChannel);
    int recvSelf(int commitTag, Channel &theChannel,
                 FEM_ObjectBroker &theBroker);

    void Print(OPS_Stream &s, int flag =0);


 protected:

  private:
    double fyp, fyn;    // positive and negative yield stress
    double ezero;       // initial strain
    double E;           // elastic modulus
    double ep;          // plastic strain at last commit

    double trialStrain; // trial strain
    double trialStress;      // current trial stress
    double trialTangent;     // current trial tangent
    double commitStrain;     // last commited strain
    double commitStress;     // last commited stress
    double commitTangent;    // last committed  tangent
```

The header file defines the interface and variables for the class
`ElasticPPcpp`. It defines the new class to be a sublass of the
UniaxialMaterial class. In the public interface, are two constructors
and a destructor in addition to minimal set of methods we showed for the
UniaxialMaterial class. There are no protected data or methods as we do
not expect this class to be subclassed. In the private section we define
a number of private variables and a number of variables. Some of these
are parameter variable which do not change with each commit, e.g. E, and
some state variable which do change, e.g. ep, fyp, and fyn.

<h4 id="implementation">Implementation</h4>
It another file, `ElasticPPcpp.cpp`, we place the code that details
what the constructors, destructor and methods do. In addition we provide
one additional procedure `OPS_ElasticPPcpp()` (NOTE it has the same name
as the class with an `OPS_` prefix). We will go through each part of the
file.

<h5 id="include_directives">Include Directives</h5>
The first part of the file contains the list of includes. It is
necessary to have an `#include` directive for each class and api file that
is used within the `.cpp` file and is not included in the header.

```cpp
#include "ElasticPPcpp.h"

#include <elementAPI.h>
#include <Vector.h>
#include <Channel.h>
#include <math.h>
#include <float.h>
```


<h5 id="constructors">Constructors</h5>

After the list of includes, we provide the 2 constructors. The
constructors are rather simple. They just initialize all the data
variables defined in the header. Note it is very important to set all
pointer values to 0 if you use pointers in your class. We will use none
here.

The first constructor is the one most typically used. The arguments
provide the materials tag, youngs modulus and initial yield point strain
values. material. The code in the constructor simply computes the
positive and negative yield stress based on the input provided.

```cpp
ElasticPPcpp::ElasticPPcpp(int tag, double e, double eyp)
:UniaxialMaterial(tag, 0),
 ezero(0.0), E(e), ep(0.0),
 trialStrain(0.0), trialStress(0.0), trialTangent(E),
 commitStrain(0.0), commitStress(0.0), commitTangent(E)
{
  fyp = E*eyp;
  fyn = -fyp;
}
```

The second constructor is called when paralell processing or the
database feature of the OpenSees application is used. It's purpose is to
create a blank `TElasticPPcpp` object, that will be filled in when the
`recvSelf()` method is invoked on the object.
```cpp
ElasticPPcpp::ElasticPPcpp()
:UniaxialMaterial(0, 0),
 fyp(0.0), fyn(0.0), ezero(0.0), E(0.0), ep(0.0),
 trialStrain(0.0), trialStress(0.0), trialTangent(E),
 commitStrain(0.0), commitStress(0.0), commitTangent(E)
{

}
```

<h5 id="destructor">Destructor</h5>
The we provide the destructor. In the destructor all memory that the
the object created or was passed to it in the constructor must be
destroyed. For this example we have no such memory. We could have left
the destructor out entirely. However, it is good practice to leave it
in your source code.
```cpp
ElasticPPcpp::~ElasticPPcpp()
{
  // does nothing                                                                                                                              
}
```

<h5 id="getcopy_method">getCopy() Method</h5>
<p>This is the method called by each element or section to get unique
copies of a material.</p>

<p>&lt;source lang="cpp"&gt; UniaxialMaterial *
ElasticPPcpp::getCopy(void) { ElasticPPcpp *theCopy = new
ElasticPPcpp(this-&gt;getTag(),E,fyp/E); theCopy-&gt;ep =
this-&gt;ep;</p>
<p>return theCopy; } &lt;/source&gt;</p>

<h5 id="settrialstrain_method">setTrialStrain() Method</h5>
This, as mentioned, is the method called when the element has
computed a nw strain for the element. The element will make subsequent
calls to `getStress()` and `getTangent()` to obtain new values of these for
the new strain. This is typically the most complicated method to write
and to determine the theory for before you even write the code. All
subsequent methods are trivial.

```cpp
int
ElasticPPcpp::setTrialStrain(double strain, double strainRate)
{
    if (fabs(trialStrain - strain) < DBL_EPSILON)
      return 0;

    trialStrain = strain;

    double sigtrial;    // trial stress                                                                                                        
    double f;           // yield function                                                                                                      

    // compute trial stress                                                                                                                    
    sigtrial = E * ( trialStrain - ezero - ep );

    //sigtrial  = E * trialStrain;                                                                                                             
    //sigtrial -= E * ezero;                                                                                                                   
    //sigtrial -= E *  ep;                                                                                                                     

    // evaluate yield function                                                                                                                 
    if ( sigtrial >= 0.0 )
        f =  sigtrial - fyp;
    else
        f = -sigtrial + fyn;

    double fYieldSurface = - E * DBL_EPSILON;
    if ( f <= fYieldSurface ) {

      // elastic                                                                                                                               
      trialStress = sigtrial;
      trialTangent = E;

    } else {

      // plastic                                                                                                                               
      if ( sigtrial > 0.0 ) {
        trialStress = fyp;
      } else {
        trialStress = fyn;
      }

      trialTangent = 0.0;
    }

    return 0;
}
```

<h5 id="trivial_methods">Trivial Methods</h5>

Next comes 3 rather simple methods that return basic information
computed in the `setTrialStrain()`. 

```cpp
double
ElasticPPcpp::getStrain(void)
{
  return trialStrain;
}

double
ElasticPPcpp::getStress(void)
{
  return trialStress;
}


double
ElasticPPcpp::getTangent(void)
{
  return trialTangent;
}
```

<h5 id="methods_dealing_with_current_state">Methods Dealing With Current
State</h5>

As mentioned, when the algorithm finds a solution state as it goes
from one converged solution to the next. As it attempts to find these
solutions it goes through a number of trial steps (each setTrialStrain()
is invoked in each of these steps). Once it finds a trial step that is
on the solution path it will stop and invoke `commitState()` on the
material. Any state variables that the material uses needs to be updated
at this time. Should the algorithm fail to find a solution it may return
to the last converged step or indeed the start. You the developer must
provide code so that your mateial can indeed go back to these states and
report correct `getTangent()` and `getStress()` values for subsequent
analysis atte,pts.

```cpp
int
ElasticPPcpp::sendSelf(int cTag, Channel &theChannel)
{
  int res = 0;
  static Vector data(9);
  data(0) = this->getTag();
  data(1) = ep;
  data(2) = E;
  data(3) = ezero;
  data(4) = fyp;
  data(5) = fyn;
  data(6) = commitStrain;
  data(7) = commitStress;
  data(8) = commitTangent;

  res = theChannel.sendVector(this->getDbTag(), cTag, data);
  if (res < 0)
    opserr << "ElasticPPcpp::sendSelf() - failed to send data\n";

  return res;
}

int
ElasticPPcpp::recvSelf(int cTag, Channel &theChannel,
                                 FEM_ObjectBroker &theBroker)
{
  int res = 0;
  static Vector data(9);
  res = theChannel.recvVector(this->getDbTag(), cTag, data);
  if (res < 0)
    opserr << "ElasticPPcpp::recvSelf() - failed to recv data\n";
  else {
    this->setTag(data(0));
    ep    = data(1);
    E     = data(2);
    ezero = data(3);
    fyp   = data(4);
    fyn   = data(5);
    commitStrain=data(6);
    commitStress=data(7);
    commitTangent=data(8);
    trialStrain = commitStrain;
    trialTangent = commitTangent;
    trialStress = commitStress;
  }

  return res;
}
```

<h5 id="methods_dealing_with_output">Methods Dealing With Output</h5>
Information is obtained by the user when the print command is invoked
by the user and also when the user issues the recorder command. When the
print command is invoked the Print method is invoked. This method simply
prints information about the element, and then asks the material to do
likewise.
```cpp
void
ElasticPPcpp::Print(OPS_Stream &s, int flag)
{
  s << "ElasticPPcpp tag: " << this->getTag() << endln;
  s << "  E: " << E << endln;
  s << "  ep: " << ep << endln;
  s << "  stress: " << trialStress << " tangent: " << trialTangent << endln;
}
```

<p>There are two methods used by the element recorders.</p>
<ol>
<li>The first method, `setResponse()`, is called when the recorder is
  created. The element informs the recorder that it can respond to a
  request of that type, if it cannot respond to the request it returns a
  0, otherwise it returns an Response object. The response object includes
  a pointer to the element, an integer flag used to id the response when
  the `getResponse()` method is called, and a Vector detailing the size of
  the response.</li>
<li>The second method, `getReponse()`, is called by the recorder when it
  is actually recording the information.</li>
</ol>

<h5 id="methods_dealing_with_databasesparallel_processing">
Methods Dealing With Databases/Parallel Processing</h5>
There are two methods provided which are required is the user uses to
use the database or parallel procesing features of the OpenSees
applications. If neither are to be used, the developer need simply
return a negative value in both methods. The idea is that the material
must pack up it's information using Vector and ID objects and send it
off to a Channel object. On the flip side, the receiving blank element
must receive the same Vector and ID data, unpack it and set the
variables.

```cpp
int
ElasticPPcpp::sendSelf(int cTag, Channel &theChannel)
{
  int res = 0;
  static Vector data(9);
  data(0) = this->getTag();
  data(1) = ep;
  data(2) = E;
  data(3) = ezero;
  data(4) = fyp;
  data(5) = fyn;
  data(6) = commitStrain;
  data(7) = commitStress;
  data(8) = commitTangent;

  res = theChannel.sendVector(this->getDbTag(), cTag, data);
  if (res < 0)
    opserr << "ElasticPPcpp::sendSelf() - failed to send data\n";

  return res;
}

int
ElasticPPcpp::recvSelf(int cTag, Channel &theChannel,
                                 FEM_ObjectBroker &theBroker)
{
  int res = 0;
  static Vector data(9);
  res = theChannel.recvVector(this->getDbTag(), cTag, data);
  if (res < 0)
    opserr << "ElasticPPcpp::recvSelf() - failed to recv data\n";
  else {
    this->setTag(data(0));
    ep    = data(1);
    E     = data(2);
    ezero = data(3);
    fyp   = data(4);
    fyn   = data(5);
    commitStrain=data(6);
    commitStress=data(7);
    commitTangent=data(8);
    trialStrain = commitStrain;
    trialTangent = commitTangent;
    trialStress = commitStress;
  }

  return res;
}
```

<h4 id="external_procedure">External Procedure</h4>
<p>This is the all importat extenal procedure that the interpreter will
parse when it comes accross your element on the command line. You need
to parse the command line, create a material using the command line
arguments you parsed and then return this material. The name of the
procedure must be OPS_YourClassName (no exceptions). If this procedure
is missing or the name is incorrect, your material will fail to
load.</p>

<p>NOTE: parsing the command line is easy with some other procedures
that are defined in the `elementAPI.h` file. In the example we show how to
get integer and double values from the command line. Other options such
as character strings and obtaining the number of input arguments are
also available.</p>

The `#ifdef` stuff at the start is required for different operating
systems.

```cpp
#ifdef _USRDLL
#define OPS_Export extern "C" _declspec(dllexport)
#elif _MACOSX
#define OPS_Export extern "C" __attribute__((visibility("default")))
#else
#define OPS_Export extern "C"
#endif


OPS_Export void *
OPS_ElasticPPcpp()
{

  // Pointer to a uniaxial material that will be returned
  UniaxialMaterial *theMaterial = 0;

  //
  // parse the input line for the material parameters
  //

  int    iData[1];
  double dData[2];
  int numData;
  numData = 1;
  if (OPS_GetIntInput(&numData, iData) != 0) {
    opserr << "WARNING invalid uniaxialMaterial ElasticPP tag" << endln;
    return 0;
  }

  numData = 2;
  if (OPS_GetDoubleInput(&numData, dData) != 0) {
    opserr << "WARNING invalid E & ep\n";
    return 0;
  }

  //
  // create a new material
  //

  theMaterial = new ElasticPPcpp(iData[0], dData[0], dData[1]);

  if (theMaterial == 0) {
    opserr << "WARNING could not create uniaxialMaterial of type ElasticPPCpp\n";
    return 0;
  }

  // return the material
  return theMaterial;
}
```


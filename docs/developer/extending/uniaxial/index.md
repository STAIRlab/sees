---
title: New Material Models
...

# Material Models

## Introduction

This document shows how to add a new material implementation to
OpenSees. The hierarchical nature of the OpenSees software architecture
allows new material models to be seamlessly added to the framework. By
keeping element and material implementations separate, a new material
model can be used in an existing element without modifying the element
implementation, and vice versa.

The remainder of this document is laid out as follows. First, the
UniaxialMaterial interface is listed and explained. Then, an example
UniaxialMaterial implementation, HardeningMaterial, is presented. Along
with the C++ implementation, it is shown how to 1) add the new model to
the OpenSees Tcl model builder, and 2) make the new model "movable" for
parallel processing and database programming. Finally, a FORTRAN
interface for programming UniaxialMaterial models in OpenSees is
described.

## UniaxialMaterial Interface

Implementations of the UniaxialMaterial interface are used in several
contexts within the OpenSees modeling framework. Due to their
simplicity, these models can define both stress-strain and
force-deformation relationships. It is up to the calling object, be it
an element object or another material object, to interpret the meaning
appropriately.

Listed below is the UniaxialMaterial class interface. All methods in the
UniaxialMaterial interface are public, there are no protected or private
data or methods. Following the UniaxialMaterial class interface listing,
each method in the interface is described.

```cpp
#include <Material.h>

class Response;
class Information;

class UniaxialMaterial : public Material
{
   public:
      UniaxialMaterial(int tag, int classTag);    
      virtual ~UniaxialMaterial(void);

      virtual int setTrialStrain(double strain, double strainRate = 0.0) = 0;
      virtual double getStrain(void) = 0;
      virtual double getStrainRate(void);
      virtual double getStress(void) = 0;
      virtual double getTangent(void) = 0;
      virtual double getDampTangent(void);
      virtual double getSecant(void);

      virtual int commitState(void) = 0;
      virtual int revertToLastCommit(void) = 0;    
      virtual int revertToStart(void) = 0;        

      virtual UniaxialMaterial *getCopy(void) = 0;

      virtual Response *setResponse(char **argv, int argc, Information &matInfo);
      virtual int getResponse(int responseID, Information &matInfo);    

   protected:
    
   private:
};
```

A note about the C++ syntax seen in the UniaxialMaterial interface. The
keyword "virtual" at the start of a method declaration indicates this
method may be overridden by a subclass of UniaxialMaterial. The
UniaxialMaterial base class provides default implementations for its
virtual methods. The notation "= 0" at the end of the method declaration
indicates the method is *pure* virtual, meaning it *must* be defined by
subclasses because the UniaxialMaterial base class does not provide a
default implementation.

The UniaxialMaterial base class constructor takes a tag and classTag as
its arguments. The tag passed to the constructor identifies this
UniaxialMaterial as unique among all other UniaxialMaterial objects, and
the classTag is used primarily for parallel processing and database
programming. Class tags are defined in the file classTags.h. The tag and
classTag arguments are passed to the Material class constructor, where
they are in turn passed to the TaggedObject and MovableObject class
constructors, respectively. The UniaxialMaterial destructor is declared,
but does not do anything as the UniaxialMaterial base class contains no
data.


The method `setTrialStrain()` takes one or two arguments, an updated
strain and strain rate. The strain rate is an optional argument, with
default value $0.0$. This method is pure virtual, so it must be
implemented in all subclasses of UniaxialMaterial. 

The next two methods,
`getStrain()` and `getStrainRate()`, are to return the current strain
and strain rate of this UniaxialMaterial. The method `getStrain()` is
pure virtual, while `getStrainRate()` is only virtual; by default it
returns $0.0$, but may be overridden in subclasses if needed.
```cpp
    double
    UniaxialMaterial::getStrainRate(void)
    {
       return 0.0;
    }
```


The `getDampTangent()` method is next, and is to 
return the current
damping tangent, which is the partial derivative of the current stress
with respect to the current strain rate,

$$\eta = \frac{\partial{\sigma}}{\partial{\dot{\varepsilon}}} \: .$$

By default, this method returns $0.0$, and it may be overridden in
subclasses of UniaxialMaterial where there is strain rate dependence.
```cpp
    double
    UniaxialMaterial::getDampTangent(void)
    {
       return 0.0;
    }
```

Finally, the `getSecant()` method is provided to return the material
secant, which is the current stress divided by the current strain,

$$D_s = \frac{\sigma}{\varepsilon} \: .$$

By default, this method returns the result of dividing the current
stress by the current strain. If the current strain is zero, the current
tangent is returned instead.
```cpp
    double
    UniaxialMaterial::getSecant(void)
    {
       double strain = this->getStrain();
       double stress = this->getStress();

       if (strain != 0.0)
          return stress/strain;
       else
          return this->getTangent();
    }
```

The next set of methods deal with possible path dependent behavior of
UniaxialMaterial models. All Material objects in OpenSees are
responsible for keeping track of and updating their own history
variables. First, the method `commitState()` is invoked to inform a
`UniaxialMaterial` object that its current state is on the converged
solution path and its internal history variables should be updated
accordingly. Next, the method `revertToLastCommit()` is provided to let
a UniaxialMaterial object know that it should return to its last
committed state at. Finally, `revertToStart()` informs the
UniaxialMaterial object to revert to its initial state, i.e., at the
start of the analysis. All three of these methods are pure virtual, and
thus must be implemented in all subclasses of UniaxialMaterial.


## Example -- HardeningMaterial

In this section, it is shown how the rate-independent uniaxial hardening
material model given in Simo & Hughes, *Computational Inelasticity*
(1998) is implemented in OpenSees. First, the class implementation is
shown, followed by its inclusion in the Tcl model builder.

### Class Implementation

The HardeningMaterial class interface is shown below. Here, no methods
are virtual since this class provides implementations for the
corresponding methods inherited from the UniaxialMaterial class.

::: {.center}
![](../Material.svg) 
:::

Note, three additional methods not declared in the UniaxialMaterial
interface, `sendSelf()`, `recvSelf()`, and `Print()`, must be defined in
implementations of UniaxialMaterial. These methods are inherited from
higher level classes in the OpenSees framework, particularly,
TaggedObject and MovableObject. An explanation of these methods is
provided in what follows.

```cpp
    #include <UniaxialMaterial.h>

    class HardeningMaterial : public UniaxialMaterial
    {
       public:
          HardeningMaterial(int tag, double E, double sigmaY, double Hiso, double Hkin);
          HardeningMaterial();
          ~HardeningMaterial();

          int setTrialStrain(double strain, double strainRate = 0.0); 
          double getStrain(void);          
          double getStress(void);
          double getTangent(void);

          int commitState(void);
          int revertToLastCommit(void);    
          int revertToStart(void);        

          UniaxialMaterial *getCopy(void);
        
          int sendSelf(int commitTag, Channel &theChannel);  
          int recvSelf(int commitTag, Channel &theChannel, 
                       FEM_ObjectBroker &theBroker);    
        
          void Print(OPS_Stream &s, int flag = 0);
        
       protected:
        
       private:
          // Material parameters
          double E;       // Elastic modulus
          double sigmaY;  // Yield stress
          double Hiso;    // Isotropic hardening modulus
          double Hkin;    // Kinematic hardening modulus

          // Committed history variables
          double CplasticStrain;  // Committed plastic strain
          double CbackStress;     // Committed back stress;
          double Chardening;      // Committed internal hardening variable

          // Trial history variables
          double TplasticStrain;  // Trial plastic strain
          double TbackStress;     // Trial back stress
          double Thardening;      // Trial internal hardening variable

          // Trial state variables
          double Tstrain;   // Trial strain
          double Tstress;   // Trial stress
          double Ttangent;  // Trial tangent
    };
```

The first two methods defined for HardeningMaterial are the
constructors. The first constructor takes the material tag and the
material parameters: elastic modulus, $E$, yield stress, $\sigma_y$,
isotropic hardening modulus, $H_{iso}$, and kinematic hardening modulus,
$H_{kin}$. The UniaxialMaterial base class constructor is invoked with
the arguments tag and `MAT_TAG_Hardening` (defined in `classTags.h`). The
material parameters for this object are initialized in the
initialization list with the arguments passed to the constructor, and
all history variables are initialized by invoking `revertToStart()`. The
second constructor is a default constructor which sets all material
parameters to $0.0$ then invokes `revertToStart()`.

```cpp
    HardeningMaterial::HardeningMaterial(int tag, double e, double s,
                                         double hi, double hk)
    :UniaxialMaterial(tag,MAT_TAG_Hardening),
     E(e), sigmaY(s), Hiso(hi), Hkin(hk)
    {
       // Initialize variables
       this->revertToStart();
    }

    HardeningMaterial::HardeningMaterial()
    :UniaxialMaterial(0,MAT_TAG_Hardening),
     E(0.0), sigmaY(0.0), Hiso(0.0), Hkin(0.0)
    {
       // Initialize variables
       this->revertToStart();
    }
```

The next method defined is the destructor, which does nothing since no
memory is dynamically allocated by a HardeningMaterial object.

    HardeningMaterial::~HardeningMaterial()
    {
       // Does nothing
    }

The following methods deal with the material state determination. The
return mapping algorithm is coded in `setTrialStrain()`. The stress and
tangent of this HardeningMaterial object are computed and stored in the
instance variables Tstress and Ttangent and returned by the methods
`getStress()` and `getTangent()`, respectively. The trial strain, stored
in the instance variable Tstrain, is returned by the method
`getStrain()`.

```cpp
    int 
    HardeningMaterial::setTrialStrain(double strain, double strainRate)
    {
       // Set total strain
       Tstrain = strain;
        
       // Elastic trial stress
       Tstress = E * (Tstrain-CplasticStrain);
        
       // Compute trial stress relative to committed back stress
       double xsi = Tstress - CbackStress;

       // Compute yield criterion
       double f = fabs(xsi) - (sigmaY + Hiso*Chardening);
        
       // Elastic step ... no updates required
       if (f <= 0.0) {
          // Set trial tangent
          Ttangent = E;
       }
       // Plastic step ... perform return mapping algorithm
       else {
          // Compute consistency parameter
          double dGamma = f / (E+Hiso+Hkin);
       
          // Find sign of xsi
          int sign = (xsi < 0) ? -1 : 1;

          // Bring trial stress back to yield surface
          Tstress -= dGamma*E*sign;
        
          // Update plastic strain
          TplasticStrain = CplasticStrain + dGamma*sign;
        
          // Update back stress
          TbackStress = CbackStress + dGamma*Hkin*sign;
        
          // Update internal hardening variable
          Thardening = Chardening + dGamma;
        
          // Set trial tangent
          Ttangent = E*(Hkin+Hiso) / (E+Hkin+Hiso);
       }

       return 0;
    }

    double 
    HardeningMaterial::getStress(void)
    {
       return Tstress;
    }

    double 
    HardeningMaterial::getTangent(void)
    {
       return Ttangent;
    }

    double 
    HardeningMaterial::getStrain(void)
    {
       return Tstrain;
    }
```

The next set of methods deal with the path dependent behavior of this
HardeningMaterial object. The method `commitState()` sets the committed
history variables to be their corresponding trial values. Nothing needs
to be done in the method `revertToLastCommit()`, and all history
variables are set to $0.0$ in `revertToStart()`.

```cpp
    int 
    HardeningMaterial::commitState(void)
    {
       // Commit trial state variables
       CplasticStrain = TplasticStrain;
       CbackStress = TbackStress;
       Chardening = Thardening;

       return 0;
    }

    int 
    HardeningMaterial::revertToLastCommit(void)
    {
       // Nothing to do here
       return 0;
    }

    int 
    HardeningMaterial::revertToStart(void)
    {
       // Reset committed history variables
       CplasticStrain = 0.0;
       CbackStress = 0.0;
       Chardening = 0.0;

       // Reset trial history variables
       TplasticStrain = 0.0;
       TbackStress = 0.0;
       Thardening = 0.0;

       // Initialize state variables
       Tstrain = 0.0;
       Tstress = 0.0;
       Ttangent = E;

       return 0;
    }
```

The `getCopy()` method is defined so this HardeningMaterial object can
provide a clone of itself to a calling object, be it an Element, Fiber,
or other Material object. The constructor is invoked to create a new
object, then all instance variables are copied to the new object. The
calling object is responsible for deleting this dynamically allocated
memory.

    UniaxialMaterial*
    HardeningMaterial::getCopy(void)
    {
       HardeningMaterial *theCopy = 
          new HardeningMaterial(this->getTag(), E, sigmaY, Hiso, Hkin);

       // Copy committed history variables
       theCopy->CplasticStrain = CplasticStrain;
       theCopy->CbackStress = CbackStress;
       theCopy->Chardening = Chardening;

       // Copy trial history variables
       theCopy->TplasticStrain = TplasticStrain;
       theCopy->TbackStress = TbackStress;
       theCopy->Thardening = Thardening;

       // Copy trial state variables
       theCopy->Tstrain = Tstrain;
       theCopy->Tstress = Tstress;
       theCopy->Ttangent = Ttangent;
        
       return theCopy;
    }

The next two methods are defined for parallel processing and database
programming, and are inherited from MovableObject. The first method,
`sendSelf()`, packs the material properties and committed history
variables in a Vector, then sends the Vector across the Channel object
passed as an argument to the method. The second method, `recvSelf()`,
receives data from the Channel object, then populates the data of this
HardeningMaterial object with the received data.

    int 
    HardeningMaterial::sendSelf(int cTag, Channel &theChannel)
    {
       static Vector data(8);
      
       data(0) = this->getTag();
       data(1) = E;
       data(2) = sigmaY;
       data(3) = Hiso;
       data(4) = Hkin;
       data(5) = CplasticStrain;
       data(6) = CbackStress;
       data(7) = Chardening;
      
       int res = theChannel.sendVector(this->getDbTag(), cTag, data);
       if (res < 0) 
          opserr << "HardeningMaterial::sendSelf() - failed to send data\n";

       return res;
    }

    int 
    HardeningMaterial::recvSelf(int cTag, Channel &theChannel, 
                                FEM_ObjectBroker &theBroker)
    {
       static Vector data(8);
       
       int res = theChannel.recvVector(this->getDbTag(), cTag, data);
      
       if (res < 0) {
          opserr << "HardeningMaterial::recvSelf() - failed to receive data\n";
          this->setTag(0);      
       }
       else {
          this->setTag((int)data(0));
          E = data(1);
          sigmaY = data(2);
          Hiso = data(3);
          Hkin = data(4);
          CplasticStrain = data(5);
          CbackStress = data(6);
          Chardening = data(7);

          // Set the trial state variables
          revertToLastCommit();
       }
        
       return res;
    }

The final HardeningMaterial method is `Print()`, which writes the
material name, tag, and parameters to the output stream passed as an
argument. This method is inherited from TaggedObject.

    void 
    HardeningMaterial::Print(OPS_Stream &s, int flag)
    {
       s << "HardeningMaterial, tag: " << this->getTag() << endln;
       s << "  E: " << E << endln;
       s << "  sigmaY: " << sigmaY << endln;
       s << "  Hiso: " << Hiso << endln;
       s << "  Hkin: " << Hkin << endln;
    }

### Tcl Model Builder

The new HardeningMaterial model must be added to the OpenSees Tcl model
builder in order for it to be used by analysis models defined in Tcl
script files. The general from of the uniaxialMaterial command is as
follows:

       uniaxialMaterial materialType tag <specific material parameters>

So, for a HardeningMaterial object, it is necessary to read in the
material parameters that are passed to its constructor, namely the
elastic modulus, yield stress, and isotropic and kinematic hardening
moduli. The general form of the command will be:

       uniaxialMaterial Hardening tag E sigmaY Hiso Hkin

An example command to add a HardeningMaterial object with tag $1$,
elastic modulus of $30000.0$, yield stress of $60.0$, isotropic
hardening modulus of $0.0$, and kinematic hardening modulus of $1000.0$
may then look like:

       uniaxialMaterial Hardening 1 30000.0 60.0 0.0 1000.0

How these values are parsed and used to construct a HardeningMaterial
object is described next. The parsing of input data for all
UniaxialMaterial models is done in the function
`TclModelBuilderUniaxialMaterialCommand` contained in the file
`TclModelBuilderUniaxialMaterialCommand.cpp`. In this file there are
multiple if/else statements, one for each UniaxialMaterial that can be
added to the model builder. To add the new model only requires adding an
additional case with the accompanying code to parse the Tcl command
line.

The above command is split into an array of character strings (`argv`) by
the Tcl interpreter, then sent to the
`TclModelBuilderUniaxialMaterialCommand` function. `argv[0]`
 contains the command name `"uniaxialMaterial"`, `argv[1]` holds the material
keyword `"Hardening"`, `argv[2]` contains the material tag, and the
remaining entries in the `argv` array hold the specific material
parameters. These parameters are the arguments needed to call the
HardeningMaterial constructor. The number of elements in the `argv` array
is stored in the variable `argc`.

Calls are made to the Tcl routines `Tcl_GetInt` and `Tcl_GetDouble` to
get integer and double values from the character strings contained in
argv. These routines perform error checking and return the pre-defined
value `TCL_OK` if there was no error. Once the UniaxialMaterial has been
allocated, it is added to the Tcl model builder at the end of the
`TclModelBuilderUniaxialMaterialCommand` function, after the multiple
if/else statement has ended.

```cpp
    int
    TclModelBuilderUniaxialMaterialCommand(ClientData clienData, Tcl_Interp *interp,
                                           int argc, char **argv,
                                           TclModelBuilder *theTclBuilder)
    {

       // Pointer to a UniaxialMaterial that will be added to the model builder
       UniaxialMaterial *theMaterial = 0;

       if (strcmp(argv[1],"Elastic") == 0) {
          //
          // Additional code not shown
          //
       }

       else if (strcmp(argv[1],"Hardening") == 0) {
          if (argc < 7) {
             opserr << "WARNING insufficient arguments\n";
             printCommand(argc,argv);
             opserr << "Want: uniaxialMaterial Hardening tag E sigmaY Hiso Hkin" << endln;
             return TCL_ERROR;
          }

          int tag;
          double E, sigmaY, Hiso, Hkin;

          if (Tcl_GetInt(interp, argv[2], &tag) != TCL_OK) {
             opserr << "WARNING invalid uniaxialMaterial Hardening tag" << endln;
             return TCL_ERROR;      
          }

          if (Tcl_GetDouble(interp, argv[3], &E) != TCL_OK) {
             opserr << "WARNING invalid E\n";
             opserr << "uniaxialMaterial Hardening: " << tag << endln;
             return TCL_ERROR;  
          }

          if (Tcl_GetDouble(interp, argv[4], &sigmaY) != TCL_OK) {
             opserr << "WARNING invalid sigmaY\n";
             opserr << "uniaxialMaterial Hardening: " << tag << endln;
             return TCL_ERROR;
          }

          if (Tcl_GetDouble(interp, argv[5], &Hiso) != TCL_OK) {
             opserr << "WARNING invalid Hiso\n";
             opserr << "uniaxialMaterial Hardening: " << tag << endln;
             return TCL_ERROR;  
          }

          if (Tcl_GetDouble(interp, argv[6], &Hkin) != TCL_OK) {
             opserr << "WARNING invalid Hkin\n";
             opserr << "uniaxialMaterial Hardening: " << tag << endln;
             return TCL_ERROR;  
          }

          // Parsing was successful, allocate the material
          theMaterial = new HardeningMaterial(tag, E, sigmaY, Hiso, Hkin);       
       }

       //
       // Additional code not shown
       //

       // Now add the material to the modelBuilder
       if (theTclBuilder->addUniaxialMaterial(*theMaterial) < 0) {
          opserr << "WARNING could not add uniaxialMaterial to the model builder\n";
          opserr << *theMaterial << endln;
          delete theMaterial; // invoke the material objects destructor,
                              // otherwise memory leak
          return TCL_ERROR;
       }

       return TCL_OK;
    }
```

### FEM_ObjectBroker

In order for the new `HardeningMaterial` object to be used for parallel
processing and database programming, the `getNewUniaxialMaterial()`
method in the `FEM_ObjectBroker` class must be modified. An additional
case statement should be added, as shown below. The `MAT_TAG_Hardening`
classTag is the same pre-defined value passed to the `UniaxialMaterial`
constructor by the HardeningMaterial constructor described earlier. The
`FEM_ObjectBroker` simply returns a blank `HardeningMaterial` object, whose
data can be subsequently populated by invoking `recvSelf()`.

```
    UniaxialMaterial*
    FEM_ObjectBroker::getNewUniaxialMaterial(int classTag)
    {
       switch(classTag) {

       case MAT_TAG_Hardening:
          return new HardeningMaterial();

       //
       // Additional cases not shown
       //

       default:
          opserr << "FEM_ObjectBroker::getPtrNewUniaxialMaterial - ";
          opserr << " - no UniaxialMaterial type exists for class tag ";
          opserr << classTag << endln;
          return 0;
       }        
    }
```

<strong><center>
Michael H. Scott and Gregory L. Fenves

PEER, University of California, Berkeley

August 21, 2001

Version 1.1
</center></strong>


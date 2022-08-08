# A FORTRAN Interface for UniaxialMaterial Models

Subclasses of UniaxialMaterial hide their implementation details from
calling objects, i.e., calling objects only see the public interface
defined in the UniaxialMaterial base class. How the interface is
implemented is encapsulated by each subclass of UniaxialMaterial. Thus,
a particular UniaxialMaterial implementation need not be written in C++
as long as the implementation conforms to the UniaxialMaterial
interface.

As an example, the FEDEAS uniaxial material library developed by F.C.
Filippou is used as a FORTRAN interface for UniaxialMaterial models in
OpenSees. This example is meant to demonstrate the process of linking
OpenSees with other material libraries and is not limited to just the
FEDEAS library. Material libraries with any well-defined interface, e.g.
DRAIN, may be linked in a similar manner. Similar concepts carry
directly over to implementing NDMaterial and SectionForceDeformation
models in FORTRAN.

### FEDEAS subroutine interface

The subroutine interface defined for a FEDEAS uniaxial material model
named "ML1D" is shown below.

    subroutine ML1D(matpar,hstvP,hstv,epsP,sigP,deps,sig,tang,ist)

The subroutine arguments are given as follows:

1. `matpar` - a double array of material parameters (in)

2. `hstvP` - a double array of committed history variables (in)

3. `hstv` - a double array of trial history variables (out)

4. `epsP` - strain at the last committed state (in)

5. `sigP` - stress at the last committed state (in)

6. `deps` - change in strain from the last committed state (in)

7. `sig` - the stress at the current trial state (out)

8. `tang` - the tangent at the current trial state (out)

9. `ist` - integer indicating the operation to be performed (in): 0 -
    return number of material parameters and history variables, 1 -
    compute stress and tangent, 2 - compute stress and secant

### FedeasMaterial Implementation in OpenSees

This section presents an implementation of UniaxialMaterial capable of
wrapping any subroutine that conforms to the FEDEAS interface described
in the previous section. This implementation, FedeasMaterial, manages
the data arrays sent to the FEDEAS subroutine, i.e., FedeasMaterial is
responsible for storing the material parameters and history variables,
as well as for swapping trial and committed history variables.

::: {.center}
![](../FedeasMaterial.svg) 
:::

FedeasMaterial is a subclass of UniaxialMaterial, as shown in
figure [\[fig:Fedeas$$
](#fig:Fedeas){reference-type="ref"
reference="fig:Fedeas"}. Subclasses of FedeasMaterial are responsible
for defining constructors which take the appropriate material
parameters. All other functionality (state determination, swapping of
history variables, etc.) is common to all subclasses of FedeasMaterial.
Therefore, this functionality is defined in the base class,
FedeasMaterial.

The FedeasMaterial class interface is shown below. All methods are
declared as virtual so they may be overridden by subclasses of
FedeasMaterial.

    #include <UniaxialMaterial.h>

    class FedeasMaterial : public UniaxialMaterial
    {
       public:
          FedeasMaterial(int tag, int classTag, int nhv, int ndata);
          virtual ~FedeasMaterial();
         
          virtual int setTrialStrain(double strain, double strainRate = 0.0);
          virtual double getStrain(void);
          virtual double getStress(void);
          virtual double getTangent(void);
         
          virtual int commitState(void);
          virtual int revertToLastCommit(void);    
          virtual int revertToStart(void);        
         
          virtual UniaxialMaterial *getCopy(void);
         
          virtual int sendSelf(int commitTag, Channel &theChannel);  
          virtual int recvSelf(int commitTag, Channel &theChannel, 
                              FEM_ObjectBroker &theBroker);    
         
          virtual void Print(OPS_Stream &s, int flag = 0);
         
       protected:
          // Invokes the FORTRAN subroutine
          virtual int invokeSubroutine(int ist);
         
          double *data;         // Material parameters array
          double *hstv;         // History array: first half is committed, second is trial
         
          int numData;          // Number of material parameters
          int numHstv;          // Number of history variables
         
          double epsilonP;      // Committed strain
          double sigmaP;        // Committed stress
         
       private:
          double epsilon;       // Trial strain
          double sigma;         // Trial stress
          double tangent;       // Trial tangent
    };

Instance variables are declared in FedeasMaterial to store history
variables and material parameters. First, data is a double array of size
numData, the number of material parameters for this object. Next, hstv
is a double array of size 2\*numHstv, where numHstv is the number of
history variables needed for this FedeasMaterial object. Note that
committed history variables are stored in the first half of the hstv
array, while the trial values are kept in the second half. The values
epsilonP and sigmaP are the committed strain and stress, respectively,
of this FedeasMaterial object, as they are required by the FEDEAS
subroutine interface. Finally, three trial state variables, epsilon,
sigma, and tangent are defined to store the current strain, stress, and
tangent.

The FedeasMaterial constructor initializes the number of history
variables and number of material parameters with arguments passed to the
constructor. The UniaxialMaterial base class constructor is invoked with
the tag and classTag arguments. The trial and committed strain and
stress are initialized to $0.0$. Then, the history variable and material
parameter arrays are allocated. All entries in the history variable and
material parameter arrays are initialized to $0.0$.

    FedeasMaterial::FedeasMaterial(int tag, int classTag, int nhv, int ndata)
    :UniaxialMaterial(tag,classTag),
     data(0), hstv(0), numData(ndata), numHstv(nhv),
     epsilonP(0.0), sigmaP(0.0),
     epsilon(0.0), sigma(0.0), tangent(0.0)
    {
       if (numHstv < 0)
          numHstv = 0;
         
       if (numHstv > 0) {
          // Allocate history array
          hstv = new double[2*numHstv];
          if (hstv == 0)
             g3ErrorHandler->fatal("%s -- failed to allocate history array -- type %d",
                                   "FedeasMaterial::FedeasMaterial", this->getClassTag());

          // Initialize to zero
          for (int i = 0; i < 2*numHstv; i++)
             hstv[i] = 0.0;
       }
         
       if (numData < 0)
          numData = 0;
         
       if (numData > 0) {
          // Allocate material parameter array
          data = new double[numData];
          if (data == 0)
             g3ErrorHandler->fatal("%s -- failed to allocate data array -- type %d",
                                   "FedeasMaterial::FedeasMaterial", this->getClassTag());

          // Initialize to zero
          for (int i = 0; i < numData; i++)
             data[i] = 0.0;
       }
    }

The FedeasMaterial destructor deallocates the memory allocated in the
constructor to hold the history variables and material parameters.

    FedeasMaterial::~FedeasMaterial()
    {
       if (hstv != 0)
          delete [] hstv;
         
       if (data != 0)
          delete [] data;
    }

The next group of FedeasMaterial methods deals with material state
determination. First, `setTrialStrain()` stores the trial strain, then
invokes the FEDEAS subroutine with ist = 1, indicating that normal
stress and tangent quantities should be computed. The methods
`getStrain()`, `getStress()`, and `getTangent()` return the strain,
stress, and tangent of this FedeasMaterial.

    int
    FedeasMaterial::setTrialStrain(double strain, double strainRate)
    {
       // Store the strain
       epsilon = strain;
         
       // Tells subroutine to do normal operations for stress and tangent
       int ist = 1;
         
       // Call the subroutine
       return this->invokeSubroutine(ist);
    }

    double
    FedeasMaterial::getStrain(void)
    {
       return epsilon;
    }

    double
    FedeasMaterial::getStress(void)
    {
       return sigma;
    }

    double
    FedeasMaterial::getTangent(void)
    {
       return tangent;
    }

The next three methods deal with the path dependent behavior of this
FedeasMaterial object. The `commitState()` method copies the trial
history variables from the second half of the hstv array to the first
half, where the committed values are stored. The committed values are
copied to the trial values in `revertToLastCommit()`, and all values are
set to $0.0$ in the `revertToStart()` method.

    int
    FedeasMaterial::commitState(void)
    {
       // Set committed values equal to corresponding trial values
       for (int i = 0; i < numHstv; i++)
          hstv[i] = hstv[i+numHstv];
         
       epsilonP = epsilon;
       sigmaP = sigma;
         
       return 0;
    }

    int
    FedeasMaterial::revertToLastCommit(void)
    {
       // Set trial values equal to corresponding committed values
       for (int i = 0; i < numHstv; i++)
          hstv[i+numHstv] = hstv[i];
         
       epsilon = epsilonP;
       sigma = sigmaP;
         
       return 0;
    }

    int
    FedeasMaterial::revertToStart(void)
    {
       // Set all trial and committed values to zero
       for (int i = 0; i < 2*numHstv; i++)
          hstv[i] = 0.0;
         
       epsilonP = 0.0;
       sigmaP = 0.0;
         
       return 0;
    }

A copy of this FedeasMaterial object is returned by `getCopy()`. First,
the FedeasMaterial constructor is called with the necessary tag, type,
and array size data. Then, the committed strain and stress, all history
variables, and material parameters are copied to the new object before
it is returned.

    UniaxialMaterial*
    FedeasMaterial::getCopy(void)
    {
       FedeasMaterial *theCopy = 
          new FedeasMaterial(this->getTag(), this->getClassTag(), numHstv, numData);
         
       // Copy history variables
       int i;
       for (i = 0; i < 2*numHstv; i++)
          theCopy->hstv[i] = hstv[i];
         
       for (i = 0; i < numData; i++)
          theCopy->data[i] = data[i];
         
       theCopy->epsilonP = epsilonP;
       theCopy->sigmaP = sigmaP;
         
       return theCopy;
    }

The next two methods are defined for parallel processing and database
programming. The first method, `sendSelf()`, packs the tag and array
size information for this FedeasMaterial object into an ID vector and
sends it across the Channel. Then, the material properties and committed
history variables are put in a Vector, and sent as well. The second
method, `recvSelf()`, receives both the ID and Vector data from the
Channel object, then populates the data of this FedeasMaterial object
with the appropriate data.

    int 
    FedeasMaterial::sendSelf(int commitTag, Channel &theChannel)
    {
       int res = 0;
         
       static ID idData(3);
         
       idData(0) = this->getTag();
       idData(1) = numHstv;
       idData(2) = numData;
         
       res += theChannel.sendID(this->getDbTag(), commitTag, idData);
       if (res < 0) 
          opserr << "FedeasMaterial::sendSelf() - failed to send ID data\n";
         
       Vector vecData(numHstv+numData+2);
         
       int i, j;
       // Copy only the committed history variables into vector
       for (i = 0; i < numHstv; i++)
          vecData(i) = hstv[i];
         
       // Copy material properties into vector
       for (i = 0, j = numHstv; i < numData; i++, j++)
          vecData(j) = data[i];
         
       vecData(j++) = epsilonP;
       vecData(j++) = sigmaP;
         
       res += theChannel.sendVector(this->getDbTag(), commitTag, vecData);
       if (res < 0) 
          opserr << "FedeasMaterial::sendSelf() - failed to send Vector data\n";
         
       return res;
    }

    int
    FedeasMaterial::recvSelf(int commitTag, Channel &theChannel,
                             FEM_ObjectBroker &theBroker)
    {
       int res = 0;
         
       static ID idData(3);
         
       res += theChannel.recvID(this->getDbTag(), commitTag, idData);
       if (res < 0) {
          opserr << "FedeasMaterial::recvSelf() - failed to receive ID data\n";
          return res;
       }
         
       this->setTag(idData(0));
       numHstv = idData(1);
       numData = idData(2);
         
       Vector vecData(numHstv+numData+2);
         
       res += theChannel.recvVector(this->getDbTag(), commitTag, vecData);
       if (res < 0) {
          opserr << "FedeasMaterial::recvSelf() - failed to receive Vector data\n";
          return res;
       }
         
       int i, j;
       // Copy committed history variables from vector
       for (i = 0; i < numHstv; i++)
          hstv[i] = vecData(i);
         
       // Copy material properties from vector
       for (i = 0, j = numHstv; i < numData; i++, j++)
          data[i] = vecData(j);
         
       epsilonP = vecData(j++);
       sigmaP   = vecData(j++);
         
       return res;
    }

The `Print()` method outputs the name of this FedeasMaterial object to
the stream passed as an argument. More cases can be added to the switch
statement as additional subroutines are added.


    void
    FedeasMaterial::Print(OPS_Stream &s, int flag)
    {
       s << "FedeasMaterial, type: ";
               
       switch (this->getClassTag()) {
       case MAT_TAG_FedeasHardening:
          s << "Hardening" << endln;
          break;

       // Add more cases as needed
           
       default:
          s << "Material identifier = " << this->getClassTag() << endln;
          break;
       }
    }

In order to link the FORTRAN subroutine with the OpenSees C++ libraries,
the following external function declarations are needed. There are two
syntactic styles for these declarations, one for Win32 and the other for
everything else. The preprocessor directives put the proper declaration
into the source code. Additional declarations may be added as more
subroutines are included in OpenSees.

    #ifdef _WIN32

    extern "C" int _stdcall HARD_1(double *matpar, double *hstvP, double *hstv,
                                   double *strainP, double *stressP, double *dStrain,
                                   double *tangent, double *stress, int *ist);

    #define hard_1_ HARD_1

    // Add more declarations as needed

    #else

    extern "C" int hard_1_(double *matpar, double *hstvP, double *hstv,
                           double *strainP, double *stressP, double *dStrain,
                           double *tangent, double *stress, int *ist);

    // Add more declarations as needed

    #endif

The method `invokeSubroutine()` calls the appropriate subroutine based
on the material classTag. The FedeasMaterial instance variables are
passed to the FORTRAN subroutine from this method. Additional cases in
the switch statement can be added as more subroutines are linked with
OpenSees.

    int
    FedeasMaterial::invokeSubroutine(int ist)
    {
       // Compute strain increment
       double dEpsilon = epsilon-epsilonP;
         
       switch (this->getClassTag()) {
       case MAT_TAG_FedeasHardening:
          hard_1_(data, hstv, &hstv[numHstv], &epsilonP, &sigmaP, &dEpsilon, 
                  &sigma, &tangent, &ist);
          break;
           
       // Add more cases as needed

       default:
          g3ErrorHandler->fatal("%s -- unknown material type",
                                "FedeasMaterial::invokeSubroutine");
          return -1;
       }
         
       return 0;
    }

### Example -- FedeasHardeningMaterial

The material data array defined in FedeasMaterial is populated by its
subclasses. As an example, consider the case where the uniaxial
hardening material is coded in a FORTRAN subroutine. In order to link
this subroutine with OpenSees, a subclass of FedeasMaterial,
FedeasHardeningMaterial, must be created (see
figure [fig:FedeasHardening](#fig:FedeasHardening){reference-type="ref"
reference="fig:FedeasHardening"}). The functionality of this subclass is
to populate the material parameter array and to determine the number of
history variables required for analysis.

::: {.center}
![Fedeas hardening material](../FedeasHardeningMaterial.svg){#fig:FedeasHardening}
:::

As additional FEDEAS subroutines are added to OpenSees, new subclasses
of FedeasMaterial must be added in order to populate the data array.
This is all that need be done in the derived class as the base class,
FedeasMaterial, contains all the computational code and keeps track of
path dependent behavior. This functionality is inherited from the
FedeasMaterial base class. However, the FedeasMaterial class must be
modified such that the appropriate subroutine is called during state
determination from the method `invokeSubroutine()`.

#### FEDEAS Hardening Subroutine

This section contains the implementation of the uniaxial hardening
material coded as a FORTRAN subroutine using the FEDEAS interface. The
subroutine declares local variables to store the material parameters
passed through the matpar array. The committed history variables are
received from hstvP, and the trial history variables are written to hstv
upon return. The trial stress and tangent are also set upon return in
the variables sig and tang.

<details><summary>FORTRAN source code</summary>

```fortran
          subroutine Hard_1(matpar,hstvP,hstv,epsP,sigP,deps,sig,tang,ist)
    c I  matpar contains fixed properties (4)
    c     E    = Elastic modulus             --> matpar(1)
    c     sigY = Yield stress                --> matpar(2)
    c     Hiso = Isotropic hardening modulus --> matpar(3)
    c     Hkin = Kinematic hardening modulus --> matpar(4)
    c
    c I  hstvP contains committed history variables:
    c     ep    = hstvP(1) --> plastic strain
    c     alpha = hstvP(2) --> internal hardening variable
    c     kappa = hstvP(3) --> back stress for kinematic hardening
    c    
    c O  hstv will be set to the corresponding trial values of hstvP
    c     hstv(1) = ep    
    c     hstv(2) = alpha 
    c     hstv(3) = kappa 
    c
    c I  epsP: strain at last committed state
    c I  sigP: stress at last committed state
    c I  deps: current strain increment
    c O  sig : updated stress
    c O  tang: updated tangent
    c I  ist : tangent calculation switch 
    c             1 = tangent, 2 = incremental secant, 3 = total secant

          implicit none
     
    c     Arguments
          integer ist
          real*8  matpar(4),hstvP(3),hstv(3)
          real*8  epsP,sigP,deps
          real*8  sig,tang

    c     Local variables
          real*8  E,sigY,Hiso,Hkin
          real*8  ep,alpha,kappa   
          real*8  eps,f,xsi,dGamma
          integer sgn

    c     Material parameters
          E    = matpar(1)
          sigY = matpar(2)
          Hiso = matpar(3)
          Hkin = matpar(4)

    c     History variables
          ep    = hstvP(1)
          alpha = hstvP(2)
          kappa = hstvP(3)

    c     Current strain
          eps = epsP + deps    

    c     Elastic predictor
          sig = E * (eps - ep)

    c     Stress relative to back stress
          xsi = sig - kappa

    c     Yield function
          f = dabs(xsi) - (sigY + Hiso*alpha)

    c     Inside yield surface
          if (f <= 0.0) then
             tang = E
    c     Outside yield surface ... do return mapping
          else
    c     Consistency parameter
             dGamma = f / (E+Hiso+Hkin)

    c     Normal to yield surface
             if (xsi <= 0.d0) then
                sgn = -1
             else
                sgn = 1
             endif

    c     Updated stress
             sig = sig - dGamma*E*sgn
        
    c     Updated plastic strain
             ep = ep + dGamma*sgn

    c     Updated back stress
             kappa = kappa + dGamma*Hkin*sgn
        
    c     Updated internal hardening variable
             alpha = alpha + dGamma

    c     Elasto-plastic tangent
             tang = E*(Hkin+Hiso) / (E+Hkin+Hiso)
          endif

    c     Update history variables
          hstv(1) = ep
          hstv(2) = alpha
          hstv(3) = kappa

    c     Compute requested tangent
          if (ist==2.and.deps/=0.d0) then
            tang = (sig-sigP)/deps
          else if (ist==3.and.eps/=0.d0)then
            tang = sig/eps
          else
    c     add additional cases, if needed
          endif          

          return

          end subroutine 
```

</details>

#### FedeasHardeningMaterial Subclass

As stated previously, the functionality of the FedeasHardeningMaterial
class is to read in the material parameters required for the Hard_1
subroutine invoked from the FedeasMaterial method `invokeSubroutine()`.
In addition, the required number of history variables must be passed to
the FedeasMaterial base class.

The class interface for FedeasHardeningMaterial is shown below. The
constructor takes the tag and material parameters as arguments. No other
methods are declared in the FedeasHardeningMaterial interface as all
functionality is inherited from FedeasMaterial.

    #include <FedeasMaterial.h>

    class FedeasHardeningMaterial : public FedeasMaterial
    {
       public:
          FedeasHardeningMaterial(int tag, double E, double sigmaY,
                                  double Hiso, double Hkin);
          FedeasHardeningMaterial(void);
          ~FedeasHardeningMaterial();

       protected:

       private:
    };

The constructor takes the tag, elastic modulus, yield stress, and
isotropic and kinematic hardening moduli as arguments. The
FedeasMaterial class constructor is called with the tag and classTag
`MAT_TAG_FedeasHardening` defined in classTags.h and the number of history
variables and material parameters required for this particular material
model. Then the material parameters are inserted into the data array.
The default constructor simply invokes the base class constructor, and
the destructor does nothing.

    FedeasHardeningMaterial::FedeasHardeningMaterial(int tag,
                                double E, double sigmaY, double Hiso, double Hkin):
    // 3 history variables and 4 material parameters
    FedeasMaterial(tag, MAT_TAG_FedeasHardening, 3, 4)
    {
       data[0] = E;
       data[1] = sigmaY;
       data[2] = Hiso;
       data[3] = Hkin;
    }

    FedeasHardeningMaterial::FedeasHardeningMaterial(void):
    FedeasMaterial(0, MAT_TAG_FedeasHardening, 3, 4)
    {
       // Does nothing
    }

    FedeasHardeningMaterial::~FedeasHardeningMaterial(void)
    {
       // Does nothing
    }

#### Important Polymorphic Note

Should any method in the FedeasMaterial class need to be overridden,
e.g., if a subclass does not want all of its history variables set to
$0.0$ in `revertToStart()`, the `getCopy()` method must also be
overridden to return a pointer to the subclass. If `getCopy()` is not
overridden, the dynamic type of the returned pointer will be of the
FedeasMaterial type and the overridden method, e.g., `revertToStart()`,
will not be called.

### Tcl Model Builder

Adding the FedeasHardeningMaterial model to the Tcl model builder is
done in exactly the same manner as for HardeningMaterial since both
models have the same material parameters. Only the material allocation
would change. The following line in
`TclModelBuilderUniaxialMaterialCommand.cpp`

          // Parsing was successful, allocate the material
          theMaterial = new HardeningMaterial(tag, E, sigmaY, Hiso, Hkin); 

would be changed to

```cpp
// Parsing was successful, allocate the material
theMaterial = new FedeasHardeningMaterial(tag, E, sigmaY, Hiso, Hkin); 
```

### `FEM_ObjectBroker`

As for the HardeningMaterial class, an additional case needs to be added
to the `getNewUniaxialMaterial()` method in FEM_ObjectBroker in order
for the FedeasHardeningMaterial class to be used for parallel processing
and database programming.

    UniaxialMaterial*
    FEM_ObjectBroker::getNewUniaxialMaterial(int classTag)
    {
       switch(classTag) {

       case MAT_TAG_Hardening:
          return new HardeningMaterial();

       case MAT_TAG_FedeasHardening:
          return new FedeasHardeningMaterial();

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


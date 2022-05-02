# C API 2

## Model Building

-------------------------------------------------------------------

```{.cpp}
Domain*                  OPS_GetDomain(void);
```

```
eleObj*     OPS_GetElement(int* eleTag);
matObj*     OPS_GetMaterialType(char* type, int sizeType);
eleObj*     OPS_GetElementType(char* type, int sizeType);
int         OPS_AllocateElement(eleObject * theEle, int* matTags, int* matType);
int         OPS_AllocateMaterial(matObject * theMat);
limCrvObj*  OPS_GetLimitCurveType(char* type, int sizeType);
int         OPS_AllocateLimitCurve(limCrvObject * theLimCrv);
```

### Coordinate Transformations
```{.cpp}
CrdTransf*               OPS_GetCrdTransf(int crdTag);
```

### Materials
```{.c}
UniaxialMaterial*        OPS_GetUniaxialMaterial(int matTag);
NDMaterial*              OPS_GetNDMaterial(int matTag);
matObj*                  OPS_GetMaterial(int* matTag, int* matType);
int addPlasticMaterial(PlasticHardeningMaterial &theMaterial)=0;
PlasticHardeningMaterial *getPlasticMaterial(int tag)=0;
```

### Sections
```{.cpp}
SectionForceDeformation* OPS_GetSectionForceDeformation(int secTag);
FrictionModel*           OPS_GetFrictionModel(int frnTag);
LimitCurve*              OPS_GetLimitCurve(int LimCrvTag);
int addSection(SectionForceDeformation &theSection)=0;
SectionForceDeformation *getSection(int tag)=0;
int addSectionRepres(SectionRepres &theSectionRepres)=0;
SectionRepres *getSectionRepres(int tag)=0;
```


### Other

#### Yield Surface
```{.cpp}
int addYieldSurface_BC(YieldSurface_BC &theYS)=0
YieldSurface_BC *getYieldSurface_BC(int tag)=0;
int addYS_EvolutionModel(YS_Evolution &theModel)=0;
YS_Evolution *getYS_EvolutionModel(int tag)=0;
```

#### Cyclic Models
```{.cpp}
int addCyclicModel(CyclicModel &theModel);
CyclicModel *getCyclicModel(int tag);
```

#### Damage models
```{.cpp}
int addDamageModel(DamageModel &theModel);
DamageModel *getDamageModel(int tag);
```

#### Friction models
```{.cpp}
int            addFrictionModel(FrictionModel &theFrnMdl);
FrictionModel *getFrictionModel(int tag);
```

## Runtime

-------------------------------------------------------------------

```{.cpp}
int     OPS_GetNDF();
int     OPS_GetNDM();

extern FE_Datastore* OPS_GetFEDatastore();
extern "C" const char* OPS_GetInterpPWD();

AnalysisModel**             OPS_GetAnalysisModel(void);
EquiSolnAlgo**              OPS_GetAlgorithm(void);
ConstraintHandler**         OPS_GetHandler(void);
DOF_Numberer**              OPS_GetNumberer(void);
LinearSOE**                 OPS_GetSOE(G3_Runtime*);
EigenSOE**                  OPS_GetEigenSOE(void);
StaticAnalysis**            OPS_GetStaticAnalysis(void);
DirectIntegrationAnalysis** OPS_GetTransientAnalysis(void);
VTDI_Analysis**             OPS_GetVTDI_Analysis(void);
// VTDI_Analysis**          OPS_GetVariableTimeStepTransientAnalysis(void);
StaticIntegrator**          OPS_GetStaticIntegrator(void);
TransientIntegrator**       OPS_GetTransientIntegrator(void);
ConvergenceTest**           OPS_GetTest(void);
bool*                       OPS_builtModel(void);
```

## Conducting Analysis

```{.c}
int* OPS_GetNumEigen(void);
int  OPS_InvokeMaterial(eleObject*, int*, modelState*, double*, double*, double*, int*);
int  OPS_InvokeMaterialDirectly(matObject**, modelState*, double*, double*, double*, int*);
int  OPS_InvokeMaterialDirectly2(matObject*, modelState*, double*, double*, double*, int*);
int  OPS_GetNodeDisp(int* nodeTag, int* sizeData, double* data);
int  OPS_GetNodeVel(int* nodeTag, int* sizeData, double* data);
int  OPS_GetNodeAccel(int* nodeTag, int* sizeData, double* data);
int  OPS_GetNodeIncrDisp(int* nodeTag, int* sizeData, double* data);
int  OPS_GetNodeIncrDeltaDisp(int* nodeTag, int* sizeData, double* data);
int  OPS_GetNodeCrd(int* nodeTag, int* sizeData, double* data);

int OPS_numIter(void);
```

## IO

```{.c}
int         OPS_GetNumRemainingInputArgs();
int         OPS_ResetCurrentInputArg(int cArg);
int         OPS_GetIntInput(int* numData, int* data);
int         OPS_SetIntOutput(int* numData, int* data, bool scalar);
int         OPS_GetDoubleInput(int* numData, double* data);
int         OPS_SetDoubleOutput(int* numData, double* data, bool scalar);
const char* OPS_GetString(); // does a strcpy
const char* OPS_GetStringFromAll(char* buffer, int len); // does a strcpy
int         OPS_SetString(const char* str);
int         OPS_GetStringCopy(char** cArray); // returns a new copy

int       OPS_ResetInput(ClientData clientData, Tcl_Interp * interp, int cArg, int mArg, TCL_Char * *argv, Domain * domain, TclModelBuilder * builder);
int         OPS_ResetInputNoBuilder(ClientData clientData, Tcl_Interp * interp, int cArg, int mArg, TCL_Char * *argv, Domain * domain);
int       OPS_GetString(char *cArray, int sizeArray); // does a strcpy
void      OPS_GetMaterialPtr(int *matTag, matObj *theRes);
```

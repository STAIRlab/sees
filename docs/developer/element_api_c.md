

## IO API

```
int  OPS_GetIntInput(int* numData, int* data);
int  OPS_GetDoubleInput(int* numData, double* data);
int  OPS_GetString(char* cArray, int sizeArray);
int  OPS_Error(char*, int length);
```

## Model Building API

```
matObj* OPS_GetMaterial(int* matTag, int* matType);
void    OPS_GetMaterialPtr(int*, matObj*);
eleObj* OPS_GetElement(int*);
matObj* OPS_GetMaterialType(char* type, int sizeType);
eleObj* OPS_GetElementType(char*, int);
int     OPS_AllocateElement(eleObj*, int* matTags, int* maType);
int     OPS_AllocateMaterial(matObj*);

limCrv* OPS_GetLimitCurveType(char* type, int sizeType);//**MRL
int     OPS_AllocateLimitCurve(limCrvObj*);//**MRL

int    OPS_InvokeMaterial(struct eleObj*, int*, modelState*, double*, double*, double*, int*);
int    OPS_InvokeMaterialDirectly(matObj**, modelState*, double*, double*, double*, int*);
int    OPS_InvokeMaterialDirectly2(matObj*, modelState*, double*, double*, double*, int*);

int    OPS_GetNodeCrd(int* nodeTag, int* sizeData, double* data);
int    OPS_GetNodeDisp(int* nodeTag, int* sizeData, double* data);
int    OPS_GetNodeVel(int* nodeTag, int* sizeData, double* data);
int    OPS_GetNodeAcc(int* nodeTag, int* sizeData, double* data);
int    OPS_GetNodeIncrDisp(int* nodeTag, int* sizeData, double* data);
int    OPS_GetNodeIncrDeltaDisp(int* nodeTag, int* sizeData, double* data);
```


## Runtime API

```{.c}
int     OPS_GetNDF();
int     OPS_GetNDM();

AnalysisModel** OPS_GetAnalysisModel(void);
EquiSolnAlgo** OPS_GetAlgorithm(void);
ConstraintHandler** OPS_GetHandler(void);
DOF_Numberer** OPS_GetNumberer(void);
LinearSOE** OPS_GetSOE(void);
EigenSOE** OPS_GetEigenSOE(void);
StaticAnalysis** OPS_GetStaticAnalysis(void);
DirectIntegrationAnalysis** OPS_GetTransientAnalysis(void);
VariableTimeStepDirectIntegrationAnalysis** OPS_GetVariableTimeStepTransientAnalysis(void);
int* OPS_GetNumEigen(void);
StaticIntegrator** OPS_GetStaticIntegrator(void);
TransientIntegrator** OPS_GetTransientIntegrator(void);
ConvergenceTest**     OPS_GetTest(void);
bool*                 OPS_builtModel(void);
```


```{.c}
#define ISW_INIT 0
#define ISW_COMMIT 1
#define ISW_REVERT 2
#define ISW_FORM_TANG_AND_RESID 3
#define ISW_FORM_MASS 4
#define ISW_REVERT_TO_START 5
#define ISW_DELETE 6

#define ISW_SET_RESPONSE 7
#define ISW_GET_RESPONSE 8
```

```{.c}
#define OPS_UNIAXIAL_MATERIAL_TYPE 1
#define OPS_SECTION2D_TYPE 2
#define OPS_SECTION3D_TYPE 3
#define OPS_PLANESTRESS_TYPE 4
#define OPS_PLANESTRAIN_TYPE 5
#define OPS_THREEDIMENSIONAL_TYPE 6
#define OPS_SECTION_TYPE 7
```

```{.c}
typedef struct modState modelState;
typedef void (*matFunct)(struct matObject*, modelState*, double* strain, double* tang, double* stress, int* isw, int* error);
typedef struct limCrvObject limCrvObj;
typedef void (*eleFunct)(struct eleObject*, modelState*, double* tang, double* resid, int* isw, int* error);
typedef struct eleObject eleObj;


typedef struct matObject matObj;

typedef void (*limCrvFunct)(struct limCrvObject*, modelState*, double* strain, double* tang, double* stress, int* isw, int* error);
```


```{.c}
struct modState {
    double time;
    double dt;
};

struct matObject {
    int tag;
    int matType;
    int nParam;
    int nState;
    double* theParam;
    double* cState;
    double* tState;
    matFunct matFunctPtr;
    void* matObjectPtr;
};

struct limCrvObject {
    int tag;
    int nParam;
    int nState;
    double* theParam;
    double* cState;
    double* tState;
    limCrvFunct limCrvFunctPtr;
    void* limCrvObjectPtr;
};

struct eleObject {
    int tag;
    int nNode;
    int nDOF;
    int nParam;
    int nState;
    int nMat;
    int* node;
    double* param;
    double* cState;
    double* tState;
    matObj** mats;
    eleFunct eleFunctPtr;
};

```

## Runtime API

OPS_GetNDF(void)
OPS_GetNDM(void)

OPS_InvokeMaterialObject(struct matObject *theMat, modelState *theModel,
OPS_Error(char *errorMessage, int length)
OPS_GetMaterial(int *matTag, int *matType)
OPS_GetElement(int *eleTag)
OPS_GetElementType(char *type, int sizeType)
OPS_GetMaterialType(char *type, int sizeType)
OPS_GetLimitCurveType(char *type, int sizeType)
OPS_AllocateLimitCurve(limCrvObject *theLimCrv)
OPS_AllocateMaterial(matObject *theMat)
OPS_AllocateElement(eleObject *theEle, int *matTags, int *matType)

OPS_GetNodeCrd(int *nodeTag, int *sizeCrd, double *data)
OPS_GetNodeDisp(int *nodeTag, int *sizeData, double *data)
OPS_GetNodeVel(int *nodeTag, int *sizeData, double *data)
OPS_GetNodeAccel(int *nodeTag, int *sizeData, double *data)
OPS_GetNodeIncrDisp(int *nodeTag, int *sizeData, double *data)
OPS_GetNodeIncrDeltaDisp(int *nodeTag, int *sizeData, double *data)

OPS_InvokeMaterial(eleObject *theEle, int *mat, modelState *model,
OPS_InvokeMaterialDirectly(matObject **theMat, modelState *model,
OPS_InvokeMaterialDirectly2(matObject *theMat, modelState *model,
OPS_GetUniaxialMaterial(int matTag)
OPS_GetNDMaterial(int matTag)
OPS_GetSectionForceDeformation(int secTag)

OPS_GetCrdTransf(int crdTag)
OPS_GetFrictionModel(int frnTag)

OPS_GetFEDatastore()
OPS_GetInterpPWD()
OPS_GetDomain(void)
OPS_GetLimitCurve(int LimCrvTag)
OPS_GetAnalysisModel(void)
OPS_GetAlgorithm(void)
OPS_GetHandler(void)
OPS_GetNumberer(void)
OPS_GetSOE(void)
OPS_GetEigenSOE(void)
OPS_GetStaticAnalysis(void)
OPS_GetTransientAnalysis(void)
OPS_GetVariableTimeStepTransientAnalysis(void)
OPS_GetNumEigen(void)
OPS_GetStaticIntegrator(void)
OPS_GetTransientIntegrator(void)
OPS_GetTest(void)
OPS_builtModel(void)
OPS_numIter()

## Parsing API

```{.c}
OPS_GetString(void)
OPS_GetStringFromAll(char *buffer, int len)
OPS_SetString(const char *str)
OPS_GetStringCopy(char **arrayData)

OPS_GetNumRemainingInputArgs()
OPS_ResetCurrentInputArg(int cArg)
OPS_ResetInput(ClientData clientData, Tcl_Interp *interp, int cArg, int mArg,
OPS_ResetInputNoBuilder(ClientData clientData, Tcl_Interp *interp, int cArg,
OPS_GetIntInput(int *numData, int *data)
OPS_SetIntOutput(int *numData, int *data, bool scalar)
OPS_GetDoubleInput(int *numData, double *data)
OPS_SetDoubleOutput(int *numData, double *data, bool scalar)
```

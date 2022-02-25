# G3 API



## Model Building

```{.cpp}
extern Domain* G3_getDomain(Tcl_Interp*);
```

### Materials
```{.cpp}
extern UniaxialMaterial* G3_getUniaxialMaterialInstance(Tcl_Interp*, int);
```

```{.cpp}
int G3_addUniaxialMaterial(Tcl_Interp*, UniaxialMaterial*);
```

### Loading
```{.cpp}
int G3_addTimeSeries(Tcl_Interp *, TimeSeries *);
```

```{.cpp}
TimeSeries* G3_getTimeSeries(Tcl_Interp *, int);
```

```{.cpp}
StaticAnalysis* G3_getStaticAnalysis(Tcl_Interp*);
```

```{.cpp}
int G3_setStaticAnalysis(Tcl_Interp*, StaticAnalysis*);
```

```{.cpp}
StaticIntegrator* G3_getStaticIntegrator(Tcl_Interp*);
```

```{.cpp}
int G3_setStaticIntegrator(Tcl_Interp*, StaticIntegrator*);
```

```{.cpp}
TclSafeBuilder *G3_getSafeBuilder(Tcl_Interp *);
```



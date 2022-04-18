# G3 API

## Model Building

```cpp
Domain* G3_getDomain(G3_Runtime*);
```

### Materials
```cpp
UniaxialMaterial* G3_getUniaxialMaterialInstance(G3_Runtime*, int);
```

```cpp
int G3_addUniaxialMaterial(G3_Runtime*, UniaxialMaterial*);
```

### Loading
```cpp
int G3_addTimeSeries(G3_Runtime *, TimeSeries *);
```

```cpp
TimeSeries* G3_getTimeSeries(G3_Runtime *, int);
```

```cpp
StaticAnalysis* G3_getStaticAnalysis(G3_Runtime*);
```

```cpp
int G3_setStaticAnalysis(G3_Runtime*, StaticAnalysis*);
```

```cpp
StaticIntegrator* G3_getStaticIntegrator(G3_Runtime*);
```

```cpp
int G3_setStaticIntegrator(G3_Runtime*, StaticIntegrator*);
```

```cpp
TclSafeBuilder *G3_getSafeBuilder(G3_Runtime *);
```

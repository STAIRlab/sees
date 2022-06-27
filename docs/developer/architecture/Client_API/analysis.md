# Analysis API

## Static Analysis

```cpp
G3_setStaticAnalysis(G3_Runtime* rt, StaticAnalysis* analysios)
```


## Transient Analysis

```cpp
G3_setTransientAnalysis(G3_Runtime* rt, DirectIntegrationAnalysis* analysis);
```

## Systems of Equations

```cpp
G3_setLinearSoe(G3_Runtime* rt, LinearSOE* soe);
```
Point the runtime, `rt`, to the [`LinearSOE`] pointer, `soe`. If the
runtime is aware of a [`StaticAnalysis`] or [`DirectIntegrationAnalysis`],
their respective `setLinearSOE()` methods will be called.

```cpp
LinearSOE** G3_getLinearSoePtr(G3_Runtime* rt);
```
Get the current system of equations.

```cpp
LinearSOE *G3_getDefaultLinearSoe(G3_Runtime* rt, int flags);
```
`flags` is unused right now but could be useful                                                                                      
for ensuring properties about the SOE, like
forcing fullGen.


[`StaticAnalysis`]: ../class_interface/analysis/analysis/StaticAnalysis
[`LinearSOE`]: ../class_interface/sys_of_eqn/linearSOE/LinearSOE

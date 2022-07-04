# AlgebraicHysteretic

This package provides an infrastructure for constructing
algebraic univariate hysteretic models.


```tcl
uniaxialMaterial OOHysteretic tag? 
     bkbn+? unlRul+? stfDeg+? strDeg+?
    <bkbn-? unlRul-? stfDeg-? strDeg-?> 
    <pinchX? pinchY?>
```


- `HystereticBackbone`

  ```tcl
  hystereticBackbone ReeseSoftClay tag? pu? y50? n?
  hystereticBackbone ReeseSand tag? kx? ym? pm? yu? pu?
  hystereticBackbone ReeseStiffClayBelowWS tag? Esi? y50? As?  Pc?
  hystereticBackbone Raynor tag? Es? fy? fsu? Epsilonsh? Epsilonsm? C1? Ey?
  hystereticBackbone Capped tag? hystereticBackboneTag? capTag?
  hystereticBackbone LinearCapped tag? backboneTag? eCap? E? sRes?
  hystereticBackbone Material tag? matTag?
  ```

<!--
      hystereticBackbone Bilinear
        void *theBB = OPS_BilinearBackbone(rt);

      hystereticBackbone Trilinear
        void *theBB = OPS_TrilinearBackbone(rt);

      hystereticBackbone Multilinear
        void *theBB = OPS_MultilinearBackbone(rt);

      hystereticBackbone Arctangent
        void *theBB = OPS_ArctangentBackbone(rt);

      hystereticBackbone Mander
        void *theBB = OPS_ManderBackbone(rt);
-->

- `UnloadingRule`
  ```tcl
  unloadingRule type? tag? <specific unloadingRule args>
  ```

  - Ductility (Takeda)

  - `Energy`: models hysteretic strength
    degradation with the deterioration parameter developed by
    Rahnama and Krawinkler (1993).

  - Constant
  - Karsan

- `StiffnessDegradation`
  - Section, 
  - Energy, 
  - Constant, 
  - Ductility, 
  - ACI, 
  - Petrangeli


- `StrengthDegradation`
  ```tcl
  strengthDegradation type? tag? <specific strengthDegradation args>
  ```




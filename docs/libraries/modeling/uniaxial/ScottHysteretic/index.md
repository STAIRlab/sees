# ScottHysteretic

```tcl
uniaxialMaterial OOHysteretic tag? 
     bkbn+? unlRul+? stfDeg+? strDeg+?
    <bkbn-? unlRul-? stfDeg-? strDeg-?> 
    <pinchX? pinchY?>
```


- HystereticBackbone

    hystereticBackbone type? tag? <specific hystereticBackbone args>

      hystereticBackbone ReeseSoftClay tag? pu? y50? n?
      hystereticBackbone ReeseSand tag? kx? ym? pm? yu? pu?
      hystereticBackbone ReeseStiffClayBelowWS tag? Esi? y50? As?  Pc?
      hystereticBackbone Raynor tag? Es? fy? fsu? Epsilonsh? Epsilonsm? C1? Ey?
      hystereticBackbone Capped tag? hystereticBackboneTag? capTag?
      hystereticBackbone LinearCapped tag? backboneTag? eCap? E? sRes?
      hystereticBackbone Material tag? matTag?" << endln;

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

- UnloadingRule

    unloadingRule type? tag? <specific unloadingRule args>

- StiffnessDegradation


- StrengthDegradation

    strengthDegradation type? tag? <specific strengthDegradation args>


## Class Interface




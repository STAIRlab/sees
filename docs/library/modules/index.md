

- Misc
  - `background`
  - `mesh`
  - `remesh`
  - `Hfiber`
  - `generateInterfacePoints`
  - `multipleNormalSpring`


- PyGen, Scott J. Brandenberg
  - `PySimple1Gen`
  - `TzSimple1Gen`

- UCSD, Prishati Raychowdhury
  - `ShallowFoundationGen`

- Reliability
  - `parameter`
  - `addToParameter`
  - `updateParameter`
  - **element** []
  - **uniaxialMaterial** []

- force/displBeamColumn
  - `beamIntegration`

- `UpdatedLagrangianBeamColumn` by Rohit Kaul (rkaul@stanford.edu), Greg Deierlein   (ggd@stanford.edu)
  - **element** UpdatedLagrangianBeamColumn
  - **element** element2dYS03 (Uses **YieldSurface** objects)
  - `cyclicModel`

- `FrictionBearing`
  - `frictionModel`
  - **element** TripleFrictionPendulum
  - **element** RJWatsonEqsBearing
  - **element** flatSliderBearing
  - **element** singleFPBearing
  - **element** MultiFP2d

- CompGeoMech
  - **nDmaterial** `Template3Dep`

- Altoonash / SNAP
  - **element** Joint2D
  - **uniaxialMaterial** SNAP\*
  - `damageModel`

- YieldSurface
  - **section** YS_Section\*
  - yieldSurface_BC
  - ysEvolutionModel
  - plasticMaterial

- LimitState Material
  - **uniaxialMaterial** LimitState...
  - `limitCurve`

- AlgebraicHystereis
  - **uniaxialMaterial** OOHysteretic...
  - `unloadingRule`
  - `strengthDegradation`
  - `stiffnessDegradation`
  - `hystereticBackbone`



# Material

Description: This file contains the implementation of 
MaterialBackbone, which treats a uniaxial material as
a hysteretic backbone by removing path dependency, i.e.
commitState is never called on the uniaxial material.

Code developed by: <span style="color:blue">MHS</span>
Created: Aug 2000

## C++ Interface

```cpp
class MaterialBackbone : public HystereticBackbone
{
 public:
  MaterialBackbone(int tag, UniaxialMaterial &material);
  
 private:
  UniaxialMaterial *theMaterial;
};
```

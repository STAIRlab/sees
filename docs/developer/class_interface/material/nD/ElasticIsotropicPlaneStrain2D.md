\
# ElasticIsotropicPlaneStrain2D 

```cpp
#include <material/nD/ElasticIsotropicPlaneStrain2D.h>
```

class ElasticIsotropicPlaneStrain2D : public ElasticIsotropicMaterial\

TaggedObject\
MovableObject\
Material\
NDMaterial\
ElasticIsotropicMaterial\

\
ElasticIsotropicPlaneStrain2D provides the implementation of an elastic
isotropic material which exhibits plane strain behavior in two
dimensions.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\

\

To construct an ElasticIsotropicPlaneStrain2D whose unique integer tag
among NDMaterials in the domain is given by *tag*. The material model
have Young's modulus *E* and Poisson's ratio *v*.

\
Does nothing.

\
Sets the value of the current trial strain vector, $\myepsilon$, to be
*strain*. Returns $0$.
$$\myepsilon := \left[
   \begin{array}{c}
       \epsilon_{xx} \\
       \epsilon_{yy}   \\
       2 \gamma_{xy}   
   \end{array} 
 \right]$$


Returns the material stress vector, $\mysigma$, for the current trial
strain.
$$\mysigma := \left[
   \begin{array}{c}
       \sigma_{xx} \\
       \sigma_{yy}   \\
       \tau_{xy}   
   \end{array} 
 \right]$$


Returns the material tangent stiffness matrix, $\D$.
$$\D := \frac{E}{(1+\nu)(1-2\nu)} \left[
   \begin{array}{ccc}
         1-\nu &     \nu &      0 \\
           \nu &   1-\nu &      0 \\
             0 &       0 & 1-2\nu
   \end{array} 
 \right]$$


Returns $0$.

Returns $0$.

Returns $0$.

Returns a pointer to a new ElasticIsotropicPlaneStrain2D, with the same
values for *tag*, *E*, and $\nu$. It is up to the caller to ensure that
the destructor is invoked.

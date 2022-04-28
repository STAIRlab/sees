# Transformation

>UNDER CONSTRUCTION.

```cpp
#include <analysis/handler/TransformationConstraintHandler.h>

class TransformationConstraintHandler: 
public ConstraintHandler
    MovableObject
    ConstraintHandler
```


The TransformationConstraintHandler class is a class which deals with
both single and multi point constraints using the Transformation method.
This is done by, in addition to creating a DOF_Group object for each
Node and an FE_Element for each Element in the Domain, creating either a
TransformationSP_FE or a TransformationMP_FE object for each constraint
in the Domain. It is these objects that enforce the constraints by
moifying the tangent matrix and residual vector.

### Constructor

\
### Destructor

\
// Public Methods\

\

\

\

\
The integer *HANDLER_TAG_TransformationConstraintHandler* (defined in
 `<classTags.h>`) is passed to the TransformationConstraintHandler
constructor.


\
Currently invokes `clearAll()`, this will change when `clearAll()` is
rewritten.

\

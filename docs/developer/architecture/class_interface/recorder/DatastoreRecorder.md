


# DatastoreRecorder 

```cpp
#include <recorder/DatastoreRecorder.h>
```



class DatastoreRecorder: public Recorder



Recorder






A DatastoreRecorder object is used in the program to invoke
`commitState()` on an FE_Datastore object when `commit()` is invoked on
a Domain. The class is included in the framework so that the Domain
class does not have to be modified for FE_Datastore objects.

// Constructor






// Destructor






// Public Methods











Saves a pointer to the object *theDatastore*.




Does nothing.




Returns the result of invoking `commitState(commitTag)` on
*theDatastore* object.

Returns the result of invoking `restoreState(commitTag)` on
*theDatastore* object.

Does nothing.

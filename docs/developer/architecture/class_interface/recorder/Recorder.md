


# Recorder 

```cpp
#include <recorder/Recorder.h>
```



class Recorder







The Recorder class is an abstract class which is introduced to allow
information to be saved during the analysis. The interface defines two
pure virtual methods `record()` and `playback()`. `record()` is a method
which is called by the Domain object during a `commit()`. The
`playback()` method can be called by the analyst after the analysis has
been performed.

// Constructor






// Destructor






// Public Methods











Does nothing.




Does nothing.




Invoked by the Domain object after `commit()` has been invoked on all
the domain component objects. What the Recorder records depends on the
concrete subtype.

Invoked by the analyst after the analysis has been performed. What the
Recorder does depends on the concrete subtype.

Invoked by the Domain object when `revertToStart()` is invoked on the
Domain object. What the Recorder does depends on the concrete subtype.

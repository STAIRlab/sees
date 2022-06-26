


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


### Public Methods


```cpp
virtual int record(int commitTag, double timeStamp) =0;
```

This is the method that is called when the recorder is called upon to record/save information. The method is called with a tag that will be unique and the current time in the domain.
More specifically, the method is invoked by the Domain object after `commit()` has been invoked on all
the domain component objects. What the Recorder records depends on the
concrete subtype.

```
virtual int setDomain(Domain &theDomain);
```
This is the method that is called when the new recorder object is first added to the domain. It is inside this method that all data, typically memory and pointer values, need to be initialized for subsequent record commands.


```cpp
virtual int domainChanged(void);
```
this is a method called when something major has happened in the Domain, eg. a new element, node, constraint and/or load pattern has been added to the domain or removed from the domain. It is necessasry for the Recorder to check in this call if it's pointers are still valid (i.e. if an element it was recording info for has been removed from the domain, it will have been deleted and it's old pointer information will no longer be valid.)

```cpp
virtual int sendSelf(int commitTag, Channel &theChannel);  
virtual int recvSelf(int commitTag, Channel &theChannel, FEM_ObjectBroker &theBroker);
```
These methods are called in parallel applications. When invoked the recorders send/recv information about what they are recording.

```cpp
virtual int restart(void);
```
Invoked by the Domain object when `revertToStart()` is invoked on the
Domain object. What the Recorder does depends on the concrete subtype.

```cpp
virtual double getRecordedValue(int clmnId, int rowOffset, bool reset) { return 0; } //added by SAJalali
```


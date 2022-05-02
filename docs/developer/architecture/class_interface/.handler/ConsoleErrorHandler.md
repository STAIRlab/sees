


# ConsoleErrorHandler 

```cpp
#include <handler/ConsoleErrorHandler.h>
```



class ConsoleErrorHandler



ErrorHandler






The ConsoleErrorHandler class is a concrete subclass of error handler
which sends the error messages to the opserr stream.

// Constructor






// Destructor






// Public Methods










Does nothing.




Does nothing.




Creates a va_list using `va_start()` on the ellipses arguments and
invokes the `outputMessage(opserr, msg, va_list)`{.cpp} routine in the parent
class. It then invokes `va_end()` on this va_list and returns.

Creates a va_list using `va_start()` on the ellipses arguments and
invokes the `outputMessage(opserr, msg, va_list)`{.cpp} routine in the parent
class. It then invokes `va_end()` on this va_list, and finally
terminates the program with an `exit()`.

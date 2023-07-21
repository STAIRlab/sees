
# To-do

- `section("Fiber", ...)`

# No Fix

- `defaultUnits`



# APIs Design

## Legacy API (`opensees.openseespy`)

- `OpenSeesPy` class loosly wraps `TclRuntime`. Forwards member access
  to `TclRuntime::eval`

- `opensees.openseespy` module creates an instance of `OpenSeesP`
  as a private global variable.

- when the `opensees.openseespy` module is star-imported
  (i.e, `from opensees.openseespy import *`), the `__all__`
  variable (defined in `openseespy.py`) variable is iterated
  over, and `__getattr__` is called for each symbol name.

- when a symbol is requested from the `opensees.openseespy` module,
  (eg, doing `import opensees.openseespy as ops; ops.model()`)
  the special Python function `__getattr__()` (defined in `openseespy.py`) 
  is called, which dynamically creates a function that wraps the 
  `OpenSeesPy::tcl_call` method of the global `OpenSeesPy` instance.

  > NOTE: the aforementioned functions are only created if the function
  > name is contained in the special Python variable `__all__`, defined
  > in `openseespy.py`.


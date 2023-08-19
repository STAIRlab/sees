# Motivation / Need

Whenever a function is invoked from OpenSeesPy, the resulting *effect* and/or
return value will depend on an arbitrary collection of global variables that
hold the current *state* of the library. This very is wrong. A *library* should
not have a *state* (this is what classes are for). Not only does the library
have a state, but access to and mutation of this state is not controlled in any
kind of an organized or predictable way. There is no simple way for users to
get a full representation of this state. It is not clear how any particular
function invokation will alter this state. Furthermore, the declarations of
variables that comprise this state are randomly sprinkled throughout the
OpenSees code base. OpenSeesPy is a soup of global variables, and there is not
workspace inspector like in Matlab that can begin to help users graple with this.

Not only is this stateful nature at the core of the existing OpenSeesPy
library, but this is actually becoming an (anti) pattern in the OpenSees
codebase.

Some concrete examples of this pattern:

- The input API.
  Example: When someone wants to add a new material, they are told to call
  `OPS_GetInt()` to get the tag for their material. What int? Where is it?
  Where will it come from?
  
  In [REFERENCE], it is said that this API will aid the future incorporation
  of new front-end interpreters. This API does not make this any more probable:

    - Nearly every scripting languages implements a C API that looks like Tcl's for extending
    - There *shouldnt* be any new "OpenSees interpreters". We dont want to produce "interpreters".
      Interpreters are highly complex programs. OpenSees should operate instead on *data structures*.
      The unified API should be through associative arrays (eg JSON).

  Furthermore,

- All the tagged object containers. Whenever someone has a new type they want
  to contribute, the current state of affairs indicates to them that
  they should declare a new static container and store everything there.


Some direct implications of this:

- **We (1) breed bad programmers, and (2) deter good programmers.**
  Any users of the OpenSeesPy library that are new to programming will
  get the impression that this kind of programming is okay. They will 
  think its *okay* for a call to a function like `section('Fiber', 1)`
  to determine what will happen when they call `patch('rect', ...)`.

- **Libraries cannot be reliably constructed around OpenSeesPy.** Say I want to use
  a finite element framework to write a cross-section utility library. I want 
  to write a function
  `get_torsion_constant(section_data, section_mesh=None)`. Users should be able to
  call this function with some section parameters, and get back a scalar torsion constant
  that they can then go on to incorporate into a model that they are analyzing.
  If the user analyzes their model with OpenSees, but I used OpenSees to model the torsion
  constant, the user needs to trust that the state of the OpenSees interpreter  will be 
  *exactly* the same when `get_torsion_constant` returns, as when it was invoked. This
  drastically complicates the job of the library developer, and instills in the end user
  and uneasy feeling towards use of any library that is also using OpenSeesPy.


- Developer community:
  - Accepting any external contributions is extremely error-prone. 
    We cannot expect that contributors completely understand every
    variable that comprises this state.

  - It is very difficult for new contributors to understand the inner-workings
    OpenSees. 



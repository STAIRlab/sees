
# Introduction

In this document we will look at the C++ code that is required to
introduce a new Truss element, fElmt02, into g3. The new class will call
a fortran element subroutine elmt02(), which implements a linear elastic
truss element using the FEAP (http://www.ce.berkeley.edu/rlt/feap)
element interface. To introduce the new class into g3, two new files are
created, `fElmt02.h` and `fElmt02.cpp`, to define the class interface and
implementation. In addition, two existing files are modified,
`TclPlaneTruss.cpp` and `FEM_ObjectBroker.cpp`. The new files are outlined in
the following subsections. The changes to the two existing files are
similar to those outlined in 'How to Introduce a New Element into g3'.
It should be noted that some additional work may be required by the
authors to get other feap element subroutines into g3. This is a
consequence of the information the element routines are obtaining from
the common blocks. The files outlined in this document can be found in
the `SRC/element/feap` directory of the software distribution.

## `fElmt02.h`

The file `fElmt02.h` defines the class interface and details information
about the instance variables associated with the objects of type
`fElmt02`. The interface first declares that the `fElmt02` class inherits
from the fElement class.

```cpp
    class fElmt02 : public fElement {
```

The fElement class is an abstract class which has been provided to hide
most of the details of interfacing FEAP element subroutines with g3. It
is the fElement class which is responsible for invoking the FEAP
subroutine with the appropriate arguments and for managing the data
(property and history data) associated with each element. Each new
subclass of fElement is responsible for providing the fElement class
with information about the element identifier, element end nodes, size
of property data, and size of history data associated with the element.

The fElmt02 interface then defines three constructors and a destructor.
The first two constructors can be used by the analyst to construct the
fElmt05 objects. The arguments passed to these constructors include the
elements id and the id's of the two end nodes. In addition to these, the
first constructor takes the elements cross sectional area, youngs
modulus, and an optional mass density. If no mass density is specified
$0$ is assumed. This information is not passed in the second
constructor. Instead it is obtained by calling the fortran element
subroutine with the isw switch set to $1$. The third constructor is used
in parallel and database programming. The destructor is the method
called when the object is being destroyed. It is called so that memory
associated with the object is returned to the system.

```cpp
      public:
        // constructors
        fElmt02(int tag, int Nd1, int Nd2, double A, double E, double M =0.0);
        fElmt02(int tag, int Nd1, int Nd2, int iow);
        fElmt02();    

        // destructor
        ~fElmt02();      // not actually needed
```

There are no public or protected members defined for this class and no
class or instance variables associated with objects of this class. The
parent class fElement defines the methods and instance variables.

## `fElmt02.cpp`

The `fElmt02.cpp` file contains the implementation. This file contains the
implementation of the three constructors and the destructor defined in
the interface. The first constructor takes as arguments the objects
identifier, the identifiers of the two end nodes, the objects area,
youngs modulus and mass density. The constructor first invokes the
fElement constructor with the objects identifier, a class identifier,
the integer value $2$ indicating that the FEAP subroutine `elmt02()` is to
be invoked, the integer $3$ indicating the number of element properties
associated with the subroutine (i.e. size of d), the integer $2$
indicating two nodes are associated with the element, the integer $2$
indicating the dimension of the mesh, the integer $2$ indicating the
number of degrees-of-freedom per node, and two integers $0$ and $0$
indicating the sizes of $nh1$ and $nh3$ are $0$ for this FEAP element.
The constructor then fills in the property Vector, data, and the ID,
connectedNodes, with the appropriate information. Note that data and
connectedNodes, which are pointers to the Vector and ID objects, are
declared as protected variables in fElement class interface. This
constructor basically does the work typically performed when the FEAP
subroutine is invoked with isw switch set to $1$.

```cpp
fElmt02::fElmt02(int tag, int nd1, int nd2, double E, double A, double rho)
:fElement(tag, ELE_TAG_fElmt02, 2, 3, 2, 0, 0)
{
    // fill  in the property data - feap routine: d(1)=A,d(2)=E,d(3)=rho
    (*data)(0) = A;       
    (*data)(1) = E;
    (*data)(2) = rho;

    // fill in the two end nodes  - feap routine: ix(1)=nd1, ix(2)=nd2
    (*connectedNodes)(0) = nd1; 
    (*connectedNodes)(1) = nd2;   
}
```

The second constructor takes as arguments the objects identifier, the
identifiers of the two end nodes, and an integer indicating an output
file where the element data will be written. The constructor first
invokes the fElement constructor with the objects identifier, a class
identifier, the integer value $2$ indicating that the FEAP subroutine
elmt02() is to be invoked, the integer $3$ indicating the number of
element properties associated with the subroutine (i.e. size of d), the
integer $2$ indicating two nodes are associated with the element, the
integer $2$ indicating the dimension of the mesh, the integer $2$
indicating the number of degrees-of-freedom per node, and the integer
iow. The fElement() constructor will in turn invoke the fortran element
subroutine elmt02(), with the isw switch set to $1$, to read in the
element data and set the sizes of $nh1$ and $nh3$. **Note that to use
this constructor, the feap input routines pinput() and tinput() have to
be overridden**. After the base constructor has been called, the
constructor then fills in the ID, connectedNodes, with the appropriate
node information.

    fElmt02::fElmt02(int tag, int nd1, int nd2, int iow)
    :fElement(tag, ELE_TAG_fElmt02, 2, 3, 2, 2, 2, iow)
    {
        // fill in the two end nodes  - feap routine: ix(1)=nd1, ix(2)=nd2
        (*connectedNodes)(0) = nd1; 
        (*connectedNodes)(1) = nd2;   
    }

The third constructor and the destructor are then provided. The second
constructor, which is used by an FEM_ObjectBroker, simply invokes an
fElement constructor with the classTag. Nothing more is required. The
destructor does nothing (might even remove it?)

    fElmt02::fElmt02()
    :fElement(ELE_TAG_fElmt02)    
    {
        // does nothing
    }

    fElmt02::~fElmt02()
    {
        // does nothing
    }

# Example

The g3 interpreter can now be modified to include this new element. The
modifications to allow the introduction of the new command

      fTruss eleId iNodeID jNodeId A E

into g3 are similar to those outlined in 'How to Introduce a New Element
into g3'. The example g3tcl script for the static analysis of a simple
linear three bar truss example, shown in
figure [\[example1\]](#example1){reference-type="ref"
reference="example1"}, is given below:

<details class="note"><summary>Tcl script</summary>

    #create the ModelBuilder object
    model Tcl2dTruss

    # build the model 

    # add nodes - command: node nodeId xCrd yCrd
    node 1   0.0  0.0
    node 2 144.0  0.0
    node 3 168.0  0.0
    node 4  72.0 96.0

    # add the fElmt02 elements - command: fTruss eleID node1 node2 A E
    fTruss 1 1 4 10.0 3000
    fTruss 2 2 4 5.0 3000
    fTruss 3 3 4 5.0 3000

    # set the boundary conditions - command: fix nodeID xResrnt? yRestrnt?
    fix 1 1 1 
    fix 2 1 1
    fix 3 1 1

    # apply the load - command: load nodeID xForce yForce
    load 4 100 -50

    # build the components for the analysis object
    system BandSPD
    constraints Plain
    integrator LoadControl 1
    algorithm Linear
    numberer RCM

    # create the analysis object 
    analysis Static 1

    # perform the analysis
    analyze

    # print the results at node 4 and at all elements
    print node 4
    print ele
</details>

<details class="note"><summary>Input script for FEAP</summary>

    Feap ** example 1
    4,3,2,2,2,2

    coordinates
    1 0   0.0  0.0
    2 0 144.0  0.0
    3 0 168.0  0.0
    4 0  72.0 96.0

    elements
    1 0 1 1 4
    2 0 2 2 4
    3 0 2 3 4

    boundary restraints
    1 0 1 1
    2 0 1 1
    3 0 1 1

    forces
    4 0 100.0 -50.0

    mate,1
    user,2
    10,3000,0

    mate,2
    user,2
    5,3000,0

    end

    batch
    tang,,1
    disp,,4
    stre,all
    end

    interactive

    stop

</details>

When g3 is run and the commands outlined above are input by the analyst
at the interpreter prompt, or are sourced in from a file, the following
output is generated:


     Node: 4
            Coordinates  : 72 96 
            commitDisps: 0.530093 -0.177894 
            unbalanced Load: 100 -50 

      Element:    1 type: elmt02   iNode:     1 jNode:     4
                    Area: .100E+02 Youngs Modulus: .300E+04 Rho: .000E+00
                    strain:  0.14645E-02     axial force:  0.43935E+02
      Element:    2 type: elmt02   iNode:     2 jNode:     4
                    Area: .500E+01 Youngs Modulus: .300E+04 Rho: .000E+00
                    strain: -0.38364E-02     axial force: -0.57546E+02
      Element:    3 type: elmt02   iNode:     3 jNode:     4
                    Area: .500E+01 Youngs Modulus: .300E+04 Rho: .000E+00
                    strain: -0.36874E-02     axial force: -0.55311E+02


The following can be found at the end of the FEAP output file:


     Feap ** example 1                                                             

      N o d a l   D i s p l a c e m e n t s     Time       0.00000E+00
                                                Prop. Ld.  1.00000E+00

       Node     1 Coord     2 Coord     1 Displ     2 Displ
          4  7.2000E+01  9.6000E+01  5.3009E-01 -1.7789E-01
     *Macro   3 * stre all            v:   0.00       0.00       0.00    
                                                               t=     0.07     0.05
      Element:    1 type: elmt02   iNode:     1 jNode:     4
                    Area: .100E+02 Youngs Modulus: .300E+04 Rho: .000E+00
                    strain:  0.14645E-02     axial force:  0.43935E+02
      Element:    2 type: elmt02   iNode:     2 jNode:     4
                    Area: .500E+01 Youngs Modulus: .300E+04 Rho: .000E+00
                    strain: -0.38364E-02     axial force: -0.57546E+02
      Element:    3 type: elmt02   iNode:     3 jNode:     4
                    Area: .500E+01 Youngs Modulus: .300E+04 Rho: .000E+00
                    strain: -0.36874E-02     axial force: -0.55311E+02


---------------------------------

<b><center>
How to Introduce a FEAP Element into g3

Version 0.1 - Preliminary Draft

December 20, 1999

Frank McKenna and Gregory L. Fenves

PEER, University of California at Berkeley
</center></b>


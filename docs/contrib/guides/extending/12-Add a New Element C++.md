# Add a New Element C++

<p>To add a new Element module using the C++ language, the developer
must:</p>
<ol>
<li>provide a new C++ subclass of the Element class</li>
<li>provide an interface function that will be used to parse the input
and create the new element.</li>
</ol>
<p>Unlike the C and Fortran modules, no information about the state of
the model is passed as arguments to the element methods. It is the
responsibility of the element to obtain this information using it's
assocaiations.</p>
<p>NOTE: This document assumes the reader is familiar with the C++
programming language.</p>
<h3 id="element_class">Element Class</h3>
<p>The Element class itself is an abstract base class. It inherits from
both the DomainComponent class, which is itself a subclass of
TaggedObject class and the MovableObject class. The class has a large
number of methods defined in the interface, not all these methods need
to be included in a new Element class. The following is the minimal
interface that should be considered:</p>
<p>The Element Class:</p>
<p>
```cpp
 class Element : public DomainComponent {
public: Element(int tag, int classTag); virtual ~Element();</p>
<p>// initialization virtual int setDomain(Domain *theDomain);</p>
<p>// methods dealing with nodes and number of external dof virtual int
getNumExternalNodes(void) const =0; virtual const ID
&amp;getExternalNodes(void) =0; virtual Node **getNodePtrs(void) =0;
virtual int getNumDOF(void) =0;</p>
<p>// methods dealing with committed state and update virtual int
commitState(void); // called when a converged solution has been obtained
for a time step virtual int revertToLastCommit(void) = 0; // called when
the soln algorithm has failed to converge to a solution at a time step
virtual int revertToStart(void); // called when model is rest to initial
conditions virtual int update(void); // called when a new trial step has
been set at the nodes</p>
<p>// methods dealing with element stiffness virtual const Matrix
&amp;getTangentStiff(void) =0; virtual const Matrix
&amp;getInitialStiff(void) =0;</p>
<p>// methods dealing with element forces virtual void zeroLoad(void);
virtual int addLoad(ElementalLoad *theLoad, double loadFactor); virtual
const Vector &amp;getResistingForce(void) =0;</p>
<p>// public methods for output void Print(OPS_Stream &amp;s, int flag
=0); virtual Response *setResponse(const char **argv, int argc,
OPS_Stream &amp;theHandler); virtual int getResponse(int responseID,
Information &amp;eleInformation);</p>
<p>// method for database/parallel processing int sendSelf(int
commitTag, Channel &amp;theChannel); int recvSelf(int commitTag, Channel
&amp;theChannel, FEM_ObjectBroker &amp;theBroker);</p>
<p>}</p>
<p>
```
</p>
<h3 id="example___truss2d">Example - Truss2D</h3>
<p>In the following section we will provide all necessary code to add a
new 2d planar truss element into an OpenSees interpreter. To demonstrate
the power of object-oriented programming, the stress-strain relationship
will be provided by a UniaxialMaterial object.</p>
<h4 id="header">Header</h4>
<p>The header for thew new class, which we will call Truss2D is as
follows:</p>
<p>
```cpp
 // include directives</p>
<ol>
<li>include &lt;Element.h&gt;</li>
<li>include &lt;Matrix.h&gt;</li>
<li>include &lt;Vector.h&gt;</li>
</ol>
<p>// forward declarations class UniaxialMaterial;</p>
<p>class Truss2D : public Element { public: // constructors Truss2D(int
tag, int Nd1, int Nd2, UniaxialMaterial &amp;theMaterial, double A);</p>
<p>Truss2D();</p>
<p>// destructor ~Truss2D();</p>
<p>// initialization int setDomain(Domain *theDomain);</p>
<p>// public methods to obtain inforrmation about dof &amp; connectivity
int getNumExternalNodes(void) const; const ID
&amp;getExternalNodes(void); Node **getNodePtrs(void); int
getNumDOF(void);</p>
<p>// public methods to set the state of the element int
commitState(void); int revertToLastCommit(void); int
revertToStart(void); int update(void);</p>
<p>// public methods to obtain stiffness const Matrix
&amp;getTangentStiff(void); const Matrix &amp;getInitialStiff(void);</p>
<p>// public method to obtain resisting force const Vector
&amp;getResistingForce(void);</p>
<p>// method for obtaining information specific to an element void
Print(OPS_Stream &amp;s, int flag =0); Response *setResponse(const char
**argv, int argc, OPS_Stream &amp;s); int getResponse(int responseID,
Information &amp;eleInformation);</p>
<p>// public methods for database/parallel processing int sendSelf(int
commitTag, Channel &amp;theChannel); int recvSelf(int commitTag, Channel
&amp;theChannel, FEM_ObjectBroker &amp;theBroker); void Print(OPS_Stream
&amp;s, int flag =0);</p>
<p>protected:</p>
<p>private: // private member functions - only available to objects of
the class double computeCurrentStrain(void) const;</p>
<p>// private attributes - a copy for each object of the class
UniaxialMaterial *theMaterial; // pointer to a material ID
externalNodes; // contains the id's of end nodes Matrix trans; // hold
the transformation matrix double L; // length of truss (undeformed
configuration) double A; // area of truss Node *theNodes[2]; // node
pointers</p>
<p>// static data - single copy for all objects of the class static
Matrix trussK; // class wide matrix for returning stiffness static
Vector trussR; // class wide vector for returning residual };</p>
<ol>
<li>endif</li>
</ol>
<p>
```
</p>
<p>The header file defines the interface and variables for the class
Truss2D. It defines the new class to be a sublass of the Element class.
In the public interface, are two constructors and a destructor in
addition to minimal set of methods we showed for the Element class.
There are no protected data or methods as we do not expect this class to
be subclassed. In the private section, we define one private method,
computeCurrentStrain(), and we define a number of private variables and
a number of static variables.</p>
<p>The header has a number of #include directives, one is needed for the
base class and every class used as a variable in the list of data
(except those that are used as pointers). For those classes that only
appear as pointers in the header file (Node, UniaxialMaterial) a forward
declaration is all that is needed (the include could also have been
used, but using the forward declaration simplifies dependencies and
reduces the amount of code that ha to be recompiled later if changes are
made).</p>
<h4 id="implementation">Implementation</h4>
<p>It another file, Truss2D.cpp, we place the code that details what the
constructors, destructor and methods do. In addition we provide one
additional procedure OPS_Truss2D() (NOTE it has the same name as the
class with an OPS_ prefix). We will go through each part of the
file.</p>
<h5 id="include_directives">Include Directives</h5>
<p>The first part of the file contains the list of includes. It is
necessary to have an #include directive for each class and api file that
is used within the .cpp file and is not included in the header.</p>
<p>
```cpp
</p>
<ol>
<li>include "Truss2D.h"</li>
</ol>
<ol>
<li>include &lt;elementAPI.h&gt;</li>
<li>include &lt;G3Globals.h&gt;</li>
<li>include &lt;Information.h&gt;</li>
<li>include &lt;Domain.h&gt;</li>
<li>include &lt;Node.h&gt;</li>
<li>include &lt;Channel.h&gt;</li>
<li>include &lt;Message.h&gt;</li>
<li>include &lt;FEM_ObjectBroker.h&gt;</li>
<li>include &lt;UniaxialMaterial.h&gt;</li>
<li>include &lt;Renderer.h&gt;</li>
<li>include &lt;ElementResponse.h&gt;</li>
</ol>
<ol>
<li>include &lt;math.h&gt;</li>
<li>include &lt;stdlib.h&gt;</li>
<li>include &lt;string.h&gt;</li>
</ol>
<p>
```
</p>
<h5 id="static_variables">Static Variables</h5>
<p>Next, we initialize the static variables. For this example we are
using 2 static-variables (objects shared by each Truss2D object that is
created), one to return the tangent matrix and the other to return the
resisting force.</p>
<p>
```cpp
 // initialise the class wide variables
Matrix Truss2D::trussK(4,4); Vector Truss2D::trussR(4);

```
</p>
<h5 id="constructors">Constructors</h5>
<p>After the list of includes, we provide the 2 constructors. The
constructors are rather simple. They just initialize all the data
variables defined in the header. Note it is very important to set all
pointer values to 0.</p>
<p>The first constructor is the one most typically used. The arguments
provide the elements tag, the tags of the two end nodes, the element's
area and a copy of the element's material. The code in the constructor
does the following:</p>
<ol>
<li>The elements tag and a 0 are passed to the Element constructor.</li>
<li>The matreial pointer, theMaterial, is set to a copy of the material
obtained from the material that is passed in the arguments.</li>
<li>The externalNodes array is set to be an array of size 2 and it's
values are set to the nodal tags of the 2 nodes.</li>
<li>The theNodes array components are set to be 0.</li>
</ol>
<p>It should be noted that the static variables dealing with length,
transformations, and nodes are set to 0 in the constructors. They will
be filled in when the setDomain() method is invoked on the object.</p>
<p>
```cpp
 Truss2D::Truss2D(int tag, int Nd1, int Nd2,
UniaxialMaterial &amp;theMat, double a)</p>
<dl>
<dt></dt>
<dd>
Element(tag, 0),
</dd>
</dl>
<p>externalNodes(2), trans(1,4), L(0.0), A(a) { // get a copy of the
material object for our own use theMaterial = theMat.getCopy(); if
(theMaterial == 0) { opserr &lt;&lt; "FATAL TrussCPP::TrussCPP() - out
of memory, could not get a copy of the Material\n"; exit(-1); }</p>
<p>// fill in the ID containing external node info with node id's if
(externalNodes.Size() != 2) { opserr &lt;&lt; "FATAL
TrussCPP::TrussCPP() - out of memory, could not create an ID of size
2\n"; exit(-1); }</p>
<p>externalNodes(0) = Nd1; externalNodes(1) = Nd2;</p>
<p>theNodes[0] = 0; theNodes[1] = 0; } 
```
</p>
<p>The second constructor is called when paralell processing or the
database feature of the OpenSees application is used. It's pupose is to
create a blank Truss2D object, that will be filled in when the
recvSelf() method is invoked on the object.</p>
<p>
```cpp
 Truss2D::Truss2D()</p>
<dl>
<dt></dt>
<dd>
Element(0, 0),
</dd>
</dl>
<p>theMaterial(0), externalNodes(2), trans(1,4), L(0.0), A(0.0) {
theNodes[0] = 0; theNodes[1] = 0; } 
```
</p>
<h5 id="destructor">Destructor</h5>
<p>The we provide the destructor. In the destructor all memory that the
Truss2D created or was passed to it in the constructor must be
destroyed. For our example, we need to invoke the destructor on the copy
of the material object.</p>
<p>
```cpp
 Truss2D::~Truss2D() { if (theMaterial != 0)
delete theMaterial; } 
```
</p>
<p>===== setDomain() Initialization Method</p>
<p>The setDomain() method is invoked when the truss element is being
added to the Domain. It is in this method that most of the private
variables of the object are determined. The method returns 0 if
successfull, a negative number if not. In the method we obtain pointers
to the end nodes, nodal coordinates are obtained and the elements length
and transformation matrix is set once the coordinates have been
obtained.</p>
<p>
```cpp
 void Truss2D::setDomain(Domain *theDomain)
{ // check Domain is not null - invoked when object removed from a
domain if (theDomain == 0) { return; }</p>
<p>// first ensure nodes exist in Domain and set the node pointers Node
*end1Ptr, *end2Ptr; int Nd1 = externalNodes(0); int Nd2 =
externalNodes(1); end1Ptr = theDomain-&gt;getNode(Nd1); end2Ptr =
theDomain-&gt;getNode(Nd2); if (end1Ptr == 0) { opserr &lt;&lt; "WARNING
Truss2D::setDomain() - at truss " &lt;&lt; this-&gt;getTag() &lt;&lt; "
node " &lt;&lt; Nd1 &lt;&lt; " does not exist in domain\n"; return; //
don't go any further - otherwise segemntation fault } if (end2Ptr == 0)
{ opserr &lt;&lt; "WARNING Truss2D::setDomain() - at truss " &lt;&lt;
this-&gt;getTag() &lt;&lt; " node " &lt;&lt; Nd2 &lt;&lt; " does not
exist in domain\n"; return; // don't go any further - otherwise
segemntation fault } theNodes[0] = end1Ptr; theNodes[1] = end2Ptr; //
call the DomainComponent class method THIS IS VERY IMPORTANT
this-&gt;DomainComponent::setDomain(theDomain);</p>
<p>// ensure connected nodes have correct number of dof's int dofNd1 =
end1Ptr-&gt;getNumberDOF(); int dofNd2 = end2Ptr-&gt;getNumberDOF(); if
((dofNd1 != 2) || (dofNd2 != 2)) { opserr &lt;&lt;
"Truss2D::setDomain(): 2 dof required at nodes\n"; return; }</p>
<p>// now determine the length &amp; transformation matrix const Vector
&amp;end1Crd = end1Ptr-&gt;getCrds(); const Vector &amp;end2Crd =
end2Ptr-&gt;getCrds();</p>
<p>double dx = end2Crd(0)-end1Crd(0); double dy =
end2Crd(1)-end1Crd(1);</p>
<p>L = sqrt(dx*dx + dy*dy);</p>
<p>if (L == 0.0) { opserr &lt;&lt; "WARNING Truss2D::setDomain() -
Truss2D " &lt;&lt; this-&gt;getTag() &lt;&lt; " has zero length\n";
return; // don't go any further - otherwise divide by 0 error }</p>
<p>double cs = dx/L; double sn = dy/L;</p>
<p>trans(0,0) = -cs; trans(0,1) = -sn; trans(0,2) = cs; trans(0,3) = sn;
} 
```
</p>
<h5 id="methods_dealing_with_nodes">Methods Dealing With Nodes</h5>
<p>Next comes 4 rather simple methods that return basic information
about the elements nodes. These are one line methods that should not
need any explanation! 
```cpp
 int
Truss2D::getNumExternalNodes(void) const { return 2; }</p>
<p>const ID &amp; Truss2D::getExternalNodes(void) { return
externalNodes; }</p>
<p>Node ** Truss2D::getNodePtrs(void) { return theNodes; }</p>
<p>int Truss2D::getNumDOF(void) { return 4; } 
```
</p>
<h5 id="methods_dealing_with_current_state">Methods Dealing With Current
State</h5>
<p>
```cpp
 int Truss2D::commitState() { return
theMaterial-&gt;commitState(); }</p>
<p>int Truss2D::revertToLastCommit() { return
theMaterial-&gt;revertToLastCommit(); }</p>
<p>int Truss2D::revertToStart() { return
theMaterial-&gt;revertToStart(); }</p>
<p>int Truss2D::update() { // determine the current strain given trial
displacements at nodes double strain =
this-&gt;computeCurrentStrain();</p>
<p>// set the strain in the materials
theMaterial-&gt;setTrialStrain(strain);</p>
<p>return 0; } 
```
</p>
<h5 id="methods_to_return_tangent_matrix">Methods To Return Tangent
Matrix</h5>
<p>In both methods, we obtain the appropriate tangent from the material
and use this to return the transformed matrix.</p>
<p>
```cpp
 const Matrix &amp;
Truss2D::getTangentStiff(void) { if (L == 0.0) { // length = zero -
problem in setDomain() warning message already printed trussK.Zero();
return trussK; }</p>
<p>// get the current E from the material for the last updated strain
double E = theMaterial-&gt;getTangent();</p>
<p>// form the tangent stiffness matrix trussK = trans^trans; trussK *=
A*E/L;</p>
<p>// return the matrix return trussK; }</p>
<p>const Matrix &amp; Truss2D::getInitialStiff(void) { if (L == 0.0) {
// length = zero - problem in setDomain() warning message already
printed trussK.Zero(); return trussK; }</p>
<p>// get the current E from the material for the last updated strain
double E = theMaterial-&gt;getInitialTangent();</p>
<p>// form the tangent stiffness matrix trussK = trans^trans; trussK *=
A*E/L;</p>
<p>// return the matrix return trussK; } 
```
</p>
<h5 id="methods_to_return_resisting_force">Methods To Return Resisting
Force</h5>
<p>In this method we obtain the stress from the material and use this to
return the transformed force vector.</p>
<p>
```cpp
 const Vector &amp;
Truss2D::getResistingForce() { if (L == 0.0) { // if length == 0,
problem in setDomain() trussR.Zero(); return trussR; }</p>
<p>// want: R = Ku - Pext</p>
<p>// force = F * transformation double force =
A*theMaterial-&gt;getStress(); for (int i=0; i&lt;4; i++) trussR(i) =
trans(0,i)*force;</p>
<p>return trussR; } 
```
</p>
<h5 id="methods_dealing_with_output">Methods Dealing With Output</h5>
<p>Information is obtained by the user when the print command is invoked
by the user and also when the user issues the recorder command. When the
print command is invoked the Print method is invoked. This method simply
prints information about the element, and then asks the material to do
likewise.</p>
<p>
```cpp
 void Truss2D::Print(OPS_Stream &amp;s, int
flag) { s &lt;&lt; "Element: " &lt;&lt; this-&gt;getTag(); s &lt;&lt; "
type: Truss2D iNode: " &lt;&lt; externalNodes(0); s &lt;&lt; " jNode: "
&lt;&lt; externalNodes(1); s &lt;&lt; " Area: " &lt;&lt; A; s &lt;&lt; "
\t Material: " &lt;&lt; *theMaterial; } 
```
</p>
<p>There are two methods used by the element recorders.</p>
<ol>
<li>The first method, setResponse(), is called when the recorder is
created. The element informs the recorder that it can respond to a
request of that type, if it cannot respond to the request it returns a
0, otherwise it returns an Response object. The response object includes
a pointer to the element, an integer flag used to id the response when
the getResponse() method is called, and a Vector detailing the size of
the response.</li>
<li>The second method, getReponse(), is called by the recorder when it
is actually recording the information.</li>
</ol>
<p>
```cpp
 Response * Truss2D::setResponse(const char
**argv, int argc, OPS_Stream &amp;output) { Response *theResponse =
0;</p>
<p>output.tag("ElementOutput");
output.attr("eleType",this-&gt;getClassType());
output.attr("eleTag",this-&gt;getTag()); int numNodes =
this-&gt;getNumExternalNodes(); const ID &amp;nodes =
this-&gt;getExternalNodes(); static char nodeData[32];</p>
<p>for (int i=0; i&lt;numNodes; i++) { sprintf(nodeData,"node%d",i+1);
output.attr(nodeData,nodes(i)); }</p>
<p>if (strcmp(argv[0],"force") == 0 || strcmp(argv[0],"forces") == 0 ||
strcmp(argv[0],"globalForce") == 0 || strcmp(argv[0],"globalForces") ==
0) { const Vector &amp;force = this-&gt;getResistingForce(); int size =
force.Size(); for (int i=0; i&lt;size; i++) {
sprintf(nodeData,"P%d",i+1); output.tag("ResponseType",nodeData); }
theResponse = new ElementResponse(this, 1,
this-&gt;getResistingForce()); }</p>
<p>else if (strcmp(argv[0],"dampingForce") == 0 ||
strcmp(argv[0],"dampingForces") == 0) { const Vector &amp;force =
this-&gt;getResistingForce(); int size = force.Size(); for (int i=0;
i&lt;size; i++) { sprintf(nodeData,"P%d",i+1);
output.tag("ResponseType",nodeData); } theResponse = new
ElementResponse(this, 2, this-&gt;getResistingForce()); } else if
(strcmp(argv[0],"axialForce") ==0) return new ElementResponse(this, 3,
0.0);</p>
<p>output.endTag(); return theResponse; }</p>
<p>int Truss2D::getResponse(int responseID, Information &amp;eleInfo) {
double strain;</p>
<p>switch (responseID) { case -1: return -1; case 1: // global forces
return eleInfo.setVector(this-&gt;getResistingForce()); case 2: return
eleInfo.setVector(this-&gt;getRayleighDampingForces()); case 3:
theMaterial-&gt;setTrialStrain(strain); return eleInfo.setDouble(A *
theMaterial-&gt;getStress()); default: return 0; } } 
```
</p>
<h5 id="methods_dealing_with_databasesparallel_processing">Methods
Dealing With Databases/Parallel Processing</h5>
<p>There are two methods provided which are required is the user uses to
use the database or parallel procesing features of the OpenSees
applications. If neither are to be used, the developer need simply
return a negative value in both methods. The idea is that the element
must pack up it's information using Vector and ID objects and send it
off to a Channel object. On the flip side, the receiving blank element
must receive the same Vector and ID data, unpack it and set the
variables.</p>
<p>
```cpp
 int Truss2D::sendSelf(int commitTag,
Channel &amp;theChannel) { int res;</p>
<p>// note: we don't check for dataTag == 0 for Element // objects as
that is taken care of in a commit by the Domain // object - don't want
to have to do the check if sending data int dataTag =
this-&gt;getDbTag();</p>
<p>// Truss2D packs it's data into a Vector and sends this to theChannel
// along with it's dbTag and the commitTag passed in the arguments</p>
<p>Vector data(5); data(0) = this-&gt;getTag(); data(1) = A; data(2) =
theMaterial-&gt;getClassTag(); int matDbTag =
theMaterial-&gt;getDbTag(); // NOTE: we do have to ensure that the
material has a database // tag if we are sending to a database channel.
if (matDbTag == 0) { matDbTag = theChannel.getDbTag(); if (matDbTag !=
0) theMaterial-&gt;setDbTag(matDbTag); } data(3) = matDbTag;</p>
<p>res = theChannel.sendVector(dataTag, commitTag, data); if (res &lt;
0) { opserr &lt;&lt; "WARNING Truss2D::sendSelf() - failed to send
Vector\n"; return -1; }</p>
<p>// Truss2D then sends the tags of it's two end nodes res =
theChannel.sendID(dataTag, commitTag, externalNodes); if (res &lt; 0) {
opserr &lt;&lt; "WARNING Truss2D::sendSelf() - failed to send ID\n";
return -2; }</p>
<p>// finally Truss2D asks it's material object to send itself res =
theMaterial-&gt;sendSelf(commitTag, theChannel); if (res &lt; 0) {
opserr &lt;&lt; "WARNING Truss2D::sendSelf() - failed to send the
Material\n"; return -3; }</p>
<p>return 0; }</p>
<p>int Truss2D::recvSelf(int commitTag, Channel &amp;theChannel,
FEM_ObjectBroker &amp;theBroker) { int res; int dataTag =
this-&gt;getDbTag();</p>
<p>// Truss2D creates a Vector, receives the Vector and then sets the //
internal data with the data in the Vector</p>
<p>Vector data(5); res = theChannel.recvVector(dataTag, commitTag,
data); if (res &lt; 0) { opserr &lt;&lt; "WARNING Truss2D::recvSelf() -
failed to receive Vector\n"; return -1; }</p>
<p>this-&gt;setTag((int)data(0)); A = data(1); // Truss2D now receives
the tags of it's two external nodes res = theChannel.recvID(dataTag,
commitTag, externalNodes); if (res &lt; 0) { opserr &lt;&lt; "WARNING
Truss2D::recvSelf() - failed to receive ID\n"; return -2; }</p>
<p>// we create a material object of the correct type, // sets its
database tag and asks this new object to recveive itself. int matClass =
data(2); int matDb = data(3);</p>
<p>theMaterial = theBroker.getNewUniaxialMaterial(matClass); if
(theMaterial == 0) { opserr &lt;&lt; "WARNING Truss2D::recvSelf() -
failed to create a Material\n"; return -3; }</p>
<p>// we set the dbTag before we receive the material - this is
important theMaterial-&gt;setDbTag(matDb); res =
theMaterial-&gt;recvSelf(commitTag, theChannel, theBroker); if (res &lt;
0) { opserr &lt;&lt; "WARNING Truss2D::recvSelf() - failed to receive
the Material\n"; return -3; }</p>
<p>return 0; }</p>

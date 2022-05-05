# Add a New UniaxialMaterial C++

<p>To add a new Uniaxial Material module using the C++ language, the
developer must:</p>
<ol>
<li>provide a new C++ subclass of the UniaxialMaterial class</li>
<li>provide an interface function that will be used to parse the input
and create the new material.</li>
</ol>
<p>Unlike the C and Fortran modules, no information about the state of
the model is passed as arguments to the material methods. It is the
responsibility of the material to okeep whatever information it needs.
This information will include both parameters (information needed to
define the material) and state variables or history variables
(information needed by the material to remember it's current state for
the computation of the stress and tangent)</p>
<p>NOTE: This document assumes the reader is familiar with the C++
programming language.</p>
<h3 id="uniaxialmaterial_class">UniaxialMaterial Class</h3>
<p>The Uniaxial class itself is an abstract base class. It inherits from
both the Material class, which is itself a subclass of TaggedObject
class and the MovableObject class. The class has a large number of
methods defined in the interface, not all these methods need to be
included in a new UniaxialMaterial class. The following is the minimal
interface that should be considered:</p>
<p>The UniaxialMaterial Class:</p>
<p>&lt;source lang="cpp"&gt;</p>
<ol>
<li>ifndef ElasticPPcpp_h</li>
<li>define ElasticPPcpp_h</li>
</ol>
<p>// Written: fmk // // Description: This file contains the class
definition for // ElasticPPcpp. ElasticPPcpp provides the abstraction //
of an elastic perfectly plastic uniaxial material, // // What: "@(#)
ElasticPPcpp.h, revA"</p>
<ol>
<li>include &lt;UniaxialMaterial.h&gt;</li>
</ol>
<p>class UniaxialMaterial : public Material { public: UniaxialMaterial
(int tag, int classTag); virtual ~UniaxialMaterial();</p>
<p>virtual int setTrialStrain (double strain, double strainRate =0)
=0;</p>
<p>virtual double getStrain (void) = 0; virtual double getStrainRate
(void); virtual double getStress (void) = 0; virtual double getTangent
(void) = 0; virtual double getInitialTangent (void) = 0;</p>
<p>virtual int commitState (void) = 0; virtual int revertToLastCommit
(void) = 0; virtual int revertToStart (void) = 0;</p>
<p>virtual UniaxialMaterial *getCopy (void) = 0;</p>
<p>virtual Response *setResponse (const char **argv, int argc,
OPS_Stream &amp;theOutputStream); virtual int getResponse (int
responseID, Information &amp;matInformation);</p>
<p>virtual int sendSelf(int commitTag, Channel &amp;theChannel); virtual
int recvSelf(int commitTag, Channel &amp;theChannel, FEM_ObjectBroker
&amp;theBroker);</p>
<p>virtual void Print(OPS_Stream &amp;s, int flag =0);</p>
<p>protected:</p>
<p>private: } &lt;/source&gt;</p>
<p>The methods with =0; are methods that you must implement for the
class to link successfully with OpenSees. The other classes are
optional.</p>
<p>The setTriaStrain() is the method called by an element when a new
strain in the material is to be set. Subsequent calls to getTangent()
and getStress() are to return thecorresponding tangent and stress values
for that stress. setTrialStrain() is invoked as the solution algorithm
tries a number of trial solution steps as it goes from one commited
solution to the next on the solution path.</p>
<p>The commitState() method is invoked when a trial solution has been
determined to be on the solution path. It is the responsibility of the
material to be able to back track to that solution if a
revertToLastCOmmit() is invoked. This will happen if the algorithm fails
to find a solution on the solution path.</p>
<p>The getCopy() method is invoked by an element in the elements
constructor. The material is to return a unique copy of itself to the
element. This way different elements can use the same material type with
the same properties, with each element having it's own unique copy.</p>
<p>The setResponse()/getResponse() typically do not have to be provided.
These are the methods called by a recorder after a commit(). If you are
appy with the existing responses fro a UniaxialMaterial which responds
to "stress", "strain", "tangent", "stressANDstrain" you do not have to
implement these methods. The example below shows them just for those ew
who want additional info out of their materials.</p>
<p>The sendSelf()/recvSelf() methods are used in parallel processing
with OpenSeesSP and when using the database command. If you don't
envision using the material in these situations you can again ignore
these methods. Again I am only showing them in the code for those even
fewer who would do this.</p>
<p>The commit() method is what is called</p>
<h3 id="example___elasticppecpp">Example - ElasticPPecpp</h3>
<p>In the following section we will provide all necessary code to add a
new elastic perfectly plastic material into an OpenSees interpreter.</p>
<h4 id="header">Header</h4>
<p>The header for thew new class, which we will call Truss2D is as
follows:</p>
<p>&lt;source lang="cpp"&gt;</p>
<ol>
<li>ifndef ElasticPPcpp_h</li>
<li>define ElasticPPcpp_h</li>
</ol>
<ol>
<li>include &lt;UniaxialMaterial.h&gt;</li>
</ol>
<p>class ElasticPPcpp : public UniaxialMaterial { public:
ElasticPPcpp(int tag, double E, double eyp); ElasticPPcpp();</p>
<p>~ElasticPPcpp();</p>
<p>int setTrialStrain(double strain, double strainRate = 0.0); double
getStrain(void); double getStress(void); double getTangent(void);</p>
<p>double getInitialTangent(void) {return E;};</p>
<p>int commitState(void); int revertToLastCommit(void); int
revertToStart(void);</p>
<p>UniaxialMaterial *getCopy(void);</p>
<p>int sendSelf(int commitTag, Channel &amp;theChannel); int
recvSelf(int commitTag, Channel &amp;theChannel, FEM_ObjectBroker
&amp;theBroker);</p>
<p>void Print(OPS_Stream &amp;s, int flag =0);</p>
<p>protected:</p>
<p>private: double fyp, fyn; // positive and negative yield stress
double ezero; // initial strain double E; // elastic modulus double ep;
// plastic strain at last commit</p>
<p>double trialStrain; // trial strain double trialStress; // current
trial stress double trialTangent; // current trial tangent double
commitStrain; // last commited strain double commitStress; // last
commited stress double commitTangent; // last committed tangent
&lt;/source&gt;</p>
<p>The header file defines the interface and variables for the class
ElasticPPcpp. It defines the new class to be a sublass of the
UniaxialMaterial class. In the public interface, are two constructors
and a destructor in addition to minimal set of methods we showed for the
UniaxialMaterial class. There are no protected data or methods as we do
not expect this class to be subclassed. In the private section we define
a number of private variables and a number of variables. Some of these
are parameter variable which do not change with each commit, e.g. E, and
some state variable which do change, e.g. ep, fyp, and fyn.</p>
<h4 id="implementation">Implementation</h4>
<p>It another file, ElasticPPcpp.cpp, we place the code that details
what the constructors, destructor and methods do. In addition we provide
one additional procedure OPS_ElasticPPcpp() (NOTE it has the same name
as the class with an OPS_ prefix). We will go through each part of the
file.</p>
<h5 id="include_directives">Include Directives</h5>
<p>The first part of the file contains the list of includes. It is
necessary to have an #include directive for each class and api file that
is used within the .cpp file and is not included in the header.</p>
<p>&lt;source lang="cpp"&gt;</p>
<ol>
<li>include "ElasticPPcpp.h"</li>
</ol>
<ol>
<li>include &lt;elementAPI.h&gt;</li>
<li>include &lt;Vector.h&gt;</li>
<li>include &lt;Channel.h&gt;</li>
<li>include &lt;math.h&gt;</li>
<li>include &lt;float.h&gt;</li>
</ol>
<p>&lt;/source&gt;</p>
<h5 id="static_variables">Static Variables</h5>
<p>Next, we initialize the static variables. For this example we are
using 1 static-variables to keep track of the number of times the
external procedure to parse and create such an object is called.</p>
<p>&lt;source lang="cpp"&gt; static int numElasticPPcpp = 0;
&lt;/source&gt;</p>
<h5 id="constructors">Constructors</h5>
<p>After the list of includes, we provide the 2 constructors. The
constructors are rather simple. They just initialize all the data
variables defined in the header. Note it is very important to set all
pointer values to 0 if you use pointers in your class. We will use none
here.</p>
<p>The first constructor is the one most typically used. The arguments
provide the materials tag, youngs modulus and initial yield point strain
values. material. The code in the constructor simply computes the
positive and negative yield stress based on the input provided.</p>
<p>&lt;source lang="cpp"&gt; ElasticPPcpp::ElasticPPcpp(int tag, double
e, double eyp)</p>
<dl>
<dt></dt>
<dd>
UniaxialMaterial(tag, 0),
</dd>
</dl>
<p>ezero(0.0), E(e), ep(0.0), trialStrain(0.0), trialStress(0.0),
trialTangent(E), commitStrain(0.0), commitStress(0.0), commitTangent(E)
{ fyp = E*eyp; fyn = -fyp; } &lt;/source&gt;</p>
<p>The second constructor is called when paralell processing or the
database feature of the OpenSees application is used. It's purpose is to
create a blank TElasticPPcpp object, that will be filled in when the
recvSelf() method is invoked on the object.</p>
<p>&lt;source lang="cpp"&gt; ElasticPPcpp::ElasticPPcpp()</p>
<dl>
<dt></dt>
<dd>
UniaxialMaterial(0, 0),
</dd>
</dl>
<p>fyp(0.0), fyn(0.0), ezero(0.0), E(0.0), ep(0.0), trialStrain(0.0),
trialStress(0.0), trialTangent(E), commitStrain(0.0), commitStress(0.0),
commitTangent(E) {</p>
<p>}</p>
<p>&lt;/source&gt;</p>
<h5 id="destructor">Destructor</h5>
<p>The we provide the destructor. In the destructor all memory that the
the object created or was passed to it in the constructor must be
destroyed. For this example we have no such memory. We could have left
the destructor out entirely. Hoowever, it is good practice to leave it
in your source code.</p>
<p>&lt;source lang="cpp"&gt; ElasticPPcpp::~ElasticPPcpp() { // does
nothing } &lt;/source&gt;</p>
<h5 id="getcopy_method">getCopy() Method</h5>
<p>This is the method called by each element or section to get unique
copies of a material.</p>
<p>&lt;source lang="cpp"&gt; UniaxialMaterial *
ElasticPPcpp::getCopy(void) { ElasticPPcpp *theCopy = new
ElasticPPcpp(this-&gt;getTag(),E,fyp/E); theCopy-&gt;ep =
this-&gt;ep;</p>
<p>return theCopy; } &lt;/source&gt;</p>
<h5 id="settrialstrain_method">setTrialStrain() Method</h5>
<p>This, as mentioned, is the method called when the element has
computed a nw strain for the element. The element will make subsequent
calls to getStress() and getTangent() to obtain new values of these for
the new strain. This is typically the most complicated method to write
and to determine the theory for before you even write the code. ALl
subsequent methods are trivial.</p>
<p>&lt;source lang="cpp"&gt; int ElasticPPcpp::setTrialStrain(double
strain, double strainRate) { if (fabs(trialStrain - strain) &lt;
DBL_EPSILON) return 0;</p>
<p>trialStrain = strain;</p>
<p>double sigtrial; // trial stress double f; // yield function</p>
<p>// compute trial stress sigtrial = E * ( trialStrain - ezero - ep
);</p>
<p>//sigtrial = E * trialStrain; //sigtrial -= E * ezero; //sigtrial -=
E * ep;</p>
<p>// evaluate yield function if ( sigtrial &gt;= 0.0 ) f = sigtrial -
fyp; else f = -sigtrial + fyn;</p>
<p>double fYieldSurface = - E * DBL_EPSILON; if ( f &lt;= fYieldSurface
) {</p>
<p>// elastic trialStress = sigtrial; trialTangent = E;</p>
<p>} else {</p>
<p>// plastic if ( sigtrial &gt; 0.0 ) { trialStress = fyp; } else {
trialStress = fyn; }</p>
<p>trialTangent = 0.0; }</p>
<p>return 0; }</p>
<p>&lt;/source&gt;</p>
<h5 id="trivial_methods">Trivial Methods</h5>
<p>Next comes 3 rather simple methods that return basic information
computed in the setTrialStrain(). You do of course have the option to
ignore the setTrialStrain() method and compute the stress and tangent
quantities again in the interests of saving memory. &lt;source
lang="cpp"&gt; double ElasticPPcpp::getStrain(void) { return
trialStrain; }</p>
<p>double ElasticPPcpp::getStress(void) { return trialStress; }</p>
<p>double ElasticPPcpp::getTangent(void) { return trialTangent; }</p>
<p>&lt;/source&gt;</p>
<h5 id="methods_dealing_with_current_state">Methods Dealing With Current
State</h5>
<p>As mentioned, when the algorithm finds a solution state as it goes
from one converged solution to the next. As it attempts to find these
solutions it goes through a number of trial steps (each setTrialStrain()
is invoked in each of these steps). Once it finds a trial step that is
on the solution path it will stop and invoke commitState() on the
material. Any state variables that the material uses needs to be updated
at this time. Should the algorithm fail to find a solution it may return
to the last converged step or indeed the start. You the developer must
provide code so that your mateial can indeed go back to these states and
report correct getTangent() and getStress() values for subsequent
analysis atte,pts.</p>
<p>&lt;source lang="cpp"&gt; int ElasticPPcpp::commitState(void) {
double sigtrial; // trial stress double f; // yield function</p>
<p>// compute trial stress sigtrial = E * ( trialStrain - ezero - ep
);</p>
<p>// evaluate yield function if ( sigtrial &gt;= 0.0 ) f = sigtrial -
fyp; else f = -sigtrial + fyn;</p>
<p>double fYieldSurface = - E * DBL_EPSILON; if ( f &gt; fYieldSurface )
{ // plastic if ( sigtrial &gt; 0.0 ) { ep += f / E; } else { ep -= f /
E; } }</p>
<p>commitStrain = trialStrain; commitTangent=trialTangent; commitStress
= trialStress;</p>
<p>return 0; }</p>
<p>int ElasticPPcpp::revertToLastCommit(void) { trialStrain =
commitStrain; trialTangent = commitTangent; trialStress =
commitStress;</p>
<p>return 0; }</p>
<p>int ElasticPPcpp::revertToStart(void) { trialStrain = commitStrain =
0.0; trialTangent = commitTangent = E; trialStress = commitStress =
0.0;</p>
<p>ep = 0.0;</p>
<p>return 0; }</p>
<p>&lt;/source&gt;</p>
<h5 id="methods_dealing_with_output">Methods Dealing With Output</h5>
<p>Information is obtained by the user when the print command is invoked
by the user and also when the user issues the recorder command. When the
print command is invoked the Print method is invoked. This method simply
prints information about the element, and then asks the material to do
likewise.</p>
<p>&lt;source lang="cpp"&gt; void ElasticPPcpp::Print(OPS_Stream &amp;s,
int flag) { s &lt;&lt; "ElasticPPcpp tag: " &lt;&lt; this-&gt;getTag()
&lt;&lt; endln; s &lt;&lt; " E: " &lt;&lt; E &lt;&lt; endln; s &lt;&lt;
" ep: " &lt;&lt; ep &lt;&lt; endln; s &lt;&lt; " stress: " &lt;&lt;
trialStress &lt;&lt; " tangent: " &lt;&lt; trialTangent &lt;&lt; endln;
} &lt;/source&gt;</p>
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
<p>&lt;source lang="cpp"&gt;</p>
<p>&lt;/source&gt;</p>
<h5 id="methods_dealing_with_databasesparallel_processing">Methods
Dealing With Databases/Parallel Processing</h5>
<p>There are two methods provided which are required is the user uses to
use the database or parallel procesing features of the OpenSees
applications. If neither are to be used, the developer need simply
return a negative value in both methods. The idea is that the material
must pack up it's information using Vector and ID objects and send it
off to a Channel object. On the flip side, the receiving blank element
must receive the same Vector and ID data, unpack it and set the
variables.</p>
<p>&lt;source lang="cpp"&gt; int ElasticPPcpp::sendSelf(int cTag,
Channel &amp;theChannel) { int res = 0; static Vector data(9); data(0) =
this-&gt;getTag(); data(1) = ep; data(2) = E; data(3) = ezero; data(4) =
fyp; data(5) = fyn; data(6) = commitStrain; data(7) = commitStress;
data(8) = commitTangent;</p>
<p>res = theChannel.sendVector(this-&gt;getDbTag(), cTag, data); if (res
&lt; 0) opserr &lt;&lt; "ElasticPPcpp::sendSelf() - failed to send
data\n";</p>
<p>return res; }</p>
<p>int ElasticPPcpp::recvSelf(int cTag, Channel &amp;theChannel,
FEM_ObjectBroker &amp;theBroker) { int res = 0; static Vector data(9);
res = theChannel.recvVector(this-&gt;getDbTag(), cTag, data); if (res
&lt; 0) opserr &lt;&lt; "ElasticPPcpp::recvSelf() - failed to recv
data\n"; else { this-&gt;setTag(data(0)); ep = data(1); E = data(2);
ezero = data(3); fyp = data(4); fyn = data(5); commitStrain=data(6);
commitStress=data(7); commitTangent=data(8); trialStrain = commitStrain;
trialTangent = commitTangent; trialStress = commitStress; }</p>
<p>return res; } &lt;/source&gt;</p>
<h4 id="external_procedure">External Procedure</h4>
<p>This is the all importat extenal procedure that the interpreter will
parse when it comes accross your element on the command line. You need
to parse the command line, create a material using the command line
arguments you parsed and then return this material. The name of the
procedure must be OPS_YourClassName (no exceptions). If this procedure
is missing or the name is incorrect, your material will fail to
load.</p>
<p>NOTE: parsing the command line is easy with some other procedures
that are defined in the elementAPI.h file. In the example we show how to
get integer and double values from the command line. Other options such
as character strings and obtaining the number of input arguments are
also available.</p>
<p>The #ifdef stuff at the start is required for different operating
systems.</p>
<p>&lt;source lang="cpp"&gt;</p>
<ol>
<li>ifdef _USRDLL</li>
<li>define OPS_Export extern "C" _declspec(dllexport)</li>
<li>elif _MACOSX</li>
<li>define OPS_Export extern "C"
__attribute__((visibility("default")))</li>
<li>else</li>
<li>define OPS_Export extern "C"</li>
<li>endif</li>
</ol>
<p>OPS_Export void * OPS_ElasticPPcpp() { // print out some KUDO's if
(numElasticPPcpp == 0) { opserr &lt;&lt; "ElasticPPcpp unaxial material
- Written by fmk UC Berkeley Copyright 2008 - Use at your Own Peril\n";
numElasticPPcpp =1; }</p>
<p>// Pointer to a uniaxial material that will be returned
UniaxialMaterial *theMaterial = 0;</p>
<p>// // parse the input line for the material parameters //</p>
<p>int iData[1]; double dData[2]; int numData; numData = 1; if
(OPS_GetIntInput(&amp;numData, iData) != 0) { opserr &lt;&lt; "WARNING
invalid uniaxialMaterial ElasticPP tag" &lt;&lt; endln; return 0; }</p>
<p>numData = 2; if (OPS_GetDoubleInput(&amp;numData, dData) != 0) {
opserr &lt;&lt; "WARNING invalid E &amp; ep\n"; return 0; }</p>
<p>// // create a new material //</p>
<p>theMaterial = new ElasticPPcpp(iData[0], dData[0], dData[1]);</p>
<p>if (theMaterial == 0) { opserr &lt;&lt; "WARNING could not create
uniaxialMaterial of type ElasticPPCpp\n"; return 0; }</p>
<p>// return the material return theMaterial; } &lt;/source&gt;</p>

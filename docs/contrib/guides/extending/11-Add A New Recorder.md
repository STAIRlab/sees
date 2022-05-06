# Add A New Recorder

<p>A Recorder in the interpreted OpenSees applications is used to obtain
information from the model during the analysis. To add a new Recorder
option into the interpreted applications, the developer must provide a
new C++ subclass of the Recorder class and an interface function that
will be used to parse the input and create the new recorder.</p>
<h3 id="recorder_class">Recorder Class</h3>
<p>The Recorder class itself is an abstract base class. It inherits from
both the TaggedObject class and the MovableObject class. The class has a
minimal interface, which is as shown below:</p>
<p>The Recorder Class:</p>
<p>
```cpp
 class Recorder: public MovableObject,
public TaggedObject { public: Recorder(int classTag); virtual
~Recorder();</p>
<p>virtual int record(int commitTag, double timeStamp) =0;</p>
<p>virtual int restart(void); virtual int domainChanged(void); virtual
int setDomain(Domain &amp;theDomain); virtual int sendSelf(int
commitTag, Channel &amp;theChannel); virtual int recvSelf(int commitTag,
Channel &amp;theChannel, FEM_ObjectBroker &amp;theBroker);</p>
<p>virtual void Print(OPS_Stream &amp;s, int flag);</p>
<p>protected: protected:</p>
<p>private: static int lastRecorderTag; }; 
```
</p>
<p>The most important methods in the interface are:</p>
<ol>
<li>setDomain() - this is the method that is called when the new
recorder object is first added to the domain. It is inside this method
that all data, typically memory and pointer values, need to be
initialized for subsequent record commands.</li>
<li>record() - this is the method that is called when the recorder is
called upon to record/save information. The method is called with a tag
that will be unique and the current time in the domain.</li>
</ol>
<p>Other Important methods are:</p>
<ol>
<li>domainChanged() - this is a method called when something major has
happened in the Domain, ie. a new element, node, constraint and/or load
pattern has been added to the domain or removed from the domain. It is
necessasry for the Recorder to check in this call if it's pointers are
still valid (i.e. if an element it was recording info for has been
removed from the domain, it wuill have been deleted and it's old pointer
information will no longer be valid.)</li>
<li>send/recvSelf() - are two methods called in parallel applications.
When invoked the recorders send/recv information about what they are
recording.</li>
<li>restart() - this method is called if restart() is invoked on the
Domain. What the recorder does is up to you the developer.</li>
</ol>
<h3 id="example___sumelementforcesrecorder">Example -
SumElementForcesRecorder</h3>
<p>In the following section we will provide all necessary code to add a
new recorder. The purpose of this recorder will be to sum the forces
obtained from the list of inputted elements. The recorder will use the
getResistingForce() method in the elements to obtain these forces. A
similar class exists in the framework, which uses the
setResponse()/getResponse() methods in the element interface. To
demonstrate some of the output file options, the result will go to
either the screen, a text file, or a binary file. More output options
are of course available and the developer should look at existing
recorder options.</p>
<h4 id="header">Header</h4>
<p>The header for thew new class, which we will call
SumElementForcesRecorder is as follows:</p>
<p>
```cpp
</p>
<ol>
<li>ifndef SumElementForcesRecorder_h</li>
<li>define SumElementForcesRecorder_h</li>
</ol>
<ol>
<li>include &lt;Recorder.h&gt;</li>
<li>include &lt;Information.h&gt;</li>
<li>include &lt;ID.h&gt;</li>
</ol>
<p>class Domain; class Vector; class Matrix; class Element; class
Response; class FE_Datastore;</p>
<p>class SumElementForcesRecorder: public Recorder { public: //
constructors SumElementForcesRecorder(); SumElementForcesRecorder(const
ID eleID, bool echoTime, OPS_Stream *theOutputHandler); // destructors
~SumElementForcesRecorder();</p>
<p>// public methods int record(int commitTag, double timeStamp); int
restart(void); int domainChanged(void); int setDomain(Domain
&amp;theDomain); const char *getClassType(void) const; int sendSelf(int
commitTag, Channel &amp;theChannel); int recvSelf(int commitTag, Channel
&amp;theChannel, FEM_ObjectBroker &amp;theBroker);</p>
<p>protected:</p>
<p>private: int numEle; // the number of elements Element
**theElements;// pointer to array of element pointers ID eleID; // ID
(integer list) of element tags to record</p>
<p>Domain *theDomain; // pointer to domain holding elements OPS_Stream
*theOutput;// pointer to output location bool echoTimeFlag; // flag
indicating if pseudo time to be printed Vector *data; // Vector (double
array) to store sum of element forces };</p>
<ol>
<li>endif</li>
</ol>
<p>
```
</p>
<p>The header file defines the interface and variables for the class
SumElementForceRecorder. It defines the new class to be a sublass of the
Recorder class. In the public interface are 2 constructors and 1
destructor in addition to all the methods defined for the Recorder
class. There are no protected data or methods as we do not expect this
class to be subclassed. In the private section we store data that will
be used by the SumElementForceRecorder objects. The header has a number
of #include directives, one is needed for the base class and every class
used as a variable in the list of data (except those that are used as
pointers). For those classes that only appear as pointers in the header
file (Domain, Vector, Element, OPS_Stream) a forward declaration is all
that is needed (the include could also have been used, but using the
forward declaration simplifies dependencies and reduces the amount of
code that ha to be recompiled later if changes are made).</p>
<h4 id="implementation">Implementation</h4>
<p>It another file, SumElementForcesRecorder.cpp, we place the code that
details what the constructors, destructor and methods do. In addition we
provide one additional procedure OPS_SumElementForcesRecorder() (NOTE it
has the same name as the class with an OPS_ prefix). We will go through
each part of the file.</p>
<h5 id="include_directives">Include Directives</h5>
<p>The first part of the file contains the list of includes. It is
necessary to have an #include directive for each class and api file that
is used within the .cpp file and is not included in the header.</p>
<p>
```cpp
</p>
<ol>
<li>include "SumElementForcesRecorder.h"</li>
<li>include &lt;elementAPI.h&gt;</li>
</ol>
<ol>
<li>include &lt;Domain.h&gt;</li>
<li>include &lt;Element.h&gt;</li>
<li>include &lt;ElementIter.h&gt;</li>
<li>include &lt;Matrix.h&gt;</li>
<li>include &lt;Vector.h&gt;</li>
<li>include &lt;ID.h&gt;</li>
<li>include &lt;string.h&gt;</li>
<li>include &lt;Response.h&gt;</li>
<li>include &lt;Message.h&gt;</li>
<li>include &lt;Channel.h&gt;</li>
<li>include &lt;FEM_ObjectBroker.h&gt;</li>
</ol>
<ol>
<li>include &lt;StandardStream.h&gt;</li>
<li>include &lt;BinaryFileStream.h&gt;</li>
<li>include &lt;DataFileStream.h&gt;</li>
</ol>
<ol>
<li>include &lt;elementAPI.h&gt;</li>
</ol>
<p>
```
</p>
<h5 id="constructors">Constructors</h5>
<p>After the list of includes, we provide the 2 constructors. The
constructors are rather simple. They just initialize all the data
variables defined in the header. Note it is very important to set all
pointer values to 0.</p>
<p>
```cpp

SumElementForcesRecorder::SumElementForcesRecorder()</p>
<dl>
<dt></dt>
<dd>
Recorder(-1),
</dd>
</dl>
<p>numEle(0), theElements(0), eleID(0), theDomain(0), theOutput(0),
echoTimeFlag(true), data(0) {</p>
<p>}</p>
<p>SumElementForcesRecorder::SumElementForcesRecorder(const ID ele, bool
echoTime, OPS_Stream *theoutput)</p>
<dl>
<dt></dt>
<dd>
Recorder(-1),
</dd>
</dl>
<p>numEle(0), theElements(0), eleID(ele), theDomain(0),
theOutput(theoutput), echoTimeFlag(echoTime), data(0) { // set numEle
numEle = eleID.Size(); if (numEle == 0) { opserr &lt;&lt; "WARNING
SumElementForcesRecorder::SumElementForcesRecorder() - no elements tags
passed in input!\n"; } } 
```
</p>
<h5 id="destructor">Destructor</h5>
<p>The we provide the destructor. In the destructor all memory that the
Recorder created or was passed to it in the constructor must be
destroyed. Failing to delete this memory, will result in memory
leaks.</p>
<p>
```cpp

SumElementForcesRecorder::~SumElementForcesRecorder() { if (theElements
!= 0) delete [] theElements;</p>
<p>if (data != 0) delete data;</p>
<p>if (theOutput != 0) delete theOutput; } 
```
</p>
<h5 id="record_method">record() Method</h5>
<p>After the destructor, we provide the code for the record() method. It
does the following operations:</p>
<ol>
<li>Zeros the vector which will contain the final sum</li>
<li>If the time stamp is needed, it places it at the first location in
the vector.</li>
<li>Loops over all valid elements adding their resting force to the
vector.</li>
<li>Send the vector to the output handler to be written.</li>
<li>Returns success.</li>
</ol>
<p>
```cpp
 int SumElementForcesRecorder::record(int
commitTag, double timeStamp) { // check for initialization if (data ==
0) { opserr &lt;&lt; "SumElementForcesRecorder::record() - setDomain()
has not been called\n"; return -1; }</p>
<p>// zero the data vector data-&gt;Zero();</p>
<p>int forceSize = data-&gt;Size(); int startLoc = 0;</p>
<p>// write the time if echTimeFlag set if (echoTimeFlag == true) {
(*data)(0) = timeStamp; forceSize -= 1; startLoc = 1; }</p>
<p>// // for each element that has been added to theElements add force
contribution //</p>
<p>for (int i=0; i&lt; numEle; i++) { if (theElements[i] != 0) { int loc
= startLoc; const Vector &amp;force =
theElements[i]-&gt;getResistingForce(); int forceSize = force.Size();
for (int j=0; j&lt;forceSize; j++, loc++) (*data)(loc) += force(j); }
}</p>
<p>// // send the response vector to the output handler for o/p //</p>
<p>if (theOutput != 0) theOutput-&gt;write(*data);</p>
<p>// succesfull completion - return 0 return 0; } 
```
</p>
<h5 id="restart_and_domainchanged_methods">restart() and domainChanged()
methods</h5>
<p>Afte the record() method, we have the two simple short methods
restart() and domainChanged(). restart does nothing and domainChanged
simply calls the objects own setDomain() method.</p>
<p>
```cpp
 int SumElementForcesRecorder::restart(void)
{ return 0; }</p>
<p>int SumElementForcesRecorder::domainChanged(void) { if (theDomain !=
0) this-&gt;setDomain(*theDomain); } 
```
</p>
<h5 id="setdomain_method">setDomain() Method</h5>
<p>The setDomain() method follows. In this method we perform the
following:</p>
<ol>
<li>set the pointer for the enclosing domain object.</li>
<li>allocate space from memoory for our array of ponters and our data
vector.</li>
<li>initialize the array components to be 0 or point to an element given
by the eleID.</li>
<li>determine the size of the vector that will be used to store the sum
of the forces.</li>
<li>allocate space for the vector.</li>
</ol>
<p>
```cpp
 int
SumElementForcesRecorder::setDomain(Domain &amp;theDom) { theDomain =
&amp;theDom;</p>
<p>// set numEle if (numEle == 0) { opserr &lt;&lt; "WARNING
SumElementForcesRecorder::initialize() - no elements tags passed in
input!\n"; return 0; }</p>
<p>// create theElements, an array of pointers to elements theElements =
new Element *[numEle]; if (theElements == 0) { opserr &lt;&lt; "WARNING
SumElementForcesRecorder::initialize() - out of memory\n"; numEle = 0;
// set numEle = 0, in case record() still called return -1; }</p>
<p>// // loop over the list of elements, // if element exists add it's
pointer o the array // get its resisting force, check size to determine
compatable with others //</p>
<p>int sizeArray = -1;</p>
<p>for (int i=0; i&lt;numEle; i++) { int eleTag = eleID(i); Element
*theEle = theDomain-&gt;getElement(eleTag);</p>
<p>if (theEle != 0) {</p>
<p>const Vector &amp;force = theEle-&gt;getResistingForce(); int
forceSize = force.Size(); if (sizeArray == -1) { sizeArray = forceSize;
theElements[i] = theEle; } else if (sizeArray != forceSize) { opserr
&lt;&lt; "WARNING: forces mismatch - element: " &lt;&lt; eleTag &lt;&lt;
" will not be included\n"; theElements[i] = 0; } else { theElements[i] =
theEle; } } else { theElements[i] = 0; } }</p>
<p>// if echTimeFlag is set, add room for the time to be output if
(echoTimeFlag == true) sizeArray++;</p>
<p>// create the vector to hold the data data = new
Vector(sizeArray);</p>
<p>if (data == 0 || data-&gt;Size() != sizeArray) { opserr &lt;&lt;
"SumElementForcesRecorder::initialize() - out of memory\n"; delete []
theElements; theElements = 0; numEle = 0; }</p>
<p>return 0; } 
```
</p>
<h5 id="sendself_and_recvself_methods">sendSelf() and recvSelf()
methods</h5>
<p>These methods only need be provided if the object will be used in a
parallel program. We provide their implementation for completeness,
though typicall developers are interested in running the code in a
sequential application and should just return -1.</p>
<p>
```cpp
 static char myClassType[] =
{"SumElementForcesRecorder"};</p>
<p>const char * SumElementForcesRecorder::getClassType(void) const {
return myClassType; }</p>
<p>int SumElementForcesRecorder::sendSelf(int commitTag, Channel
&amp;theChannel) { // send in an ID (integar array) to the receiving
object the following: // recorder tag // size of eleID // class tag of
handler // echoTimeFlag</p>
<p>static ID idData(5); idData(0) = this-&gt;getTag();; idData(1) =
eleID.Size(); idData(2) = theOutput-&gt;getClassTag(); if (echoTimeFlag
== true) idData(3) = 1; else idData(3) = 0;</p>
<p>if (theChannel.sendID(0, commitTag, idData) &lt; 0) { opserr &lt;&lt;
"SumElementForcesRecorder::recvSelf() - failed to recv idData\n"; return
-1; }</p>
<p>// send eleID to receiving object if (theChannel.sendID(0, commitTag,
eleID) &lt; 0) { opserr &lt;&lt; "SumElementForcesRecorder::sendSelf() -
failed to send idData\n"; return -1; }</p>
<p>// send theOutput to receiving object if
(theOutput-&gt;sendSelf(commitTag, theChannel) &lt; 0) { opserr &lt;&lt;
"SumElementForcesRecorder::sendSelf() - failed to send theOutput\n";
return -1; }</p>
<p>return 0; } 
```
</p>
<p>
```cpp
 int SumElementForcesRecorder::recvSelf(int
commitTag, Channel &amp;theChannel, FEM_ObjectBroker &amp;theBroker) {
// receive from the sending object the ID static ID idData(5); if
(theChannel.recvID(0, commitTag, idData) &lt; 0) { opserr &lt;&lt;
"SumElementForcesRecorder::recvSelf() - failed to recv idData\n"; return
-1; }</p>
<p>// with the data received // setTag // resize the eleID array // set
echoTimeFlag // get an outputHandler</p>
<p>this-&gt;setTag(idData(0)); eleID.resize(idData(1)); idData(2) =
theOutput-&gt;getClassTag(); if (idData(3) == 0) echoTimeFlag = true;
else echoTimeFlag = false;</p>
<p>if (theOutput != 0 &amp;&amp; theOutput-&gt;getClassTag() !=
idData(4)) delete theOutput;</p>
<p>theOutput = theBroker.getPtrNewStream(idData(4)); if (theOutput == 0)
{ opserr &lt;&lt; "SumElementForcesRecorder::recvSelf() - failed to get
Output of correct type\n"; return -1; }</p>
<p>// receive eleID if (theChannel.recvID(0, commitTag, eleID) &lt; 0) {
opserr &lt;&lt; "SumElementForcesRecorder::recvSelf() - failed to recv
eleID\n"; return -1; }</p>
<p>// get theOutput to receive data if
(theOutput-&gt;recvSelf(commitTag, theChannel, theBroker) &lt; 0) {
opserr &lt;&lt; "SumElementForcesRecorder::sendSelf() - failed to send
theOutput\n"; return -1; }</p>
<p>return 0; } 
```
</p>
<h4 id="interface_function">Interface Function</h4>
<p>At the end of the implementation file is the interface function. This
function is required by all new classes. It is a function which will use
the api to</p>
<ol>
<li>parse the input</li>
<li>based on the input create objects</li>
<li>create a recorder object of the correct type, and return it to the
calling function.</li>
</ol>
<p>The interface function is the function that is called when the
interpreter comes across the command telling it to create a
SumElementForcesRecorder.</p>
<p>
```cpp
</p>
<ol>
<li>ifdef _USRDLL</li>
<li>include &lt;windows.h&gt;</li>
<li>define OPS_Export extern "C" _declspec(dllexport)</li>
<li>elif _MACOSX</li>
<li>define OPS_Export extern "C"
__attribute__((visibility("default")))</li>
<li>else</li>
<li>define OPS_Export extern "C"</li>
<li>endif</li>
</ol>
<p>static int numSumElementForcesREcorder = 0;</p>
<p>OPS_Export void * OPS_SumElementForcesRecorder() { Recorder
*theRecorder = 0;</p>
<p>int numRemainingArgs = OPS_GetNumRemainingInputArgs();</p>
<p>// check for quick return, possibly parallel case if
(numRemainingArgs == 0) { Recorder *theRecorder = new
SumElementForcesRecorder(); }</p>
<p>// // parse args //</p>
<p>int numEle = 0, eleTag; ID eleID(0);</p>
<p>OPS_Stream *theOutputStream = 0; int outMode = 0; // standard stream
bool echoTime = false;</p>
<p>bool doneParsingArgs = false; char data[100]; char outputName[200];
char **eleArgs = 0; int numEleArgs = 0; while (numRemainingArgs &gt; 0)
{ if (OPS_GetString(data,100) &lt; 0) return 0;</p>
<p>// output to standard file if (strcmp(data,"-file") == 0) { outMode =
1; if (OPS_GetString(outputName,200) &lt; 0) return 0; numRemainingArgs
-= 2; }</p>
<p>// output to binary file else if (strcmp(data,"-binary") == 0) {
outMode = 2; if (OPS_GetString(outputName,200) &lt; 0) return 0;
numRemainingArgs -= 2; }</p>
<p>// echo domain time stamp in output else if (strcmp(data,"-time") ==
0) { echoTime = true; numRemainingArgs -= 1; }</p>
<p>// read the list of elements &amp; place in an ID else if
((strcmp(data,"-ele") == 0) || (strcmp(data,"-eles") == 0) ||
(strcmp(data,"-element") == 0)) {</p>
<p>numRemainingArgs --; int one = 1; while (numRemainingArgs &gt; 0
&amp;&amp; OPS_GetIntInput(&amp;one, &amp;eleTag) == 0) { eleID[numEle]
= eleTag; numEle++; numRemainingArgs--; } doneParsingArgs = true; }</p>
<p>// // create the output handler //</p>
<p>if (outMode == 0) theOutputStream = new StandardStream(); if (outMode
== 1) theOutputStream = new DataFileStream(outputName); else if (outMode
== 2) theOutputStream = new BinaryFileStream(outputName);</p>
<p>// // create the recorder //</p>
<p>theRecorder = new SumElementForcesRecorder(eleID, echoTime,
theOutputStream);</p>
<p>// return it return theRecorder; } 
```
</p>
<h4 id="example_script">Example Script</h4>
<p>(OpenSeesDeveloper/recorder/example1.tcl)</p>
<p>An example OpenSees tcl input file for this new recorder is:</p>
<p>
```tcl
</p>
<ol>
<li>create the model</li>
</ol>
<p>model basic -ndm 2 -ndf 2 node 1 0.0 0.0 node 2 144.0 0.0 node 3
168.0 0.0 node 4 72.0 96.0 uniaxialMaterial Elastic 1 3000 element truss
1 1 4 10.0 1 element truss 2 2 4 5.0 1 element truss 3 3 4 5.0 1 fix 1 1
1 fix 2 1 1 fix 3 1 1</p>
<p>pattern Plain 1 Linear {</p>
<ol>
<li>apply the load - command: load nodeID xForce yForce</li>
</ol>
<p>load 4 100 -50 }</p>
<ol>
<li>Create the analysis</li>
</ol>
<p>system ProfileSPD constraints Plain integrator LoadControl 1.0
algorithm Linear numberer RCM analysis Static recorder Element -file
a.out -time -ele 1 2 3 forces recorder SumElementForcesRecorder -file
b.out -time -ele 1 2 3</p>
<ol>
<li>perform the analysis</li>
</ol>
<p>analyze 10 
```
</p>
<h4 id="example_output">Example Output</h4>
<p>The output shows that the model is in equilibrium, and that at node 4
the node the element resisting forces are equal to the applied
forces.</p>
<p>
```tcl
 1 -100 50 100 -50 2 -200 100 200 -100 3
-300 150 300 -150 4 -400 200 400 -200 5 -500 250 500 -250 6 -600 300 600
-300 7 -700 350 700 -350 8 -800 400 800 -400 9 -900 450 900 -450 10
-1000 500 1000 -500 
```
</p>

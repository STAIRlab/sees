# Add a New Element Fortran

<p><strong>to be completed</strong></p>
<p>To add a new Element module using the Fortran language, the developer
must provide a new Fortran routine for the Element.</p>
<p>Some information about the state of the model is passed as arguments
to the element methods. The input arguments are:</p>
<ul>
<li>the element object, <em>eleObj</em></li>
<li>the model state, <em>modl</em></li>
<li>the isw switch, <em>isw</em>, which indicates what action is needed
for each invocation of the procedure.</li>
</ul>
<p>The output arguments are:</p>
<ul>
<li>the tangent stiffness matrix, <em>tang</em></li>
<li>the residual vector, <em>resid</em></li>
<li>the error code, <em>error</em></li>
</ul>

<p>The name of the routine is important for the OpenSees interpreter:
when it encounters a new element type it will look for a library with
the same name of the element.</p>
<p>NOTE: This document assumes the reader is familiar with the Fortran
programming language.</p>

<h3 id="element_routine">Element Routine</h3>
<p>It should be noted the command contains all underscores. This is a
consequence of the Fortran compiler, which for the compiler used output
the procedure is in all lower case. Please note that before calling
memory allocated for the pointers the Fortran code must make a call to
the Fortran routine c f pointer().</p>

<h3 id="example___truss2d">Example - Truss2D</h3>
<p>In the following section we will provide all necessary code to add a
new 2d planar truss element into an OpenSees interpreter. The
stress-strain relationship will be provided by a UniaxialMaterial
object. Please refer to the comments inserted in the code for further
explanations.</p>
<p>Please note that the following example has been corrected and
expanded by the author of this page. The following code may not match
the actual version in the OpenSees repository.</p>

```fortran
SUBROUTINE
trussf(eleObj,modl,tang,resid,isw,error)</p>
<p>!DEC$ IF DEFINED (_DLL) !DEC$ ATTRIBUTES DLLEXPORT :: TRUSSF !DEC$
END IF</p>
<p>use elementTypes use elementAPI implicit none</p>
<p>type(eleObject)::eleObj type(modelState)::modl double precision
tang(4, *) double precision resid(4) integer::isw; integer::error;</p>
<p>integer :: tag, nd1, nd2, matTag, numCrd, i, j, numDOF real *8,
pointer::theParam(:) integer, pointer::theNodes(:)</p>
<p>double precision A, dx, dy, L, cs, sn double precision dLength,
force, k</p>
<p>integer :: iData(3); integer :: matTags(2);</p>
<p>type(c_ptr) :: theCMatPtr type(c_ptr), pointer :: theCMatPtrPtr(:)
type(matObject), pointer :: theMat</p>
<p>double precision dData(1), nd1Crd(2), nd2Crd(2) double precision
d1(2), d2(2), tran(4) double precision strs(1), strn(1), tng(1)</p>
<p>integer numData, err, matType</p>
```

The main IF/THEN structure of the routine begins
here; it is needed to select the proper code depending on what the flag
`isw` is requesting. 

```fortran
IF (isw.eq.ISW_INIT) THEN
c get the input data - tag? nd1? nd2? A? matTag?
numData = 3 err = OPS_GetIntInput(numData, iData) tag = iData(1); nd1
= iData(2); nd2 = iData(3);
numData = 1 err = OPS_GetDoubleInput(numData, dData) A =
dData(1);
numData = 1 err = OPS_GetIntInput(numData, iData) matTag =
iData(1);
c Allocate the element state
eleObj%tag = tag eleObj%nnode = 2 eleObj%ndof = 4 eleObj%nparam = 4
eleObj%nstate = 0 eleObj%nmat = 1
matTags(1) = matTag; matType = OPS_UNIAXIAL_MATERIAL_TYPE; err =
OPS_AllocateElement(eleObj, matTags, matType)
c Initialize the element properties
call c_f_pointer(eleObj%param, theParam, [4]); call
c_f_pointer(eleObj%node, theNodes, [2]);
numCrd = 2; err = OPS_GetNodeCrd(nd1, numCrd, nd1Crd); err =
OPS_GetNodeCrd(nd2, numCrd, nd2Crd);
dx = nd2Crd(1)-nd1Crd(1); dy = nd2Crd(2)-nd1Crd(2);
L = sqrt(dx*dx + dy*dy);
if (L == 0.0) then c OPS_Error("Warning - truss element has zero length\n", 1); return; end if
cs = dx/L; sn = dy/L;
theParam(1) = A; theParam(2) = L; theParam(3) = cs; theParam(4) =
sn;
theNodes(1) = nd1; theNodes(2) = nd2;
ELSE IF (isw == ISW_COMMIT) THEN
```

In ISW_COMMIT, the state of the model is saved. If
your element uses state variables, save them here. 

```fortran
<p>call c_f_pointer(eleObj%mats, theCMatPtrPtr, [1]); theCMatPtr =
theCMatPtrPtr(1);</p>
<p>j=OPS_InvokeMaterialDirectly(theCMatPtr, modl, strn, strs, + tng,
isw)</p>
<p>ELSE IF (isw == ISW_REVERT_TO_START) THEN</p>
<p>call c_f_pointer(eleObj%mats, theCMatPtrPtr, [1]); theCMatPtr =
theCMatPtrPtr(1);</p>
<p>j=OPS_InvokeMaterialDirectly(theCMatPtr, modl, strn, strs, + tng,
isw)</p>
<p>ELSE IF (isw == ISW_FORM_MASS) THEN</p>
```

In `ISW_FORM_MASS`, the mass matrix (if given by the
element) must be returned in TANG. IMPORTANT: if your element returns no
mass, remember to initialize TANG to zero! If not initialized, Fortran
will return a mass matrix with random values. Also, do not overwrite
RESID! 

```fortran
ELSE IF (isw == ISW_FORM_TANG_AND_RESID) THEN
```

In `ISW_FORM_TANG_AND_RESID`, all the trials during a
non-linear analysis are performed. DO NOT save state variables here.

```fortran
call c_f_pointer(eleObj%param, theParam, [4]);
 call
c_f_pointer(eleObj%node, theNodes, [2]);
 call c_f_pointer(eleObj%mats,
theCMatPtrPtr, [1]);
 theCMatPtr = theCMatPtrPtr(1);

A = theParam(1);
 L = theParam(2);
 cs = theParam(3);
 sn = theParam(4);

nd1 = theNodes(1);
 nd2 = theNodes(2);

numDOF = 2;
err = OPS_GetNodeDisp(nd1, numDOF, d1);
err = OPS_GetNodeDisp(nd2, numDOF, d2);

tran(1) = -cs;
tran(2) = -sn;
tran(3) = cs;
tran(4) = sn;

dLength = 0.0;
do i = 1,2 
  dLength = dLength - (d2(i)-d1(i)) * tran(i);
 continue
strn(1) = dLength/L;

c i = 0 c i=OPS_InvokeMaterial(eleObj, i, modl, strn, strs, tng, isw)
j=OPS_InvokeMaterialDirectly(theCMatPtr, modl, strn, strs, + tng, isw)
force = A*strs(1);
 k = A*tng(1)/L;

do i =1,4 resid(i) = force * tran(i);
 do j = 1,4 tang(i,j) = k * tran(i)*tran(j);
 continue continue
END IF
END IF
c return error code error = 0
END SUBROUTINE trussf
```

<h3 id="compilation_instructions_for_visual_studio_on_windows"
>Compilation Instructions for Visual Studio on Windows</h3>

<p>The compilation can be carried out with Visual Studio, if Windows
machines are used. Intel Visual Fortran can be used, it integrates
itself with Visual Studio IDE during installation.</p>


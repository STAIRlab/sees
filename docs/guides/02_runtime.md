# Runtime

record
recorder

printModel

POST

```py
render.elastica(model, displ): ...
```

MODLEING (MOVE TO LIBRARY?)

- [`remove`](core/remove)
- [`setElementRayleighDampingFactors`](core/setElementRayleighDampingFactors)
- [`modalDamping`](core/modalDamping)

ANALYSIS?

```py
def eig(model,  number, **runtime)-> (freq, displ): ...
def rha(model, pattern, **runtime)-> (): ...
```

```py
def rt.incr(self, model, pattern, force|displ=<float>)
```

- [`sdfResponse`](core/sdfResponse)
- [`InitialStateAnalysis`](core/InitialStateAnalysis)

systemSize
getLoadFactor
testIter
testNorm
numFact
numIter
- [`loadConst`](core/loadConst)

?

- [`setNumthread`](core/setNumthread)
- [`getNumthread`](core/getNumthread)


## Runtime

- [`getTime`]
- [`setTime`](core/setTime)

- [`setNodeCoord`](core/setNodeCoord)
- [`setNodeDisp`](core/setNodeDisp)
- [`setNodeVel`](core/setNodeVel)
- [`setNodeAccel`](core/setNodeAccel)

- [`reactions`](core/reactions)

- [`setPrecision`](core/setPrecision)
- [`updateElementDomain`](core/updateElementDomain)
- [`updateMaterialStage`](core/updateMaterialStage)

- [`reset`](core/reset)
- [`wipe`](core/wipe)
- [`wipeAnalysis`](core/wipeAnalysis)


## Utilities
- [`convertBinaryToText`](core/convertBinaryToText)
- [`convertTextToBinary`](core/convertTextToBinary)
- [`stripXML`](core/stripXML)
- [`restore`](core/restore)
- [`save`](core/save)
- [`database`](core/database)


sectionForce
sectionDeformation
sectionStiffness
sectionFlexibility
sectionLocation
sectionWeight

getEleTags
eleDynamicalForce
eleForce
eleNodes
eleResponse
basicDeformation
basicForce
basicStiffness

getNodeTags
nodeDisp
nodeAccel
nodeVel
nodeBounds
nodeCoord
nodeEigenvector
nodeDOFs
nodeMass
nodePressure
nodeReaction
nodeResponse
nodeUnbalance

printA
printB
printGID

version
logFile


<!--
- [`start`](core/start)
- [`stop`](core/stop)
-->

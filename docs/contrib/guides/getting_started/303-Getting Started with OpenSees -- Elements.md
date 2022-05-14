# Getting Started with OpenSees -- Elements

<p>The elastic columns and beams are defined using the OpenSees <a
href="Elastic_Beam_Column_Element" title="wikilink">Elastic Beam Column
Element</a>. The characteristics of a 2-D elastic element depend on the
material modulus and the section area and moment of inertia. Because the
elements in this frame represent reinforced-concrete elements, the value
of 4227 ksi for the elastic modulus of concrete will be used.</p>
<p>The following values represent the area and moment of inertia of the
columns and beams:</p>
<ul>
<li>Columns</li>
</ul>
<dl>
<dt></dt>
<dd>
Area=(5*12)*(5*12)=3600
</dd>
<dd>
Iz = 1/12*(5*12)*(5*12)^3=1080000
</dd>
</dl>
<ul>
<li>Beams</li>
</ul>
<dl>
<dt></dt>
<dd>
Area=(5*12)*(8*12)=5760
</dd>
<dd>
Iz = 1/12*(5*12)*(8*12)^3=4423680
</dd>
</dl>
<p>The OpenSees <a href="Geometric_Transformation_Command"
title="wikilink">Geometric Transformation Command</a> defines how the
element coordinates correlate to the global model coordinates.
&lt;br&gt; In a 2D problem, element orientation does not need to be
considered, and can be the same for all elements. The linear
transformation will be used in this demonstration:</p>
<p><em>geomTransf Linear $transfTag &lt;-jntOffset $dXi $dYi $dXj
$dYj&gt;</em></p>
<p>
```Tcl
 geomTransf Linear 1 
```
</p>
<p>The following commands define the two columns (element 1 and 2) and
the beam (element 3):</p>
<p>

```tcl
# element elasticBeamColumn $eleTag $iNode $jNode $A $E $Iz $transfTag
element elasticBeamColumn 1 1 3 3600 4227 1080000 1 
element elasticBeamColumn 2 2 4 3600 4227 1080000 1 
element elasticBeamColumn 3 3 4 5760 4227 4423680 1 
```

</p>
<p>The element connectivity is shown in the following figure:</p>
<figure>
<img src="/OpenSeesRT/contrib/static/GettingStartedNodes.jpg" title="GettingStartedNodes.jpg"
alt="GettingStartedNodes.jpg" />
<figcaption aria-hidden="true">GettingStartedNodes.JPG</figcaption>
</figure>
<hr />

<p>Return to <a href="Getting_Started_with_OpenSees"
title="wikilink">Getting Started with OpenSees</a></p>


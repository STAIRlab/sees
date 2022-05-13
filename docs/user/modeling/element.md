
---
title: element
...

<style>
h1 {
    font-family: var(--md-code-font-family);
    color: var(--md-code-fg-color) !important;
    font-feature-settings: "kern";
}
</style>

# element



<div style="width: 95%; padding-left: 5%">

<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">ZeroLength</span>(name, nodes, materials, dofs, orientation, do_rayleigh, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>nodes</td><td><code>[iNode,jNode]</code></td><td><table>
<tr><td>iNode</td><td><code>Ref(Node)</code></td><td></tr>
<tr><td>jNode</td><td><code>Ref(Node)</code></td><td></tr>
</table>
</tr>
<tr><td>materials</td><td><code>[materials1,materials2,materials3,materials4,materials5,materials6]</code></td><td><table>
<tr><td>materials1</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials2</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials3</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials4</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials5</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials6</td><td><code>Ref(uniaxial)</code></td><td></tr>
</table>
</tr>
<tr><td>dofs = ['$dx', '$dy', '$dz', '$rx', '$ry', '$rz']</td><td><code>[dofs1,dofs2,dofs3,dofs4,dofs5,dofs6]</code></td><td><table>
<tr><td>dofs1</td><td><code>Int</code></td><td></tr>
<tr><td>dofs2</td><td><code>Int</code></td><td></tr>
<tr><td>dofs3</td><td><code>Int</code></td><td></tr>
<tr><td>dofs4</td><td><code>Int</code></td><td></tr>
<tr><td>dofs5</td><td><code>Int</code></td><td></tr>
<tr><td>dofs6</td><td><code>Int</code></td><td></tr>
</table>
</tr>
<tr><td>orientation</td><td><code>[[x1,x2,x3],[yp1,yp2,yp3]]</code></td><td><table>
<tr><td>x</td><td><code>[x1,x2,x3]</code></td><td><table>
<tr><td>x1</td><td><code>Num</code></td><td></tr>
<tr><td>x2</td><td><code>Num</code></td><td></tr>
<tr><td>x3</td><td><code>Num</code></td><td></tr>
</table>
</tr>
<tr><td>yp</td><td><code>[yp1,yp2,yp3]</code></td><td><table>
<tr><td>yp1</td><td><code>Num</code></td><td></tr>
<tr><td>yp2</td><td><code>Num</code></td><td></tr>
<tr><td>yp3</td><td><code>Num</code></td><td></tr>
</table>
</tr>
</table>
</tr>
<tr><td>do_rayleigh</td><td><code>Int</code></td><td></tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">ZeroLength3D</span>(name, nodes, materials, dofs, orientation, do_rayleigh, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>nodes</td><td><code>[iNode,jNode]</code></td><td><table>
<tr><td>iNode</td><td><code>Ref(Node)</code></td><td></tr>
<tr><td>jNode</td><td><code>Ref(Node)</code></td><td></tr>
</table>
</tr>
<tr><td>materials</td><td><code>[materials1,materials2,materials3,materials4,materials5,materials6]</code></td><td><table>
<tr><td>materials1</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials2</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials3</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials4</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials5</td><td><code>Ref(uniaxial)</code></td><td></tr>
<tr><td>materials6</td><td><code>Ref(uniaxial)</code></td><td></tr>
</table>
</tr>
<tr><td>dofs = ['$dx', '$dy', '$dz', '$rx', '$ry', '$rz']</td><td><code>[dofs1,dofs2,dofs3,dofs4,dofs5,dofs6]</code></td><td><table>
<tr><td>dofs1</td><td><code>Int</code></td><td></tr>
<tr><td>dofs2</td><td><code>Int</code></td><td></tr>
<tr><td>dofs3</td><td><code>Int</code></td><td></tr>
<tr><td>dofs4</td><td><code>Int</code></td><td></tr>
<tr><td>dofs5</td><td><code>Int</code></td><td></tr>
<tr><td>dofs6</td><td><code>Int</code></td><td></tr>
</table>
</tr>
<tr><td>orientation</td><td><code>[[x1,x2,x3],[yp1,yp2,yp3]]</code></td><td><table>
<tr><td>x</td><td><code>[x1,x2,x3]</code></td><td><table>
<tr><td>x1</td><td><code>Num</code></td><td></tr>
<tr><td>x2</td><td><code>Num</code></td><td></tr>
<tr><td>x3</td><td><code>Num</code></td><td></tr>
</table>
</tr>
<tr><td>yp</td><td><code>[yp1,yp2,yp3]</code></td><td><table>
<tr><td>yp1</td><td><code>Num</code></td><td></tr>
<tr><td>yp2</td><td><code>Num</code></td><td></tr>
<tr><td>yp3</td><td><code>Num</code></td><td></tr>
</table>
</tr>
</table>
</tr>
<tr><td>do_rayleigh</td><td><code>Int</code></td><td></tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">forceBeamColumn</span>(name,<br>&emsp;&emsp;&emsp;nodes,<br>&emsp;&emsp;&emsp;transform,<br>&emsp;&emsp;&emsp;integration,<br>&emsp;&emsp;&emsp;consistent_mass,<br>&emsp;&emsp;&emsp;mass_density,<br>&emsp;&emsp;&emsp;**kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>nodes</td><td><code>[iNode,jNode]</code></td><td><table>
<tr><td>iNode</td><td><code>Ref(Node)</code></td><td></tr>
<tr><td>jNode</td><td><code>Ref(Node)</code></td><td></tr>
</table>
</tr>
<tr><td>geom</td><td><code>Ref(geomTransf)</code></td><td></tr>
<tr><td>integration</td><td><code>BeamInt</code></td><td></tr>
<tr><td>cMass</td><td><code>Flg</code></td><td>Flag indicating whether to use consistent mass matrix.</tr>
<tr><td>mass</td><td><code>Num</code></td><td>element mass per unit length</tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">DisplBeamColumn</span>(name,<br>&emsp;&emsp;&emsp;nodes,<br>&emsp;&emsp;&emsp;transform,<br>&emsp;&emsp;&emsp;integration,<br>&emsp;&emsp;&emsp;consistent_mass,<br>&emsp;&emsp;&emsp;mass_density,<br>&emsp;&emsp;&emsp;**kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>nodes</td><td><code>[iNode,jNode]</code></td><td><table>
<tr><td>iNode</td><td><code>Ref(Node)</code></td><td></tr>
<tr><td>jNode</td><td><code>Ref(Node)</code></td><td></tr>
</table>
</tr>
<tr><td>geom</td><td><code>Ref(geomTransf)</code></td><td></tr>
<tr>
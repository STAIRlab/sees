
---
title: section
...

<style>
h1 {
    font-family: var(--md-code-font-family);
    color: var(--md-code-fg-color) !important;
    font-feature-settings: "kern";
}
</style>

# section



This module provides constructors for `SectionForceDeformation` objects
which represent force-deformation (or resultant stress-strain) 
relationships at beam-column and plate sample points.


<div style="width: 95%; padding-left: 5%">

<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">FiberSection</span>(name, torsional_stiffness, areas, **kwds)
</span>



<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>GJ</td><td><code>Num</code></td><td>linear-elastic torsional stiffness assigned to the section (optional, default = no torsional stiffness)</tr>
<tr><td>areas</td><td><code>[]</code></td><td><table>
</table>
</tr>

</tbody>
</table>
<!-- </blockquote> -->


<!-- <blockquote> -->
<span style="font-feature-settings: kern; color: var(--md-code-fg-color) !important; font-family: var(--md-code-font-family);">
    <span style="color:#900">SectionAggregator</span>(name, materials, section, **kwds)
</span>


![](/figures/SectionAggregator.gif)

<table>
<colgroup>
  <col style="width: 10%" ><col style="width: 30%" ><col style="width: 60%" >
</colgroup>
<tbody>

<tr><td>name</td><td><code>Tag</code></td><td></tr>
<tr><td>materials</td><td><code>{dof : material ...}</code></td><td>the force-deformation quantity to be modeled by this section object.<table>
<tr><td>dof</td><td><code>Flg</code></td><td></tr>
<tr><td>material</td><td><code>Ref(uniaxial)</code></td><td>tags of previously-defined `UniaxialMaterial` objects</tr>
</table>
</tr>
<tr><td>section</td><td><code>Ref(section)</code></td><td>tag of previously-defined Section object to which the UniaxialMaterial objects are aggregated as additional force-deformation relationships</tr>

</tbody>
</table>
<!-- </blockquote> -->

</div>

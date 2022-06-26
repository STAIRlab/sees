# FourNodeTetrahedron

<figure>
<img src="/OpenSeesRT/contrib/static/Tet.png" title="Tet.png" alt="Tet.png" />
<figcaption aria-hidden="true">Tet.png</figcaption>
</figure>

<p>This command is used to construct a standard four-node tetrahedron
element objec with one-point Gauss integration.</p>

```tcl
element FourNodeTetrahedron $eleTag $node1 $node2 $node3
        $node4 $matTag < $b1 $b2 $b3 >
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><strong>`node1` `node2`</strong></p>
<p><strong>`node3` `node4`</strong></p></td>
<td><p>four nodes defining element boundaries, input order is shown in
the figure.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>tag of nDMaterial</p></td>
</tr>
<tr class="even">
<td><p><strong>`b1` `b2` `b3`</strong></p></td>
<td><p>body forces in global x,y,z directions</p></td>
</tr>
</tbody>
</table>

Because sometimes bricks will give you headaches! Use this if you
don't care much about the stress/strain fields (tets are notoriously
bad). Otherwise, you can use the 10-node quadratic tetrahedron (in
development).

<p>NOTE:</p>
<ol>
<li>The valid queries to a FourNodeTetrahedron element when creating an
ElementRecorder object are 'forces', 'stresses,' ('strains' version &gt;
2.2.0) and 'material $matNum matArg1 matArg2 ...' Where $matNum refers
to the material object at the integration point corresponding to the
node numbers in the isoparametric domain.</li>
<li>This element can only be defined in -ndm 3 -ndf 3</li>
</ol>

## Examples

## References

<!-- TODO: change link to wayback web -->

<p><a
href="https://www.colorado.edu/engineering/CAS/courses.d/AFEM.d/AFEM.Ch09.d/AFEM.Ch09.pdf">Carlos
Felipa's AFEM Course: Chapter 9 The Linear Tetrahedron.</a></p>
<hr />
<p>Code Developed by <a href="http://www.joseabell.com">José A. Abell at
Universidad de los Andes, Chile</a></span></p>

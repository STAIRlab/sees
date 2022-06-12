# Coulomb Friction

<p>This command is used to construct a <a
href="http://en.wikipedia.org/wiki/Friction%22Coulomb">friction"</a>
model object. Coulomb's Law of Friction states that kinetic friction is
independent of the sliding velocity.</p>

```tcl
frictionModel Coulomb $frnTag $mu
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">frnTag</code></td>
<td><p>unique friction model object tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">mu</code></td>
<td><p>coefficient of friction</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/CoulombFriction.png" title="CoulombFriction.png"
alt="CoulombFriction.png" />
<figcaption aria-hidden="true">CoulombFriction.png</figcaption>
</figure>
<hr />

## Examples

```tcl
frictionModel Coulomb 1 0.163
```

<hr />
<p>RELATED TO:</p>
<ul>
<li><a
href="http://opensees.berkeley.edu/wiki/index.php/Flat_Slider_Bearing_Element">Flat
Slider Bearing Element</a></li>
<li><a
href="http://opensees.berkeley.edu/wiki/index.php/Single_Friction_Pendulum_Bearing_Element">Single
Friction Pendulum Bearing Element</a></li>
<li><a
href="http://opensees.berkeley.edu/wiki/index.php/Triple_Friction_Pendulum_Element">Triple
Friction Pendulum Bearing Element</a></li>
</ul>
<hr />
<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>

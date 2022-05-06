# SensitivityIntegrator Command

<dl>
<dt></dt>
<dd>
For static analysis, the only option currently available is the
following, which must be defined before the ‘analysis’ command.
</dd>
</dl>

```tcl
sensitivityIntegrator -static
```
<dl>
<dt></dt>
<dd>
For the dynamic case, currently only the Newmark algorithm is available.
Two command need to be used together:
</dd>
</dl>

```tcl
integrator NewmarkWithSensitivity $gamma
        $beta
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">gamma</code></p></td>
<td><p>Newmark parameter gamma.</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">beta</code></p></td>
<td><p>Newmark parameter beta.</p></td>
</tr>
</tbody>
</table>

```tcl
sensitivityIntegrator -definedAbove
```
<dl>
<dt></dt>
<dd>
Currently, ‘-definedAbove’ is the only option available in OpenSees.
This means that the same integration scheme (i.e.,
</dd>
<dd>
‘NewmarkWithSensitivity’) is used to perform both response and response
sensitivity analysis.
</dd>
</dl>
<hr />
<dl>
<dt></dt>
<dd>
Reference:
</dd>
<dd>
Haukaas T., Der Kiureghian A. (2004). “Finite element reliability and
sensitivity methods for performance-based earthquake
</dd>
<dd>
engineering.” Report No. 2003/14, Pacific Earthquake Engineering
Research Center, April 2004.
</dd>
</dl>
<dl>
<dt></dt>
<dd>
Haukaas T., Der Kiureghian A. (2005). “Parameter sensitivity and
importance measures in nonlinear finite element reliability
</dd>
<dd>
analysis.” Journal of Engineering Mechanics (ASCE), 131(10):1013-1026.
</dd>
</dl>

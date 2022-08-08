# Drift

The Drift type records the displacement drift between two nodes. The
drift is taken as the ratio between the prescribed relative displacement
and the specified distance between the nodes. The command to create a
drift recorder is:

```tcl
recorder Drift < -file $fileName > < -xml $fileName > < -binary $fileName > 
  < -tcp $inetAddress $port > < -precision $nSD > < -time > 
  -iNode $inode1 $inode2 ... -jNode $jnode1 $jnode2 ... 
  -dof $dof1 $dof2 ... -perpDirn $perpDirn1 $perpDirn2...
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">fileName</code></p></td>
<td><p>name of file to which output is sent. Each line of the file
contains the result for a committed state of the domain file output is
either in xml format (-xml option), textual (-file option) or binary
(-binary option)</p></td>
</tr>
<tr class="even">
<td><p><strong>inetAddr</strong></p></td>
<td><p>ip address, "xx.xx.xx.xx", of remote machine to which data is
sent</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">port</code></p></td>
<td><p>port on remote machine awaiting tcp</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">nSD</code></p></td>
<td><p>number of significant digits (optional, default is 6)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-flag">-time</code></p></td>
<td><p>using this option places domain time in first entry of each data
line (optional, default: omitted)</p></td>
</tr>
<tr class="even">
<td><p><code>inode1 inode2 ...</code></p></td>
<td><p>tags of set of i nodes for which drift is being recorded</p></td>
</tr>
<tr class="odd">
<td><p><code>jnode1 jnode2 ...</code></p></td>
<td><p>tags of set of j nodes for which drift is being recorded</p></td>
</tr>
<tr class="even">
<td><p><code>dof1 dof2 ...</code></p></td>
<td><p>set of nodal degrees of freedom for which drift is being
recorded. Valid range is from 1 through <a href="Model_command"
title="wikilink">ndf</a> (the number of nodal degrees of
freedom).</p></td>
</tr>
<tr class="odd">
<td><p><code>perpDirn1 perpDirn2 ...</code></p></td>
<td><p>set of perpendicular global directions (`1`=$X$, `2`=$Y$, `3`=$Z$). This
input is needed to calculate the length between the nodes whose drift is
calculated.</p></td>
</tr>
</tbody>
</table>

<p>NOTES</p>

- Only one of `-file`, `-xml`, `-binary`, `-tcp` will be used. If multiple specified last option is used.
- `-tcp` option only available for version 2.2.1 and higher.
- Does not work in **OpenSeesSP**.


## Examples
```tcl
recorder Drift -file drift.out -time -iNode 1 2 -jNode 3 4 -dof 1 -perpDirn 2
```
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

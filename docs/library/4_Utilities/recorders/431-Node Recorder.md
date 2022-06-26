# Node

The Node recorder type records the response of a number of nodes at
every converged step. The command to create a node recorder is:

```tcl
recorder Node < -file $fileName > < -xml $fileName >
      < -binary $fileName > < -tcp $inetAddress $port > 
      < -precision $nSD > < -timeSeries $tsTag > < -time > < -dT $deltaT >
      < -closeOnWrite > < -node $node1 $node2 ... > 
      < -nodeRange $startNode $endNode > 
      < -region $regionTag > -dof ($dof1 $dof2 ...) $respType
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">fileName</code></p></td>
<td><p>name of file to which output is sent. file output is either in
xml format (`-xml` option), plain text (`-file` option) or binary (`-binary`
option).</p></td>
</tr>
<tr class="even">
<td><p><strong>inetAddr</strong></p></td>
<td><p>ip address, `xx.xx.xx.xx`, of remote machine to which data is
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
<td><p>optional, using this option places domain time in first entry of
each data line, default is to have time ommitted</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-flag">-closeOnWrite</code></p></td>
<td><p>optional. using this option will instruct the recorder to invoke
a close on the data handler after every timestep. If this is a file it
will close the file on every step and then re-open it for the next step.
Note, this greatly slows the execution time, but is useful if you need
to monitor the data during the analysis.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">deltaT</code></p></td>
<td><p>time interval for recording. will record when next step is
`deltaT` greater than last recorder step. (optional, default: records at
every time step)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">tsTag</code></p></td>
<td><p>the tag of a previously constructed TimeSeries, results from node
at each time step are added to load factor from series</p></td>
</tr>
<tr class="odd">
<td><p><strong>`node1` `node2` ..</strong></p></td>
<td><p>tags of nodes whose response is being recorded (optional,
default: omitted)</p></td>
</tr>
<tr class="even">
<td><p><strong>`startNode` `endNode` ..</strong></p></td>
<td><p>tag for start and end nodes whose response is being recorded
(optional, default: omitted)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">regionTag</code></p></td>
<td><p>a region tag; to specify all nodes in the previously defined
region. (optional)</p></td>
</tr>
<tr class="even">
<td><p><code>dof1 dof2 ...</code></p></td>
<td><p>the specified dof at the nodes whose response is
requested.</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">respType</code></p></td>
<td><p>a string indicating response required. Response types are given
in table below.</p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><strong>disp</strong></p></td>
<td><p>displacement\*</p></td>
</tr>
<tr class="even">
<td><p><strong>vel</strong></p></td>
<td><p>velocity\*</p></td>
</tr>
<tr class="odd">
<td><p><strong>accel</strong></p></td>
<td><p>acceleration\*</p></td>
</tr>
<tr class="even">
<td><p><strong>incrDisp</strong></p></td>
<td><p>incremental displacement</p></td>
</tr>
<tr class="odd">
<td><p><strong>"eigen i"</strong></p></td>
<td><p>eigenvector for mode i</p></td>
</tr>
<tr class="even">
<td><p><strong>reaction</strong></p></td>
<td><p>nodal reaction</p></td>
</tr>
<tr class="odd">
<td><p><strong>rayleighForces</strong></p></td>
<td><p>damping forces</p></td>
</tr>
</tbody>
</table>

<p>RETURNS</p>
<p><strong>&gt;0</strong> an integer tag that can be used as a handle on
the recorder for the <a href="Remove_Command" title="wikilink"> remove
recorder</a> commmand.</p>
<p><strong>-1</strong> recorder command failed if integer
<strong>-1</strong> returned.</p>

<p>NOTES</p>

<ul>
<li>Only one of `-file`, `-xml`, `-binary`, `-tcp` will be used. If multiple
  specified last option is used.</li>
<li>`-tcp` option only available for version 2.2.1 and higher.</li>
<li>In case you want to remove a recorder you need to know the tag for
  that recorder. Here is an example on how to get the tag of a
  recorder:</li>

      set tagRc [recorder Node -file nodesD.out -time -node 1 2 3 4 -dof 1 2 disp]

</ul>


<p>EXAMPLES</p>
- Generates output file `nodesD.out` that contains relative displacements
  in $x$ and $y$ direction at nodes 1, 2, 3, and 4. The output file will
  contain 9 columns (time, disp. in x at node 1, disp. in y at node 1, ...
  , disp. in y at node 4))
  ```tcl
  recorder Node -file nodesD.out -time -node 1 2 3 4 -dof 1 2 disp;
  ```

- For a `UniformExcitation` analysis, this command generates output file
  `nodesA.out` that contains absolute accelerations (ground motion
  acceleration + relative acceleration) in x direction for nodes 1, 2, 3,
  and 4. NOTE that if no `TimeSeries` is provided and a uniform excitation
  analysis is performed, the relative accelerations are recorded.
  ```tcl
  recorder Node -file nodesA.out -timeSeries 1 -time -node 1 2 3 4 -dof 1 accel;
  ```

<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>


# Node Envelope Recorder

<p>The EnvelopeNode recorder type records the min, max and absolute max
of a number of nodal response quantaties. The command to create a node
envelope recorder is:</p>

```tcl
recorder EnvelopeNode < -file $fileName > < -xml $fileName > < -precision $nSD > 
  < -time > < -closeOnWrite > < -timeSeries $tsTag > < -node $node1 $node2 ... > 
  < -nodeRange $startNode $endNode > < -region $regionTag > -dof ($dof1 $dof2 ...) 
  $respType
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">fileName</code></p></td>
<td><p>name of file to which output is sent. file output is either in
xml format (-xml option), textual (-file option) or binary (-binary
option)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">nSD</code></p></td>
<td><p>number of significant digits (optional, default is 6)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-flag">-time</code></p></td>
<td><p>(optional using this option places domain time in first entry of
each data line, default is to have time ommitted)</p></td>
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
<td><p><code class="parameter-table-variable">tsTag</code></p></td>
<td><p>the tag of a previously constructed TimeSeries, results from node
at each time step are added to load factor from series</p></td>
</tr>
<tr class="even">
<td><p><code>node1 node2 ..</code></p></td>
<td><p>tags of nodes whose response is being recorded (optional,
default: omitted)</p></td>
</tr>
<tr class="odd">
<td><p><code>startNode endNode ..</code></p></td>
<td><p>tag for start and end nodes whose response is being recorded
(optional, default: omitted)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">regionTag</code></p></td>
<td><p>a region tag; to specify all nodes in the previously defined
region. (optional)</p></td>
</tr>
<tr class="odd">
<td><p><code>dof1 dof2 ...</code></p></td>
<td><p>the specified dof at the nodes whose response is
requested.</p></td>
</tr>
<tr class="even">
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
<td><p>displacement*</p></td>
</tr>
<tr class="even">
<td><p><strong>vel</strong></p></td>
<td><p>velocity*</p></td>
</tr>
<tr class="odd">
<td><p><strong>accel</strong></p></td>
<td><p>acceleration*</p></td>
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
</tbody>
</table>
<p>RETURNS</p>
<p><strong>&gt;0</strong> an integer tag that can be used as a handle on
the recorder for the <a href="Remove_Command" title="wikilink"> remove
recorder</a> commmand.</p>
<p><strong>-1</strong> recorder command failed if integer
<strong>-1</strong> returned.</p>

## Examples

```tcl
recorder EnvelopeNode -file nodesD.out -time -node 1 2 3 4 -dof 1 2 disp
recorder EnvelopeNode -file nodesA.out -time -timeSeries 1 -node 1 2 3 4 -dof 1 accel
```

<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

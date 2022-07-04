# ElementEnvelopeRecorder

The Envelope Element recorder type records the response of a number
of elements at every converged step. The response recorded is
element-dependent and also depends on the arguments which are passed to
the setResponse() element method. When the object is terminated, through
the use of a <a href="wipe_Command" title="wikilink"> wipe</a>, <a
href="exit_Command" title="wikilink"> exit</a>, or <a
href="remove_Command" title="wikilink"> remove</a> the object will
output the min, max and absolute max values on 3 seperate lines of the
output file for each quantity.

```tcl
recorder EnvelopeElement < -file $fileName > < -xml $fileName > < -binary $fileName > 
  < -precision $nSD > < -time > < -closeOnWrite > < -ele ($ele1 $ele2 ...) >
  < -eleRange $startEle $endEle > < -region $regTag > $arg1 $arg2
  ...
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
<td><p><code>ele1 ele2 ..</code></p></td>
<td><p>tags of elements whose response is being recorded -- selected
elements in domain (optional, default: omitted)</p></td>
</tr>
<tr class="even">
<td><p><code>startEle endEle ..</code></p></td>
<td><p>tag for start and end elements whose response is being recorded
-- range of selected elements in domain (optional, default:
omitted)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">regTag</code></p></td>
<td><p>previously-defined tag of region of elements whose response is
being recorded -- region of elements in domain (optional)</p></td>
</tr>
<tr class="even">
<td><p><code>arg1 arg2 ...</code></p></td>
<td><p>arguments which are passed to the setResponse() element
method</p></td>
</tr>
</tbody>
</table>
<p>RETURNS</p>
<p><strong>&gt;0</strong> an integer tag that can be used as a handle on
the recorder for the <a href="Remove_Command" title="wikilink"> remove
recorder</a> commmand.</p>
<p><strong>-1</strong> recorder command failed if integer
<strong>-1</strong> returned.</p>
<p>NOTE:</p>
<p>The setResponse() element method is dependent on the element type,
and is described with the <a href="Element_Command"
title="wikilink">Element Command</a>.</p>
<p>EXAMPLE</p>

## Examples

```tcl
recorder Element -file Element1.out -time -ele 1 3 section 1 fiber 0.10 0.10 stressStrain
```

<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

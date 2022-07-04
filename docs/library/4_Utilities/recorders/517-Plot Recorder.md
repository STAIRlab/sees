# Plot Recorder

This recorder type opens a graphical window for the plotting of the
contents of the prescribed file. The prescribed file can be the output
of an other recorder.

```tcl
recorder plot $fileName $windowTitle $xLoc $yLoc $xPixels
        $yPixels -columns $xCol0 $yCol0 &lt;-columns $xCol1 $yCol1&gt;
        ...
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><p><code class="parameter-table-variable">fileName</code></p></td>
<td><p>name of file from which data will be read</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">windowTitle</code></p></td>
<td><p>title of window to be opened</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">xLoc yLoc</code></p></td>
<td><p>`xLoc`, `yLoc` specifies location on screen of top left corner of
window</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">xPixels yPixels</code></p></td>
<td><p>`xPixels`, `yPixels` specifies width and height in pixels of window
to open</p></td>
</tr>
<tr class="odd">
<td><p><strong>xCol yCol ...</strong></p></td>
<td><p>integers specifying which columns to plot for $x$ and $y$ axis.</p></td>
</tr>
</tbody>
</table>

<p>NOTES</p>
<ul>
<li>At least one set of columns must be specified, additional ones may
be specified.</li>
<li>the only way to save the image is a screen capture.</li>
</ul>

<hr />

## Examples
```tcl
recorder Plot node.out "Nodal Displacement" 10 10 400 400 -columns 1 2
```
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>

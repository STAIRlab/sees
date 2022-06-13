# Numberer Command

<p>This command is used to construct the DOF_Numberer object. The
DOF_Numberer object determines the mapping between equation numbers and
degrees-of-freedom -- how degrees-of-freedom are numbered.</p>

```tcl
numberer numbererType? arg1? ...
```
<hr />
<p>The type of DOF_Numberer created and the additional arguments
required depends on the <strong>numbererType?</strong> provided in the
command.</p>
<p>The following contain information about numbererType? and the args
required for each of the available dof numberer types:</p>
<ol>
<li><a href="Plain_Numberer" title="wikilink">Plain Numberer</a></li>
<li><a href="RCM_Numberer" title="wikilink"> Reverse Cuthill-McKee
Numberer</a></li>
<li><a href="AMD_Numberer" title="wikilink"> Alternative_Minimum_Degree
Numberer</a></li>
</ol>

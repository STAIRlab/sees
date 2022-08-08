# Load Patterns

The `opensees.pattern` module (or `pattern` Tcl command) is used to construct 
a `LoadPattern`. Each `LoadPattern` in OpenSees has a <a
href="Time_Series_Command" title="wikilink"> TimeSeries</a> associated
with it. In addition it may contain `ElementLoads`, `NodalLoads` and
`SinglePointConstraints`. Some of these `SinglePoint` constraints may be
associated with `GroundMotions`.


The Tcl command has the following form:

```tcl
pattern patternType? arg1? ...
```

<hr />

<p>The type of pattern created and the additional arguments required
depends on the <strong>patternType?</strong> provided in the command.
The following contain information about patternType? and the additional
args required for each of the available pattern types:</p>
<ol>
<li><a href="Plain_Pattern" title="wikilink">Plain Pattern</a></li>
<li><a href="Uniform_Excitation_Pattern" title="wikilink">Uniform
Excitation Pattern</a></li>
<li><a href="Multi-Support_Excitation_Pattern"
title="wikilink">Multi-Support Excitation Pattern</a></li>
<li><a href="DRM_Load_Pattern" title="wikilink">DRM Load
Pattern</a></li>
</ol>

:::{apidoc="opensees.pattern.TimeSeries"}
:::


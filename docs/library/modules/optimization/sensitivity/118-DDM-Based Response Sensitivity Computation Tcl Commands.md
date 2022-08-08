# DDM-Based Response Sensitivity Computation Tcl Commands:

<p>Created by: <span style="color:blue"> <a href="Quan_Gu"
title="wikilink">Quan Gu</a> (Xiamen University, China), <a
href="Joel_P._Conte" title="wikilink">Joel P. Conte</a> (UCSD), Michele
Barbato (LSU), Yong Li (UCSD)</span></p>
<hr />
<p><a href="Sensitivity_Analysis" title="wikilink"> Return to
Sensitivity Analysis User Page</a></p>
<hr />
<p>&lt;!-- INTRODUCTION --&gt; <h1>Introduction</h1> The
following Analysis commands are added to the interpreter to create the
Analysis and perform the analysis:</p>
<p>&lt;!-- General commands --&gt; <h1>General
Commands</h1></p>
<p>::; <h3><a href="reliability_Command"
title="wikilink">reliability Command</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
This command creates the reliability domain in which the sensitivity,
reliability and optimization components are kept. This reliability
domain is parallel to the finite element (FE) domain in OpenSees.
Currently, the commands for stand-alone sensitivity analysis (e.g.,
sensitivityIntegrator, sensitivityAlgorithm) are set in the reliability
domain only and, thus, the ‘reliability’ command must be used before any
stand-alone sensitivity analysis.
</dd>
</dl>
</dd>
</dl>
<p>::; <h3><a href="parameter_Command" title="wikilink">parameter
Command</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
In DDM-based FE response sensitivity analysis, the sensitivity
parameters can be material, geometry or discrete loading parameters.
</dd>
</dl>
</dd>
</dl>
<p>::; <h3><a href="addToParameter_Command"
title="wikilink">addToParameter Command</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
In case that more objects (e.g., element, section) are mapped to an
existing parameter, the following command can be used to relate these
additional objects to the specific parameter.
</dd>
</dl>
</dd>
</dl>
<p>::; <h3><a href="updateParameter_Command"
title="wikilink">updateParameter Command</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
Once the parameters in FE model are defined, their value can be updated.
</dd>
</dl>
</dd>
</dl>
<p>::; <h3><a href="sensitivityIntegrator_Command"
title="wikilink">sensitivityIntegrator Command</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
Define the sensitivity integrator.
</dd>
</dl>
</dd>
</dl>
<p>::; <h3><a href="sensitivityAlgorithm_Command"
title="wikilink">sensitivityAlgorithm Command</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
Define the sensitivity algorithm.
</dd>
</dl>
</dd>
</dl>
<p>::; <h3><a href="recorder_Commands" title="wikilink">recorder
Commands</a></h3></p>
<dl>
<dt></dt>
<dd>
<dl>
<dt></dt>
<dd>
To record the nodal response and response sensitivity.
</dd>
</dl>
</dd>
</dl>

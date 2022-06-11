# Constraints commands

<p>In OpenSees there are two types of constraints:</p>
<ol>
<li><strong>Single Point constraints</strong> which prescribe the
movement (typically 0) of a single dof at a node. There are a number of
commands for defining single-point coonstraints:
<ul>
<li><a href="fix_command" title="wikilink"> fix</a></li>
<li><a href="fixX_command" title="wikilink"> fixX</a></li>
<li><a href="fixY_command" title="wikilink"> fixY</a></li>
<li><a href="fixZ_command" title="wikilink"> fixZ</a></li>
</ul></li>
<li><strong>Multi-Point constraints</strong> which prescribe that the
movement of certain dof at one node are defined by the movement of
certain dof at another node. There again are a number of commands for
defining multi-point constraints.
<ul>
<li><a href="equalDOF_command" title="wikilink"> equalDOF</a></li>
<li><a href="rigidDiaphragm_command" title="wikilink">
rigidDiaphragm</a></li>
<li><a href="rigidLink_command" title="wikilink"> rigidLink</a></li>
</ul></li>
</ol>

# System Command

<p>This command is used to construct the LinearSOE and LinearSolver
objects to store and solve the system of equations in the analysis.</p>

```tcl
system systemType? arg1? ...
```
<hr />
<p>The type of LinearSOE created and the additional arguments required
depends on the <strong>systemType?</strong> provided in the command.</p>
<p>The following contain information about systemType? and the args
required for each of the available aystem types:</p>
<ol>
<li><a href="BandGeneral_SOE" title="wikilink">BandGeneral SOE</a></li>
<li><a href="BandSPD_SOE" title="wikilink">BandSPD SOE</a></li>
<li><a href="ProfileSPD_SOE" title="wikilink">ProfileSPD SOE</a></li>
<li><a href="SuperLU_SOE" title="wikilink">SuperLU SOE</a></li>
<li><a href="UmfPack_SOE" title="wikilink">UmfPack SOE</a></li>
<li><a href="FullGeneral" title="wikilink">FullGeneral</a></li>
<li><a href="SparseSYM_SOE" title="wikilink">SparseSYM SOE</a></li>
<li><a href="Mumps" title="wikilink">Mumps</a></li>
<li><a href="Cusp" title="wikilink">Cusp</a></li>
</ol>

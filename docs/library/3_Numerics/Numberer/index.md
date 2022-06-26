# DOF Numberers
The numbering of the degrees of freedom in the domain is done by the following methods

- [Plain]() -- Uses the numbering provided by the user
- [RCM](RCM) (Reverse Cuthill-McKee numberer) -- Renumber DOFs to minimize the matrix band-width using the Reverse Cuthill-McKee algorithm
- <a href="AMD_Numberer" title="wikilink">AMD</a> Alternative minimum degree


<hr />

The `numberer` Tcl command is used to construct the `DOF_Numberer` object. The
`DOF_Numberer` object determines the mapping between equation numbers and
degrees-of-freedom -- how degrees-of-freedom are numbered.

```tcl
numberer numbererType? arg1? ...
```

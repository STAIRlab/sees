# Add A New Material

<p>The OpenSees applications allows developers to use their own material
modules to the application. Unlike most other programs, the materials
are added at run-time and not at compile time. The advantage of this is
the the developers:</p>
<ol>
<li>Do not need the OpenSees source files or libraries to compile and
link the application.</li>
<li>Can share their modules with others without having to provide the
source code.</li>
</ol>

```plantuml
Material <|-- UniaxialMaterial 
Material <|-- SectionForceDeformation 
Material <|-- NDMaterial
```

<p>The material modules can be written using either C++, C, or Fortran.
Whatever the language the developer wishes to use, the material modules
make use of the <a href="OpenSees_API" title="wikilink">OpenSees
API</a>.</p>
<ol>
<li><a href="Add_a_New_UniaxialMaterial_C++" title="wikilink">Add a New UniaxialMaterial C++</a></li>
<li><a href="Add_a_New_UniaxialMaterial_C" title="wikilink">Add a New UniaxialMaterial C</a></li>
<li><a href="Add_a_New_UniaxialMaterial_Fortran" title="wikilink">Add a New UniaxialMaterial Fortran</a></li>
<li><a href="Add_a_New_nDMaterial_C++" title="wikilink">Add a New nDMaterial C++</a></li>
<li><a href="Add_a_New_nDMaterial_C" title="wikilink">Add a New nDMaterial C</a></li>
<li><a href="Add_a_New_ndMaterial_Fortran" title="wikilink">Add a New ndMaterial Fortran</a></li>
</ol>

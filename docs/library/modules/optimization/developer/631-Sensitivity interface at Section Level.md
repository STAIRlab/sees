# Sensitivity interface at Section Level

<p><a
href="Extension_of_an_existing_material,cross_section,_and_element_for_DDM-based:"
title="wikilink">Return to Extension of an existing material,cross
section, and element for DDM-based:</a></p>
<hr />

The following functions need to be implemented in each section for
sensitivity computation:

```tcl
int setParameter(const char **argv, int argc, Parameter &param);
```

```tcl
int updateParameter (int parameterID, Information &info);
```

```tcl
int activateParameter(int passedParameterID);
```

```tcl
const Vector& getStressResultantSensitivity(int gradIndex, bool conditional);
```

```tcl
const Vector& getSectionDeformationSensitivity(int gradIndex);
```

```tcl
const Matrix& getInitialTangentSensitivity(int gradIndex);
```

```tcl
int commitSensitivity(const Vector& sectionDeformationGradient,int gradIndex, int numGrads);
```

</dl>

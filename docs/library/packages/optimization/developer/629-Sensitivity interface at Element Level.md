# Sensitivity interface at Element Level

The following functions need to be implemented in each element for
sensitivity computation:

<p><a
href="Extension_of_an_existing_material,cross_section,_and_element_for_DDM-based:"
title="wikilink">Return to Extension of an existing material,cross section, and element for DDM-based:</a></p>
<hr />

```cpp
int setParameter(const char **argv, int argc, Parameter &amp;param);
```

```cpp
int updateParameter (int parameterID, Information &amp;info);
```

```cpp
int activateParameter(int passedParameterID);
```

```cpp
const Vector &amp; getResistingForceSensitivity(int gradIndex);
```

```cpp
int commitSensitivity(int gradIndex, int numGrads);
```

```cpp
const Matrix &amp; getInitialStiffSensitivity(int gradIndex);
```

```cpp
const Matrix &amp; getDampSensitivity(int gradIndex);
```

```cpp
const Matrix &amp; getMassSensitivity(int gradIndex);
```


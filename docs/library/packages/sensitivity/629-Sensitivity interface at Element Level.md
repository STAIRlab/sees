# Sensitivity interface at Element Level

<p>The following functions need to be implemented in each element for
sensitivity computation:</p>
<p><a
href="Extension_of_an_existing_material,cross_section,_and_element_for_DDM-based:"
title="wikilink">Return to Extension of an existing material,cross
section, and element for DDM-based:</a></p>
<hr />
<dl>
<dt></dt>
<dd>
int setParameter(const char **argv, int argc, Parameter &amp;param);
</dd>
<dd>
int updateParameter (int parameterID, Information &amp;info);
</dd>
<dd>
int activateParameter(int passedParameterID);
</dd>
<dd>
const Vector &amp; getResistingForceSensitivity(int gradIndex);
</dd>
<dd>
int commitSensitivity(int gradIndex, int numGrads);
</dd>
<dd>
const Matrix &amp; getInitialStiffSensitivity(int gradIndex);
</dd>
<dd>
const Matrix &amp; getDampSensitivity(int gradIndex);
</dd>
<dd>
const Matrix &amp; getMassSensitivity(int gradIndex);
</dd>
</dl>

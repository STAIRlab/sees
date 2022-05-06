# GettingStartedInputFile.tcl -- Element Section

<p>__NOTOC__ <img src="/OpenSeesRT/contrib/static/BuildingTclLogo.gif" title="BuildingTclLogo.gif"
alt="BuildingTclLogo.gif" /> 
```Tcl
</p>
<ol>
<li>ELEMENT SECTION ---------------------------------------</li>
</ol>
<p>addSectionData SectionLabel 30x30RCRectangularFiber addSectionData
SectionDescription "Square Rectangular RC Section" addSectionData
SectionModelLabel RCRectangularFiber; addSectionData H 30*\$in;
addSectionData B 30*\$in; addSectionData NBarBot 6; # number of bottom
longitudinal reinforcing bars in section addSectionData NBarTop 6; #
number of top longitudinal reinforcing bars in section addSectionData
NBarInt 6; # total number of intermediate bars in section (2 bars per
layer) addSectionData BarSizeBot #9; addSectionData BarSizeTop #9;
addSectionData BarSizeInt #9; addSectionData CoverBot 2.6*\$in;
addSectionData CoverTop 2.6*\$in; addSectionData CoverInt 2.6*\$in;
addSectionData CoreMaterialLabel 4ksiConfinedConcrete; addSectionData
CoverMaterialLabel 4ksiUnconfinedConcrete; addSectionData
ReinfMaterialLabel 60ksiReinforcingSteel; addSection</p>
<p>addSectionData SectionLabel 30x60RCRectangularFiber addSectionData
SectionDescription "Rectangular RC Section" addSectionData
SectionModelLabel RCRectangularFiber; addSectionData H 60*\$in;
addSectionData B 30*\$in; addSectionData NBarBot 6; # number of bottom
longitudinal reinforcing bars in section addSectionData NBarTop 4; #
number of top longitudinal reinforcing bars in section addSectionData
NBarInt 6; # total number of intermediate bars in section (2 bars per
layer) addSectionData BarSizeBot #9; addSectionData BarSizeTop #11;
addSectionData BarSizeInt #6; addSectionData CoverBot 2.6*\$in;
addSectionData CoverTop 2.6*\$in; addSectionData CoverInt 2.6*\$in;
addSectionData CoreMaterialLabel 4ksiConfinedConcrete; addSectionData
CoverMaterialLabel 4ksiUnconfinedConcrete; addSectionData
ReinfMaterialLabel 60ksiReinforcingSteel; addSection</p>
<p>puts --DoneSections--</p>
<p>
```
</p>
<hr />
<p>Return to <a href="Getting_Started_with_BuildingTcl"
title="wikilink">Getting Started with BuildingTcl</a></p>

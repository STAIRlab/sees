# Sensitivity Analysis

<p>Created by: <span style="color:blue"> <a href="Quan_Gu"
title="wikilink">Quan Gu</a> (Xiamen University, China), <a
href="Joel_P._Conte" title="wikilink">Joel P. Conte</a> (UCSD), Michele
Barbato (LSU), Yong Li (UCSD)</span></p>
<hr />
<p>This manual is intended to outline the basic commands currently
available within the OpenSees interpreter for performing DDM
(<strong>Direct Differentiation Method</strong>)-based response
sensitivity analysis. This interpreter is an extension of the Tcl/Tk
language for use with OpenSees. The existing Tcl commands for Finite
Element response-only computation are described in the OpenSees user’s
guide available online at <a
href="http://opensees.berkeley.edu">http://opensees.berkeley.edu</a>
and, thus, are not repeated in this document. The notation used herein
is the same as that used in the Tcl commands manual for response-only
computation. Only new Tcl commands for DDM-based response sensitivity
computation are presented and explained in detail.</p>
<p>This manual is subdivided as follows:</p>
<ol>
<li><a href="DDM-Based_Response_Sensitivity_Computation_Tcl_Commands:"
title="wikilink">DDM-Based Response Sensitivity Computation Tcl
Commands:</a> commands added to the interpreter for response sensitivity
computation.</li>
<li><a href="Demonstration_Examples:" title="wikilink">Demonstration
Examples:</a> five demonstration examples used to illustrate and
validate the DDM-based response sensitivity analysis components
implemented in OpenSees.</li>
<li><a
href="Extension_of_an_existing_material,cross_section,_and_element_for_DDM-based:"
title="wikilink">Extension of an existing material,cross section, and
element for DDM-based:</a> the necessary functions needed for
implementation of the DDM-based response sensitivity computation are
listed and explained.</li>
<li><a href="Tcl_input_files_for_the_provided_application_examples:"
title="wikilink">Tcl input files for the provided application
examples:</a> Tcl input files for the above five application
examples.</li>
</ol>
<hr />

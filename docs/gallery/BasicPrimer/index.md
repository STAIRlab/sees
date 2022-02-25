

<!--
---
template: card_index.html
...
-->

# The OpenSees Examples Primer

<center><b>
Version 1.2

August 20, 2001

Frank McKenna and Michael Scott

Pacific Earthquake Engineering Research Center University of California, Berkeley
</b></center>

## Introduction

To conduct a simulation, the user creates various objects
which serve either of three main purposes:

1.  **Modeling**: The user first creates a ModelBuilder object which
    defines the type of model, and commands available for building the
    model. With a ModelBuilder defined, the user then creates the
    Element, Node, LoadPattern and Constraint objects that define the
    model. In this primer, the use of a basic ModelBuilder will be
    demonstrated.

2.  **Analysis**: After defined the model, the next step is to create
    the Analysis object for analyzing the model. This may be a simple
    static linear analysis or a transient non-linear analysis. In
    OpenSees, an Analysis object is composed of several component
    objects, which define how the analysis is performed. The component
    objects consist of the following: SolutionAlgorithm, Integrator,
    ConstraintHandler, DOF_Numberer, SystemOfEqn, Solver, and
    AnalysisModel. This approach provides a great deal of flexibility in
    how an analysis is conducted.

3.  **Post-processing**: Once the model and analysis have been
    defined, the user has the option of specifying what is to be
    monitored during the analysis. This, for example, could be the
    displacement history at a node or internal state of an element in a
    transient analysis or the entire state of the model at each step in
    the solution procedure. Several Recorder objects are created to
    store what the user wants to examine.

In the examples, Tcl scripts are used to create a model, analysis, and
output specification. The examples are (1) simple truss structure, (2)
reinforced concrete portal frame, (3) two-story multi-bay reinforced
concrete frame, and (4) a three-dimensional frame. The examples are not
meant to be completely realistic, but they are representative of typical
structures. The analyses performed on these models consist of simple
static analysis, pushover analysis and transient analysis. An example of
moment-curvature analysis is also performed on a reinforced concrete
section.

<div class="row">
<div class="d-flex col-lg-6 col-md-6 col-sm-6 col-xs-12 docutils"><div class="card w-100 shadow comparison-card text-center comparison-card-excel docutils"><img alt="img-top" class="card-img-top" 
  src="./fig_files/Example3.svg"><div class="card-body docutils"><p class="card-text">
   ...or other spreadsheet programs will find that many of the concepts are
   transferrable to pandas.
</p></div><div class="card-footer docutils"><p class="card-text"><a class="sphinx-bs btn text-wrap btn-secondary stretched-link reference internal" href="comparison/comparison_with_spreadsheets.html#compare-with-spreadsheets"><span class="std std-ref">Learn more</span></a></p></div></div></div>

<div class="d-flex col-lg-6 col-md-6 col-sm-6 col-xs-12 docutils"><div class="card w-100 shadow comparison-card text-center comparison-card-excel docutils"><img alt="img-top" class="card-img-top" 
  src="./fig_files/Example5.svg"><div class="card-body docutils"><p class="card-text">
   ...or other spreadsheet programs will find that many of the concepts are
   transferrable to pandas.
</p></div><div class="card-footer docutils"><p class="card-text"><a class="sphinx-bs btn text-wrap btn-secondary stretched-link reference internal" href="comparison/comparison_with_spreadsheets.html#compare-with-spreadsheets"><span class="std std-ref">Learn more</span></a></p></div></div></div>
</div>


<style>
.d-flex {
    display: flex !important;
}
.comparison-card {
    background: #FFF;
    border-radius: 0;
    padding: 30px 10px 10px 10px;
    margin: 10px 0px;
}
.text-center {
    text-align: center !important;
}
.w-100 {
    width: 100% !important;
}
.shadow {
    box-shadow: 0 .5rem 1rem rgba(0,0,0,.15) !important;
}
.card {
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #fff;
    background-clip: border-box;
    border: 1px solid rgba(0,0,0,.125);
    border-radius: .25rem;
}
</style>


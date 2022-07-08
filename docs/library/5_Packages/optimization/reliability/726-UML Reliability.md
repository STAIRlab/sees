# UML Reliability

<hr />

<p>Reliability</p>

```plantuml
package "OpenSees" #DDDDDD {
Domain -- Analysis 
Domain -- Recorder 
ModelBuilder -- Domain 
}

package "Reliability" #CCCCCC {
ReliabilityDomain -- ReliabilityAnalysis
ReliabilityAnalysis <|-- FORMAnalysis 
ReliabilityAnalysis <|-- SORMAnalysis 
ReliabilityAnalysis <|-- SORMAnalysis
ReliabilityAnalysis <|-- FOSMAnalysis 
ReliabilityAnalysis <|-- OutCrossingAnalysis 
ReliabilityAnalysis <|-- SamplingAnalysis
ReliabilityAnalysis <|-- SystemAnalysis 
}
```

<hr />

<p>Reliability Domain</p>

```plantuml
ReliabilityDomain o-- RandomVariable 
ReliabilityDomain o-- RandomVariablePositioner 
ReliabilityDomain o-- CorrelationCoefficient
ReliabilityDomain o-- PerformanceFunction 
ReliabilityDomain o-- Filter
ReliabilityDomain o-- ModulatingFunction 
ReliabilityDomain o-- Spectrum
```

<hr />

<p>Reliability Analysis</p>

```plantuml
ReliabilityAnalysis o-- FindDesignPoint
ReliabilityAnalysis o-- SearchDirection 
ReliabilityAnalysis o-- StepSizeRule 
ReliabilityAnalysis o-- FindCurvatures 
ReliabilityAnalysis o-- FunctionEvaluator 
ReliabilityAnalysis o-- RandomNuberGenerator
ReliabilityAnalysis o-- GradGEvaluator 
ReliabilityAnalysis o-- ProbabilityTransformation 
ReliabilityAnalysis o-- MeritFunctionCheck
ReliabilityAnalysis o- ConvergenceCheck 
```


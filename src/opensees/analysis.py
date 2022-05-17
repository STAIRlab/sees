from . import tcl

class Analysis:
    def __init__(self, model, strategy, patterns):
        if not hasattr(model, "_rt") or model._rt is None:
            from . import tcl
            self.rt = tcl.TclRuntime()
            self.rt.model(model)
        else:
            self.rt = model

        # Currently, all analysis constructors take the `strategy`
        # argument as a C++ std::vector<std::string>, so
        # parameters must be cast as strings.
        self._strategy = {
            k: [str(i) for i in v]
            for k,v in strategy.items()
        }

        self.patterns = patterns
        if patterns is not None:
            for pattern in patterns.values():
                self.rt.eval(tcl.dumps(pattern))

    def system(self, *args): pass

    def integrator(self, *args): pass

    def handler(self, *args): pass

    def analyze(self, *args, **kwds):
        self._analysis.analyze(*args)



class StaticAnalysis(Analysis):
    def __init__(self, model, strategy=None, patterns=None):
        if strategy is None:
            strategy = {
                "algorithm": ["Newton"],
                "integrator": ["LoadControl"]
            }
        super().__init__(model, strategy=strategy, patterns=patterns)

        # Import C++ bindings and create an instance of the analysis
        from . import libOpenSeesRT
        self._analysis = libOpenSeesRT._StaticAnalysis(self.rt._rt, self._strategy)





class DirectIntegrationAnalysis(Analysis):
    """
    DirectIntegrationAnalysis(patterns=[
        pattern.MultipleSupport(
            components = [
            #   node, dof,  history
                ( 1,   1,   pattern.ResponseComponent(accel, displ, veloc)),
                ( 2,   1,   pattern.ResponseComponent(accel, displ, veloc))
            ]
        ),

        pattern.UniformAcceleration([
        #    dof   history
            ( 1,   pattern.ResponseComponent(accel, displ, veloc))
          ]
        )

    ])
    """

    def __init__(self,
        model,
        strategy:  dict,
        patterns:  dict = None,
        recorders: list = None,
        inherit:   str  = None,
        gravity:   dict = None
    ):
        super().__init__(model, strategy=strategy, patterns=patterns)
        # Import C++ bindings and create an instance of the analysis
        from . import libOpenSeesRT
        self._analysis = libOpenSeesRT._DirectIntegrationAnalysis(self.rt._rt, self._strategy)


def eigen(model, num):
    pass

def modes(model, num):
    pass


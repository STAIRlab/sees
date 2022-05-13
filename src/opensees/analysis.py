from opensees.ast import Num


def eigen(model, num):
    pass

def modes(model, num):
    pass

class Analysis:
    def __init__(self, model, strategy, patterns):
        if not hasattr(model, "_rt") or model._rt is None:
            from . import tcl
            self._rt = tcl.TclRuntime()
        else:
            self._rt = model._rt
        from . import libOpenSeesRT

        strategy = {
                k: [str(i) for i in v]
                for k,v in strategy.items()
        }

        self._analysis = libOpenSeesRT._StaticAnalysis(self._rt, strategy)

        self.patterns = patterns

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
        patterns:  dict,
        strategy:  dict,
        recorders: list,
        inherit:   str  = None,
        gravity:   dict = None
    ):
        super().__init__(self, model, strategy=strategy, patterns=patterns)






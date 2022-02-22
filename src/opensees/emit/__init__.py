from .opensees import OpenSeesWriter
from .writer import ModelWriter
from .fedeas import FEDEAS_Writer

class JSON(ModelWriter):
    def dump(self):
        import json

        out = {
            "StructuralAnalysisModel":{
                "properties": {"crdTransformations": [
                    
                ]},
                "geometry": {
                    "nodes": [
                        {**n, "crd": [float(i) for i in n.crd]} for n in self.model.nodes
                    ],
                    "elements": [
                    ]
                }
            }
        }
        return json.dumps(out, indent=2)

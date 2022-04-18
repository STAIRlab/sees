from .writer import ModelWriter

class OpenSeesWriter(ModelWriter):
    def __init__(self, model=None):
        if hasattr(model,"apply"):
            model = model.apply({})
        self.model = model
        self.comment_char = "#"

    def dump_initialize(self, definitions={}):
        cmds = "# Parameters\n" + "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n\n"
        ndm, ndf = self.model.ndm, self.model.ndf
        dof_keys = "dx dy dz rx ry rz"
        dofs = " ".join( str(i) for i in range(1, ndf + 1))
        cmds += f"# Create ModelBuilder (with {ndm} dimensions and {ndf} DOF/node)\n"
        cmds += f"model BasicBuilder -ndm {ndm} -ndf {ndf}\n"
        cmds += f"lassign {{{dofs}}} {dof_keys}"
        return cmds

    def dump_elements(self, *elems, definitions={}):
        transforms = set()
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        for i, el in enumerate(elems):
            #el.init()
            if el.name is None:
                el.name = i+1
            try:
                cmds += "\nelement " + " ".join(str(p) for p in el.ops_elem.serialize(tag=i))
            except:
                cmds += "\n" + " ".join(el.get_cmd_str()) + "\n"

            if hasattr(el, "_transform") and el._transform:
                transforms.update({el._transform})

        return "".join(" ".join(t.get_cmd_str()) + "\n" for t in transforms) + cmds

    @classmethod 
    def dump_sections(self, *sections, definitions={}):
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        for sect in sections:
            cmds += " ".join(sect.get_cmd_str()) + "\n"
        return cmds
    
    def dump_materials(self, *materials, definitions={}):
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        all_materials = self.model.materials
        for i,mat in enumerate(all_materials):
            if mat.name is None:
                mat.name = i+1
            try:
                cmds += " ".join(mat.get_cmd_str()) + "\n"
            except:
                try:
                    cmds += "\nuniaxialMaterial " + " ".join(str(p) for p in mat.serialize(tag=i))
                except:
                    pass
        return cmds

    def dump_constraints(self, definitions={}):
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        for n in self.model.nodes:
            if 'boun' in n.kwds and any(n.kwds["boun"]):
                cmds += f"fix {n.name} {' '.join(str(i) for i in n.kwds['boun'])}\n"

        #model = self.model
        #for n in model.nodes:
        #    if any(n.constraints):
        #        cmds += f"fix {n.tag} {' '.join(str(i) for i in n.constraints)}\n"

        #if hasattr(model, "links"):
        #    for link in model.links:
        #        cmds += f"rigidLink {link['type']} {' '.join(str(n.tag) for n in link['nodes'])}\n"
        return cmds

    def dump_connectivity(self, definitions={}):
        cmds = "\n".join(f"set {k} {v};" for k,v in definitions.items()) + "\n"
        for i,nd in enumerate(self.model.nodes):
            nd.name = i
            cmds +=  " ".join(nd.get_cmd_str()) + "\n"
        cmds += self.dump_elements(*self.model.elems)
        return cmds



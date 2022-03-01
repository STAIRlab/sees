APIDOC = python3 tools/doc.py
APIDIR = docs/api/

apidocs:
	$(APIDOC) opensees.section > $(APIDIR)/modeling/section.md
	$(APIDOC) opensees.patch > $(APIDIR)/modeling/patch.md
	$(APIDOC) opensees.patch --attr layer > $(APIDIR)/modeling/layer.md
	$(APIDOC) opensees.lib > $(APIDIR)/core.md
	$(APIDOC) opensees.lib --attr uniaxial > $(APIDIR)/modeling/uniaxial.md
	$(APIDOC) opensees.lib --attr element > $(APIDIR)/modeling/element.md
	$(APIDOC) opensees.lib --attr constraint > $(APIDIR)/modeling/constraint.md


.PHONY: docs

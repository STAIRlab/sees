APIDOC = python3 tools/doc.py
APIDIR = docs/api/

apidocs:
	$(APIDOC) opensees.section > $(APIDIR)/section.md
	$(APIDOC) opensees.patch > $(APIDIR)/patch.md
	$(APIDOC) opensees.patch --attr layer > $(APIDIR)/layer.md
	$(APIDOC) opensees.lib > $(APIDIR)/core.md
	$(APIDOC) opensees.lib --attr uniaxial > $(APIDIR)/uniaxial.md
	$(APIDOC) opensees.lib --attr element > $(APIDIR)/element.md
	$(APIDOC) opensees.lib --attr constraint > $(APIDIR)/constraint.md


.PHONY: docs

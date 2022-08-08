section  = CrossSection(A=..., J=..., ixc=..., iyc=...)
material = Elastic(E=..., G=...)
geometry = ["Linear", [0, 1, 0]]
integration = [
]





opensees.element.ElasticBeamColumn(section, material, geometry)
opensees.element.ForceBeamColumn(integration, material, geometry)

opensees.element.ElasticBeamColumn(A, E, G, J, iyc, ixc, geom)
opensees.element.ElasticBeamColumn(A, J, iyc, ixc, geom, material=material)
(
    section  = section,
    material = material,
    geometry = ["Linear"],
)

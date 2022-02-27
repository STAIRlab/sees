
section.Fiber(1 , elements=[
    # Create the concrete core fibers
    patch.rect(1 10 1 cover-y1, cover-z1, y1-cover z1-cover),

    # Create the concrete cover fibers (top, bottom, left, right)
    patch.rect(2, [10, 1],      -y1, z1-cover,       y1,       z1),
    patch.rect(2, [10, 1],      -y1,      -z1,       y1, cover-z1),
    patch.rect(2, [ 2, 1],      -y1, cover-z1, cover-y1, z1-cover),
    patch.rect(2, [ 2, 1], y1-cover, cover-z1,       y1, z1-cover),

    # Create the reinforcing fibers (left, middle, right)
    layer.straight( [3, 3], As, y1-cover, z1-cover, y1-cover, cover-z1),
    layer.straight( [3, 2], As,      0.0, z1-cover,      0.0, cover-z1),
    layer.straight( [3, 3], As, cover-y1, z1-cover, cover-y1, cover-z1),
])

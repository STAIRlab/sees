import opensees as ops
k = 60
m = 2
g = 386.4

model = ops.model(ndm=1, ndf=1)

model.node(1, 0)
model.node(2, 0, mass=m)
model.node(3, 0)
# model.mass(2,m)
model.fix(1,1)
model.fix(3,1)

material = ops.uniaxial.Elastic(None, k)
elem = ops.element.ZeroLength(None, [1, 2], mat=[material], dir=[1])

# ops.element.ZeroLength(2, [2, 3], mat=[1], dir=[1])

model.elem(1, [1, 2], elem)
model.elem(2, [2, 3], elem)

pattern = ops.pattern.MultipleSupport(None, [
    (1, 1, ops.pattern.TimeSeries(1, dt=0.02, file='tabasFN.txt', scale=g)),
    (3, 2, ops.pattern.TimeSeries(2, dt=0.02, file='tabasFP.txt', scale=g))
  ]
)



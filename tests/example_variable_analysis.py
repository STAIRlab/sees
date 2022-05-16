import opensees
import opensees.analysis


material = opensees.uniaxial.Elastic(1, 3000.0)
truss = opensees.element.Truss(1, [1, 2], 10.0, material)

m = opensees.model(ndm=1, ndf=1,
    nodes = {
        1: [0.0],
        2: [72.0]
    },
    elems = [
        (truss, [1,2])
    ]
    #zeros = [[1], [1]]
)
m.fix(1,1)

# pattern.Plain(1, "linear", [
#     pattern.load(2, 100.0)
# ])

strategy = dict(
    constraints = ("Transformation",),
    numberer = ("ParallelPlain",),
    test = ("NormDispIncr", 1e-6, 6, 2),
    system = ('ProfileSPD',),
    #integrator = ("Newmark", 0.5, 0.25),
    algorithm = ("Linear",),
    analysis = ("Variable",)
)
# ops.analysis('Transient')
ana = opensees.analysis.DirectIntegrationAnalysis(m, strategy)


ana.analyze(5, 0.0001)#, 0.00001, 0.001, 10)
time = ana.rt.time()
print(f'time: ', time)
approx_vtime = 0.0001 + 0.001  # One step at target, then one step at maximum
assert 0.99 < time / approx_vtime < 1.01,  (time,  approx_vtime)
ops.setTime(0.0)
# Can still run a non-variable analysis - since analyze function has multiple dispatch.
ops.analyze(5, 0.0001)
time = ops.getTime()
print(f'time: ', ops.getTime())
approx_vtime = 0.0001 * 5  # variable transient is not active so time should be dt * 5
# If variable transient is not active then time would be 0.0005
assert 0.99 < time / approx_vtime < 1.01,  (time,  approx_vtime)

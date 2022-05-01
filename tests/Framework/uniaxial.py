import opensees.tcl

mat = "1"
fy  = 150e3
E   = 100e3
b   = 0.04
R0  = 4
cR1 = 0.9240
cR2 = 0.1500

rt = opensees.tcl.TclRuntime()
rt.eval(f"""
model uniaxial
uniaxialMaterial Steel02 {mat} {fy} {E} {b} {R0} {cR1} {cR2}
""")


import libOpenSeesRT
addr = rt._interp.tk.interpaddr()
builder = libOpenSeesRT.get_builder(addr)
print(builder.getUniaxialMaterial(mat))



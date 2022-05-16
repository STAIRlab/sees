import bin/libdmg.so

model uniaxial

set fy  150e3
set E   100e3
set b   0.04
set R0  4
set cR1 0.9240
set cR2 0.1500
set mat 2

set Ccd 0.5

dmg::evol mbeta "beta" 4.2 1.0

dmg::load Uni "pos" -evol "beta" -Cd0 3.0 -Cd1 125 -Cwc 0.12  -E $E -fy $fy
dmg::load Uni "neg" -evol "beta" -Cd0 3.0 -Cd1 125 -Cwc 0.12  -E $E -fy $fy

# Create a 1d wrapper named "a"
dmg::wrap 1d "a" "pos" "neg" -Ccd $Ccd


uniaxialMaterial FEDEAS::Steel02 $mat $fy $E $b $R0 $cR1 $cR2

#                                    w m
uniaxialMaterial FedeasDamageWrapper 1 2 -damage a


with UniaxialMaterial $mat {
  #foreach s [linspace 1 10 100] {}
  strain 1.0 -commit
  puts "[stress] [tangent]"
  commit
  strain 2.0 -commit
  puts "[stress] [tangent]"
}



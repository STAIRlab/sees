model basic -ndm 3

node 1 0.0 0.0 0.0
node 2 4.0 6.0 0.0
node 3 8.0 6.0 0.0
node 4 8.0 0.0 0.0

#          A   E    G   J   I   I  t
set beam {1.0 1.0  1.0 1.0 1.0 1.0 1}
set vect {0.0 0.0 1.0}
geomTransf Linear 1 {*}$vect

element elasticBeamColumn 1 2 1 {*}$beam
element elasticBeamColumn 2 2 3 {*}$beam
element elasticBeamColumn 3 3 4 {*}$beam

print -JSON -file test.json


# regex for variable names
NAME="[A-z][A-z0-9]*"
# regex for expressions
EXPR='\[expr ([A-z0-9-+=/ \.\*]*)\]'
RE_LOGI='[=!><]'
#EXPR='\[expr ([A-z0-9-+/ \(\)\.\*]*)\]'

# use perl
SEDE="perl -pe"

OPS_PREFIX="ops."
OPS_CMDS=(
  node
  fix
  rigidLink
  element
  section
  patch
  layer

  analyze
  algorithm

)

cat - <<EOF
from math import cos,sin,sqrt,pi
EOF

cat $1 | {
  $SEDE "s|lappend ($NAME) (.*)|\1.append(\2)|g"
} | {
  $SEDE "s|set *($NAME) (.*)|\1 = \2|g"
} | {
  $SEDE "s|\[incr ($NAME)\]|\1 += 1|g"
} | {
  # when `incr` found inside braces, keep braces
  # so for loops can be identified later
  $SEDE "s|{incr ($NAME) ([A-z0-9]*)}|{\1 += \2}|g"
} | {
  $SEDE "s|{incr ($NAME) ([A-z0-9]*)}|{\1 += \2}|g"
} | {
  # wrap strings in quotes
  $SEDE "s|([A-z']) ([A-z][0-9\w/.]*) |\1 '\2' |g"
} | {
  # remove dollar signs
  sed 's:\$::g'
} | {
  # change || to `or`
  sed 's: || : or :g'
} | {
  $SEDE "s:set *($NAME) *$EXPR:\1 = \2:g"
} | {
  $SEDE "s:set *($NAME) *([0-9.]*):\1 = \2:g"
} | {
  $SEDE "s:$EXPR:\1:g"
} | {
#
# Control flow
#
  # if
  $SEDE "s|^([ \t]*)if {([A-z0-9-+!=/ \.\*]*)} {$|\1if \2:|g"
} | {
  # else
  $SEDE "s|} else {|else:|g"
} | {
  # for {i = start} {test} {incr}
  $SEDE "s|for \{($NAME) *= *0\} \{$NAME *$RE_LOGI *($NAME)\} \{$NAME *+= *1\} \{|for \1 in range(\2):|g"
} | {
  $SEDE "s|for {i = 0} {i < 8} {i += 1}|for i in range(8):|g"
} | {
  # remove closing brace
  $SEDE "s|^([ \t]*)};* *$||g"
} | {
#
# Misc
#
  # puts command with form `puts "string"`
  $SEDE 's|puts "(.*)"|print("\1")|g'

  # replace use of *in unit
  $SEDE 's|\*in([/\*-+ ])|*inch\1|g'
}


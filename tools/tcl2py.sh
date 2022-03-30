# regex for variable names
NAME="[A-z][A-z0-9]*"
# regex for expressions
EXPR='\[expr ([\(\)A-z0-9-+=/ \.\*]*)\]'
RE_LOGI='[=!><]'
#EXPR='\[expr ([A-z0-9-+/ \(\)\.\*]*)\]'

# use perl
SEDE="perl -pe"

OPS_PREFIX="ops"
declare -a OPS_CMDS=(
  node
  fix
  rigidLink
  element
  section
  patch
  layer
  analyze
  algorithm
  system
)

cat - <<EOF
from math import cos,sin,sqrt,pi
import opensees as ${OPS_PREFIX}
EOF

cat $1 | {
  $SEDE "s|\t| |g"
} | {
  #
  # Procedures
  #
  $SEDE "s/^proc ([A-z0-9_]*) \{(.*)\} \{/def \1(\2):/g"
} | {
  $SEDE "s|lappend ($NAME) (.*)|\1.append(\2)|g"
} | {
  $SEDE 's|set *([A-z][A-z0-9_]*) ([A-z][A-z.0-9_-]*)$|\1 = '\2'|g if !/#/ && !/"/'
} | {
  $SEDE "s|set *($NAME) (.*)|\1 = \2|g"' if !/#/ && !/"/'
} | {
  $SEDE "s|\[incr ($NAME)\]|\1 += 1|g"
} | {
  # when `incr` found inside braces, keep braces
  # so for loops can be identified later
  $SEDE "s|{incr ($NAME) ([A-z0-9]*)}|{\1 += \2}|g"
} | {
  $SEDE "s|{incr ($NAME) ([A-z0-9]*)}|{\1 += \2}|g"
} | {
## wrap words in quotes if line does not contain a " or #
  # end of line
  $SEDE "s:([A-z'])"' ([A-z][0-9\w/.]*)$'":\1 '\2':g if /^[ A-z]/ &&"' !/"/ && !/#/'
} | {
  # inside line
  $SEDE "s:([A-z'])"' ([A-z][0-9\w/.]*) '":\1 '\2', :g if /^[ A-z]/ &&"' !/"/ && !/#/'
} | {

## remove dollar signs
  sed 's:\$::g'
} | {
  # change || to `or`
  sed 's: || : or :g'
} | {
  $SEDE 's:pow\(([A-z0-9.]*),([A-z0-9.]*)\):\1**\2:g'
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
  $SEDE 's|^([ \t]*)if {([A-z0-9-+"!=/ \.\*]*)} {$|\1if \2:|g'
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
  # && Operator
  $SEDE 's|&&| and |g'
} | {
  # puts command with form `puts "string"`
  $SEDE 's|puts "(.*)"|print("\1")|g'

  # replace use of *in unit
  $SEDE 's|\*in([/\*-+ ])|*inch\1|g'
} | {
#
# Flag options
#
  # first treat flat followed by flag as boolean
  $SEDE s/" -([A-z]*) -"/' \1=True, -/g if !/"/ && !/#/'
} | {
  # treat flags at end of line as boolean
  $SEDE s/" -([A-z]*)$"/' \1=True/g if !/"/ && !/#/'
} | {
  $SEDE s/" -([A-z]*) ([0-9] [0-9 ]{1,})"/' \1=[\2], /g if !/"/ && !/#/ && !/\(/'
} | {
  $SEDE s/" -([A-z]*) '/ \1='\2/g"' if !/"/ && !/#/ && !/\(/'
} | {
  $SEDE s/" -([A-z]*) ([A-z0-9.]*)"/' \1=\2, /g if !/"/ && !/#/ && !/\(/'
} | {
  $SEDE s/",  section ([0-9]* [ 0-9]*)/, section=[\1], /g"
} | {
#
# 
# Simple model commands
  $SEDE "s/(section) ([A-z 0-9-.'=,]*)"'/model.\1(${2})/g if !/"/ && !/#/'
} | {
  $SEDE "s/(node|mass|fixZ|fixY|fixX|geomTransf|element) ([A-z 0-9-.'=,]*)"'/model.\1(${2})/g if !/"/ && !/#/'
} | {
  # Simple analysis commands
  $SEDE "s/(system|numberer|recorder|rayleigh|analyze|loadConst|algorithm|test|timeSeries|integrator|analysis|constraints|remove) ([A-z 0-9-.'=,]*)"'/ana.\1(${2})/g if !/"/ && !/#/'
} | {
# spaces to commas
  $SEDE "s/([A-z0-9'.]) {1,}([A-z0-9'.])/\1, \2/g"' if /^[A-z]/ && !/"/ && !/#/ && !/^if / && !/^def /'
} | {
  $SEDE "s/(?=^(def) )([A-z0-9'.]) {1,}([A-z0-9'.])/\1, \2/g"
} 


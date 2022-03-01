NAME="[A-z][A-z0-9]*"
#EXPR='\[expr ([A-z0-9-+/ \(\)\.\*]*)\]'
EXPR='\[expr ([A-z0-9-+/ \.\*]*)\]'
SEDE="perl -pe"

cat $1 \
  | sed 's:\$::g' \
  | $SEDE "s:set *($NAME) *$EXPR:\1 = \2:g" \
  | $SEDE "s:set *($NAME) *([0-9.]*):\1 = \2:g" \
  | $SEDE "s:$EXPR:\1:g"


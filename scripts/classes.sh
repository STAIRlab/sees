shopt -s globstar
for i in $1/**/*.h; do
  filename="$(basename $i)"
  classname="${filename/.h/}"

  #grep " $classname(" $i | grep -v -e "$classname([A-z0-9, ]*$" -e "class " -e "()"
  grep " $classname(" $i -A 10 | grep -v -e "(.*);"
done

#! /bin/bash

# $0 will be the file name
echo $0 $1 $2 $3


# if the variable is unset
my_country=${country:-China}
echo $my_country



# unlimited number of inputs
args=("$@")

# ./05input.sh my name eric
# my name eric
echo ${args[0]} ${args[1]} ${args[2]}

#./05input.sh my name eric
# 3
echo $#

#./05input.sh test_input_file.txt
: '
this is eric test file
this is line 2
'

while read line
do
  echo "$line"
done < "${1:-/dev/stdin}"


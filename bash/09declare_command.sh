#! /bin/bash

# bash doesn't support strong type, but `declare` allows you to update attributes to variables within the
# scope of your shell

# delcare int
declare -i bar
# empty
echo ${bar}
bar=x
# 0
echo ${bar}
bar=1
# 1
echo ${bar}

#error
bar=3.14
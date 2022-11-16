#! /bin/bash

car=('BMW', 'Toyota', 'Honda')

# print all values
echo "${car[@]}"

echo "${car[0]}"

# 3
echo "${#car[@]}"

# remove an element
unset "car[1]"
echo "${#car[@]}"

car[1]="Mercede"
echo "${car[@]}"
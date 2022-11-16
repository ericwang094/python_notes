#! /bin/bash

count=11

# number comparison

if [ $count -eq 9 ]
then
  echo "the condition is true"
else
  echo "the condition is false"
fi

if [ $count -ne 9 ]
then
  echo "the condition is true"
else
  echo "the condition is false"
fi

if (( count < 9 ))
then
  echo "the number is < 10"
else
  echo "the number is >= 10"
fi

if [ $count -eq 10 ]
then
  echo "the number is 10"
elif [ $count -gt 10 ]
then
  echo "the number is greater than 10 "
else
  echo "the number is >= 10"
fi

# && and

if [ $count -gt 9 ] && [ $count -lt 12 ]
then
  echo "count is > 9 and < 11"
fi

if [[ $count -gt 9 && $count -lt 12 ]]
then
  echo "count is > 9 and < 11"
fi

if [ $count -gt 9 ] || [ $count -lt 12 ]
then
  echo "count is > 9 or < 11"
fi
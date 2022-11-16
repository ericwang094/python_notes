#! /bin/bash

MESSAGE="Hello Linux Audience"
export MESSAGE
./07secondScript.sh

echo "enter 1st string"
read st1

echo "enter 2nd string"
read st2

if [ "$st1" == "$st2" ]
then
  echo "both strings match"
else
  echo "strings not match"
fi
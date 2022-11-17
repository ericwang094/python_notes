#! /bin/bash

mkdir -p my_folder

echo "Enter directory name to check"

direct=${direct:-"my_folder"}
#read direct

if [ -d "$direct" ]
then
  echo "$direct exists"
else
  echo "$direct doesn't exists"
fi

myfile=my_folder/myfile
touch $myfile
if [[ -f $myfile ]]
then
  echo "$myfile exists"
  echo "random context" > $myfile
fi

# read file
if [[ -f "$myfile" ]]
then
  while IFS= read -r line
  do
    echo "$line"
  done < $myfile
else
  ehoc "$myfile doesn't exists"
fi
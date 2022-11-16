# bin/bash

: '
my comments
'
count=10

if [ $count -eq 10 ]
then
  echo "here"
fi

if [ $count -gt 9 ] && [ $count -lt 11 ]
then
  echo "here"
fi

if [[ $count -gt 9 && $count -lt 11 ]]
then
  echo "here"
fi

number=1
while [ $number -lt 5 ]
do
  echo $number
  number=$((number+1))
done

for i in {1..5}
do
  echo $i
done

for (( i=0; i<10; i++ ))
do
  echo $i
done
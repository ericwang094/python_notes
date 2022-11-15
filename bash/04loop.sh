# usr/bin/bash

number=1
while [ $number -lt 10 ]
do
  echo "$number"
  number=$(( number+1 ))
done

number=1
until [ $number -ge 10 ]
do
  echo $number
  number=$(( number+1 ))
done

echo "for loop"

for i in {0..10}
do
  echo $i
done

echo "step for loop"
for i in {0..10..2}
do
  echo $i
done

echo "another loop"
for (( i=0; i<5; i++))
do
  echo "$i"
done

echo "loop with condition"
for (( i=0; i<10; i++))
do
  if [ "$i" -lt 5 ]
  then
    continue
  fi
  echo "$i"
done
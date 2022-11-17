#! /bin/bash

#select car in BMW MERCEDESE TESLA ROVER TOYOTA
#do
#  echo "You have selected $car"
#done

# switch statement

select car in BMW MERCEDES TELSA ROVER TOYOTA; do
  case $car in
    BMW)
      echo "BMW SELECTED";;
    MERCEDES)
      echo "MERCEDES SELECTED";;
    TELSA)
      echo "TELSA SELECTED";;
    ROVER)
      echo "ROVER SELECTED";;
    TOYOTA)
      echo "TOYOTA SELECTED";;
    *)
      echo "ERROR!";;
  esac
done

#! /bin/bash

function funcName()
{
  echo "this is new functions"
}

funcName

function funcPrint()
{
  echo $1
}

funcPrint Hi

function funcCheck()
{
  returningValue="Using Function right now"
}

returningValue="outside function"
echo $returningValue

funcCheck
# no local variable
echo $returningValue


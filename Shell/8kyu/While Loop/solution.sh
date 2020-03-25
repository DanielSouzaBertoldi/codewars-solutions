#!/bin/bash

countToTwenty() {
  x=1
  while [ $x -le 20 ];
  do
    echo Count: $x
    let x=x+1
  done
}

countToTwenty
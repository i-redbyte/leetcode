#!/bin/bash
filename='file.txt'
n=0
while read -r line; do
  n=$((n + 1))
  if [ $n -eq 10 ]; then
    break
  fi
done <$filename

echo "$line"

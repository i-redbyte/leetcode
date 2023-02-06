#!/usr/bin/env bash

for i in $(seq $(head -1 file.txt | tr ' ' '\n' | wc -l) ); do
  line=$(cut -f "$i" -d ' ' file.txt | tr '\n' ' ')
  echo "${line%% }"
done
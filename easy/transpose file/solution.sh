#!/usr/bin/env bash

while IFS= read -r line; do
  array+=("$line")
done <file.txt

num_columns=$(echo "${array[0]}" | wc -w)

IFS=' ' read -ra headers <<<"${array[0]}"

for i in $(seq 1 "$num_columns"); do
  printf '%s\t' "${headers[$i - 1]}"

  for line in "${array[@]:1}"; do
    IFS=' ' read -ra words <<<"$line"
    printf '%s\t' "${words[$i - 1]}"
  done
  printf "\n"
done

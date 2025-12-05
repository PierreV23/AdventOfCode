#!/usr/bin/env bash

set -e

if [ "$#" -eq 2 ]; then
    FILE="input.txt"
elif [ "$#" -eq 3 ]; then
    FILE=$(printf "test%02d.txt" "$3")
else
    echo day part optional[test id]
    exit
fi



DAY=$(printf "%02d" "$1")
PART=$2
# echo $FILE
# echo $DAY
# echo $PART

zig build -Dday="day$DAY/p$PART"

cat "inputs/day$DAY/$FILE" | ./zig-out/bin/aoc

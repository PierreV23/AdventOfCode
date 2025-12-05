#!/usr/bin/env bash

zig build -Dday=day02/p2; cat inputs/day02/input.txt | ./zig-out/bin/aoc | grep -P '^([0-9]+?)\1+$' | paste -sd+ | bc

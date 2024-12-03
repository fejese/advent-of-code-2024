#!/usr/bin/env python3

import re

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"

MUL_PATTERN: re.Pattern = re.compile(r"mul\((\d+),(\d+)\)")
OP_PATTERN: re.Pattern = re.compile(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))")

with open(INPUT_FILE_NAME, "r") as input_file:
    input = input_file.read().strip()


enabled = True
op_matches = OP_PATTERN.findall(input)
# print(input, op_matches)
total = 0
for op, op_a, op_b in op_matches:
    if op == "do()":
        enabled = True
    elif op == "don't()":
        enabled = False
    else:
        if enabled:
            total += int(op_a) * int(op_b)

print(total)

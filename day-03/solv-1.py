#!/usr/bin/env python3

import re

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

MUL_PATTERN: re.Pattern = re.compile(r"mul\((\d+),(\d+)\)")

with open(INPUT_FILE_NAME, "r") as input_file:
    input = input_file.read().strip()

mul_matches = MUL_PATTERN.findall(input)
# print(input, mul_matches)
print(sum(int(a) * int(b) for a, b in mul_matches))

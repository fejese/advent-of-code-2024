#!/usr/bin/env python3

from typing import List

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def process_equation(value: int, operands: List[int]) -> int:
    if len(operands) == 1:
        if value == operands[-1]:
            return value
        return 0

    if value < operands[0]:
        return 0

    if 0 != process_equation(value, [operands[0] + operands[1]] + operands[2:]):
        return value

    return process_equation(value, [operands[0] * operands[1]] + operands[2:])


def process_line(line: str) -> int:
    parts = line.split(":")
    value = int(parts[0])
    operands = [int(n) for n in parts[1].strip().split(" ")]
    return process_equation(value, operands)


result = 0
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file.readlines():
        result += process_line(line.strip())

print(result)

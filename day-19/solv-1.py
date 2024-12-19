#!/usr/bin/env python3

from typing import Dict, List, Set

# INPUT_FILE_NAME: str = "test-input"
from collections import defaultdict


INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    PATTERNS: Set[str] = {
        part.strip() for part in input_file.readline().strip().split(", ")
    }
    input_file.readline()
    DESIGNS: List[str] = [line.strip() for line in input_file.readlines()]


POSSIBLE_CACHE: Dict[str, bool] = {}


def is_possible(design: str, level: int = 0) -> bool:
    prefix = "  " * level
    if design in POSSIBLE_CACHE:
        print(f"{prefix}cached: {design}, {POSSIBLE_CACHE[design]}")
        return POSSIBLE_CACHE[design]

    if design in PATTERNS:
        print(f"{prefix}possible: {design}")
        POSSIBLE_CACHE[design] = True
        return True

    for pattern in PATTERNS:
        if design.startswith(pattern):
            if is_possible(design[len(pattern) :], level + 1):
                print(f"{prefix}possible: {design}")
                POSSIBLE_CACHE[design] = True
                return True

    print(f"{prefix}impossible: {design}")
    POSSIBLE_CACHE[design] = False
    return False


possible_count: int = 0
for design in DESIGNS:
    if is_possible(design):
        # print(f"possible: {design}")
        possible_count += 1
    else:
        pass
        # print(f"impossible: {design}")

print(f"{possible_count=}")

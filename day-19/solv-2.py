#!/usr/bin/env python3

from typing import Dict, List, Set

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    PATTERNS: Set[str] = {
        part.strip() for part in input_file.readline().strip().split(", ")
    }
    input_file.readline()
    DESIGNS: List[str] = [line.strip() for line in input_file.readlines()]


POSSIBLE_CACHE: Dict[str, int] = {}
POSSIBLE_CACHE[""] = 1


def possible_count(design: str, level: int = 0) -> int:
    prefix = "  " * level
    if design in POSSIBLE_CACHE:
        print(f"{prefix}cached: {design}, {POSSIBLE_CACHE[design]}")
        return POSSIBLE_CACHE[design]

    count: int = 0
    for pattern in PATTERNS:
        if design.startswith(pattern):
            count += possible_count(design[len(pattern) :], level + 1)

    print(f"{prefix}possible count: {design} => {count}")
    POSSIBLE_CACHE[design] = count
    return count


all_possible_count: int = 0
for design in DESIGNS:
    all_possible_count += possible_count(design)

print(f"{all_possible_count=}")

#!/usr/bin/env python3

from collections import defaultdict
from typing import Dict, Set


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

W = 0
H = 0
antennas: Dict[str, Set[complex]] = defaultdict(set)
with open(INPUT_FILE_NAME, "r") as input_file:
    for y, line in enumerate(input_file.readlines()):
        for x, char in enumerate(line.strip()):
            W = max(W, x)
            H = max(H, y)
            if char != ".":
                antennas[char].add(complex(x, y))
H += 1
W += 1

antinodes: Set[complex] = set()

for antenna_set in antennas.values():
    for antenna in antenna_set:
        for other_antenna in antenna_set:
            if antenna == other_antenna:
                continue
            diff = other_antenna - antenna
            antinodes.add(other_antenna + diff)
            antinodes.add(antenna - diff)

antinodes = {
    antinode
    for antinode in antinodes
    if 0 <= antinode.real < W
    if 0 <= antinode.imag < H
}

print(antinodes)
print(len(antinodes))

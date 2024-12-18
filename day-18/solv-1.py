#!/usr/bin/env python3

from typing import Dict, List, Set

# INPUT_FILE_NAME, GRID_SIZE, BYTE_LIMIT = "test-input", 7, 12
INPUT_FILE_NAME, GRID_SIZE, BYTE_LIMIT = "input", 71, 1024

DIRECTIONS: List[complex] = [
    LEFT := complex(-1, 0),
    RIGHT := complex(1, 0),
    UP := complex(0, -1),
    DOWN := complex(0, 1),
]


with open(INPUT_FILE_NAME, "r") as input_file:
    byte_positions: Set[complex] = {
        complex(*(int(part) for part in line.strip().split(",", 1)))
        for line in input_file.readlines()[:BYTE_LIMIT]
    }

start = complex(0, 0)
target = complex(GRID_SIZE - 1, GRID_SIZE - 1)

distances: Dict[complex, int] = {start: 0}
to_visit: Set[complex] = {start}

while to_visit:
    current = to_visit.pop()
    current_distance = distances[current]

    for direction in DIRECTIONS:
        next_position = current + direction
        next_distance = current_distance + 1

        if next_position.real < 0 or next_position.real >= GRID_SIZE:
            continue
        if next_position.imag < 0 or next_position.imag >= GRID_SIZE:
            continue

        if next_position in byte_positions:
            continue

        if distances.get(next_position, float("inf")) <= next_distance:
            continue

        distances[next_position] = next_distance
        to_visit.add(next_position)

# print(distances)
print(distances[target])

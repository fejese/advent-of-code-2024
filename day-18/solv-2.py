#!/usr/bin/env python3

from typing import Dict, List, Set, Optional

# INPUT_FILE_NAME, GRID_SIZE = "test-input", 7
INPUT_FILE_NAME, GRID_SIZE = "input", 71

DIRECTIONS: List[complex] = [
    LEFT := complex(-1, 0),
    RIGHT := complex(1, 0),
    UP := complex(0, -1),
    DOWN := complex(0, 1),
]


with open(INPUT_FILE_NAME, "r") as input_file:
    BYTE_POSITIONS: List[complex] = [
        complex(*(int(part) for part in line.strip().split(",", 1)))
        for line in input_file.readlines()
    ]

START = complex(0, 0)
TARGET = complex(GRID_SIZE - 1, GRID_SIZE - 1)


def get_min_distance_to_target(byte_positions: Set[complex]) -> Optional[int]:
    distances: Dict[complex, int] = {START: 0}
    to_visit: Set[complex] = {START}

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
    return distances.get(TARGET)


for byte_idx, byte_position in enumerate(BYTE_POSITIONS):
    min_distance = get_min_distance_to_target(set(BYTE_POSITIONS[: byte_idx + 1]))
    # print(f"{byte_position=} {min_distance=}")
    if min_distance is None:
        print(f"No solution for {byte_idx=} {byte_position=}")
        print(f"{int(byte_position.real)},{int(byte_position.imag)}")
        break

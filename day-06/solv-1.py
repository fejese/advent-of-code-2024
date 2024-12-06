#!/usr/bin/env python3

from typing import List, Set, Optional


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    GRID: List[str] = [l.strip() for l in input_file.readlines()]

W = len(GRID[0])
H = len(GRID)

DIRECTIONS: List[complex] = [
    complex(0, -1),
    complex(1, 0),
    complex(0, 1),
    complex(-1, 0),
]

guard_pos = complex(0, 0)
guard_dir_idx = 0
for y in range(H):
    if (x := GRID[y].find("^")) != -1:
        guard_pos = complex(x, y)
        break

# print(guard_pos, guard_dir_idx)

visited = set()
while True:
    visited.add(guard_pos)
    next_pos = guard_pos + DIRECTIONS[guard_dir_idx]
    if not (0 <= next_pos.real < W and 0 <= next_pos.imag < H):
        break

    if GRID[int(next_pos.imag)][int(next_pos.real)] == "#":
        guard_dir_idx = (guard_dir_idx + 1) % 4
        # print("turning", guard_dir)
    else:
        guard_pos = next_pos
        # print("moving", guard_pos)

print(len(visited))

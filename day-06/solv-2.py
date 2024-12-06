#!/usr/bin/env python3

from collections import defaultdict
from typing import List, Set, Optional

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    GRID: List[str] = [l.strip() for l in input_file.readlines()]

W: int = len(GRID[0])
H: int = len(GRID)

DIRECTIONS: List[complex] = [
    complex(0, -1),
    complex(1, 0),
    complex(0, 1),
    complex(-1, 0),
]


def run(guard_pos: complex, extra_block: Optional[complex] = None) -> Set[complex]:
    guard_dir_idx = 0
    visited = defaultdict(set)
    while True:
        if extra_block and guard_dir_idx in visited[guard_pos]:
            return set()
        visited[guard_pos].add(guard_dir_idx)
        next_pos = guard_pos + DIRECTIONS[guard_dir_idx]

        if not (0 <= next_pos.real < W and 0 <= next_pos.imag < H):
            break
        if (GRID[int(next_pos.imag)][int(next_pos.real)] == "#") or (
            extra_block is not None and next_pos == extra_block
        ):
            guard_dir_idx = (guard_dir_idx + 1) % 4
        else:
            guard_pos = next_pos

    return set(visited.keys())


guard_start_pos = complex(0, 0)
for y in range(H):
    if (x := GRID[y].find("^")) != -1:
        guard_start_pos = complex(x, y)
        break

all_visited = run(guard_start_pos)

loop_positions = 0
for visited in all_visited:
    if visited == guard_start_pos:
        continue

    if not run(guard_start_pos, visited):
        loop_positions += 1

print(loop_positions)

#!/usr/bin/env python3

from collections import defaultdict
from typing import List

# INPUT_FILE_NAMES: List[str] = [f"test-input-{i}" for i in range(5, 9)]
INPUT_FILE_NAMES: List[str] = ["input"]


def get_score(grid: List[List[int]], x: int, y: int) -> int:
    w = len(grid[0])
    h = len(grid)
    to_visit = {complex(x, y): 1}
    visited = set()
    nines = defaultdict(int)

    while to_visit:
        to_visit_new = defaultdict(int)
        for pos, combinations in to_visit.items():

            visited.add(pos)

            curr_level = grid[int(pos.imag)][int(pos.real)]
            if curr_level == 9:
                nines[pos] += combinations
                continue

            for offset in [
                complex(0, 1),
                complex(0, -1),
                complex(1, 0),
                complex(-1, 0),
            ]:
                new_pos = pos + offset
                if not ((0 <= new_pos.real < w) and (0 <= new_pos.imag < h)):
                    continue

                if new_pos in visited:
                    continue

                if grid[int(new_pos.imag)][int(new_pos.real)] != curr_level + 1:
                    continue

                to_visit_new[new_pos] += combinations

        to_visit = to_visit_new

    return sum(nines.values())


def get_total_score(grid: List[List[int]]) -> int:
    total_score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                total_score += get_score(grid, x, y)
    return total_score


for input_file_name in INPUT_FILE_NAMES:
    with open(input_file_name, "r") as input_file:
        grid = [
            [-1 if ch == "." else int(ch) for ch in l.strip()]
            for l in input_file.readlines()
        ]

    print(get_total_score(grid))

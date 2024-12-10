#!/usr/bin/env python3

from typing import List

# INPUT_FILE_NAMES: List[str] = [f"test-input-{i}" for i in range(1, 6)]
INPUT_FILE_NAMES: List[str] = ["input"]


def get_score(grid: List[List[int]], x: int, y: int) -> int:
    w = len(grid[0])
    h = len(grid)
    to_visit = {complex(x, y)}
    visited = set()
    nines = set()

    while to_visit:
        pos = to_visit.pop()
        visited.add(pos)

        curr_level = grid[int(pos.imag)][int(pos.real)]
        if curr_level == 9:
            nines.add(pos)
            continue

        for offset in [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]:
            new_pos = pos + offset
            if not ((0 <= new_pos.real < w) and (0 <= new_pos.imag < h)):
                continue

            if new_pos in visited:
                continue

            if grid[int(new_pos.imag)][int(new_pos.real)] != curr_level + 1:
                continue

            to_visit.add(new_pos)

    return len(nines)


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

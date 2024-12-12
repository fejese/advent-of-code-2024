#!/usr/bin/env python3

from typing import List, Set, Tuple

# INPUT_FILE_NAMES: List[str] = [f"test-input-{i}" for i in range(3)]
INPUT_FILE_NAMES: List[str] = ["input"]


def get_plot(grid: List[str], pos: complex) -> Tuple[Set[complex], int, int]:
    w = len(grid[0])
    h = len(grid)

    flower = grid[int(pos.imag)][int(pos.real)]

    visited = set()
    to_visit = {pos}
    circ = 0

    while to_visit:
        pos = to_visit.pop()
        visited.add(pos)

        for offset in [complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)]:
            next_pos = pos + offset
            if next_pos in visited:
                continue
            if (
                next_pos.real < 0
                or next_pos.real >= w
                or next_pos.imag < 0
                or next_pos.imag >= h
            ):
                circ += 1
                continue

            if grid[int(next_pos.imag)][int(next_pos.real)] == flower:
                to_visit.add(next_pos)
            else:
                circ += 1

    return visited, len(visited), circ


def solve(grid: List[str]) -> None:
    w = len(grid[0])
    h = len(grid)

    visited = set()
    result = 0

    for y in range(h):
        for x in range(w):
            if (pos := complex(x, y)) in visited:
                continue
            plots, area, circ = get_plot(grid, pos)
            visited.update(plots)
            cost = area * circ
            # print(f"found plot ({grid[y][x]}), {area=}, {circ=}, {cost=}")
            result += cost

    print(f"{result=}")


for input_file_name in INPUT_FILE_NAMES:
    with open(input_file_name, "r") as input_file:
        grid = [line.strip() for line in input_file.readlines()]
        solve(grid)

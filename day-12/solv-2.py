#!/usr/bin/env python3

from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional

# INPUT_FILE_NAMES: List[str] = [f"test-input-{i}" for i in (0, 1, 3, 4, 2)]
INPUT_FILE_NAMES: List[str] = ["input"]

DIRS: List[complex] = [
    UP := complex(0, -1),
    RIGHT := complex(1, 0),
    DOWN := complex(0, 1),
    LEFT := complex(-1, 0),
]


def add_side(
    sides: Dict[complex, List[Tuple[complex, complex]]],
    pos: complex,
    offset: complex,
) -> None:
    if offset == UP:
        new_side = (pos, pos + RIGHT)
    elif offset == DOWN:
        new_side = (pos + DOWN, pos + DOWN + RIGHT)
    elif offset == LEFT:
        new_side = (pos, pos + DOWN)
    elif offset == RIGHT:
        new_side = (pos + RIGHT, pos + RIGHT + DOWN)
    else:
        raise Exception(f"unknown offset {offset}")

    sides[offset].append(new_side)


def try_combine_sides(
    side: Tuple[complex, complex], other_side: Tuple[complex, complex]
) -> Optional[Tuple[complex, complex]]:
    for i in (0, 1):
        for j in (0, 1):
            if side[i] == other_side[j]:
                return (side[1 - i], other_side[1 - j])
    return None


def merge_first(
    sides: List[Tuple[complex, complex]], search_start_idx: int
) -> Optional[int]:
    EMPTY = (complex(0, 0), complex(0, 0))

    for idx, side in enumerate(sides[search_start_idx:], search_start_idx):
        if side == EMPTY:
            continue
        for other_idx, other_side in enumerate(sides[idx + 1 :], idx + 1):
            if other_side == EMPTY:
                continue

            if new_side := try_combine_sides(side, other_side):
                sides[idx] = new_side
                sides[other_idx] = EMPTY
                return idx


def count_merged_sides(sides: List[Tuple[complex, complex]]) -> int:
    EMPTY = (complex(0, 0), complex(0, 0))
    search_start_idx = 0

    while search_start_idx is not None:
        search_start_idx = merge_first(sides, search_start_idx)

    return len([side for side in sides if side != EMPTY])


def get_plot(grid: List[str], pos: complex) -> Tuple[Set[complex], int, int]:
    w = len(grid[0])
    h = len(grid)

    flower = grid[int(pos.imag)][int(pos.real)]

    visited = set()
    to_visit = {pos}
    sides: Dict[complex, List[Tuple[complex, complex]]] = defaultdict(list)

    while to_visit:
        pos = to_visit.pop()
        visited.add(pos)

        for offset in DIRS:
            next_pos = pos + offset
            if next_pos in visited:
                continue
            if (
                next_pos.real < 0
                or next_pos.real >= w
                or next_pos.imag < 0
                or next_pos.imag >= h
            ):
                add_side(sides, pos, offset)
                continue

            if grid[int(next_pos.imag)][int(next_pos.real)] == flower:
                to_visit.add(next_pos)
            else:
                add_side(sides, pos, offset)

    side_count = sum(count_merged_sides(sides_) for sides_ in sides.values())

    return visited, len(visited), side_count


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

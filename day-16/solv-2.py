#!/usr/bin/env python3

from collections import defaultdict
from typing import Dict, List, Set, Tuple

# INPUT_FILE_NAME: str = "test-input"
# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"

EMPTY: int = 0
WALL: int = 1

STEP_COST: int = 1
TURN_COST: int = 1000

DIRECTIONS: List[complex] = [
    complex(1, 0),
    complex(0, -1),
    complex(-1, 0),
    complex(0, 1),
]


with open(INPUT_FILE_NAME, "r") as input_file:
    string_grid = [line.strip() for line in input_file.readlines()]


H = len(string_grid)
W = len(string_grid[0])
grid = {}
start = complex(0, 0)
end = complex(0, 0)
for j in range(H):
    for i in range(W):
        if string_grid[j][i] == "S":
            start = complex(i, j)
        if string_grid[j][i] == "E":
            end = complex(i, j)
        grid[complex(i, j)] = WALL if string_grid[j][i] == "#" else EMPTY

direction_idx = 0
visited: Dict[Tuple[complex, int], int] = {}
to_visit: Set[Tuple[complex, int, int]] = {(start, direction_idx, 0)}

while to_visit:
    pos, direction_idx, cost = to_visit.pop()
    # print(f"visiting: {pos} {direction_idx} {DIRECTIONS[direction_idx]} {cost}")
    visited_idx = (pos, direction_idx)

    if visited_idx in visited and (prev_cost := visited[visited_idx]) <= cost:
        # print(f"  already visited ({prev_cost=})")
        continue

    visited[visited_idx] = cost
    # print(f"  new cost: {cost}")

    for rot_cnt in range(-1, 3):
        next_step_cost = cost + STEP_COST + (abs(rot_cnt) * TURN_COST)
        next_direction_idx = (direction_idx + rot_cnt) % len(DIRECTIONS)
        next_pos = pos + (DIRECTIONS[next_direction_idx])
        # print(f"  next: {next_pos} {next_direction_idx} {DIRECTIONS[next_direction_idx]} {next_step_cost}")
        if grid[next_pos] == WALL:
            # print("    wall")
            pass
        else:
            # print("    tovs")
            to_visit.add((next_pos, next_direction_idx, next_step_cost))

# print(visited)
# for dir_idx in range(len(DIRECTIONS)):
#     print(visited.get((end, dir_idx)))

if not any((end, dir_idx) in visited for dir_idx in range(len(DIRECTIONS))):
    print("no path found")
    exit(1)

print(
    min_cost := min(
        cost
        for dir_idx in range(len(DIRECTIONS))
        if (cost := visited.get((end, dir_idx))) is not None
    )
)

to_visit_backtrack = {
    (end, direction_idx)
    for direction_idx in range(len(DIRECTIONS))
    if visited.get((end, direction_idx)) == min_cost
}
# print(to_visit_backtrack)

path = set()
while to_visit_backtrack:
    pos, direction_idx = to_visit_backtrack.pop()
    cost = visited[(pos, direction_idx)]
    # print(f"visiting: {pos} {direction_idx} {DIRECTIONS[direction_idx]} {cost}")
    path.add(pos)
    for rot_cnt in range(-1, 3):
        prev_pos = pos - (DIRECTIONS[direction_idx])
        prev_step_cost = cost - STEP_COST - (abs(rot_cnt) * TURN_COST)
        prev_direction_idx = (direction_idx + rot_cnt) % len(DIRECTIONS)
        if prev_step_cost == visited.get((prev_pos, prev_direction_idx)):
            to_visit_backtrack.add((prev_pos, prev_direction_idx))
            # print(f"  {prev_pos} {prev_direction_idx} {DIRECTIONS[prev_direction_idx]} {prev_step_cost}")

# print(path)
print(len(path))

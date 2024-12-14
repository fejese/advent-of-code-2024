#!/usr/bin/env python3

from collections import defaultdict
from typing import Dict, Set, Tuple


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

dimensions = complex(0, 0)
with open(INPUT_FILE_NAME, "r") as input_file:
    robots: Dict[complex, Set[Tuple[complex, complex]]] = defaultdict(set)

    for line in input_file.readlines():
        parts = line.split()
        left, right = parts[0], parts[1]
        robot: Tuple[complex, complex] = (
            complex(*[int(c) for c in left.split("=")[1].split(",", 2)]),
            complex(*[int(c) for c in right.split("=")[1].split(",", 2)]),
        )
        if line.startswith("size"):
            dimensions = robot[0]
        else:
            robots[robot[0]].add(robot)

# print(dimensions)
# print(robots)

h_half = int(dimensions.imag) // 2
v_half = int(dimensions.real) // 2

step = 0
found = False
while True:
    pic = []
    for j in range(int(dimensions.imag)):
        line = ""
        for i in range(int(dimensions.real)):
            if j == h_half or i == v_half:
                line += " "
                continue
            robot_count = len(robots[complex(i, j)])
            line += "X" if robot_count else "."
        pic.append(line)
        if "XXXXXXXXXXXXX" in line:
            found = True
    if found:
        print("\n".join(pic))
        print(step)
        break
    step += 1

    new_robots: Dict[complex, Set[Tuple[complex, complex]]] = defaultdict(set)
    for robot_sets in robots.values():
        for robot in robot_sets:
            new_robot = (
                complex(
                    int(robot[0].real + robot[1].real) % int(dimensions.real),
                    int(robot[0].imag + robot[1].imag) % int(dimensions.imag),
                ),
                robot[1],
            )
            new_robots[new_robot[0]].add(new_robot)
    robots = new_robots

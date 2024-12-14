#!/usr/bin/env python3

from collections import defaultdict


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    robots = [
        tuple(
            complex(*[int(c) for c in part.split("=")[1].split(",")])
            for part in line.split()
        )
        for line in input_file.readlines()
    ]
    dimensions = robots[0][0]
    robots = robots[1:]

# print(dimensions)
# print(robots)

new_robots = defaultdict(int)
for robot in robots:
    new_robots[
        complex(
            int(robot[0].real + robot[1].real * 100) % int(dimensions.real),
            int(robot[0].imag + robot[1].imag * 100) % int(dimensions.imag),
        )
    ] += 1

print(new_robots)
h_half = int(dimensions.imag) // 2
v_half = int(dimensions.real) // 2
quadrants = defaultdict(int)

for j in range(int(dimensions.imag)):
    for i in range(int(dimensions.real)):
        if j == h_half or i == v_half:
            # print(" ", end="")
            continue
        q = int(j < h_half) + 2 * int(i < v_half)
        robot_count = new_robots[complex(i, j)]
        quadrants[q] += robot_count
    #     print(
    #         str(robot_count) if robot_count else ".",
    #         end=""
    #     )
    # print()

# print(quadrants)

if any(q == 0 for q in quadrants.values()):
    print(0)
else:
    result = 1
    for q in quadrants:
        result *= quadrants[q]
    print(result)

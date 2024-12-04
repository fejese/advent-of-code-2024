#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    grid = [l.strip() for l in input_file.readlines()]

H = len(grid)
W = len(grid[0])

MS = {"M", "S"}


def is_xmas(grid, x, y):
    if grid[y][x] != "A":
        return False
    if {grid[y - 1][x - 1], grid[y + 1][x + 1]} != MS:
        return False
    if {grid[y - 1][x + 1], grid[y + 1][x - 1]} != MS:
        return False

    return True


count = 0
for y in range(1, H - 1):
    for x in range(1, W - 1):
        if is_xmas(grid, x, y):
            count += 1

print(count)

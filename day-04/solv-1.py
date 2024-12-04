#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    grid = [l.strip() for l in input_file.readlines()]

H = len(grid)
W = len(grid[0])

LETTERS = "XMAS"
DIRECTIONS = [(vd, hd) for hd in [-1, 0, 1] for vd in [-1, 0, 1] if vd != 0 or hd != 0]


def is_valid_coord(x, y):
    return 0 <= x < W and 0 <= y < H


def is_xmas(grid, x, y, direction):
    for i in range(1, len(LETTERS)):
        x += direction[0]
        y += direction[1]
        if not is_valid_coord(y, x):
            return False
        if grid[y][x] != LETTERS[i]:
            return False

    return True


count = 0
for y in range(H):
    for x in range(W):
        if grid[y][x] != LETTERS[0]:
            continue
        for direction in DIRECTIONS:
            if is_xmas(grid, x, y, direction):
                count += 1

print(count)

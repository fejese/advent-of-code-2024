#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input-0"
# INPUT_FILE_NAME: str = "test-input-1"
INPUT_FILE_NAME: str = "input"

ROBOT: str = "@"
WALL: str = "#"
EMPTY: str = "."
BOX: str = "O"
UP: str = "^"
DOWN: str = "v"
LEFT: str = "<"
RIGHT: str = ">"

NULL_COORD = (-1, -1)


def print_grid(grid):
    for line in grid:
        print("".join(line))
    print()


def attempt_move(grid, robot, direction):
    di, dj = direction

    new_robot = (robot[0] + di, robot[1] + dj)
    if grid[new_robot[1]][new_robot[0]] == WALL:
        return robot
    elif grid[new_robot[1]][new_robot[0]] == EMPTY:
        return new_robot

    first_empty = NULL_COORD
    box_count = 0
    i, j = robot
    while True:
        i += di
        j += dj
        if grid[j][i] == WALL:
            return robot
        elif grid[j][i] == EMPTY:
            first_empty = (i, j)
            break
        elif grid[j][i] == BOX:
            box_count += 1

    grid[first_empty[1]][first_empty[0]] = BOX
    grid[new_robot[1]][new_robot[0]] = EMPTY

    return new_robot


with open(INPUT_FILE_NAME, "r") as input_file:
    grid_part, seq_part = input_file.read().split("\n\n")

grid = [[c for c in line.strip()] for line in grid_part.strip().split("\n")]
H = len(grid)
W = len(grid[0])
robot = (-1, -1)
for j in range(H):
    for i in range(W):
        if grid[j][i] == ROBOT:
            robot = (i, j)
            grid[j][i] = EMPTY
            break
    if robot[0] != -1:
        break
seq = seq_part.replace("\n", "").strip()

for step in seq:
    # print_grid(grid)
    # print(robot, step)
    if step == UP:
        robot = attempt_move(grid, robot, (0, -1))
    elif step == DOWN:
        robot = attempt_move(grid, robot, (0, 1))
    elif step == LEFT:
        robot = attempt_move(grid, robot, (-1, 0))
    elif step == RIGHT:
        robot = attempt_move(grid, robot, (1, 0))

print_grid(grid)

result = 0
for j in range(H):
    for i in range(W):
        if grid[j][i] == BOX:
            result += j * 100 + i
print(result)

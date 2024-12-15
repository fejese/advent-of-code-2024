#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input-0"
# INPUT_FILE_NAME: str = "test-input-1"
INPUT_FILE_NAME: str = "input"

ROBOT: str = "@"
WALL: str = "#"
EMPTY: str = "."
BOX: str = "O"
BOXL: str = "["
BOXR: str = "]"
UP: str = "^"
DOWN: str = "v"
LEFT: str = "<"
RIGHT: str = ">"

NULL_COORD = (-1, -1)


def print_grid(grid, robot):
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if (i, j) == robot:
                print(ROBOT, end="")
            else:
                print(grid[j][i], end="")
        print()
    print()


def attempt_move_h(grid, robot, direction):
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
        elif grid[j][i] == BOXL or grid[j][i] == BOXR:
            box_count += 1

    empty = first_empty
    while empty != new_robot:
        i, j = empty
        grid[j][i] = grid[j - dj][i - di]
        empty = (i - di, j - dj)
    grid[new_robot[1]][new_robot[0]] = EMPTY

    return new_robot


def can_move_v(grid, box, direction):
    di, dj = direction

    new_box = (box[0] + di, box[1] + dj)
    if grid[new_box[1]][new_box[0]] == WALL:
        return False
    elif grid[new_box[1]][new_box[0]] == EMPTY:
        return True

    other_box_dir = -1 if grid[new_box[1]][new_box[0]] == BOXR else 1
    other_box = (new_box[0] + other_box_dir, new_box[1])

    return can_move_v(grid, new_box, direction) and can_move_v(
        grid, other_box, direction
    )


def move_v(grid, box, direction):
    di, dj = direction

    new_box = (box[0] + di, box[1] + dj)
    if (new_box_val := grid[new_box[1]][new_box[0]]) in (BOXL, BOXR):
        other_box_dir = -1 if new_box_val == BOXR else 1
        other_box = (new_box[0] + other_box_dir, new_box[1])
        move_v(grid, new_box, direction)
        move_v(grid, other_box, direction)

    grid[new_box[1]][new_box[0]] = grid[box[1]][box[0]]
    grid[box[1]][box[0]] = EMPTY


def attempt_move_v(grid, robot, direction):
    di, dj = direction

    new_robot = (robot[0] + di, robot[1] + dj)
    if grid[new_robot[1]][new_robot[0]] == WALL:
        return robot
    elif grid[new_robot[1]][new_robot[0]] == EMPTY:
        return new_robot

    box = new_robot
    other_box_dir = -1 if grid[box[1]][box[0]] == BOXR else 1
    other_box = (box[0] + other_box_dir, box[1])

    if not can_move_v(grid, box, direction) or not can_move_v(
        grid, other_box, direction
    ):
        return robot

    move_v(grid, box, direction)
    move_v(grid, other_box, direction)

    return new_robot


with open(INPUT_FILE_NAME, "r") as input_file:
    grid_part, seq_part = input_file.read().split("\n\n")

grid = [
    " ".join(
        [
            (
                f"{WALL} {WALL}"
                if c == WALL
                else (
                    f"{BOXL} {BOXR}"
                    if c == BOX
                    else (f"{EMPTY} {EMPTY}" if c == EMPTY else f"{ROBOT} {EMPTY}")
                )
            )
            for c in line.strip()
        ]
    ).split(" ")
    for line in grid_part.strip().split("\n")
]
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
    # print_grid(grid, robot)
    # print(robot, step)
    if step == UP:
        robot = attempt_move_v(grid, robot, (0, -1))
    elif step == DOWN:
        robot = attempt_move_v(grid, robot, (0, 1))
    elif step == LEFT:
        robot = attempt_move_h(grid, robot, (-1, 0))
    elif step == RIGHT:
        robot = attempt_move_h(grid, robot, (1, 0))

print_grid(grid, robot)

result = 0
for j in range(H):
    for i in range(W):
        if grid[j][i] == BOXL:
            result += j * 100 + i
print(result)

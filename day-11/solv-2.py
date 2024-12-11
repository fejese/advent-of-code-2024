#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


CACHE = dict()


def solve_rock(rock: int, steps_left: int) -> int:
    if steps_left == 0:
        return 1

    if (rock, steps_left) in CACHE:
        return CACHE[(rock, steps_left)]

    if rock == 0:
        solution = solve_rock(1, steps_left - 1)
    elif len(rock_str := str(rock)) % 2 == 0:
        solution = solve_rock(
            int(rock_str[: len(rock_str) // 2]), steps_left - 1
        ) + solve_rock(int(rock_str[len(rock_str) // 2 :]), steps_left - 1)
    else:
        solution = solve_rock(rock * 2024, steps_left - 1)

    CACHE[(rock, steps_left)] = solution
    return solution


def solve(line: str) -> None:
    rocks = [int(c) for c in line.split()]
    rounds = 75
    rocks = rocks[2:]

    total_rocks = 0
    for rock in rocks:
        rock_solution = solve_rock(rock, rounds)
        print(f"Rock {rock}: ", rock_solution)
        print("Cache size:", len(CACHE))
        total_rocks += rock_solution

    print(total_rocks)


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        solve(line.strip())

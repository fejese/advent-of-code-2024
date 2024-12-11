#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def solve(line: str) -> None:
    rocks = [int(c) for c in line.split()]
    rounds = rocks[0]
    print_steps = rocks[1]
    rocks = rocks[2:]

    for _ in range(rounds):
        new_rocks = list()
        for rock in rocks:
            if rock == 0:
                new_rocks.append(1)
            elif len(rock_str := str(rock)) % 2 == 0:
                new_rocks.append(int(rock_str[: len(rock_str) // 2]))
                new_rocks.append(int(rock_str[len(rock_str) // 2 :]))
            else:
                new_rocks.append(rock * 2024)

        rocks = new_rocks
        if print_steps:
            print(" ".join(str(rock) for rock in rocks))

    print(len(rocks))
    print()


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        solve(line.strip())

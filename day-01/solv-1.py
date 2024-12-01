#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

list_a = []
list_b = []
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        parts = line.strip().split()
        list_a.append(int(parts[0]))
        list_b.append(int(parts[1]))

list_a.sort()
list_b.sort()

diff_sum = 0
for a, b in zip(list_a, list_b):
    diff = abs(a - b)
    # print(a, b, diff)
    diff_sum += diff

print(diff_sum)

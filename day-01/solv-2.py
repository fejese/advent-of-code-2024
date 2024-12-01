#!/usr/bin/env python3

from collections import defaultdict


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

list_a = []
freq = defaultdict(int)
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        parts = line.strip().split()
        list_a.append(int(parts[0]))
        freq[int(parts[1])] += 1

print(sum(a * freq[a] for a in list_a))

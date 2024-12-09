#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

EMPTY = -1

with open(INPUT_FILE_NAME, "r") as input_file:
    encoded = input_file.read().strip()

exploded = list()

file_no = 0
in_file = False
for c in encoded:
    size = int(c)
    if in_file:
        in_file = False
        for _ in range(size):
            exploded.append(EMPTY)
    else:
        in_file = True
        for _ in range(size):
            exploded.append(file_no)
        file_no += 1

last_non_empty = len(exploded) - 1
while last_non_empty >= 0 and exploded[last_non_empty] == EMPTY:
    last_non_empty -= 1

for i in range(len(exploded)):
    if exploded[i] != EMPTY:
        continue

    if i >= last_non_empty:
        break

    exploded[i] = exploded[last_non_empty]
    exploded[last_non_empty] = EMPTY
    while last_non_empty >= 0 and exploded[last_non_empty] == EMPTY:
        last_non_empty -= 1

# print(exploded)
print(sum(i * n for i, n in enumerate(exploded) if n != EMPTY))

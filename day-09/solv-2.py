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
        if size:
            exploded.append(complex(EMPTY, size))
    else:
        in_file = True
        if size:
            exploded.append(complex(file_no, size))
        file_no += 1

moved = set()
for file_to_move in range(file_no, -1, -1):
    file_pos = len(exploded) - 1
    while file_pos >= 0 and exploded[file_pos].real != file_to_move:
        file_pos -= 1
    file = exploded[file_pos]

    empty_pos = -1
    empty = None
    for maybe_empty_pos in range(0, min(len(exploded), file_pos)):
        if (
            exploded[maybe_empty_pos].real == EMPTY
            and exploded[maybe_empty_pos].imag >= file.imag
        ):
            empty_pos = maybe_empty_pos
            empty = exploded[empty_pos]
            break
    if empty_pos == -1:
        continue
    assert empty

    if empty.imag == file.imag:
        exploded[empty_pos] = file
        exploded[file_pos] = empty
        continue

    exploded[empty_pos] = file
    exploded[file_pos] = complex(EMPTY, file.imag)
    exploded.insert(empty_pos + 1, complex(EMPTY, empty.imag - file.imag))

# print(exploded)

result = 0
idx = 0
for part in exploded:
    for _ in range(int(part.imag)):
        if part.real != EMPTY:
            result += part.real * idx
        idx += 1

print(result)

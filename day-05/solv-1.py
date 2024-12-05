#!/usr/bin/env python3

from collections import defaultdict


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    rules_part, updates_part = input_file.read().split("\n\n")

update_lists = [
    [int(n) for n in l.strip().split(",")] for l in updates_part.strip().split("\n")
]
update_sets = [set(l) for l in update_lists]
update_idxs = [
    {n: i for i, n in enumerate(update_list)} for update_list in update_lists
]

rules = defaultdict(set)
for rule in rules_part.strip().split("\n"):
    lhs, rhs = rule.strip().split("|")
    rules[int(lhs)].add(int(rhs))


middles = []
for update_idx, update in enumerate(update_lists):
    print(f"processing {update_idx=}, {update=}")
    valid = True
    for page_idx, page in enumerate(update):
        for rhs_page in rules[page]:
            rhs_page_idx = update_idxs[update_idx].get(rhs_page, None)
            if rhs_page_idx is None:
                continue
            if page_idx > rhs_page_idx:
                valid = False
                print(
                    f"  not valid because index ({rhs_page_idx}) of {rhs_page} is before ({page_idx}) of {page}"
                )
                break

        if not valid:
            break

    if valid:
        middles.append(update[len(update) // 2])

print(middles)
print(sum(middles))

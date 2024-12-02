#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

safe_count = 0
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        # print(f"parsing {line=}")
        nums = [int(part) for part in line.strip().split()]
        if nums[0] == nums[1]:
            # print("  first 2 elements equal")
            continue
        increasing = nums[1] > nums[0]
        # print(f"  {increasing=}")
        safe = True
        for idx, num in enumerate(nums[1:], 1):
            diff = num - nums[idx-1]
            if diff < -3 or diff > 3:
                # print(f"  more than 3 diff at {idx=} ({diff=})")
                safe = False
                break
            if diff == 0:
                # print(f"  no change at {idx=} ({diff=})")
                safe = False
                break
            if increasing and diff < 0:
                # print(f"  increasing report with decrease at {idx=}")
                safe = False
                break
            if not increasing and diff > 0:
                # print(f"  decreasing report with increase at {idx=}")
                safe = False
                break
        if safe:
            # print("  safe")
            safe_count += 1

print(safe_count)

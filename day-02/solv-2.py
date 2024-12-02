#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def skip(nums, idx):
    return nums[:idx] + nums[idx + 1:]


def is_safe(nums, retry_on_error=False):
    if nums[0] == nums[1]:
        return is_safe(skip(nums, 0)) or is_safe(skip(nums, 1))

    increasing = nums[1] > nums[0]
    safe = True
    for idx, num in enumerate(nums[1:], 1):
        diff = num - nums[idx-1]
        if diff < -3 or diff > 3:
            return is_safe(skip(nums, idx - 1)) or is_safe(skip(nums, idx)) if retry_on_error else False
        if diff == 0:
            return is_safe(skip(nums, idx - 1)) or is_safe(skip(nums, idx)) if retry_on_error else False
        if increasing and diff < 0:
            return is_safe(skip(nums, idx - 1)) or is_safe(skip(nums, idx)) if retry_on_error else False
        if not increasing and diff > 0:
            return is_safe(skip(nums, idx - 1)) or is_safe(skip(nums, idx)) if retry_on_error else False

    return safe


safe_count = 0
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        # print(f"parsing {line=}")
        nums = [int(part) for part in line.strip().split()]
        if is_safe(nums, retry_on_error=True):
            # print("  safe")
            safe_count += 1

print(safe_count)

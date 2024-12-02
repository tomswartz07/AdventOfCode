#!/usr/bin/python

def is_safe(report):
    curr_diff = report[1] - report[0]

    for idx in range(len(report) - 1):
        new_diff = report[idx + 1] - report[idx]
        if new_diff == 0 or abs(new_diff) > 3 or (new_diff > 0) != (curr_diff > 0):
            return False
        curr_diff = new_diff
    return True


def main():
    safe_first_try = 0
    safe_with_mods = 0

    with open("input.txt", "rt", encoding="utf-8") as f:
        for line in f:
            nums = list(map(int, line.split()))
            if is_safe(nums):
                safe_first_try += 1
            else:
                for i in range(len(nums)):
                    if is_safe(nums[:i] + nums[i + 1:]):
                        safe_with_mods += 1
                        break

    print(f"Part 2: {safe_first_try + safe_with_mods}")


if __name__ == "__main__":
    main()

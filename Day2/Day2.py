import os

base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "input.txt")

with open(file_path, "r") as f:
    line = f.readlines()[0]

def parse_ranges(line):
    parts = line.split(",")
    ranges = []
    for p in parts:
        lo, hi = p.split('-')
        ranges.append((int(lo), int(hi)))
    return ranges

ranges = parse_ranges(line)

def is_double_repeat(x):
    s = str(x)
    n = len(s)
    if n % 2 != 0:
        return False
    half = n // 2
    return s[:half] == s[half:]


def part1_total_invalid(ranges):
    total = 0
    for lo, hi in ranges:
        for x in range(lo, hi + 1):
            if is_double_repeat(x):
                total += x
    return total


print(f"First Problem: {part1_total_invalid(ranges)}")

def is_repeated_string(x):
    s = str(x)
    n = len(s)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            if s == s[:size] * (n // size):
                return True
    return False

def part2_total_invalid(ranges):
    total = 0
    for lo, hi in ranges:
        for x in range(lo, hi + 1):
            if is_repeated_string(x):
                total += x
    return total

print(f"Second Problem: {part2_total_invalid(ranges)}")
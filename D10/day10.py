import os
import numpy as np
from typing import List
from collections import defaultdict


def part1(data):

    diffs = np.array([data[idx + 1] - data[idx]
                      for idx, item in enumerate(data[:-1])])
    unique_counts = np.unique(diffs, return_counts=True)

    return np.prod(unique_counts[1])


def solve_part2(data):
    ways = defaultdict(int)

    device = data.pop()
    ways[device] = 1

    for i in reversed(data):
        ways[i] = ways[i + 1] + ways[i + 2] + ways[i + 3]

    return ways[0]

if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, 'input.txt')

    # socket - 0 
    data = [0]

    with open(inputfile) as f:
        for num in f.readlines():
            data.append(int(num.strip("\n")))
    data = sorted(data)

    # console - 3 more than the max adapter
    data.append(max(data) + 3)

    print(f"Part 1 solution: {part1(data)}")

    print(f"Part 2 solution: {solve_part2(data)}")

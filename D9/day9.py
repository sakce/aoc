import os
from itertools import combinations


def part1(numbers, preamble_n):
    start = 0
    end = preamble_n

    while end < len(numbers):

        temp_nums = numbers[start:end]

        temp_combs = combinations(temp_nums, 2)

        comb_sums = map(sum, (list(temp_combs)))

        if numbers[end] not in comb_sums:
            return numbers[end]
        start += 1
        end += 1
    return "All good.."

# CONTIGUOUS SET - they are consecutive in order


def part2(data, part1_solution):
    smaller_numbers = [a for a in data if a < part1_solution]

    for idx, i in enumerate(smaller_numbers):
        temp = [i]
        idx_copy = idx
        while sum(temp) < part1_solution:
            temp.append(smaller_numbers[idx_copy+1])
            idx_copy += 1

        if sum(temp) == part1_solution:
            return (temp, min(temp) + max(temp))


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, 'input.txt')

    data = []
    with open(inputfile) as f:
        for num in f.readlines():
            data.append(int(num.strip("\n")))

    part1_solution = part1(data, 25)

    print(f"Part 1 solution: {part1_solution}")

    print(f"Part 2 solution: {part2(data, part1_solution)}")

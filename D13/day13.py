import os
import math
import pytest


def part1(earliest, bus_ids):

    diff_dict = dict()

    for bus in bus_ids:
        diff_dict[bus] = math.ceil(earliest / bus) * bus - earliest

    min_diff = min(diff_dict, key=diff_dict.get)

    return diff_dict[min_diff] * min_diff


def part2(bus_ids):
    print(bus_ids)
    offset_dict = dict()

    offset_dict[int(bus_ids[0])] = 0

    t = 0
    for bus in bus_ids[1:]:
        t += 1
        if bus == "x":
            continue
        else:
            offset_dict[int(bus)] = t


def test_part2_1():
    bus_ids_1 = ["17", "x", "13", "19"]
    assert part2(bus_ids_1) == 3417


def test_part2_2():
    bus_ids_2 = ["67", "7", "59", "61"]
    assert part2(bus_ids_2) == 754018


def test_part2_3():
    bus_ids_3 = ["67", "x", "7", "59", "61"]
    assert part2(bus_ids_3) == 779210


def test_part2_4():
    bus_ids_4 = ["67", "7", "x", "59", "61"]
    assert part2(bus_ids_4) == 1261476


def test_part2_5():
    bus_ids_5 = ["1789", "37", "47", "1889"]
    assert part2(bus_ids_5) == 1202161486


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, 'test_input.txt')

    with open(inputfile) as f:
        for idx, line in enumerate(f.readlines()):
            if idx == 0:
                earliest = int(line.strip("\n"))
            else:
                bus_ids = [int(bus) for bus in line.strip(
                    "\n").split(",") if bus != "x"]
                bus_ids_2 = [bus for bus in line.strip("\n").split(",")]

    print(f"Part 1 solution: {part1(earliest, bus_ids)}")

    print(f"Part 2 solution: {part2(bus_ids_2)}")

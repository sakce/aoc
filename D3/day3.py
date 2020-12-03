import numpy as np


f = open("input.txt", "r")
forest = f.readlines()

forest_array = np.array([line.strip("\n")*73 for line in forest])

from typing import List

def find_path(forest, steps: List[int]):
    x = 0
    y = 0
    x_step, y_step = steps[0], steps[1]

    tree_count = 0

    while y < 322:
        x += x_step
        y += y_step
        print(forest[y][x])
        if forest[y][x] == "#":
            tree_count += 1

    return tree_count

# print(forest_array[1])

def find_best(forest):
    combs = [[1,1], [3, 1], [5, 1], [7,1], [1, 2]]

    res = []
    for comb in combs:
        res.append(find_path(forest, comb))

    print(res)
    return np.prod(res)

print(find_best(forest_array))

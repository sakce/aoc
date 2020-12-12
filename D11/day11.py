import os
import numpy as np
import time

def part1(data):

    def collect_adjacent(x, y):
        points = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                  (x, y - 1), (x, y + 1),
                  (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        return points

    def fill_seat(x, y):
        return all([True if prev_grid[adjacent[0], adjacent[1]] in [0, 1, -1] else False
                    for adjacent in collect_adjacent(x + 1, y + 1)])  # + 1 to adjust for padding

    def empty_seat(x, y):
        count = 0
        for adjacent in collect_adjacent(x + 1, y + 1):
            if prev_grid[adjacent[0], adjacent[1]] == 2:
                count += 1

        if count >= 4:
            return True
        else:
            return False

    def switch_round(fill):
        if fill:
            return False
        else:
            return True

    # 0 - no seat, 1 - Empty seat, -1 - padding, 2 - full seat
    original_shape = data.shape
    curr_grid = np.zeros(shape=original_shape)

    #  Pad with rows and columns on each side - now we start from (1,1)
    data = np.pad(data, (1, 1), constant_values=(-1, -1))
    prev_grid = data.copy()

    fill = True
    round_count = 0

    while True:

        for row_idx, row in enumerate(prev_grid[1:-1]):
            for col_idx, col in enumerate(row[1:-1]):
                if fill:
                    if fill_seat(row_idx, col_idx):  # If the seat has all empty seats adjacent
                        # If the current spot is not a seat
                        if prev_grid[row_idx + 1][col_idx + 1] == 0:
                            # keep it _not a seat_
                            curr_grid[row_idx][col_idx] = 0
                        else:  # If it is a seat - make it full
                            curr_grid[row_idx][col_idx] = 2
                    else:  # if it doesn't have empty adjacent seats
                        curr_grid[row_idx][col_idx] = col  # keep it as it is

                else:  # if it's time for a emptying round
                    if empty_seat(row_idx, col_idx):  # if the seat should be empty
                        if prev_grid[row_idx + 1][col_idx + 1] == 0:
                            # make it a non-seat
                            curr_grid[row_idx][col_idx] = 0
                        else:
                            curr_grid[row_idx][col_idx] = 1  # make it empty
                    else:  # if it doesn't have at least 4 adjacent full seats
                        curr_grid[row_idx][col_idx] = col  # keep it as it is

        fill = switch_round(fill)

        curr_grid = np.pad(curr_grid, (1, 1), constant_values=(-1, -1))

        if np.array_equal(curr_grid, prev_grid):
            break
        else:
            prev_grid = curr_grid.copy()
            curr_grid = np.zeros(shape=original_shape)

        round_count += 1


    return np.count_nonzero(curr_grid == 2)  # count occupied seats



if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, 'test_input.txt')

    if "test_input" in inputfile:
        data = np.zeros(shape=(10, 10))
    else:
        data = np.zeros(shape=(90, 96))

    with open(inputfile) as f:
        for line_idx, line in enumerate(f.readlines()):
            for char_idx, char in enumerate(line.strip("\n").replace(".", "0").replace("L", "1")):
                data[line_idx, char_idx] = int(char)

    print(f"Part 1 solution: {part1(data)}")

    # print(f"Part 2 solution: {part2(data)}")

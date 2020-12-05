import os
import re
from typing import Dict, List

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

boarding_passes = []
with open(inputfile) as f:
    for line in f.readlines():
        boarding_passes.append(line.strip("\n"))


def find_row(boarding_pass: str):

    rows = list(range(0, 128))
    min_row = rows[0]
    max_row = rows[-1]

    for idx, letter in enumerate(boarding_pass[:7]):
        if idx == 6:  # If last letter
            if letter == "F":
                row = rows[0]
                return row
            else:
                row = rows[1]
                return row
        else:
            if letter == "F":
                max_row = rows[len(rows) // 2 - 1]
                # print("Lower", min_row, max_row)
                rows = list(range(min_row, max_row + 1))
            elif letter == "B":
                min_row = rows[len(rows) // 2]
                # print("Upper", min_row, max_row)
                rows = list(range(min_row, max_row + 1))
            else:
                Exception("Uh-oh")


def find_column(boarding_pass: str):

    cols = list(range(0, 8))
    min_col = cols[0]
    max_col = cols[-1]

    for idx, letter in enumerate(boarding_pass[7:]):
        # There must be a neater way to check if it's the last letter...
        if idx == 2:  # If last letter
            if letter == "L":
                col = cols[0]
                return col
            elif letter == "R":
                col = cols[1]
                return col
        else:
            if letter == "L":
                max_col = cols[len(cols) // 2 - 1]
                cols = list(range(min_col, max_col + 1))
            elif letter == "R":
                min_col = cols[len(cols) // 2]
                cols = list(range(min_col, max_col + 1))
            else:
                Exception("Uh-oh")


def find_seat_nums(boarding_list: List[str]):
    seat_numbers = []
    for item in boarding_list:
        sRow, sCol = find_row(item), find_column(item)
        seat_numbers.append([sRow, sCol])

    return (seat_numbers)


def find_seat_codes(seat_numbers: List[List[int]]):
    def multiply(x): return x[0] * 8 + x[1]
    codes = list(map(multiply, seat_numbers))

    return codes


print(max(find_seat_codes(find_seat_nums(boarding_passes))))

# Second star

seat_codes = sorted(find_seat_codes(find_seat_nums(boarding_passes)))


def find_my_seat(seat_codes: List[int]):
    # Find missing int in the range
    return [code for code in range(seat_codes[0], seat_codes[-1] + 1)
            if code not in seat_codes]


print(find_my_seat(seat_codes))

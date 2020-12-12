import os
import math
import numpy as np


def part1(data):
    """
    docstring
    """
    position = [0, 0]  # N-S , E-W

    # North 0 -> adds to position[0]
    # South 2 -> subtracts from position[0]

    # East 1 -> adds to position[1]
    # West 3 -> subtracts from position[1]

    nose = 1  # turned east at start

    def rotate(operation, nose):
        direction, angle = 1 if operation[0] == "R" else -1, int(operation[1:])

        nose = nose + direction * (angle // 90)

        return nose % 4

    def forward(operation, nose, position):
        if nose == 0:
            position[0] += int(operation[1:])
        elif nose == 1:
            position[1] += int(operation[1:])
        elif nose == 2:
            position[0] -= int(operation[1:])
        else:
            position[1] -= int(operation[1:])

        return position

    def move(operation, position):
        if operation[0] == "N":
            position[0] += int(operation[1:])
        elif operation[0] == "E":
            position[1] += int(operation[1:])
        elif operation[0] == "S":
            position[0] -= int(operation[1:])
        else:
            position[1] -= int(operation[1:])
        return position

    for op in data:
        if op[0] in ["R", "L"]:
            nose = rotate(op, nose)
        elif op[0] in ["F"]:
            position = forward(op, nose, position)
        else:
            position = move(op, position)

    return abs(position[0]) + abs(position[1])


def part2(parameter_list):
    """

    """
    waypoint = [10, 1]

    position = [0, 0]

    def rotate_waypoint(operation, waypoint):

        direction, degrees = 1 if operation[0] == "R" else - \
            1, int(operation[1:])

        # if clockwise - make it counter-clockwise
        if direction == 1: 
            degrees = 360 - degrees

        angle = np.deg2rad(degrees)
        R = np.array([[np.cos(angle), -np.sin(angle)],
                      [np.sin(angle),  np.cos(angle)]])

        o = np.atleast_2d((0, 0))
        p = np.atleast_2d((waypoint[0], waypoint[1]))

        rotated_waypoint = np.squeeze((R @ (p.T-o.T) + o.T).T)

        # print("Rotated waypoint: %s" % rotate_waypoint)

        return rotated_waypoint

    def toward_waypoint(operation, waypoint, position):

        magnitude = list(map(lambda x: x * int(operation[1:]), waypoint))

        position[0] += magnitude[0]
        position[1] += magnitude[1]

        # print("Moved position: %s" % position)

        return position

    def move_waypoint(operation, waypoint):
        if operation[0] == "N":
            waypoint[1] += int(operation[1:])
        elif operation[0] == "E":
            waypoint[0] += int(operation[1:])
        elif operation[0] == "S":
            waypoint[1] -= int(operation[1:])
        else:
            waypoint[0] -= int(operation[1:])

        # print("Moved waypoint: %s" % waypoint)
        return waypoint

    for op in data:
        if op[0] in ["R", "L"]:
            waypoint = rotate_waypoint(op, waypoint)
        elif op[0] in ["F"]:
            position = toward_waypoint(op, waypoint, position)
        else:
            waypoint = move_waypoint(op, waypoint)

    return int(abs(round(position[0])) + abs(round(position[1])))


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, 'input.txt')

    data = []

    with open(inputfile) as f:
        for line in f.readlines():
            data.append(line.strip("\n"))

    print(f"Part 1 solution: {part1(data)}")

    print(f"Part 2 solution: {part2(data)}")

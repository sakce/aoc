import os
import re
from typing import Dict, List


def accumulate(ops: Dict, idx: int, acc: int) -> (int, int):
    op = ops.get(idx)
    acc += int(op['acc'])

    return acc, idx + 1


def jump(ops: Dict, idx: int) -> int:
    op = ops.get(idx)

    return idx + int(op['jmp'])


def no_op(idx: int) -> int:
    return idx + 1


def part1(ops: Dict) -> int:

    checked = []

    idx = 0
    acc = 0

    while idx not in checked:
        checked.append(idx)
        op = ops.get(idx)

        if 'acc' in op.keys():
            acc, idx = accumulate(ops, idx, acc)
        elif 'jmp' in op.keys():
            idx = jump(ops, idx)
        else:
            idx = no_op(idx)
    return acc


def do_the_thing_part2(ops: Dict) -> (int, List[int]):

    checked = []

    idx = 0
    acc = 0

    while idx not in checked:
        if idx == 645:
            checked.append(idx)
            break
        else:
            checked.append(idx)
            op = ops.get(idx)

            if 'acc' in op.keys():
                acc, idx = accumulate(ops, idx, acc)
            elif 'jmp' in op.keys():
                idx = jump(ops, idx)
            else:
                idx = no_op(idx)
    return acc, checked


def part2(ops: Dict) -> int:
    to_change = []
    for op in ops:
        if 'acc' in ops[op].keys():
            continue
        else:
            to_change.append(op)

    for ch in to_change:
        temp_ops = ops.copy()
        key = list(temp_ops[ch].keys())[0]
        value = list(temp_ops[ch].values())[0]

        if key == 'nop':
            temp_ops[ch] = {'jmp': value}
        else:
            temp_ops[ch] = {'nop': value}

        acc, checked = do_the_thing_part2(temp_ops)

        if len(ops) - 1 in checked:  # if the index of the last row has been checked
            return acc


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, 'input.txt')

    ops = {}
    with open(inputfile) as f:
        for idx, op in enumerate(f.readlines()):
            temp = op.strip("\n").split(" ")
            op_key, op_value = temp[0], temp[1]

            ops[idx] = {op_key: op_value}

    print(f"Part 1 solution: {part1(ops)}")

    print(f"Part 2 solution: {part2(ops)}")

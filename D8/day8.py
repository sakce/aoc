import os
import re
from typing import Dict, List


def accumulate(ops: Dict, idx: int, acc: int) -> (int, int):
    '''Update the accumulate value by the value of the current operation. 
    Return update acc and the index for the next operation'''
    op = ops.get(idx)
    acc += int(op['acc'])

    return acc, idx + 1


def jump(ops: Dict, idx: int) -> int:
    '''Return the index for the next operation
    based on the value of the jump operation'''

    op = ops.get(idx)

    return idx + int(op['jmp'])


def no_op(idx: int) -> int:
    '''Return the next index. Unnecessary function in general..'''
    return idx + 1


def part1(ops: Dict) -> int:

    checked = []

    idx = 0
    acc = 0

    while idx not in checked:  # go over the ops as long as we checked it before
        checked.append(idx)
        # get the sub-dictionary of the operation that is at the idx index
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
        if idx == len(ops) - 1:  # break out of the loop if it has checked the last item of the input
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

    # go over all the items that can be changed ('jmp', 'nop')
    for ch in to_change:
        temp_ops = ops.copy()
        # temporary save of the key and value
        key = list(temp_ops[ch].keys())[0]
        value = list(temp_ops[ch].values())[0]

        # change the temporary copy of the operations,
        # with an updated value for the operation that needs changing
        # nop - becomes -> jmp ; jmp - becomes -> nop
        if key == 'nop':
            temp_ops[ch] = {'jmp': value}
        else:
            temp_ops[ch] = {'nop': value}

        # perform the check on the updated version
        acc, checked = do_the_thing_part2(temp_ops)

        # break the loop if there is a version of
        # the operations that do not lead to an infinite loop
        if len(ops) - 1 in checked:
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

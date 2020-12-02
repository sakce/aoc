from typing import List

f = open('./input.txt', "r")

numbers = sorted([int(n[:-1]) for n in f.readlines()])[::-1]
print(numbers)

clean_n = []
for big in numbers:
    if big + numbers[-1] > 2020:
        continue
    else:
        clean_n.append(big)

print(clean_n, len(clean_n))


# First star
def find_two_numbers(numbers: List[int]):
    for n in numbers:
        for check in numbers:
            if n == check:
                continue
            elif n + check == 2020:
                print(n, check, n * check)

find_two_numbers(clean_n)

# Second star
def find_three_numbers(numbers: List[int]):
    for one in numbers:
        for two in numbers:
            for three in numbers:
                if one+two+three == 2020:
                    print(one, two, three, one*two*three)

find_three_numbers(numbers)
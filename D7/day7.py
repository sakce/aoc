import os
import re
import queue


def find_shiny_part_one(data, target):

    bags_to_check = queue.Queue()

    bags_to_check.put(target)
    possible = set()

    def check_bag_contents(target):
        for bag, contents in data.items():
            for _, color in contents:
                if color == target:
                    bags_to_check.put(bag)
                    possible.add(bag)

    while not bags_to_check.empty():
        check_bag_contents(bags_to_check.get())

    return len(possible)


def find_shiny_part_two(data, target):
    bags_to_check = queue.Queue()
    bags_to_check.put(target)

    total_contained = 0

    def check_bag_contents(target):
        nonlocal total_contained

        for x in data[target]:
            if x[0] != "no":
                total_contained += int(x[0])

                [bags_to_check.put(x[1]) for _ in range(int(x[0]))]

    while not bags_to_check.empty():
        check_bag_contents(bags_to_check.get())

    return total_contained


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, 'input.txt')

    with open(inputfile) as f:
        rules = [rule.strip("\n") for rule in f.readlines()]

    pattern = re.compile(r"\d+ ([\w ]+) bags?")

    rules_dict = {}

    for rule in rules:
        outer_bag, inner_bags = rule.split(" bags contain ")
        inner_bags = inner_bags.replace(" bags", "").replace(
            " bag", "").strip(".").split(", ")

        rules_dict[outer_bag] = [((contained.split(" ", maxsplit=1)[0], contained.split(
            " ", maxsplit=1)[1])) for contained in inner_bags]

    target = "shiny gold"
    print(f"Part 1 solution: {find_shiny_part_one(rules_dict, target)}")

    print(f"Part 2 solution: {find_shiny_part_two(rules_dict, target)}")

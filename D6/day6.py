import os

def count_questions_part_one(inputfile):
    q_count = 0 
    tmp_group = []

    with open(inputfile) as f:
        for line in f.readlines():
            if line != "\n":
                tmp_group.extend(list(line.strip("\n")))

            else: # When empty line
                q_count += len(set(tmp_group))
                tmp_group = []

    return q_count

def count_questions_part_two(inputfile):
    q_count = 0 
    tmp_group = []

    with open(inputfile) as f:
        for line in f.readlines():
            if line != "\n":
                tmp_group.append(list(line.strip("\n")))

            else: # When empty line
                common_qs = set.intersection(*map(set, tmp_group)) # find common elements of lists
                q_count += len(set(common_qs))
                tmp_group = []

    return q_count


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, 'input.txt')

    print(f"Part 1 solution: {count_questions_part_one(inputfile)}")

    print(f"Part 2 solution: {count_questions_part_two(inputfile)}")


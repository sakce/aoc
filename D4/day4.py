import os
import re
from typing import Dict, List

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def read_input(filename):
    passports = []

    # To be able to read the last passport, two blank lines are needed...
    with open(filename, "a") as f:
        f.write("\n")
        f.write("\n")
    f.close()

    with open(filename, "r") as f:

        temp = dict()

        for line in f.readlines():
            # If it's a break line, passport is complete, start a new one
            if line == "\n":
                passports.append(temp)
                temp = dict()
            else:  # While we're between break lines, add all the keys of the passport
                pass_line = line.strip("\n").split(" ")
                for field in pass_line:
                    # 1st part is the key, up to the ":", 2nd - value
                    temp[str(field[:3])] = field[4:]
    return passports


def check_necessary_fields(passport_list: List[dict]):
    nec_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl',
                  'ecl', 'pid')  # 'cid' missing on purpose

    count = 0

    invalids = []
    valid_passports = []

    for passport in passports:
        if set(nec_fields).issubset(passport):
            count += 1
            valid_passports.append(passport)

        else:
            invalids.append(passport)
    return valid_passports, count


# Second star
def perform_check(single_pass: Dict):
    '''
    Performs the necessary checks on an individual passport that's previously 
    been checked for necessary fields.
    -> cid is optional

    returns True if the password is valid, False otherwise
    '''

    is_valid = [  # Birth year
        (len(single_pass["byr"]) and (
            1920 <= int(single_pass["byr"]) <= 2002)),
        # Issuance year
        (len(single_pass["iyr"]) and (
            2010 <= int(single_pass["iyr"]) <= 2020)),
        # Expiration year
        (len(single_pass["eyr"]) and (
            2020 <= int(single_pass["eyr"]) <= 2030)),
        # Hair color
        (re.match(r"^#(?:[0-9a-f]{6})$",
                  single_pass['hcl']) is not None),
        # Height
        ((re.match(r"^#(?:[0-9a-f]{6})$", single_pass['hcl']) is not None) or
         ("in" in single_pass['hgt'] and (59 <= int(single_pass['hgt'][:-2]) <= 76)))]

    return all(is_valid)


if __name__ == "__main__":

    passports = read_input(inputfile)
    valid_passports, count_part_one = check_necessary_fields(passports)

    # Print number of valid passports for Part 1
    print(count_part_one)

    # Print number of valid passports for Part 2
    print(sum([perform_check(passport) for passport in valid_passports]))

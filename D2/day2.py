f = open("./input.txt", "r")
lines = [(line.split(":")[0], line.split(":")[1]) for line in f.readlines()]


def find_good_pass_n(lines):
    count = 0
    for password in lines:

        minlet, maxlet, let = password[0].split("-")[0], password[0].split("-")[1].split(" ")[0], password[0].split("-")[1].split(" ")[1]
        # print(minlet, maxlet, let)

        # print(password[1].count(password[0][-1]))
        if (password[1].count(let) < int(minlet)) or (password[1].count(let) > int(maxlet)):
            pass
        else:
            count+=1
    print(count)
find_good_pass_n(lines)

def find_good_second_star(lines):
    count = 0
    for password in lines:

        gucci = False

        minpos, maxpos, let = int(password[0].split("-")[0]), int(password[0].split("-")[1].split(" ")[0]), password[0].split("-")[1].split(" ")[1]

        if (password[1][minpos] == let):
            if password[1][maxpos] == let:
                pass
            else:
                count += 1 
                gucci = True
        else:
            if password[1][maxpos] == let:
                count += 1
                gucci = True
            else:
                pass

    print(count)
find_good_second_star(lines)
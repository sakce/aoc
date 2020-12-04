using Combinatorics

nums = [] # there must be a more Julian way to init empty array..

open("input.txt") do f
    for num in enumerate(eachline(f))
        push!(nums, parse(Int32, num[2]))
    end
end

sorted_nums = sort(nums, rev = true)

cleaner_nums = []

for big_num in sorted_nums
    if big_num + sorted_nums[end] > 2020
        continue
    else
        push!(cleaner_nums, big_num)
    end
end

function part1(num_list)
    a = Int32
    b = Int32

    for num in enumerate(num_list)
        if 2020 - num[2] in num_list[num[1]:end]
            a = num[2]
            b = 2020 - num[2]
        else
            popfirst!(num_list)
        end
    end
    return a * b
end

println(part1(cleaner_nums))


function part2(num_list)
    min_val = num_list[end]
    min_2_val = num_list[end-1]
    max_val = num_list[1]

    clean_vals = filter(<=(2020 - min_val - min_2_val), num_list)

    for comb in combinations(cleaner_nums, 3)
        if sum(comb) == 2020
            return prod(comb)
        end
    end
end

println(part2(cleaner_nums))


# Advent of Code Day 5: https://adventofcode.com/2022/day/5
# Problem Created by Eric Wastl
# Solution by Nicolle M

import pandas as pd

# Util function
def print_top_of_stacks(stacks):    
    top_of_stack = ""
    for i in range(1, len(list(stacks.keys()))+1):
        top_of_stack += stacks[i][-1]

    print("Top of Stacks: {}".format(top_of_stack))

# Stacks for Part 1 - from problem input file 
Stacks = {
    1: ["W", "R", "F"],
    2: ["T", "H", "M", "C", "D", "V", "W", "P"],
    3: ["P", "M", "Z", "N", "L"],
    4: ["J", "C", "H", "R"],
    5: ["C", "P", "G", "H", "Q", "T", "B"],
    6: ["G", "C", "W", "L", "F", "Z"],
    7: ["W", "V", "L", "Q", "Z", "J", "G", "C"],
    8: ["P", "N", "R", "F", "W", "T", "V", "C"],
    9: ["J", "W", "H", "G", "R", "S", "V"]
}

# Read in Input using Pandas to DataFrame
df = pd.read_csv("input.txt", names=["instruction"])

print(df)

# Split instructions into num_to_be_moved, start_stack, end_stack
def parse_instruction(row):
    temp = row.instruction.split()
    row["num_move"], row["start_stack"], row["end_stack"] = int(temp[1]) , int(temp[3]), int(temp[5])
    return row

df = df.apply(lambda x: parse_instruction(x), axis=1)

print(df)

# Based on num_move, start_stack, end_stack -> move creates one at a time 
def move_crates(row):
    for i in range(0, row.num_move):
        pop_crate = Stacks[row.start_stack].pop()
        Stacks[row.end_stack].append(pop_crate)

df.apply(lambda x: move_crates(x), axis=1)

print("\nPart 1 Result")
print_top_of_stacks(Stacks)

# Stacks for Part 2
Stacks2 = {
    1: ["W", "R", "F"],
    2: ["T", "H", "M", "C", "D", "V", "W", "P"],
    3: ["P", "M", "Z", "N", "L"],
    4: ["J", "C", "H", "R"],
    5: ["C", "P", "G", "H", "Q", "T", "B"],
    6: ["G", "C", "W", "L", "F", "Z"],
    7: ["W", "V", "L", "Q", "Z", "J", "G", "C"],
    8: ["P", "N", "R", "F", "W", "T", "V", "C"],
    9: ["J", "W", "H", "G", "R", "S", "V"]
}

# Based on num_move, start_stack, end_stack -> move creates while preserving order
def move_multiple_crates(row):
    crates_to_be_moved = Stacks2[row.start_stack][-row.num_move:]
    Stacks2[row.start_stack] = Stacks2[row.start_stack][:-row.num_move]
    Stacks2[row.end_stack].extend(crates_to_be_moved)

df.apply(lambda x: move_multiple_crates(x), axis=1)

print("\nPart 2 Result")
print_top_of_stacks(Stacks2)
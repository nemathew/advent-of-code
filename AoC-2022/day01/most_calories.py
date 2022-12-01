# Advent of Code Day 1: https://adventofcode.com/2022/day/1
# Problem Created by Eric Wastl
# Solution by Nicolle M

elves_list = []

# function that takes in temp_list (list of calorie count for single elf)
# adds sum of values to global list `elves_list`
def sum_list(temp_list):
    elves_list.append(sum(temp_list))

# Read each line from file 
with open('input.txt') as f:
    temp_list = []
    for line in f.readlines():
        # Determine if line is not a newline break
        if line != "\n":
            temp_list.append(int(line)) # if not \n -> add to temp_list
        else :
            # else -> this elf is complete, sum values and rest temp_list
            sum_list(temp_list)
            temp_list = []
    

print("Elves Total Calorie Counts: \n{}\n".format(elves_list))

print("Top Calorie Count: {}\n".format(max(elves_list)))

# Reverse sort global list `elves_list` to get top three entries
top_three = sorted(elves_list, reverse=True)[:3]

print("Top Three Calorie Counts: {}\n".format(top_three))
print("Top Three Total Calories: {}\n".format(sum(top_three)))
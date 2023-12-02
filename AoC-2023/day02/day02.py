# Advent of Code Day 2: https://adventofcode.com/2023/day/2
# Problem Created by Eric Wastl
# Solution by Nicolle M

import sys

input_list = []

# Read each line from file 
with open('input.txt') as f:
    for line in f.readlines():
        # Determine if line is not a newline break
        if line != "\n":
            input_list.append(str(line)) # if not \n -> add to temp_list

###### Part 1 ##########################################################
game_dict = {}

for i in range(0,len(input_list)):
    temp_str = input_list[i]
    temp_str_outcomes = temp_str.split(":")[-1]
    game_dict[i+1] = temp_str_outcomes

for i in game_dict.keys():
    draws = game_dict[i].split(";")
    temp_dict = {}
    for d in draws: 
        blocks_list = d.split(', ')
        for b in blocks_list:
            b = b.strip()
            color_count, color = b.split( )
            if color in temp_dict.keys():
                temp_dict[color].append(int(color_count))
            else:
                temp_dict[color] = []
                temp_dict[color].append(int(color_count))

    for color in temp_dict.keys():
        temp_dict[color] = max(temp_dict[color])

    game_dict[i] = temp_dict

min_color_count = {"red":12, "green": 13, "blue":14}

sum = 0
for game in game_dict.keys():
    color_counts = game_dict[game]
    if color_counts["red"] <= min_color_count["red"] and color_counts["green"] <= min_color_count["green"] and color_counts["blue"] <= min_color_count["blue"]:
        sum += game

print("Part 1 Solution: ")  
print(sum)

###### Part 2 ##########################################################

min_cubes_power_sum = 0
for game in game_dict.keys():
    color_counts = game_dict[game]
    power = color_counts["red"] * color_counts["green"] * color_counts["blue"]
    min_cubes_power_sum += power

print("Part 2 Solution: ")  
print(min_cubes_power_sum)
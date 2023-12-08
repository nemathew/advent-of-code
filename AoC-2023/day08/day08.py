# Advent of Code Day 8: https://adventofcode.com/2023/day/8
# Problem Created by Eric Wastl
# Solution by Nicolle M

import math
input_list = []

# Read each line from file 
with open('input.txt') as f:
    for line in f.readlines():
        # Determine if line is not a newline break
        if line != "\n":
            input_list.append(str(line.strip())) # if not \n -> add to temp_list

###### Part 1 ##########################################################
directions = list(input_list[0])
nodeDict = {}

for i in input_list[1:]:
    node, leafs = i.split("=")
    node = node.strip()
    left, right = leafs.split(",")

    nodeDict[node] = [left.strip()[1:], right[:-1].strip()]

current_node = 'AAA'
steps_count = 0

while current_node != 'ZZZ':
    for i in range(0, len(directions)):
        steps_count += 1
        if directions[i] == "L":
            temp_node = current_node
            current_node = nodeDict[temp_node][0]
        else: 
            temp_node = current_node
            current_node = nodeDict[temp_node][1]

print("Part 1 Solution: ") 
print(steps_count)

###### Part 2 ##########################################################
startNodes = list({key: val for key, val in nodeDict.items() if key.endswith("A")}.keys())
endNodes = list({key: val for key, val in nodeDict.items() if key.endswith("Z")}.keys())

step_count2 = []

for i in range(0, len(startNodes)):
    current_node_2 = startNodes[i]
    count = 0

    while current_node_2[-1] != 'Z':
        for dir in range(0, len(directions)):
            count += 1
            if directions[dir] == "L":
                temp_node_2 = current_node_2
                current_node_2 = nodeDict[temp_node_2][0]
            else: 
                temp_node_2 = current_node_2
                current_node_2 = nodeDict[temp_node_2][1]
    
    step_count2.append(count)

part2 = math.lcm(*step_count2)

print("Part 2 Solution: ") 
print(part2)



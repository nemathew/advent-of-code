# Advent of Code Day 3: https://adventofcode.com/2023/day/3
# Problem Created by Eric Wastl
# Solution by Nicolle M

input_list = []
gears = {}

# Read each line from file 
with open('input.txt') as f:
    for line in f.readlines():
        # Determine if line is not a newline break
        if line != "\n":
            input_list.append(str(line.strip())) # if not \n -> add to temp_list

HEIGHT = len(input_list)
WIDTH = len(input_list[0])

def isSymbol(row, col):
    # if current row,col is outside grid dimensions, return False
    if (row < 0 or row >= HEIGHT) or (col < 0 or col >= WIDTH):
        return False
    else:
        current_space = input_list[row][col]
        # check if current_space is a number or a ".", return False
        if current_space.isdigit() or current_space==".":
            return False
        # else must be a symbol so return True
        else:
            return True

def maybeGear(num, row, col):
    # is symbol at row,col a "*"
    if input_list[row][col] == "*":
        # add num to key,value list as potential gear
        if (row, col) in gears.keys():
            gears[(row, col)].append(num)
        else:
            gears[(row, col)] =[num]

def checkAdjacentSpaces(row, start, end):
    # check spaces horizontally next to start/end for symbol
    num = int(input_list[row][start:end])
    if isSymbol(row,start-1):
        maybeGear(num, row, start-1)
        return True

    if isSymbol(row,end):
        maybeGear(num, row, end)
        return True
    
    # check spaces in row above
    for i in range(start-1, end+1):
        if isSymbol(row-1,i):
            maybeGear(num, row-1, i)
            return True
            
    # check space in row below
    for i in range(start-1, end+1):
        if isSymbol(row+1,i):
            maybeGear(num, row+1, i)
            return True
    
    return False

###### Part 1 ##########################################################
sum = 0

for i, line in enumerate(input_list):
    current_index = 0
    start_index = 0
    current_num = ""

    #loop through all chars in string line
    while current_index < len(line):
        start_index = current_index

        # check that index is within array dimensions and if it is a digit
        while current_index < WIDTH and line[current_index].isdigit():
            # if it is a digit append to current_num str and increment index
            current_num += line[current_index]
            current_index+=1

        # current_num ended
        # check if digits from start_index to current_index have any symbols adjacent to them
        if current_num != "":
            if checkAdjacentSpaces(i, start_index, current_index):
                sum = sum + int(current_num)
            current_num = ""
            
        current_index += 1
        
print("Part 1 Solution: ")  
print(sum)

###### Part 2 ##########################################################

# remove any possible gears that have len(value list) != 2
gears = {k: v for k, v in gears.items() if len(v) == 2}

gearRatioProduct = 0

# for all remaining gears, calculate gearRatioProduct and add to total sum
for v in gears.values():
    gearRatioProduct += (v[0] * v[1])

print("Part 2 Solution: ")  
print(gearRatioProduct)
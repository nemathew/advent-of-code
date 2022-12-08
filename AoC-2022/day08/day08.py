# Advent of Code Day 8: https://adventofcode.com/2022/day/8
# Problem Created by Eric Wastl
# Solution by Nicolle M

forest = []
visableTreeCount = 0

# Read in the input file
with open('input.txt') as f:
    temp_list = []
    for line in f.readlines():
        forest.append([int(d) for d in str(line.strip())])

# Part 1
for i in range(0, len(forest)):    
    for j in range(0, len(forest[i])):

        tree = forest[i][j]

        # top 
        top_list = []
        for t in range(0, i):
            top_list.append(forest[t][j])
        # bottom
        bottom_list = []
        for b in range(i + 1, len(forest)):
            bottom_list.append(forest[b][j])

        left_list = []
        for l in range(0, j):
            left_list.append(forest[i][l])
            
        right_list = []
        for r in range(j+1, len(forest[i])):
            right_list.append(forest[i][r])
            
        isVisTop, isVisBottom, isVisLeft, isVisRight = False, False, False, False

        if top_list == [] or max(top_list) < tree:
            isVisTop = True
        if bottom_list == [] or max(bottom_list) < tree:
            isVisBottom = True
        if left_list == [] or max(left_list) < tree:
            isVisLeft = True
        if right_list == [] or max(right_list) < tree:
            isVisRight = True

        if isVisTop or isVisBottom or isVisLeft or isVisRight:
            visableTreeCount += 1
        
print("Number of visible trees: {}".format(visableTreeCount))

    
# Part 2
view_dist_map = {}

for i in range(1, len(forest) - 1):
    for j in range(1, len(forest[i])-1):
        # calculate view distance
        
        #top 
        t = i - 1
        top_count = 0
        while not t < 0:
            t_tree = forest[t][j]
            current_tree = forest[i][j]

            if t_tree > current_tree:
                break
            elif t_tree == current_tree:
                top_count += 1
                break
            else:
                top_count += 1
                t -= 1

        #left 
        l = j - 1
        left_count = 0
        while not l < 0:
            l_tree = forest[i][l]
            current_tree = forest[i][j]

            if l_tree > current_tree:
                break
            elif l_tree == current_tree:
                left_count += 1
                break
            else:
                left_count += 1
                l -= 1

        #bottom 
        b = i + 1
        bottom_count = 0
        while b < len(forest):
            b_tree = forest[b][j]
            current_tree = forest[i][j]

            if b_tree > current_tree:
                break
            elif b_tree == current_tree:
                bottom_count += 1
                break
            else:
                bottom_count += 1
                b += 1

        #right 
        r = j + 1
        right_count = 0
        while r < len(forest[i]):
            r_tree = forest[i][r]
            current_tree = forest[i][j]

            if r_tree > current_tree:
                break
            elif r_tree == current_tree:
                right_count += 1
                break
            else:
                right_count += 1
                r += 1

        view_dist_map[(i,j)] = top_count * bottom_count * left_count * right_count

print("Max Viewing Distance Score: {}".format(max(view_dist_map.values())))



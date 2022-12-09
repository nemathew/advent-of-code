# Advent of Code Day 9: https://adventofcode.com/2022/day/9
# Problem Created by Eric Wastl
# Solution by Nicolle M
import math

# Read in the input file
directions = []
with open('input.txt') as f:
    for line in f.readlines():
        temp = line.split()
        directions.append([temp[0], int(temp[1])])

# Part 1
positions_visited = {}
head = (0,0)
tail = (0,0)

positions_visited[tail] = 1

for direction in directions:
    movement_dir = direction[0]
    steps = direction[1]

    for s in range(0, steps):
        if movement_dir == 'L':
            new_head = (head[0] - 1, head[1])
            if new_head[0] == tail[0] and new_head[1]==tail[1]:
                new_tail = tail
            elif math.dist([new_head[0]], [tail[0]]) > 1.0 and new_head[1] == tail[1]:
                new_tail = (tail[0] -1, tail[1])
            elif math.dist([new_head[0]], [tail[0]]) <= 1.0 and math.dist([new_head[1]], [tail[1]]) <= 1.0:
                new_tail = tail
            else:
                new_tail = head
        elif movement_dir == 'R':
            new_head = (head[0] + 1, head[1])
            if new_head[0] == tail[0] and new_head[1]==tail[1]:
                new_tail = tail
            elif math.dist([new_head[0]], [tail[0]]) > 1.0 and new_head[1] == tail[1]:
                new_tail = (tail[0] + 1, tail[1])
            elif math.dist([new_head[0]], [tail[0]]) <= 1.0 and math.dist([new_head[1]], [tail[1]]) <= 1.0:
                new_tail = tail
            else:
                new_tail = head
        elif movement_dir == 'U' :
            new_head = (head[0], head[1] + 1)
            
            if new_head[0] == tail[0] and new_head[1]==tail[1]:
                new_tail = tail            
            elif math.dist([new_head[1]], [tail[1]]) > 1.0 and new_head[0] == tail[0]:
                new_tail = (tail[0], tail[1]+1)
            elif math.dist([new_head[1]], [tail[1]]) <= 1.0 and math.dist([new_head[0]], [tail[0]]) <= 1.0:
                new_tail = tail
            else:
                new_tail = head
        else:
            new_head = (head[0], head[1]-1)
            if new_head[0] == tail[0] and new_head[1]==tail[1]:
                new_tail = tail
            elif math.dist([new_head[1]], [tail[1]]) > 1.0 and new_head[0] == tail[0]:
                new_tail = (tail[0], tail[1] - 1)
            elif math.dist([new_head[1]], [tail[1]]) <= 1.0 and math.dist([new_head[0]], [tail[0]]) <= 1.0:
                new_tail = tail
            else:
                new_tail = head

        head = new_head
        tail = new_tail

        if tail not in positions_visited.keys():
            positions_visited[tail] = 1

print("Number of positions visited by tail: {}".format(len(positions_visited.keys())))


# Part 2

long_rope_tail_pos = {}
long_rope_tail_pos[(0,0)] = 1

long_rope = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

for direction in directions:
    movement_dir = direction[0]
    steps = direction[1]

    for s in range(0, steps):


        if movement_dir == 'L': #left
            long_rope[0] = (long_rope[0][0] - 1, long_rope[0][1])
        elif movement_dir == 'R': # right
            long_rope[0] = (long_rope[0][0] + 1, long_rope[0][1])
        elif movement_dir == 'U': # up
            long_rope[0] = (long_rope[0][0], long_rope[0][1] + 1)
        else: # down
            long_rope[0] = (long_rope[0][0], long_rope[0][1] - 1)

        for i in range(1, len(long_rope)):
            if long_rope[i][0] == long_rope[i-1][0] and long_rope[i][1] == long_rope[i-1][1]:
                continue
            elif math.dist([long_rope[i][0]], [long_rope[i-1][0]]) <= 1 and math.dist([long_rope[i][1]], [long_rope[i-1][1]]) <= 1:
                continue
            # check if only x value changed (left or right) and in same row 
            elif math.dist([long_rope[i][0]], [long_rope[i-1][0]]) > 1 and long_rope[i][1] == long_rope[i-1][1]:
                if long_rope[i-1][0] < long_rope[i][0]: # moved left 
                    long_rope[i] = (long_rope[i][0]-1, long_rope[i][1])
                else: # moved right
                    long_rope[i] = (long_rope[i][0]+1, long_rope[i][1])
            # check if only y value changed (down or up) and in same column
            elif math.dist([long_rope[i][1]], [long_rope[i-1][1]]) > 1 and long_rope[i][0] == long_rope[i-1][0]:
                if long_rope[i-1][1] < long_rope[i][1]: # moved down 
                    long_rope[i] = (long_rope[i][0], long_rope[i][1]-1)
                else: # moved up
                    long_rope[i] = (long_rope[i][0], long_rope[i][1]+1)
            # diagonal change
            elif math.dist([long_rope[i][0]], [long_rope[i-1][0]]) > 1 or math.dist([long_rope[i][1]], [long_rope[i-1][1]]) > 1:
                if long_rope[i - 1][0] < long_rope[i][0]:
                     long_rope[i] = (long_rope[i][0]-1, long_rope[i][1])
                else:
                    long_rope[i] = (long_rope[i][0]+1, long_rope[i][1])
                if long_rope[i - 1][1] < long_rope[i][1]:
                     long_rope[i] = (long_rope[i][0], long_rope[i][1]-1)
                else:
                    long_rope[i] = (long_rope[i][0], long_rope[i][1]+1)
                

        if long_rope[-1] not in long_rope_tail_pos:
            long_rope_tail_pos[long_rope[-1]] = 1

print("Part 2 - Number of positions visited by tail: {}".format(len(long_rope_tail_pos.keys())))
#print(sorted(long_rope_tail_pos.keys()))
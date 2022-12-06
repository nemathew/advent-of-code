# Advent of Code Day 6: https://adventofcode.com/2022/day/6
# Problem Created by Eric Wastl
# Solution by Nicolle M

# Util Functions + Global Variables
def start_of_search(len_val):
    queue = list(message_str[0:len_val])

    for i in range(len(message_str)):
        queue.pop(0)
        queue.append(message_str[i])

        if len(set(queue)) == len(queue):
            print("# of Chars before start-of: {}".format(i+1))
            break

message_str = ""

# Read input from file 
with open('input.txt') as f:
    message_str = ''.join(f.readlines())

# Part 1
start_of_search(4)

# Part 2
start_of_search(14)

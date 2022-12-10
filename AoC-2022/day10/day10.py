# Advent of Code Day 10: https://adventofcode.com/2022/day/10
# Problem Created by Eric Wastl
# Solution by Nicolle M
import math

operations = []
cycles = {}

register = 1
current_cycle = 1


with open('input.txt') as f:
    for line in f.readlines():
        operations.append(line.split())

for op in operations:
    if op[0] == 'addx':
        cycles[current_cycle] = register
        current_cycle += 1  
        cycles[current_cycle] = register
        current_cycle += 1  
        register += int(op[1])
    else:
        cycles[current_cycle] = register
        current_cycle += 1

sum = 0
for i in range(20, 221, 40):
    sum += i * cycles[i]

print("Sum: {}".format(sum))


# Part 2

pixels = [[None]*40,[None]*40,[None]*40,[None]*40,[None]*40,[None]*40]

sort_keys = sorted(list(cycles.keys()))

for key in sort_keys:
    pix_l = math.floor((key-1) / 40)
    pixel_pos = ((key-1) % 40) 

    reg = cycles[key]

    if pixel_pos >= reg-1 and pixel_pos <= reg+1:
        pixels[pix_l][pixel_pos] = '#'
    else:
        pixels[pix_l][pixel_pos] = '.'

print(''.join(pixels[0]))
print(''.join(pixels[1]))
print(''.join(pixels[2]))
print(''.join(pixels[3]))
print(''.join(pixels[4]))
print(''.join(pixels[5]))

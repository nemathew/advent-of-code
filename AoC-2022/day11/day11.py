# Advent of Code Day 11: https://adventofcode.com/2022/day/11
# Problem Created by Eric Wastl
# Solution by Nicolle M

from dataclasses import dataclass


@dataclass
class Monkey:
    def __init__(self, name, items):
        self.name = name
        self.item_list = items
    
    def op_worry(item, op):
        old = item
        eval(op)

    



monkeys = {}
current_monkey = ""

def test(item, divisor, true_monkey, false_monkey):
        if item % divisor == 0:
            return true_monkey
        else:
            return false_monkey

with open('input.txt') as f:
    for line in f.readlines():
        monkeys.append(line.split())
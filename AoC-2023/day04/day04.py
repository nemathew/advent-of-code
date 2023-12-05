# Advent of Code Day 4: https://adventofcode.com/2023/day/4
# Problem Created by Eric Wastl
# Solution by Nicolle M

import pandas as pd
input_list = []
cards = {}

# Read each line from file 
with open('input.txt') as f:
    for line in f.readlines():
        # Determine if line is not a newline break
        if line != "\n":
            input_list.append(str(line.strip())) # if not \n -> add to temp_list

###### Part 1 ##########################################################
df = pd.DataFrame(columns=["winning_nums", "your_nums"])

# for each card in list
for i, line in enumerate(input_list):
    # remove card prefix
    line = line.split(":")[1]

    # split winning_nums and your_nums using "|"
    nums = line.split("|")
    winning_nums = nums[0].strip().split()
    your_nums = nums[1].strip().split()

    # add row to df with card num = index, columns = winning_nums, your_nums
    df.loc[i+1] = {"winning_nums": winning_nums, "your_nums": your_nums}

def findWinningNums(winning_nums, your_nums):
    your_winning_nums = []
    # create list of your numbers that are in winning numbers and return
    for i in your_nums:
        if i in winning_nums:
            your_winning_nums.append(i)
    return your_winning_nums

def score(winning_count):
    score = 0
    # calculate score starting from 1 to num_of_winning nums + 1
    #if winning count = 0 then, range would be 1-1 which will not go through loop
    for i in range(1, winning_count+1):
        if i == 1:
            score += 1
        else:
            score = score * 2
    return score

df["your_winning_nums"] = df.apply(lambda x: findWinningNums(x.winning_nums, x.your_nums), axis = 1)
df["score"] = df.apply(lambda x: score(len(x.your_winning_nums)), axis = 1)

total_score = df.score.sum()

print("Part 1 Solution: ")  
print(total_score)

###### Part 2 ##########################################################
df["countOfWinners"] = df.apply(lambda x: len(x.your_winning_nums), axis = 1)

# iterate through rows in df
for i, row in enumerate(df.itertuples(), start=1):
    # add 1 to current_card count as you have this card 
    if i in cards.keys():
        cards[i] += 1
    else:
        cards[i] = 1

    # count of current card 
    num_of_current_card = cards[i]

    # using range of next card to next card + winningCount
    # add (1 * the number of current cards you have (accounts for copies won))
    for cardNum in range(i+1, i+1 + row.countOfWinners):
        if cardNum in cards.keys():
            cards[cardNum] += 1 * num_of_current_card
        else:
            cards[cardNum] = 1  * num_of_current_card

print("Part 2 Solution: ")  
print (sum(cards.values()))
# Advent of Code Day 1: https://adventofcode.com/2022/day/1
# Problem Created by Eric Wastl
# Solution by Nicolle M

import pandas as pd

# Part 1 - X=A=1, Y=B=2, Z=C=3, WIN = 6, LOSE = 0, DRAW = 3
point_rubric = {"X": 1, "Y": 2, "Z": 3}

df = pd.read_csv("input.txt", names=["elves", "you"], delimiter=" ")

def return_score(row):
    score = 0
    score += point_rubric[row.you]

    if row.you == "X":
        if row.elves == "A":
            score += 3
        elif row.elves == "C":
            score += 6

    elif row.you == "Y":
        if row.elves == "B":
            score += 3
        elif row.elves == "A":
            score += 6
    else:
        if row.elves == "C":
           score += 3
        elif row.elves == "B":
           score += 6
    
    return score

df["your_score"] = df.apply(lambda x: return_score(x), axis=1)

print("Your Total Score: {}".format(sum(df.your_score)) )

# Part 2 - I realized I could simplify everything a lot a little late in the puzzle today
# X=LOSE, Y=DRAW, Z=WIN, ROCK = 1, PAPER = 2, SCISSORS = 3

end_point_rubric = {"X": 0, "Y": 3, "Z": 6}
winning_rubric = {"A": 2, "B": 3, "C": 1}
lose_rubric = {"A": 3, "B": 1, "C": 2}
draw_rubric = {"A": 1, "B": 2, "C": 3}

def return_score_2(row):
    score = 0

    # first add the resulting points based on whether you should win/lose/draw
    score += end_point_rubric[row.you]

    # if win -> add winning_rubric value for key=elves_choice
    if row.you == "X":
        score += lose_rubric[row.elves]
    # if draw -> add draw_rubric value for key=elves_choice
    elif row.you == "Y":
        score += draw_rubric[row.elves]
    # if lose -> add lose_rubric value for key=elves_choice
    else:
        score += winning_rubric[row.elves]

    return score

df["your_score_2"] = df.apply(lambda x: return_score_2(x), axis=1)    

print("Your Total Score 2: {}".format(sum(df.your_score_2)) )
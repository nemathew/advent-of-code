# Advent of Code Day 1: https://adventofcode.com/2022/day/1
# Problem Created by Eric Wastl
# Solution by Nicolle M

import pandas as pd

# Read in Input using Pandas to DataFrame
df = pd.read_csv("input.txt", names=["elves", "you"], delimiter=" ")

# Part 1 - X=A=1, Y=B=2, Z=C=3, WIN = 6, LOSE = 0, DRAW = 3
point_rubric = {"X": 1, "Y": 2, "Z": 3}
game_res_scores = {
    # if you choose X and Elves choose: 
    #       A=draw=3pts, B=lose=0pts, C=win=6pts
    "X": { "B" : 0, "A" : 3, "C" : 6},
    # if you choose Y and Elves choose: 
    #       A=win=6pts, B=draw=3pts, C=lose=0pts
    "Y": { "C" : 0, "B" : 3, "A" : 6},
    # if you choose Z and Elves choose: 
    #       A=lose=0pts, B=win=6pts, C=draw=3pts
    "Z": { "A" : 0, "C" : 3, "B" : 6}
}

def return_score(row):
    # add points for shape you choose based on row.you
    # add points for result from game due to shape chosen 
    return point_rubric[row.you] + game_res_scores[row.you][row.elves]
    
df["your_score"] = df.apply(lambda x: return_score(x), axis=1)

print("Your Total Score: {}".format(sum(df.your_score)) )

# Part 2 - X=LOSE, Y=DRAW, Z=WIN, ROCK = 1, PAPER = 2, SCISSORS = 3
end_res_rubric = {"X": 0, "Y": 3, "Z": 6}
game_points_score = {
    # if you want to lose=X and Elves choose: 
    # A=rock -> you choose 3=scissors, B=paper -> you choose 1=rock, C=sciccors -> you choose 2=paper
    "X": { "A": 3, "B": 1, "C": 2 },
    # if you want to draw=Y and Elves choose: 
    # A=rock -> you choose 1=rock, B=paper -> you choose 2=paper, C=sciccors -> you choose 3=scissors
    "Y": { "A": 1, "B": 2, "C": 3 },
    # if you want to win=Z and Elves choose: 
    # A=rock -> you choose 2=paper, B=paper -> you choose 3=scissors, C=sciccors -> you choose 1=rock
    "Z": { "A": 2, "B": 3, "C": 1 }
}

def return_score_2(row):
    # add points for win/lose/draw based on row.you
    # add points for which shape you choose to get result
    return end_res_rubric[row.you] + game_points_score[row.you][row.elves]

df["your_score_2"] = df.apply(lambda x: return_score_2(x), axis=1)    

print("Your Total Score 2: {}".format(sum(df.your_score_2)) )


# #################### Appendix ############################
#-----------------------------
# Original Solve for part 1  |
#-----------------------------
#     score = 0
#     score += point_rubric[row.you]
#     if row.you == "X":
#         if row.elves == "A":
#             score += 3
#         elif row.elves == "C":
#             score += 6
#     elif row.you == "Y":
#         if row.elves == "B":
#             score += 3
#         elif row.elves == "A":
#             score += 6
#     else:
#         if row.elves == "C":
#            score += 3
#         elif row.elves == "B":
#            score += 6
#
#-----------------------------
# Original Solve for part 2  |
#-----------------------------
# winning_rubric = {"A": 2, "B": 3, "C": 1}
# lose_rubric = {"A": 3, "B": 1, "C": 2}
# draw_rubric = {"A": 1, "B": 2, "C": 3}
#
# score = 0
# score += end_res_rubric[row.you]
# # if win -> add winning_rubric value for key=elves_choice
# if row.you == "X":
#     score += lose_rubric[row.elves]
# # if draw -> add draw_rubric value for key=elves_choice
# elif row.you == "Y":
#     score += draw_rubric[row.elves]
# # if lose -> add lose_rubric value for key=elves_choice
# else:
#     score += winning_rubric[row.elves]
# Advent of Code Day 6: https://adventofcode.com/2023/day/6
# Problem Created by Eric Wastl
# Solution by Nicolle M

import pandas as pd
input_list = []

# Read each line from file 
with open('input.txt') as f:
    for line in f.readlines():
        # Determine if line is not a newline break
        if line != "\n":
            input_list.append(str(line.strip())) # if not \n -> add to temp_list

###### Part 1 ##########################################################
race_times = list(input_list[0].split(":")[1].strip().split())
race_distances = list(input_list[1].split(":")[1].strip().split())

df = pd.DataFrame(columns=["time", "distance"])

for i in range(0, len(race_times)):
    df.loc[i] = {"time": int(race_times[i]), "distance": int(race_distances[i])}

def calculateDistance(holdTime, totalTime):
    travelTime = totalTime - holdTime
    distanceTraveled = holdTime * travelTime
    return distanceTraveled

def count_winning_opts(time, dist):
    winningCount = 0

    for i in range(0, time):
        distanceTraveled = calculateDistance(i, time)
        if distanceTraveled > dist:
            winningCount += 1
    return winningCount

df["countWinningOpts"] = df.apply(lambda x: count_winning_opts(x.time, x.distance), axis = 1)

winProduct = df.countWinningOpts.product()

print("Part 1 Solution: ") 
print(winProduct)

###### Part 2 ##########################################################
part2_time = int(''.join(input_list[0].split(":")[1].strip().split()))
part2_dist = int(''.join(input_list[1].split(":")[1].strip().split()))

part2_count = count_winning_opts(part2_time, part2_dist)

print("Part 2 Solution: ") 
print(part2_count)
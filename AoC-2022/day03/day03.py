# Advent of Code Day 1: https://adventofcode.com/2022/day/3
# Problem Created by Eric Wastl
# Solution by Nicolle M

import pandas as pd

# Read in Input using Pandas to DataFrame
df = pd.read_csv("input.txt", names=["pack"])

print(df)

#-----------------------------
# Solve for part 1           |
#-----------------------------
def split_pack(row):
    half_point = int(len(row.pack)/2)
    row["first"], row["second"] = row.pack[:half_point], row.pack[half_point:]
    return row


df = df.apply(lambda x: split_pack(x), axis=1)

print(df)

def return_common(row):
    first_set = set(row["first"])
    second_set = set(row["second"])
    return ''.join(first_set.intersection(second_set))

df["common_item"] = df.apply(lambda x: return_common(x), axis=1)

print(df)

def get_priority(letter):
    if letter.islower():
        priority = ord(letter) - ord('a') + 1
    else:
        priority = ord(letter) - ord('A') + 27
    return priority 

df["priority"] = df["common_item"].apply(lambda x: get_priority(x))

print(df)

print("Total Sum Priority: {}".format(sum(df["priority"])))


#-----------------------------
# Solve for part 2           |
#-----------------------------

# Create new df for part 2 -> Read in Input using Pandas to DataFrame
df_2 = pd.read_csv("input.txt", names=["pack"])

# Reshape the df so every 3 rows is transformed into a single row 
df_new = pd.DataFrame(df_2.iloc[:, 0].values.reshape((-1, 3)), columns=["elf1", "elf2", "elf3"])

def get_badge(row):
    set1, set2, set3 = set(row.elf1), set(row.elf2), set(row.elf3)
    temp_intersect = set1.intersection(set2)
    final_intersect = temp_intersect.intersection(set3)
    return ''.join(final_intersect)

df_new["badge"] = df_new.apply(lambda x: get_badge(x), axis=1)

print(df_new)

df_new["priority"] = df_new["badge"].apply(lambda x: get_priority(x))

print(df)

print("Total Sum Badge Priority: {}".format(sum(df_new["priority"])))
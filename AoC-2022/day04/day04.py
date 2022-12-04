# Advent of Code Day 4: https://adventofcode.com/2022/day/4
# Problem Created by Eric Wastl
# Solution by Nicolle M

import pandas as pd

# Read in Input using Pandas to DataFrame
df = pd.read_csv("input.txt", names=["elf1", "elf2"])

# Split ranges up into individual upper and lower values for ease of use
def get_lower_upper(row):
    row["elf1_lower"] , row["elf1_upper"] = row.elf1.split('-')
    row["elf2_lower"] , row["elf2_upper"] = row.elf2.split('-')
    return row

df = df.apply(lambda x: get_lower_upper(x), axis=1)

print(df)

def check_if_contained(row):
    elf1 = (int(row.elf1_lower), int(row.elf1_upper))
    elf2 = (int(row.elf2_lower), int(row.elf2_upper))

    # Debugging why I was getting the wrong values: I forgot to include the 
    # '=' check in previous iterations which meant I missed pairs that had 
    # the same start or end values
    # ------------------------------------------------------------------------
    # print(elf1, elf2)

    # res1 = (elf1[0] <= elf2[0] and elf1[1]>=elf2[1])
    # res2 = (elf2[0] <= elf1[0] and elf2[1]>=elf1[1])

    # print(res1 or res2)
    # ------------------------------------------------------------------------ 
    
    return ((elf1[0] <= elf2[0] and elf1[1]>=elf2[1]) 
        or (elf2[0] <= elf1[0] and elf2[1]>=elf1[1]))

df["contains"] = df.apply(lambda x: check_if_contained(x), axis=1)

print("Number of Contained Pairs: {}".format(df.contains[df.contains==True].count()))

# The rule for checking for overlapping ranges is:
# (StartA <= EndB) and (EndA >= StartB)
def does_overlap(row):
    elf1 = (int(row.elf1_lower), int(row.elf1_upper))
    elf2 = (int(row.elf2_lower), int(row.elf2_upper))

    return (elf1[0]<=elf2[1]) and (elf1[1]>=elf2[0])

df["overlap"] = df.apply(lambda x: does_overlap(x), axis=1)

print("Number of Overlapping Pairs: {}".format(df.overlap[df.overlap==True].count()))
# Advent of Code Day 4: https://adventofcode.com/2023/day/4
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
df = pd.DataFrame(columns=["hand", "bid"])

for i, line in enumerate(input_list):
    hand, bid = line.split()
    df.loc[i] = {"hand": hand, "bid": int(bid)}

def countCards(hand):
    temp = {}
    for i in hand:
        if i in temp.keys():
            temp[i] += 1
        else: 
            temp[i] = 1
    return temp

df["countCardsDict"] = df.apply(lambda x: countCards(x.hand), axis = 1)

def checkFiveOfKind(cardDict):
    if 5 in cardDict.values(): return True
    else: return False
    
def checkFourOfKind(cardDict):
    if 4 in cardDict.values(): return True
    else: return False

def checkFullHouse(cardDict):
    values = cardDict.values()
    if 3 in values and 2 in values: return True
    else: return False

def checkThreeOfKind(cardDict):
    values = cardDict.values()
    if 3 in values and 2 not in values: return True
    else: return False

def checkTwoPair(cardDict):
    cardDictValues = list(cardDict.values())
    count2s = 0
    for i in range(0, len(cardDictValues)): 
        if cardDictValues[i] == 2:
            count2s += 1
    
    if count2s == 2: return True
    else: return False
    
def checkOnePair(cardDict):
    cardDictValues = list(cardDict.values())
    count2s = 0
    for i in range(0, len(cardDictValues)): 
        if cardDictValues[i] == 2:
            count2s += 1
    
    if count2s == 1: return True
    else: return False
    
def classifyHand(countCardsDict):
    if checkFiveOfKind(countCardsDict):
        return 6
    elif checkFourOfKind(countCardsDict):
        return 5
    elif checkFullHouse(countCardsDict):
        return 4
    elif checkThreeOfKind(countCardsDict):
        return 3
    elif checkTwoPair(countCardsDict):
        return 2
    elif checkOnePair(countCardsDict):
        return 1
    else:
        return 0

df["ranked"] = df.apply(lambda x: classifyHand(x.countCardsDict), axis = 1)

df = df.sort_values(by=["ranked"])

faceCards = {"T": 10, "J": 11, "Q": 12, "K": 13, "A":14}


def replaceFaceCards(hand):
    hand = list(hand)
    for i, val in enumerate(hand):
        if val in faceCards.keys():
            hand[i] = faceCards[val]
        else:
            hand[i] = int(val)
    return hand

df_rank0 = df.loc[df.ranked == 0]
df_rank1 = df.loc[df.ranked == 1]
df_rank2 = df.loc[df.ranked == 2]
df_rank3 = df.loc[df.ranked == 3]
df_rank4 = df.loc[df.ranked == 4]
df_rank5 = df.loc[df.ranked == 5]
df_rank6 = df.loc[df.ranked == 6]

df["handsWOFaceCards"] = ""
if len(df_rank0) > 0:
    df_rank0["handsWOFaceCards"] = df_rank0.apply(lambda x: replaceFaceCards(x.hand), axis = 1)
else: df_rank0 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards"])
if len(df_rank1) > 0:
    df_rank1["handsWOFaceCards"] = df_rank1.apply(lambda x: replaceFaceCards(x.hand), axis = 1)
else: df_rank1 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards"])
if len(df_rank2) > 0:
    df_rank2["handsWOFaceCards"] = df_rank2.apply(lambda x: replaceFaceCards(x.hand), axis = 1)
else: df_rank2 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards"])
if len(df_rank3) > 0:
    df_rank3["handsWOFaceCards"] = df_rank3.apply(lambda x: replaceFaceCards(x.hand), axis = 1)
else: df_rank3 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards"])
if len(df_rank4) > 0:
    df_rank4["handsWOFaceCards"] = df_rank4.apply(lambda x: replaceFaceCards(x.hand), axis = 1)
else: df_rank4 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards"])
if len(df_rank5) > 0:
    df_rank5["handsWOFaceCards"] = df_rank5.apply(lambda x: replaceFaceCards(x.hand), axis = 1)
else: df_rank5 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards"])
if len(df_rank6) > 0:
    df_rank6["handsWOFaceCards"] = df_rank6.apply(lambda x: replaceFaceCards(x.hand), axis = 1)
else: df_rank6 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards"])

df_rank0 = df_rank0.sort_values(by="handsWOFaceCards")
df_rank1 = df_rank1.sort_values(by="handsWOFaceCards")
df_rank2 = df_rank2.sort_values(by="handsWOFaceCards")
df_rank3 = df_rank3.sort_values(by="handsWOFaceCards")
df_rank4 = df_rank4.sort_values(by="handsWOFaceCards")
df_rank5 = df_rank5.sort_values(by="handsWOFaceCards")
df_rank6 = df_rank6.sort_values(by="handsWOFaceCards")

frames = [df_rank0, df_rank1, df_rank2, df_rank3, df_rank4, df_rank5, df_rank6]
df_final = pd.concat(frames)
df_final = df_final.reset_index()


def calculateTotalBid(row):
    return row.bid * (row.name+1)

df_final["totalBid"] = df_final.apply(lambda x: calculateTotalBid(x), axis = 1)

print("~~~~~~~~~~~~ Part 1 Solution: ~~~~~~~~~~~~~~~~~")  
print(df_final["totalBid"].sum())

###### Part 2 ##########################################################

def replaceJokers(cardDict):
    keyJ = list(cardDict.keys())
    if 'J' in keyJ:
        countOfJ = cardDict['J']
        if countOfJ == 5:
            return cardDict
        del cardDict['J']
        max_val = [keys for keys,values in cardDict.items() if values == max(cardDict.values())]
        maxKey=max_val[0]
        cardDict[maxKey] += countOfJ
        
    return cardDict
    

df["jokerDict"] = df.apply(lambda x: replaceJokers(x.countCardsDict), axis = 1)
df["rankedJoker"] = df.apply(lambda x: classifyHand(x.jokerDict), axis = 1)
df = df.sort_values(by=["rankedJoker"])

df_rank_j0 = df.loc[df.rankedJoker == 0]
df_rank_j1 = df.loc[df.rankedJoker == 1]
df_rank_j2 = df.loc[df.rankedJoker == 2]
df_rank_j3 = df.loc[df.rankedJoker == 3]
df_rank_j4 = df.loc[df.rankedJoker == 4]
df_rank_j5 = df.loc[df.rankedJoker == 5]
df_rank_j6 = df.loc[df.rankedJoker == 6]

faceCardsJ = {"T": 10, "J": 1, "Q": 12, "K": 13, "A":14}

def replaceFaceCardsJ(hand):
    hand = list(hand)
    for i, val in enumerate(hand):
        if val in faceCardsJ.keys():
            hand[i] = faceCardsJ[val]
        else:
            hand[i] = int(val)
    return hand

df["handsWOFaceCardsJ"] = ""
if len(df_rank_j0) > 0:
    df_rank_j0["handsWOFaceCardsJ"] = df_rank_j0.apply(lambda x: replaceFaceCardsJ(x.hand), axis = 1)
else: df_rank_j0 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards", "jokerDict", "rankedJoker", "handsWOFaceCardsJ"])
if len(df_rank_j1) > 0:
    df_rank_j1["handsWOFaceCardsJ"] = df_rank_j1.apply(lambda x: replaceFaceCardsJ(x.hand), axis = 1)
else: df_rank_j1 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards", "jokerDict", "rankedJoker", "handsWOFaceCardsJ"])
if len(df_rank_j2) > 0:
    df_rank_j2["handsWOFaceCardsJ"] = df_rank_j2.apply(lambda x: replaceFaceCardsJ(x.hand), axis = 1)
else: df_rank_j2 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards", "jokerDict", "rankedJoker", "handsWOFaceCardsJ"])
if len(df_rank_j3) > 0:
    df_rank_j3["handsWOFaceCardsJ"] = df_rank_j3.apply(lambda x: replaceFaceCardsJ(x.hand), axis = 1)
else: df_rank_j3 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards", "jokerDict", "rankedJoker", "handsWOFaceCardsJ"])
if len(df_rank_j4) > 0:
    df_rank_j4["handsWOFaceCardsJ"] = df_rank_j4.apply(lambda x: replaceFaceCardsJ(x.hand), axis = 1)
else: df_rank_j4 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards", "jokerDict", "rankedJoker", "handsWOFaceCardsJ"])
if len(df_rank_j5) > 0:
    df_rank_j5["handsWOFaceCardsJ"] = df_rank_j5.apply(lambda x: replaceFaceCardsJ(x.hand), axis = 1)
else: df_rank_j5 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards", "jokerDict", "rankedJoker", "handsWOFaceCardsJ"])
if len(df_rank_j6) > 0:
    df_rank_j6["handsWOFaceCardsJ"] = df_rank_j6.apply(lambda x: replaceFaceCardsJ(x.hand), axis = 1)
else: df_rank_j6 = pd.DataFrame(columns=["hand", "bid", "countCardsDict", "ranked", "handsWOFaceCards", "jokerDict", "rankedJoker", "handsWOFaceCardsJ"])

df_rank_j0 = df_rank_j0.sort_values(by="handsWOFaceCardsJ")
df_rank_j1 = df_rank_j1.sort_values(by="handsWOFaceCardsJ")
df_rank_j2 = df_rank_j2.sort_values(by="handsWOFaceCardsJ")
df_rank_j3 = df_rank_j3.sort_values(by="handsWOFaceCardsJ")
df_rank_j4 = df_rank_j4.sort_values(by="handsWOFaceCardsJ")
df_rank_j5 = df_rank_j5.sort_values(by="handsWOFaceCardsJ")
df_rank_j6 = df_rank_j6.sort_values(by="handsWOFaceCardsJ")

framesJ = [df_rank_j0, df_rank_j1, df_rank_j2, df_rank_j3, df_rank_j4, df_rank_j5, df_rank_j6]
df_finalJ = pd.concat(framesJ)
df_finalJ = df_finalJ.reset_index()

df_finalJ["totalBid"] = df_finalJ.apply(lambda x: calculateTotalBid(x), axis = 1)

print("~~~~~~~ Part 2 Solution: ~~~~~~~~~~~~~")  
print(df_finalJ["totalBid"].sum())
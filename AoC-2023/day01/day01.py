import re

input_list = []
calib_list = []

# Read each line from file 
with open('input.txt') as f:
    for line in f.readlines():
        # Determine if line is not a newline break
        if line != "\n":
            input_list.append(str(line)) # if not \n -> add to temp_list

###### Part 1 ##########################################################

# loop over each line in input
for val in input_list:
    # find all digits in string and take first and last digit to create calibration num
    index_list = re.findall(r'\d', val)
    if len(index_list) == 1:
        calib_list.append(int(''.join(list([index_list[0], index_list[0]]))))
    else:
        calib_list.append(int(''.join(list([index_list[0], index_list[-1]]))))

print("Part 1 Solution: ")        
print(sum(calib_list))

###### Part 2 ##########################################################

calib_list2 = []
string_nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

# loop over each line in input
for val in input_list:
    # split line into list of words and individual digits
    res = re.split('(\d)', val)
    
    # loop over ever item in resulting split list
    for r in res:
        # do nothing if item is digit or empty string
        if r.isdigit() or r=="":
            continue
        # if item is one of the keys in dict, replace with value (ie. the equivalent digit)
        elif r in string_nums.keys():
            tempInd = res.index(r)
            res[tempInd] = str(string_nums[r])
        # some combo of letters to search for spelled out numbers in
        else:
            # store index of current item for use later
            tempInd = res.index(r)
            index_temp = []

            # loop over each key in dict
            for num in string_nums.keys():
                # find all matches to current key in this item
                extracttemp = re.finditer(num, r)

                # for each match, add set of start index, current key to temp list for use later
                for et in extracttemp:
                    index_temp.append((et.start(), num))
            
            # sort temp list to get keys in order of appearance in item
            index_temp = sorted(index_temp)

            for i in index_temp:
                # replace (index, key) pair with numberical representation of key
                index_temp[index_temp.index(i)] = str(string_nums[i[1]])
            
            # if not empty list, "replace" item with resulting temp list of numbers
            if len(index_temp) > 0:
                res = res[0:tempInd] + index_temp + res[tempInd+1:]
            else:
                res[tempInd] = ""
    
    # remove empty strings from list
    res = [i for i in res if i]
    
    # add resulting startend value to calib_list2
    if len(res) == 1:
        calib_list2.append(int(''.join(list([res[0], res[0]]))))
    else:
        calib_list2.append(int(''.join(list([res[0], res[-1]]))))


print("Part 2 Solution: ")
print(sum(calib_list2))


import re
input_list = []
calib_list = []

# Read each line from file 
with open('input.txt') as f:
    for line in f.readlines():
        # Determine if line is not a newline break
        if line != "\n":
            input_list.append(str(line)) # if not \n -> add to temp_list

for val in input_list:
    index_list = re.findall(r'\d', val)
    if len(index_list) == 1:
        calib_list.append(int(''.join(list([index_list[0], index_list[0]]))))
    else:
        calib_list.append(int(''.join(list([index_list[0], index_list[-1]]))))
        
print(sum(calib_list))
        


string_nums = {
    "zero": 0,
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
calib_list2 = []
for val in input_list:
    #print(val)
    res = re.split('(\d)', val)

    res = [i for i in res if i]
    #print(res)
    for r in res:
        if r.isdigit():
            continue
        elif r in string_nums.keys():
            tempInd = res.index(r)
            res[tempInd] = str(string_nums[r])
        else:
            tempInd = res.index(r)
            index_temp = []
            for num in string_nums.keys():
                extracttemp = re.finditer(num, r)

                for et in extracttemp:
                    index_temp.append((et.start(), num))
            index_temp = sorted(index_temp)

            for i in index_temp:
                #print(i)
                index_temp[index_temp.index(i)] = str(string_nums[i[1]])
            #print(index_temp)
            if len(index_temp) > 0:
                res = res[0:tempInd] + index_temp + res[tempInd+1:]
            else:
                res[tempInd] = ""
        
    res = [i for i in res if i]
    
    if len(res) == 1:
        calib_list2.append(int(''.join(list([res[0], res[0]]))))
    else:
        calib_list2.append(int(''.join(list([res[0], res[-1]]))))


        
print(sum(calib_list2))


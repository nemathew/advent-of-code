import pandas as pd

def input_to_list(filename):
    input_list = []
    # Read each line from file 
    with open(filename) as f:
        for line in f.readlines():
            # Determine if line is not a newline break
            if line != "\n":
                input_list.append(str(line)) # if not \n -> add to temp_list
    return input_list

def input_to_df(filename, cols):
    df = pd.read_csv(filename, names=cols, delimiter=" ")
    return df

def input_to_df(filename, cols, delim):
    df = pd.read_csv(filename, names=cols, delimiter=delim)
    return df

# Advent of Code Day 7: https://adventofcode.com/2022/day/7
# Problem Created by Eric Wastl
# Solution by Nicolle M
# Shout out to Spotify Slack thread for Day 7 
#   thanks for helping me spot my bugs--especially Niklas Gustavsson

# Global Vars + Classes
directories = []

class TreeNode:
    
    def __init__(self, parent):
        self.dirs = []
        self.parent = parent
        self.sz = 0

    def size(self):
        return self.sz + sum(d.size() for d in self.dirs)

# Part 1 
# if line[0] = '$' -> a command, parse as command 
# if line.split(" ")[0] = 'dir' -> directory 
# else (if line.split[] not cmd or directory, then we know this is a file with size, name)

root = TreeNode(None)
current_node = root

with open('input.txt') as f:
    temp_list = []
    for line in f.readlines():
        temp_list = line.split()

        if temp_list[0] == "$":
            # parse command -> cd or ls
            # cd
            if temp_list[1] == "cd":
                if temp_list[2] != '..':
                    if current_node != temp_list[2]:
                        parent_node = current_node 
                        current_node = TreeNode(parent_node)

                        directories.append(current_node)
                        parent_node.dirs.append(current_node)
                    else:
                        continue
                else:
                    current_node = current_node.parent
            # ls -> we don't need to handle ls lines as we already will point to correct node with cd commands 

        elif temp_list[0] == 'dir':
            continue
        else:
            current_node.sz += int(temp_list[0])

sizes = []
for d in directories:
    sizes.append(d.size())
sizes.sort()


tot_sum = 0
for s in sizes:
    if s < 100000:
        tot_sum += s

print("Total Sum for deletion: {}".format(tot_sum))

# Part 2 

# Total space on device = 70000000
# Space avail = tot_space - root.size()
space_avail = 70000000 - root.size()

print("Current Space Available: {}".format(space_avail))

# Total space required for update = 30000000
# Total space stil needed = tot_required - space_avail
space_needed = 30000000 - space_avail

print("Current Space Needed: {}".format(space_needed))

# iterate through sizes array from smallest to largest and 
# return the first size that is greater than the space needed as part 2 answer
for s in sizes:
    if s > space_needed:
        print("Directory Size to be deleted: {}".format(s))
        break;
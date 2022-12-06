# day 06

# https://adventofcode.com/2022/day/6

test1_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz" # 5 
test1_2 = "nppdvjthqldpwncqszvftbrmjlhg" # 6 
test1_3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # 10
test1_4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" #11
test2_1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' # 19
test2_2 ='bvwbjplbgvbhsrlpgdmjqwftvncz'# 23
test2_3 ='nppdvjthqldpwncqszvftbrmjlhg'# 23
test2_4 ='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'# 29
test2_5 ='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'# 26

inputFile='input/06_input'

# Read input
imp = open(inputFile, 'r')
ds = imp.readline()
# print(ds)

# Part 1

#ds = test1_4

startpacket = False
i = 0
while not startpacket:
    p = ds[i:i+4]
    startpacket = p[0] != p[1] and p[0] != p[2] and p[0] != p[3] and p[1] != p[2] and p[1] != p[3] and p[2] != p[3] 
    i+=1

ans1 = i+3
print("Day6 part1:", ans1)


# Part 2 

# ds = test2_5

for i in range(len(ds)):
    p = ds[i:i+14]   
    diff = True
    for c1 in range(14):
        for c2 in range(c1+1, 14,1):
            diff = diff and (p[c1] != p[c2])
            if not diff: break
        if not diff: break  
    if diff: break # jump out of loop if all letters differ

ans2 = i+14
print("Day6 part2:", ans2)


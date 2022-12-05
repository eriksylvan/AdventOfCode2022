# day 05

# https://adventofcode.com/2022/day/5
#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 

#move 1 from 2 to 1
#move 3 from 1 to 3
#move 2 from 2 to 1
#move 1 from 1 to 2

import copy

inputFile='input/05_input'
#inputFile='input/05_test_input'


def getAnswer(st):
    answer = ""
    for i in st:
        if len(i)>0:
            answer = answer + (i[-1:][0])
    return answer



stacks1 = [[] for i in range(9)]

instructions = []
crates = True
with open(inputFile) as inp:
    while True:
        row = inp.readline()
        if not row:
            break

        if row[0:2]==" 1":
            crates = False
            inp.readline() # skip empty line
            row = inp.readline()
        if crates:
            # read crates
            for p, r in enumerate(row):
                if r == '[':
                    stacks1[p//4].insert(0,row[p+1])
        else:
            # read instructions
            sp = row.strip().split(' ')
            instructions.append([int(sp[1]), int(sp[3]), int(sp[5])])

    
stacks2 = copy.deepcopy(stacks1)

for ins in instructions:
    turns = ins[0]
    frPos = ins[1]-1
    toPos = ins[2]-1
    #Part1 
    for t in range(turns):
        c = stacks1[frPos].pop()
        stacks1[toPos].append(c)
    #Part2
    l = len(stacks2[frPos])
    lift = stacks2[frPos][l-turns:]
    stacks2[frPos] = stacks2[frPos][:l-turns]
    stacks2[toPos] = stacks2[toPos] + lift
    
print("Day5 part1:", getAnswer(stacks1))
print("Day5 part2:", getAnswer(stacks2))

    
# day 09

# https://adventofcode.com/2022/day/9

from PIL import Image, ImageDraw   # python -m pip install pillow

inputFile='input/09_input'
#inputFile='input/09_test_input'



ins=[]
with open(inputFile) as input:
    for row in input:
        # print(row)
        i = row.strip().split(' ')
        dr = i[0]
        st = int(i[1])
        #print("dr:",dr,"st:",st+1)
        ins.append([dr,st])



def HeadWalk(p,inst, steps):
    #print(p, rPos, inst, steps)
    if inst == 'U':
        rPos = (p[0], p[1] + steps)
        #print('U', rPos)
    if inst == 'D':
        rPos = (p[0], p[1] - steps)
        #print('D', rPos)
    if inst == 'R':
        rPos = (p[0] + steps, p[1])
        #print('R', rPos)
    if inst == 'L':
        rPos = (p[0] - steps, p[1])
        #print('L', rPos)
    return rPos

tailMove = {(0,0):(0,0),
(0,0):(0,0),
(0,1):(0,0),
(1,1):(0,0),
(1,0):(0,0),
(1,-1):(0,0),
(0,-1):(0,0),
(-1,-1):(0,0),
(-1,0):(0,0),
(-1,1):(0,0),
(0,2):(0,1),
(1,2):(1,1),
(2,2):(1,1),
(2,1):(1,1),
(2,0):(1,0),
(2,-1):(1,-1),
(2,-2):(1,-1),
(1,-2):(1,-1),
(0,-2):(0,-1),
(-1,-2):(-1,-1),
(-2,-2):(-1,-1),
(-2,-1):(-1,-1),
(-2,0):(-1,0),
(-2,1):(-1,1),
(-2,2):(-1,1),
(-1,2):(-1,1)}

def TailWalk(tailP, headP):
    diff = (headP[0]-tailP[0],headP[1]-tailP[1])
    #print(diff)
    move = tailMove[diff]
    #print("D:",diff)
    #print("M:",move)
    rPos = (tailP[0] + move[0], tailP[1] + move[1])
    return rPos


img = Image.new('1', (1000, 1000))  # create a new black 1-bit image (BW)
pixels = img.load()         # create the pixel map

def drawRope(rope):
    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]

    for c in rope:      # for every col:
        pixels[c[0], c[1]] = 1
    img.show()

# PART 1
rope = [(0,0),(0,0)]
        # rope[0] = Head
        # rope[1] = Tail
tailPath = {}
for i in ins:
    for s in range(i[1]): # for evey step
        h = HeadWalk(rope[0], i[0],1)
        rope[0] = h
        t = TailWalk(rope[1], rope[0])
        rope[1] = t
        tailPath[t] = None

print("Day9 part1:",len(tailPath))


# PART 2
rope = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        # rope[0] = Head
        # rope[9] = Tail
rlen = len(rope)
        
tailPath = {}
for i in ins:
    for s in range(i[1]): # for evey step
        h = HeadWalk(rope[0], i[0],1)
        rope[0] = h

        for t in range(1,rlen):
            tp = TailWalk(rope[t], rope[t-1])
            rope[t] = tp
            
        tailPath[rope[rlen-1]] = None
        drawRope(rope)

drawRope(0,100,100)

print("Day9 part1:",len(tailPath))

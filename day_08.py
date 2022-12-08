# day 08

# https://adventofcode.com/2022/day/8


inputFile='input/08_input'
#inputFile='input/08_test_input'



trees=[]
with open(inputFile) as input:
    for row in input:
        # print(row)
        trees.append(row.strip())
h=len(trees)
v=len(trees[0])

def isVisibleFromNorth(th,vp,hp):
    ret = True
    for i in range(hp-1, -1, -1):
        ret = ret and (int(trees[vp][i]) < th)
    return ret    

def isVisibleFromSoth(th,vp,hp):
    ret = True
    for i in range(hp+1, h):
        ret = ret and (int(trees[vp][i]) < th)
    return ret

def isVisibleFromEast(th,vp,hp):
    ret = True
    for i in range(vp+1,v):
        ret = ret and (int(trees[i][hp]) < th)
    return ret

def isVisibleFromWest(th,vp,hp):
    ret = True
    for i in range(vp-1,-1,-1):
        ret = ret and (int(trees[i][hp]) < th)
    return ret

def viewDistNorth(th,vp,hp):
    dist = 1
    for i in range(hp-1, -1, -1):
        if (int(trees[vp][i]) >= th) or i == 0:
            break
        else:
            dist+=1
    #print(th,'N',dist)
    return dist        

def viewDistSoth(th,vp,hp):
    dist = 1
    for i in range(hp+1, h):
        if (int(trees[vp][i]) >= th) or i == h-1:
            break
        else:
            dist+=1
    #print(th,'S',dist)
    return dist

def viewDistEast(th,vp,hp):
    dist = 1
    for i in range(vp+1,v):
        if (int(trees[i][hp]) >= th) or i == v-1:
            break
        else:
            dist+=1
    #print(th,'E',dist)
    return dist

def viewDistWest(th,vp,hp):
    dist = 1
    for i in range(vp-1,-1,-1):
        if (int(trees[i][hp]) >= th) or i == 0:
            break
        else:
            dist+=1
    #print(th,'W',dist)
    return dist


# loop through all trees
hidden=0
senic=[]
for vp in range(1,v-1):
    for hp in  range(1,h-1):
        #print(trees[vp][hp])
        th=int(trees[vp][hp])
        isHidden = not isVisibleFromNorth(th,vp,hp) and not isVisibleFromSoth(th,vp,hp) and not isVisibleFromEast(th,vp,hp) and not isVisibleFromWest(th,vp,hp)
        if isHidden:
            hidden +=1 
            #print(vp, hp, th)
        senic.append(viewDistNorth(th,vp,hp) * viewDistSoth(th,vp,hp) * viewDistEast(th,vp,hp) * viewDistWest(th,vp,hp))   
tot = h*v
senic.sort(reverse = True)

print("Day8 part1:", tot - hidden)
print("Day8 part2:", senic[0])




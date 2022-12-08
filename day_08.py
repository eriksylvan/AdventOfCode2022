# day 08

# https://adventofcode.com/2022/day/8


# inputFile='input/08_input'
inputFile='input/08_test_input'



trees=[]
with open(inputFile) as input:
    for row in input:
        # print(row)
        trees.append(row.strip())
    h=len(trees)
    v=len(trees[0])

print(h,v)


def isVisibleFromNorth(th,vp,hp):return False
def isVisibleFromSoth(th,vp,hp):return False
def isVisibleFromEast(th,vp,hp):
    ret = True
    for i in range(vp+1,v):
        ret = ret and (int(trees[hp][i]) < th)
    return ret

def isVisibleFromWest(th,vp,hp):return False

# loop through all trees
for vp in range(1,v-1):
    pass
    for hp in  range(1,h-1):
        pass
        th=int(trees[vp][hp])
        print(th,end='')
        # bo = isVisibleFromNorth(th,vp,hp) and isVisibleFromSoth(th,vp,hp) and isVisibleFromEast(th,vp,hp) and isVisibleFromWest(th,vp,hp)
        isVisibleFromEast(th,vp,hp) 
    print()






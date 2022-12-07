# day 07

# https://adventofcode.com/2022/day/7


inputFile='input/07_input'
# inputFile='input/07_test_input'



class Dir:
    # A directory have one parent directory and can have directories and files
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.child = []
        self.files = []
        

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


# Read input
currentDir = Dir('/',None)
allDirs = []
allDirs.append(currentDir)
with open(inputFile) as input:

        for row in input:
            cl = row.strip().split(' ')
            if cl[0] == '$':
                # command input
                if cl[1] == 'cd':
                    #cd
                    # print('cd', cl[2])
                    if cl[2] == '..':
                        # .. jump back
                        # print('..')
                        currentDir = currentDir.parent
                    else:
                        # change dir
                        # print(cl[2])
                        # jump to directory with name
                        for cd in currentDir.child:
                            if cd.name == cl[2]:
                                currentDir = cd
                                break
                        
                else: 
                    if cl[1] == 'ls':
                        # ls
                        # print('ls')
                        pass
            else:
                # list output
                if cl[0]=='dir':
                    #dir
                    # print('dir:', cl[1])
                    d = Dir(cl[1], currentDir)
                    allDirs.append(d)
                    currentDir.child.append(d)
                    
                else:
                    # file
                    # print('file', cl[0], cl[1])
                    f = File(cl[1], int(cl[0]))
                    currentDir.files.append(f)


def getDirSize(dir):
    s=0
    # add all file sizes
    for f in dir.files:
        s+= f.size
    # add child directories sizes
    for d in dir.child:
        ds = getDirSize(d)
        s+= ds
    return s

sizes=[]
tot=0
for d in allDirs:
    size = getDirSize(d)
    sizes.append(size)
    # print(d.name, size)
    if size <= 100000:
        tot += size

print("Day7 part1:", tot)

sizes.sort(reverse=False)
free = 70000000 - sizes[-1]
toDel = 30000000 - free
for delete in sizes:
    if delete>=toDel:
        break
    
print("Day7 part2:", delete)

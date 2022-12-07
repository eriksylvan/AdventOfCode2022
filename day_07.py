# day 07

# https://adventofcode.com/2022/day/7


# inputFile='input/07_input'
inputFile='input/07_test_input'



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
currentDir = None
allDirs = []
with open(inputFile) as input:

        for row in input:
            cl = row.strip().split(' ')
            if cl[0] == '$':
                # command input
                if cl[1] == 'cd':
                    #cd
                    print('cd', cl[2])
                    if cl[2] == '..':
                        # .. jump back
                        print('..')
                        currentDir =   currentDir.parent
                    else:
                        #create dir
                        d = Dir(cl[2], currentDir)
                        currentDir = d
                        allDirs.append(d)
                else: 
                    if cl[1] == 'ls':
                        #ls
                        print('ls')
                        pass
            else:
                # list output
                if cl[0]=='dir':
                    #dir
                    print('dir:', cl[1])

                    
                else:
                    #file
                    print('file', cl[0], cl[1])
                    f = File(cl[1], int(cl[0]))
                    currentDir.files.append(f)


print("DIRS")
        
for d in allDirs:
    print(d.name)
    for f in d.files:
        print(f.name, f.size)


def getDirSize(dir):
    s=0
    # add all file sizes
    for f in dir.files:
        s+= f.size
    # acc child directories sizes
    for d in dir.child:
        s+=getDirSize(d)
    return s

print("SIZES")
for d in allDirs:
    size = getDirSize(d)
    print(d.name, size)




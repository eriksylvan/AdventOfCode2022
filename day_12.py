# day 12

# https://adventofcode.com/2022/day/13



inputFile='input/12_input'
#inputFile='input/12_test_input'


ePos = None
sPos = None

map=[]

with open(inputFile) as input:
    for i, row in enumerate(input):
        
        
        r = len(row.strip())
        
        if i==0: 
            map.append(''.join(['ö']*(r+2))) 
        if row.find('S') >= 0: 
            sPos = (row.find('S')+1, i+1)
        if row.find('E') >= 0: ePos = (row.find('E')+1, i+1)
        map.append(('ö'+row.strip()+'ö').replace('S','a').replace('E','z'))
        
    map.append(''.join(['ö']*(r+2))) 



h=len(map)
v=len(map[0])

print('S:',sPos)
print('E:',ePos)


path = {}
lowest = []
# Possible pathes:
for x in range(1, v-1, 1):
    for y in range(1, h-1, 1):
        path[(x,y)] = []
        # Up
        if ord(map[y][x])+1 >= ord(map[y-1][x]):   path[(x,y)].append((x,y-1))
        # Down
        if ord(map[y][x])+1 >= ord(map[y+1][x]):   path[(x,y)].append((x,y+1))
        # Left
        if ord(map[y][x])+1 >= ord(map[y][x-1]):   path[(x,y)].append((x-1,y))
        # Right
        if ord(map[y][x])+1 >= ord(map[y][x+1]):   path[(x,y)].append((x+1,y))
        
        #save lowest points
        if map[y][x] == 'a': lowest.append((x,y))


# BFS
def BFS(graph, start, end):
    path_list = [[start]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {start}
    if start == end:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if end in next_nodes:
            current_path.append(end)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return None

ans = BFS(path, sPos, ePos)
print("Day10 part1:", len(ans)-1)

min = 9999999999999
minPos = (0,0)
#print(lowest)
for lowPos in lowest:
    a = BFS(path, lowPos, ePos)
    if a is not None:
        if len(a) < min:
            min = len(a)
            minPos = lowPos

print("Day10 part2:", min-1, minPos, ePos)

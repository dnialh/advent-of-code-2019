import collections

s = """#################################################################################
#.........#.............#.......#.....#.#.....................#...#..c#.........#
#.###.#####.#######.#####.###.#.#.###.#.#.#######.###########.#.#.###.#.#####.#.#
#.#.#.#e..#...#.#...#.....#.#.#...#.....#..b#...#.#.........#...#.....#.#.T..r#.#
#.#.#.#.#.###.#.#.#.#.#####.#.#############.#.###.#.#####.#.#.#######.#.#.#######
#.#...#.#...#...#.#.#.#.....#.........K.#.#.#...#.#.#...#.#...#...#...#.#.......#
#.###.#.###.#.###.#.#.#.###.###########.#.#.###.#.###.#.#.#####.#.#.###.#######.#
#...#.#...#...#...#.#...#.#...#.....#...#.#.#...#.....#.#.#.....#.#...#.#.#.....#
###.#.###.#####.#########.###.#.###.#.#.#.#.#.#.#######.#.#O#####.#####.#.#.###.#
#...#.#.#...#.#.............#.#.#...#.#.#...#x#.#.....#.#.#...#z#.....#.#.#.#...#
#.###.#R###.#.#####.#.#######.#.#.###.#.#.###.#.#.###.#.#.###.#.#####.#.#.#.#####
#.#...#...#.#.....#.#.#.....#.#.#.#...#.#...#.#...#...#.#.#.......#...#...#.....#
#.#.#####.#.###.#.#.#.#.###.#.#.#.#.#######.#.#####L###.#.#.#####.#.#####.#####.#
#.#.......#...#.#.#.#.#...#...#.#.#...Y.#.#.#...#.....#.#.#.#...#.#.......#....q#
#.###########.#.#.#.#####.#######.#####.#.#.###.#######.###.#.#.#.#########.###.#
#...#.......#.#.#.#...#...#..h..#.....#.#.......#.....#...#.#.#.#.#.......#.#...#
#.#.#.#####.#.#.#.###.#.###.###.###.###.#######.#.###.###.#.#.#.#.#.#######.#.###
#.#.....#...#.#.#...#.#.#...#.....#.#...#...#...#...#...#...#.#.#.#.#.......#.#.#
#########.###.#####.#.#.#F#.#####.#.#.###.#.###.###.###.#.###.#.#.#.#.#######.#.#
#.........#...#.....#...#.#.#...#...#.#s#.#...#.#...#...#.#...#.#.#.#.#...#...#.#
#.#####.###.###.#.#####.#.###.#.###.#.#.#.###.###.###.#####.###.#.#.#.#.###.###.#
#..d#...#...#...#.#...#...#...#.#...#.#.#.#.#.....#.#.......#...#...#.#...#.#...#
#.#.#####.###.#.###.#######.###.#####.#.#.#.#######.#############.###.#.#.#.###.#
#.#.....#...#.#...#.........#.#.......#.#.......#.....#.....#.....#...#.#.#.....#
#.#####.###.#####.###########.#########.#######.#.###.###.#.#####.#.#####.#####.#
#.#...#...#...#...#.......#...........#.#.....#...#...#...#.....#.#...#.....#...#
#.#.###.#.###.#.#.#.#####.###.#######.#.#.###.#####.###.#######.#####.#.#####.###
#.#.#...#.#.#.#.#...#.....#...#.......#.#.#.#.....#...#.#.....#.#.....#.........#
#.#.#.###.#.#.#.#####.#####.#####.#####.#.#.###.#.###.#.#.#.###.#.#.#######.#####
#...#.#.#...#.#...#.#.#...#.....#.#.....#.....#.#...#...#.#.#...#.#j#.....#.#.W.#
#####.#.###.#.###.#.#.#.#.#####.#.###.#.#####.#.#########.###.###.###.###.###.#.#
#...#.#.....#.#...#.#.#.#.......#.....#.#.#...#.........#.....#.....#...#...#.#.#
#.#.#.#####.#.#.###.#.#.###############.#.#.#########.###.#########.#.#####.#.#.#
#.#...#...#.#.#w..#...#...#...........#.#.#.#.......#...#...#.....#...#.V.#...#.#
#.#####.#.###.###.#.###.#.#.###########.#.#.#####.#.###.###.###.#M#####.#.#####.#
#.....#.#...#.....#.#.#.#.#.A.#...#.....#.#.......#...#...#...#.#.......#.......#
#####.#.###.#######.#.#.#.#.#.#.#.#.#####.###########.###.###.#.###############.#
#.....#.#.#.......#.#...#.#.#...#.#.....#...#.......#.#.#.#...#.....#.#.....#...#
#.#####.#.#######.#.#####.#.#####.#####.#.#.#.###.###.#.#.#.#######.#.#.###.#.###
#............v..#.........#.....#......@#@#.....#.......#...........#.....#.....#
#################################################################################
#.#.....G.....#.....#.......#.........#@#@......#.......#...........#.......#...#
#.#.###.#####.#####.#.#####.#.###.###.#.#.#####.#####.#.#######.###.#.###.#.###.#
#.#.#.#.....#.......#.#...#...#.#.#.....#.#...#......a#.......#...#.#.#...#.#...#
#.#.#.#####.#######.#.#.#.#####.#.#####.#.#.#.###############.###.#.#.#.###.#.#.#
#.#..n....#.#.......#.#.#...#...#.....#.#.#.#...#.....#.....#...#.#...#...#.#.#.#
#.#######.#.#########.#.###.#.#######.#.#.#.#####.#.###.#.#.###.#########P#.#.###
#...#.#...#...#u..#...#.#...#.......#.#.#.#...#...#.....#.#...#.....#...#.#.#...#
#.#.#.#.#####.#.#.#.###.###.###.###.#.#.#.###.#.#########.###.#####.#.#U#.#.###.#
#.#...#p..#.#...#...#.....#.....#...#.#.#...#.#.#.....#...#...#...#...#.#.#...#.#
#.###.###.#.###########.#.###########.#####.#.#.###.#.#.###.###.#.#####.#.###.#.#
#...#.#...#...#.......#.#.#..k..#...#...#...#.#.#...#.#.#...#...#...#...#...#.#.#
#.#.###.###.#.###.###.###.#.###.#.#.###.#.###.#.#.###C#Z###.#.#####.#.###.#.#.#.#
#.#.........#.....#.#.#...#.#...#.#...#.#...#.#.#.#...#...#.#.....#.#...#.#.#.#.#
#.#################.#.#.###.#.###.###.#.#.#.#.#.#.#.#####.#.###.###.###.###.#.#.#
#m....#...........#.#...#...#...#...#.#.#.#.#.#.#.#.#.....#...#.#...#..g#.N.#...#
#.#####.#########.#.###.#.#####.###.#.#.###.#.#.#B#.#.#########.#.###.###.#####.#
#.#.....#.....#...#.....#.#...#.#...#...#...#.....#.#.......#...#...#...#.#i..#.#
###.#######.###.#########.#.###.#.#######.#########.#######.#.#####.###.#.#.#.#.#
#...#.......#...#....y....#...#.#.#.....#.#...S.#...#.....#.......#.#...#.#.#.#.#
#.###.#####.#.#.#.#########.#.#.#.#.###.#.#.###.#.###.###.#####.###.#.###.#.#.#.#
#...#.#.#...#.#.#.....#...#.#...#.....#.#.....#.#...#.#.....#.#.#...#.....#.#.#.#
###.#.#.#.###.#########.#.#.#####.#####.#######.###X#.#######.###.#.#######.###.#
#...#.#.#...#...........#.#...#...#.....#...#...#...#.#.......#...#.....#.......#
#Q###.#.###.#####.###########.#.###.###.#.#.#.#####.#.#.#######.#########.#######
#.....#...#.#...#.........#...#.#...#.#.#.#.#.....#...#...#.....#.......#.......#
#######.###.#.###########.#.#####.###.#.#.#.#####.###.###.#####.#D#####.#######.#
#.....#...#.#.......#...#...#.....#.....#.#.#...#.#....l#...#...#.#...#.......#.#
###.#.###.#.###.###.###.#####.#.#########.#.#.###.#########.#.#.#.###.#######.#.#
#...#...#.#.....#...#.......#.#.........#.#.#.#...#...#...#.#.#.#...#.......#...#
#.#####.#.#######.###.#######.#########.#.#.#.#.###.#.#.#.#.#.#.###.#.#####.#####
#.#..t#.#.....#...#.............#.....#.#.#.#.#.....#...#...#.#.#...#.#...#.....#
#.###.#.#.#####.###.###########.#.#.###.#.#.#.###############.#.#.#####.#.#####.#
#...#.....#...#.#.....#.......#...#.#...#.#.........#.........#.#.......#.#.....#
#E#.#.#####.#.#.#####.#.#####.#####.#.###.###.#######.#####.#############.#.#####
#.#.#...#...#.#...#...#.#...#...#...#...#...#.#.....#.#...#.........#.....#.#...#
###.#####.###I###.#.###.#.#.###.#####.#.#.#.###.###.#.#.#######.#####.#####.#.#.#
#...#...#...#...#.#.#...#.#...#.#...#.#.#.#..f..#.#...#.....#...#.....#...#...#.#
#.###.#.###.#.###.###.###.#####.#.#.###.#.#######.#########.#.###.#####.#.#####.#
#.J...#.....#.........#...........#.....#.............H....o#...........#.......#
#################################################################################"""

l = s.split('\n')

keys = [False] * 26

queue = collections.deque()
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == '@':
            queue.append((i,j,0))

posis = [0] * 26
for i in range(len(l)):
    for j in range(len(l[i])):
        if 'a' <= l[i][j] <= 'z':
            posis[ord(l[i][j]) - ord('a')] = (i,j)

visited = set()
visited.add((i,j))

dirX = [0,0,-1,1]
dirY = [-1,1,0,0]

reach = dict()

tupleQ = collections.deque()

while queue:
    nex = queue.popleft()

    for i in range(4):
        newX = nex[0] + dirX[i]
        newY = nex[1] + dirY[i]
        dist = nex[2] + 1

        if (newX, newY) in visited:
            pass
        else:
            visited.add((newX,newY))
            v = l[newX][newY]
            if  v == '#':
                pass
            elif v == '.':
                queue.append((newX, newY, dist))
            elif 'a' <= v <= 'z':
                if keys[ord(v) - 97]:
                    queue.append((newX, newY, dist))
                else:
                    reach[tuple(v)] = dist
                    tupleQ.append(tuple(v))
            elif 'A' <= v <= 'Z':
                print(v)
                if keys[ord(v) - 65]:
                    queue.append((newX, newY, dist))

BEST = 10**10
count = 0
while tupleQ:
    nexTup = tupleQ.popleft()
    count += 1
    if count % 1 == 0:
        print(nexTup, reach[nexTup])
    if len(nexTup) == 26:
        BEST = min(BEST, reach[nexTup])
        continue
    
    startTup = tuple(sorted(nexTup))
    lastPos = nexTup[-1]
    startPos = posis[ord(lastPos) - ord('a')]
    queue = collections.deque()
    queue.append((startPos[0], startPos[1], reach[nexTup]))
    keys = [False] * 26
    visited = set()
    for c in nexTup:
        keys[ord(c) - ord('a')] = True

    ###
    while queue:
        nex = queue.popleft()

        for i in range(4):
            newX = nex[0] + dirX[i]
            newY = nex[1] + dirY[i]
            dist = nex[2] + 1

            if (newX, newY) in visited:
                pass
            else:
                visited.add((newX,newY))
                v = l[newX][newY]
                if  v == '#':
                    pass
                elif v == '.' or v == '@':
                    queue.append((newX, newY, dist))
                elif 'a' <= v <= 'z':
                    if keys[ord(v) - 97]:
                        queue.append((newX, newY, dist))
                    else:
                        newTup = startTup + tuple(v)
                        if newTup in reach:
                            reach[newTup] = min(dist, reach[newTup])
                        else:
                            reach[newTup] = dist
                            tupleQ.append(newTup)
                elif 'A' <= v <= 'Z':
                    if keys[ord(v) - 65]:
                        queue.append((newX, newY, dist))
    ###
            
    
    
    


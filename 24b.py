s = """...#.
#.##.
#..##
#.###
##..."""

startL = []
for c in s:
    if c == '.':
        startL.append(0)
    elif c == '#':
        startL.append(1)

dirX = [-1,1,0,0]
dirY = [0,0,-1,1]

levels = []
for i in range(202):
    levels.append([0] * 25)

levels.append(startL)

for i in range(202):
    levels.append([0] * 25)


for _ in range(200):
    #Update

    nex = [[0] * 25 for asdf in range(len(levels))]

    
    for depth in range(len(levels)):
        start = levels[depth]
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:
                    continue
                
                if start[5 * i + j]:
                    for d in range(4):
                        newI = i + dirX[d]
                        newJ = j + dirY[d]
                        if 0 <= newI < 5 and 0 <= newJ < 5:
                            if newI == 2 and newJ == 2:
                                if d == 0:
                                    for v in range(5):
                                        nex[depth + 1][20 + v] += 1
                                elif d == 1:
                                    for v in range(5):
                                        nex[depth + 1][v] += 1
                                elif d == 2:
                                    for v in range(5):
                                        nex[depth + 1][5 * v + 4] += 1
                                else:
                                    for v in range(5):
                                        nex[depth + 1][5 * v] += 1
                                
                            else:
                                nex[depth][5 * newI + newJ] += 1
                        else:
                            if newI == -1:
                                nex[depth - 1][7] += 1
                            elif newI == 5:
                                nex[depth - 1][17] += 1
                            elif newJ == -1:
                                nex[depth - 1][11] += 1
                            elif newJ == 5:
                                nex[depth - 1][13] += 1
                            else:
                                print('BAD')

    startN = []
    
    for depth in range(len(levels)):
        startN.append([])
        start = levels[depth]
        for i in range(25):
            if start[i] == 1:
                if nex[depth][i] == 1:
                    startN[-1].append(1)
                else:
                    startN[-1].append(0)
            else:
                if nex[depth][i] == 1 or nex[depth][i] == 2:
                    startN[-1].append(1)
                else:
                    startN[-1].append(0)

    levels = startN

bugs = [sum(level) for level in levels]
print(bugs)
print(sum(bugs))

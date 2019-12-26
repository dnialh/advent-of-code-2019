s = """...#.
#.##.
#..##
#.###
##..."""

start = []
for c in s:
    if c == '.':
        start.append(0)
    elif c == '#':
        start.append(1)

seen = set()

def bio(l):
    out = 0
    for i in range(25):
        if l[i]:
            out += 2 ** i
    return out

dirX = [-1,1,0,0]
dirY = [0,0,-1,1]

seen.add(bio(start))
while True:
    #Update

    nex = [0] * 25

    for i in range(5):
        for j in range(5):
            if start[5 * i + j]:
                for d in range(4):
                    newI = i + dirX[d]
                    newJ = j + dirY[d]
                    if 0 <= newI < 5 and 0 <= newJ < 5:
                        nex[5 * newI + newJ] += 1

    startN = []
    for i in range(25):
        if start[i] == 1:
            if nex[i] == 1:
                startN.append(1)
            else:
                startN.append(0)
        else:
            if nex[i] == 1 or nex[i] == 2:
                startN.append(1)
            else:
                startN.append(0)

    start = startN
                        

    #Cont
    val = bio(start)

    if val in seen:
        print(val)
        break
    else:
        seen.add(val)

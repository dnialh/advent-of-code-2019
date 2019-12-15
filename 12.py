moons = []
moons.append([-1, -4, 0, 0, 0, 0]);
moons.append([4, 7, -1, 0, 0, 0]);
moons.append([-14, -10, 9, 0, 0, 0]);
moons.append([1, 2, 17, 0, 0, 0]);

TIME = 0

import itertools

s = set()

while True:
    dist = 1
    """for m in moons:
        for i in range(3):
            dCurr = abs(m[i])
            vCurr = abs(m[i + 3])

            lo = 1
            hi = 100000

            while hi - lo < 1:
                test = (lo + hi)//2

                dNew = test * (2 * vCurr + (3 * test))

                if dNew < 2 * dCurr:
                    lo = test
                else:
                    hi = test
                
                

            tCurr = lo
            
            dist = min(max(1, tCurr), dist)
    """
    TIME += dist

    
    for a,b in itertools.combinations([0,1,2,3], 2):
        m1 = moons[a]
        m2 = moons[b]

        for i in range(3):
            if m1[i] < m2[i]:
                m1[i + 3] += dist
                m2[i + 3] -= dist
            elif m1[i] > m2[i]:
                m1[i + 3] -= dist
                m2[i + 3] += dist

    for a in range(4):
        for i in range(3):
            moons[a][i] += moons[a][i + 3]
    tup = tuple(moons[0][2::3] + moons[1][2::3] + moons[2][2::3] + moons[3][2::3])
    if tup in s:
        break
    
    s.add(tup)
    if not TIME % 100000:
        print(TIME, dist)

#231615
#193053
#60425

print(TIME)
print(len(s))

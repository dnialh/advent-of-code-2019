lMaster = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,9,19,23,1,13,23,27,1,5,27,31,2,31,6,35,1,35,5,39,1,9,39,43,1,43,5,47,1,47,5,51,2,10,51,55,1,5,55,59,1,59,5,63,2,63,9,67,1,67,5,71,2,9,71,75,1,75,5,79,1,10,79,83,1,83,10,87,1,10,87,91,1,6,91,95,2,95,6,99,2,99,9,103,1,103,6,107,1,13,107,111,1,13,111,115,2,115,9,119,1,119,6,123,2,9,123,127,1,127,5,131,1,131,5,135,1,135,5,139,2,10,139,143,2,143,10,147,1,147,5,151,1,151,2,155,1,155,13,0,99,2,14,0,0]


for i in range(100):
    for j in range(100):
        l = lMaster[:]
        l[1] = i
        l[2] = j

        inp = [-1] * 1000 + [-1,-1,-1,0,191978,-1,-1,-1,-1,-1,11]
        out = []
        curr = 0
        base = 0
        
        while True:
            code = l[curr] % 100
            mode1 = l[curr] // 100 % 10
            mode2 = l[curr] // 1000 % 10
            mode3 = l[curr] // 10000 % 10


            baseInp1 = l[curr + 1]
            inp2 = l[curr + 2]
            inp3 = l[curr + 3]

            
            if mode1 == 0:
                inp1 = l[baseInp1]
            elif mode1 == 1:
                inp1 = baseInp1
            elif mode1 == 2:
                baseInp1 += base
                inp1 = l[baseInp1]
                
            if mode2 == 0:
                inp2 = l[inp2]
            elif mode2 == 2:
                inp2 = l[inp2 + base]
                
            if mode3 == 2:
                inp3 += base

            
            if code == 1:
                l[inp3] = inp1 + inp2
                curr += 4
                
            elif code == 2:
                l[inp3] = inp1 * inp2
                curr += 4
                
            elif code == 3:
                l[baseInp1] = inp.pop()
                print(baseInp1, l[baseInp1])
                curr += 2
                
            elif code == 4:
                out.append(inp1)
                curr += 2
                
            elif code == 5:
                if inp1 != 0:
                    curr = inp2
                else:
                    curr += 3
                    
            elif code == 6:
                if inp1 == 0:
                    curr = inp2
                else:
                    curr += 3

            elif code == 7:
                if inp1 < inp2:
                    outV = 1
                else:
                    outV = 0
                l[inp3] = outV
                curr += 4
                
            elif code == 8:
                if inp1 == inp2:
                    outV = 1
                else:
                    outV = 0
                l[inp3] = outV
                curr += 4
                
            elif code == 9:
                base += inp1
                curr += 2
                
            elif code == 99:
                break
            
            else:
                print('Bad')
                break
        if l[0] == 19690720:
            print(100 * i + j)

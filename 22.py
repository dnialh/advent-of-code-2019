s = """deal into new stack
deal with increment 68
cut 4888
deal with increment 44
cut -7998
deal into new stack
cut -5078
deal with increment 26
cut 7651
deal with increment 60
cut 8998
deal into new stack
deal with increment 64
cut -8235
deal into new stack
deal with increment 9
cut -8586
deal with increment 49
cut -7466
deal with increment 66
cut -565
deal with increment 19
cut -6306
deal with increment 67
deal into new stack
cut 886
deal with increment 63
cut 3550
deal with increment 36
cut 5593
deal with increment 18
deal into new stack
deal with increment 70
deal into new stack
cut 5168
deal with increment 39
cut 7701
deal with increment 2
deal into new stack
deal with increment 45
cut 6021
deal with increment 46
cut -6927
deal with increment 49
cut 4054
deal into new stack
deal with increment 33
deal into new stack
deal with increment 11
cut -3928
deal with increment 19
deal into new stack
deal with increment 32
cut -7786
deal with increment 27
deal into new stack
deal with increment 37
cut -744
deal with increment 25
cut -98
deal with increment 61
cut 2042
deal with increment 71
cut 5761
deal with increment 6
cut -2628
deal with increment 33
cut -9509
deal with increment 16
cut 2599
deal with increment 28
cut 2767
deal into new stack
cut 3076
deal with increment 61
deal into new stack
cut 1182
deal with increment 4
cut 2274
deal into new stack
deal with increment 31
cut -5897
deal into new stack
cut -3323
deal with increment 29
cut 879
deal with increment 12
deal into new stack
deal with increment 34
cut -5755
deal with increment 59
cut 7437
deal into new stack
cut 5095
deal into new stack
cut 453
deal with increment 24
cut -3537
deal with increment 41
deal into new stack"""

l = s.split('\n')

M = 119315717514047

a = 1
b = 0

def inv(x):
    return pow(x, M - 2, M)

for inst in l:
    if inst[0] == 'd':
        instP = inst.split()
        if instP[1] == 'into':
            b = (b - a) % M
            a = (-a) % M
        else:
            inc = int(instP[-1])
            a *= inv(inc)
    elif inst[0] == 'c':
        val = int(inst.split(' ')[-1])
        b += val * a

rep = 101741582076661

a, b = pow(a, rep, M), b * (pow(a, rep, M) - 1) * inv(a - 1)

print((a * 2020 + b) % M)



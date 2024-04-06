from collections import Counter
import math

for z in range(int(input())):
    n = input()
    a = *map(int, input().split()),
    c = Counter(a)
    ncK = 0
    ac=bc=0
    for e in a:
        if e==1:
            ac=1
        if e==2:
            bc=1
    ac = 0 if 1 not in a else c[1]
    bc = 0 if 2 not in a else c[2]
    print(c)
    for _, v in c.items():
        if v > 1:
            ncK += math.comb(v, 2)
            print(_,v,a,"z",math.comb(v,2))
    print(ncK + (ac * bc))
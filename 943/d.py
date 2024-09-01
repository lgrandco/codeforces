from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n, k, pb, ps = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    maxi = max(a)
    scoresS = set()
    scoresB = set()
    i = 0
    curA = 0
    curB = 0
    stopS = stopB = False
    maxA = 0
    maxB = 0
    setA = set()
    setB = set()
    while (not stopS or not stopB) and i < k:
        if not stopS or 1:
            if a[ps - 1] == maxi or ps == p[ps - 1] or ps in setA:
                stopS = True
            maxA = max(maxA, curA + a[ps - 1] * (k - i))
            curA += a[ps - 1]
            setA.add(ps)
            ps = p[ps - 1]
            # print("PS:", ps, "CURA:", curA, "MAXA:", maxA)
        if not stopB or 1:
            if a[pb - 1] == maxi or pb == p[pb - 1] or pb in setB:
                stopB = True
            maxB = max(maxB, curB + a[pb - 1] * (k - i))
            curB += a[pb - 1]
            setB.add(pb)
            pb = p[pb - 1]
            # print("PB:", pb, "CURB:", curB, "MAXB:", maxB)
        # print("hi", scoresB, scoresS)
        i += 1
    # print(scoresB, scoresS)
    print("Bodya" if maxB > maxA else "Sasha" if maxB < maxA else "Draw")

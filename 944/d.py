from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    a = input()
    n = "0"
    f = 1
    r = 0
    did = 0
    for i, e in enumerate(a):
        if e != n:
            if not (e == "1" and i == 0):
                if e == "1" and did == 0:
                    did = 1
                else:
                    r += 1
        n = e

    print(r + 1)

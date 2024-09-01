from itertools import combinations, product
from collections import deque
from collections import Counter
from collections import defaultdict
from random import shuffle

m = 2**31 - 1
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    shuffle(a)
    c = Counter(a)
    r = 0
    for e in a:
        xor_res = m ^ e
        if c[xor_res] > 0 and c[e] > 0:
            c[xor_res] -= 1
            c[e] -= 1
            r += 1
    print(n - r)

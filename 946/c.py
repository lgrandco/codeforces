from itertools import combinations, product
from collections import Counter, defaultdict, deque

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d_double = defaultdict(int)
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    d3 = defaultdict(int)
    r = 0
    for i in range(n - 3 + 1):
        a1, a2, a3 = a[i : i + 3]
        r += d1[(a1, a2)] - d_double[(a1, a2, a3)]
        r += d2[(a2, a3)] - d_double[(a1, a2, a3)]
        r += d3[(a1, a3)] - d_double[(a1, a2, a3)]
        d_double[(a1, a2, a3)] += 1
        d1[(a1, a2)] += 1
        d2[(a2, a3)] += 1
        d3[(a1, a3)] += 1
    print(r)

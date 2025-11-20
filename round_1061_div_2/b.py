from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import sys

sys.setrecursionlimit(200000)
for _ in range(int(input())):
    k, f = map(int, input().split())
    a = input().strip()
    d = {}
    k = len(a)
    queries = list(map(int, input().split()))
    f = 1 if "B" in a else 0
    for e in queries:
        if f == 0:
            print(e)
            continue
        n = e
        c = 0
        i = 0
        while n:
            n = n - 1 if a[i % k] == "A" else n // 2
            # n = n - 1
            i += 1
            c += 1
        print(c)

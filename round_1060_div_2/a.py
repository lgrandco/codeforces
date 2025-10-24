from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input()
    last = -999999
    c = 0
    for i in range(n):
        if a[i] == "1":
            if last + k <= i:
                c += 1
            last = i
    print(c)

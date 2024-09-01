from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    r = 0
    for e in product(a, b):
        if sum(e) <= k:
            r += 1
    print(r)

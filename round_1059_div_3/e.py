from itertools import combinations, product
from collections import deque
from collections import Counter
from collections import defaultdict

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    l = []

    d = defaultdict(lambda: -1)
    for i, e in enumerate(a):
        d[e] = i
    l = sorted([j for j in range(1, n + 1)], key=lambda x: d[x])
    print(*(l[i % len(l)] for i in range(k)))

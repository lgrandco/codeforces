from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    c = 0
    m = -1
    for i in range(n):
        m = max(m, a[i])
        if i % 2:
            a[i] = m
    # print(a)
    for i in range(0, n, 2):
        if i != n - 1 and a[i] >= a[i + 1]:
            c += a[i] - a[i + 1] + 1
            a[i] = a[i + 1] - 1
        if i > 0 and a[i] >= a[i - 1]:
            c += a[i] - a[i - 1] + 1
            a[i] = a[i - 1] - 1
    print(c)
    # print(a, "\n\n")

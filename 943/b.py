from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()
    i = 0
    aa = 0
    while i < m and aa < n:
        if b[i] == a[aa]:
            aa += 1
        i += 1
    print(aa)

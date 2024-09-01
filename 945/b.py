from itertools import combinations, product
from collections import deque, Counter, defaultdict
import math
import sys
from random import shuffle
from bisect import bisect_left, bisect_right

for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    k = 1
    high = n
    low = 1
    while low < high:
        k = (low + high) // 2
        old = None
        valid = True
        for i in range(n - k + 1):
            r = 0
            for e in a[i : i + k]:
                r |= e
            if old is not None and old != r:
                valid = False
                break
            old = r
        if valid:
            high = k
        else:
            low = k + 1
    if low == high:
        k = low
    print(k)

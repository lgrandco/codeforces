from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import sys, math

for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))

    if any(e % 2 != a[0] % 2 for e in a):
        print(*sorted(a))
    else:
        print(*a)

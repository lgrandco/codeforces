from itertools import combinations, product
from collections import deque, Counter, defaultdict
import math
import sys
from random import shuffle
from bisect import bisect_left, bisect_right


def p(bool):
    sys.stdout.write("YES\n" if bool else "NO\n")


ii = lambda: int(sys.stdin.readline().strip())

lst = lambda: list(map(int, sys.stdin.readline().strip().split()))

ss = lambda: sys.stdin.readline().strip()

ints = lambda: map(int, sys.stdin.readline().strip().split())

for _ in range(int(input())):
    m, n = map(int, input().split())
    l = lst()
    z = []
    _m = max(l)
    for i in range(m):
        o, a, b = input().split()
        a, b = int(a), int(b)
        if a <= _m <= b:
            _m += 1 if o == "+" else -1
        z += (_m,)
    print(*z)

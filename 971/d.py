from itertools import combinations, product
from collections import deque, Counter, defaultdict
import math
import sys
from random import shuffle
from bisect import bisect_left, bisect_right


def print_res(bool):
    sys.stdout.write("YES\n" if bool else "NO\n")


ii = lambda: int(sys.stdin.readline().strip())

lst = lambda: list(map(int, sys.stdin.readline().strip().split()))

ss = lambda: sys.stdin.readline().strip()

ints = lambda: map(int, sys.stdin.readline().strip().split())

for _ in range(int(input())):
    n = int(input())
    z = set()
    zz = set()
    for e in range(n):
        a = lst()
        z.add(a[0])
        zz.add(tuple(a))
    r = 0
    for e in zz:
        x, y = e
        if (
            (x - 1, y - 1) in zz
            and (x + 1, y - 1) in zz
            or (x - 1, y + 1) in zz
            and (x + 1, y + 1) in zz
        ):
            r += 1
    print(r + (n - len(z)) * (n - 2))

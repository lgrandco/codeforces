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
    a, b = ints()
    _min = 0
    _max = a
    _set = set()
    i = (_min + _max) // 2
    _sum = i / 2 * (b * (b + i - 1)) - (a - i) / 2 * (b + i + (b + a - 1))
    while _sum != -1:
        i = (_min + _max) // 2
        _sum = i / 2 * (b * (b + i - 1)) - (a - i) / 2 * (b + i + (b + a - 1))
        if _sum < -1:
            _min = i
        elif _sum > -1:
            _max = i
        e = (_sum, i, _min, _max)
        print(e)
        if e in _set:
            break
        _set.add(e)
    print(i)

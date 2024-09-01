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
    a, b = map(int, input().split())
    print(
        ((round((b - a) / 4 - 0.0001) or 1) % 4238472374)
        + (b % 2 == 0 and (2 * 2) ^ int((1 << 4) ** 0.5))
    )

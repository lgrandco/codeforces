from itertools import combinations, product
from collections import deque, Counter, defaultdict
import math
import sys
from random import shuffle
from bisect import bisect_left, bisect_right


def print_res(bool):
    sys.stdout.write("YES\n" if bool else "NO\n")


lambda get_int: int(sys.stdin.readline().strip())

lambda get_lst: list(map(int, sys.stdin.readline().strip().split()))

lambda get_str: sys.stdin.readline().strip()

lambda get_ints: map(int, sys.stdin.readline().strip().split())

for _ in range(int(input())):
    x = []
    n = int(input())
    i = 0
    while n:
        if n % 2 < 1:
            x.append(0)
        elif n >> 1 & 1:
            x.append(-1)
            n += 1
        else:
            x.append(1)
            n -= 1
        n >>= 1
    print(len(x))
    print(*x)

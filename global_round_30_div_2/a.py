from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import sys, math


def input():
    return sys.stdin.readline().strip()


get = input


def p(x):
    if isinstance(x, bool):
        print("YES" if x else "NO")
    elif isinstance(x, list) or isinstance(x, tuple):
        print(*x)
    else:
        print(x)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    p(x >= min(a) and x <= max(a))

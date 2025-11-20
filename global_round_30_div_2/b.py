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

    a = sorted(map(int, input().split()))
    for e in a[::-1]:
        i = 0
        otp = -1
        while a[i] < e:
            if (e % a[i]) % 2 < 1:
                otp = (a[i], e)
            i += 1
        if otp != -1:
            break
    p(otp)

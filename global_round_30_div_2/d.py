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
    n, k = map(int, input().split())

    a = list(input())
    s = list(input())
    l = []
    if a == s:
        print(0)
        continue
    for x in range(k):
        l.append(s[:])
        print(s, "azn")
        cpy = s[:]
        for i in range(n - 1, -1, -1):
            if cpy[i] != a[i]:
                s[i - 1] = cpy[i]
                s[i] = cpy[i + 1] if i + 1 < len(cpy) else a[i]
        print(s)

        if a == s:
            print(x + 1)
            for e in l[::-1]:
                print("".join(e))
            break
    else:
        print(-1)

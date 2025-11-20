from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import sys, math


def input():
    return sys.stdin.readline().strip()


get = input


def p(x):
    if isinstance(x, bool):
        print("Yes" if x else "No")
    elif isinstance(x, list) or isinstance(x, tuple):
        print(*x)
    else:
        print(x)


first_input = input()
if first_input == "first":
    for _ in range(
        int(input()) if first_input == "first" else int(first_input)
    ):
        n = int(input())
        print(n)


elif first_input == "second":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        print(n, a)

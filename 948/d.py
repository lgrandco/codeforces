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
    n = int(input())
    a = [*map(int, input().split())]

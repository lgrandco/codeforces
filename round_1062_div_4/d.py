from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import sys, math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    div = []
    i = 2
    while all(math.gcd(e, i) != 1 for e in a):
        i += 1
    print(i)

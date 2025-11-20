from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import sys, math

for _ in range(int(input())):
    a = list(map(int, input().split()))

    print(["NO", "YES"][all(e == a[0] for e in a)])

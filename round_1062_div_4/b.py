from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import sys, math

for _ in range(int(input())):
    input()
    a, b = input().strip().split()

    print("YES" if sorted(a) == sorted(b) else "NO")

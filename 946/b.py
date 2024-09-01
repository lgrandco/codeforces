from itertools import combinations, product
from collections import deque
from collections import Counter
import math
import sys
from random import shuffle
from bisect import bisect_left, bisect_right

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = sorted(set(a))
    d = {}
    for i in range(len(b)):
        d[b[i]] = b[-i - 1]
    print("".join(d[c] for c in a))

from itertools import combinations, product
from collections import deque
from collections import Counter
import math

for _ in range(int(input())):
    a = sorted(map(int, input().split()), reverse=True)
    if sum(a) % 2:
        print(-1)
        continue
    r = 0
    while a[1]:
        a[0] -= 1
        a[1] -= 1
        a = sorted(a, reverse=True)
        r += 1
    print(r)

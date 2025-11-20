from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import sys, math

for _ in range(int(input())):
    n, k, x = map(int, input().split())

    a = list(map(int, input().split()))

    # print(*sorted(range(0, x + 1), key=lambda x: min(abs(x - e) for e in a))[::-1][
    #         :k
    #     ]
    # )

    closest = [x + 1 for i in range(x + 1)]

    print(closest)

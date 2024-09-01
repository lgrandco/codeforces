from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input()
    for i in range(1, n // 2 + 1):
        a, b = divmod(n, i)
        if b:
            continue
        if (
            sum(x != y for x, y in zip(s[:i] * a, s)) < 2
            or sum(x != y for x, y in zip(s[-i:] * a, s)) < 2
        ):
            print(i)
            break
    else:
        print(n)

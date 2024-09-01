from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a, b = min(a, b), max(a, b)
    c, d = min(c, d), max(c, d)
    a_to_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12][a:b]
    a2_to_b2 = [e for e in [*range(1, 13)] if e not in a_to_b if e != a and e != b]
    if (c in a_to_b) == (d in a_to_b):
        print("NO")
    else:
        print("YES")

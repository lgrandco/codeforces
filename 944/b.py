from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    a = Counter(input()[::-1])
    if len(a) == 1:
        print("NO")
        continue
    print("YES")
    for k, b in a.items():
        print(end=k * b)
    print()

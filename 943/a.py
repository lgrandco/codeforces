from itertools import combinations, product
from collections import deque
from collections import Counter
import math

for _ in range(int(input())):
    n = int(input())
    d = {i: math.gcd(n, i) + i for i in range(1, n)}
    print(max(d, key=d.get))

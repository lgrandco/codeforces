from itertools import combinations, product
from collections import deque
from collections import Counter
import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(min(a, b), max(a, b))

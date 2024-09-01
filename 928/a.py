from itertools import combinations, product
from collections import deque
from collections import Counter
import math

for _ in range(int(input())):
    s = input()
    print("A" if Counter(s)["A"] > Counter(s)["B"] else "B")

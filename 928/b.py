from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    l = -1
    for i in range(1, n + 1):
        s = input()
        if "1" in s and l != -2:
            if l != -1 and s.index("1") != l:
                print("TRIANGLE")
                l = -2
            elif l != -1:
                print("SQUARE")
                l = -2
            else:
                l = s.index("1")

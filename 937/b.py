from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    for i in range(n * 2):
        for j in range(n * 2):
            print("#" if (j % 4 < 2) == (i % 4 < 2) else ".", end="")
        print()

from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    a, b = map(int, input().split())
    xor = a ^ b
    if xor <= a:
        print(1)
        print(xor)
    elif a > b:
        print(2)
        print(b, a)
    else:
        print(-1)

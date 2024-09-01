from itertools import combinations, product
from collections import deque
from collections import Counter
import math

for _ in range(int(input())):
    b, a = map(int, input().split())
    r = 0
    # while a > 0 or b > 0:
    #     m = 15
    #     if a > 0:
    #         a -= 1
    #         m -= 4
    #     if a > 0:
    #         a -= 1
    #         m -= 4
    #     if b > 0:
    #         b -= m
    #     r += 1
    # print(r)
    print(max(math.ceil(b / 7), math.ceil(a / 2)))

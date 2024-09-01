from itertools import combinations, product
from collections import deque, Counter, defaultdict

# for _ in range(int(input())):
# _max = 0
# m, x = map(int, input().split())
# salary = 0
# salaries = [
#     (0, 0),
# ]
# for i in range(m):
#     a, b = map(int, input().split())
#     _len = len(salaries)
#     for j in range(_len):
#         money, happiness = salaries.pop(0)
#         if money >= a:
#             salaries.append((money + x - a, happiness + b))
#             _max = max(_max, happiness + b)
#         salaries.append((money + x, happiness))
# print(salaries)
# print(_max)

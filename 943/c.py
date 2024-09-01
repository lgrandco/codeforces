from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = [a[0] + 1]
    for i in range(n - 1):
        l += (l[-1] * 2 + a[i],)
        # while l[-1] % l[-2] != a[i]:
        #     l[-1] += 1
    print(*l)

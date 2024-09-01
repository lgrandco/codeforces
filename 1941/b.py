from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1, 1, -1):
        if a[i] < 0:
            print("NO")
            break
        a[i - 1] -= 2 * a[i]
        a[i - 2] -= a[i]
    else:
        print("YES" if a[0] == 0 and a[1] == 0 else "NO")

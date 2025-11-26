from itertools import combinations, product
from collections import deque
from collections import Counter
import math


def find(a):
    for i in range(1, n + 1):
        l = [0 for j in range(i)]
        while l[0] < n:
            while l[-1] < n:
                tab = [a[id] for id in l]
                print(tab)
                s = [a[i] for i in range(len(a)) if i not in l]
                if tab == sorted(tab) and s == s[::-1]:
                    return l
                l[-1] += 1

            j = len(l) - 1
            while l[j] == n and j > 0:
                l[j] = l[j - 1]
                l[j - 1] += 1
                j -= 1
    return -1


for _ in range(int(input())):
    n = int(input())
    a = input()
    # s = ""
    # if a == a[::-1]:
    #     print(0)
    #     print("")
    # else:
    #     l = find(a)
    #     if l == -1:
    #         print(-1)
    #     else:
    #         print(len(l))
    #         print(*[e + 1 for e in l])
    print(a.count("0"))
    print(*(i + 1 for i in range(n) if a[i] == "0"))

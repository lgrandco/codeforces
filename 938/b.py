from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    l=[*map(int,input().split())]
    m=min(l)
    l2=[]
    for i in range(a):
        for j in range(a):
            l2+=[m+i*b+j*c]
    print("YES" if Counter(l)==Counter(l2)else "NO")






# 1 9 6
# 5 7 3
# 11 4 8

# 300 400
# 400 500

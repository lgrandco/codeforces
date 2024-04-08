from itertools import combinations
from collections import deque
from collections import Counter
import math

for _ in range(int(input())):
    n,m = map(int,input().split())
    l=[*map(int,input().split())]
    first=0
    last=n-1
    a=math.ceil(m/2)
    b=m//2
    c=0
    while a:
        try:
            a,l[first]=max(0,a-l[first]),max(0,l[first]-a)
            if l[first]==0:
                first+=1
                c+=1
        except:
            break
    index=c
    while b and last>=first:
        try:
            b,l[last]=max(0,b-l[last]),max(0,l[last]-b)
            if l[last]==0:
                last-=1
                c+=1
        except:
            break
    print(c)


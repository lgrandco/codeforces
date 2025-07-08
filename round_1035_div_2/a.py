from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    a,b,x,y = map(int, input().split())
    e = (b-a)//2
    d = (b-a)- e
    if a<=b:
        if a%2:
            print(d*x + e*(min(x,y)))
        else:
            print(e*x+ d*(min(x,y)))
    else:
        if a%2 and b == a-1:
            print(y)
        else:
            print(-1)

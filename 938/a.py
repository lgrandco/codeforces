from itertools import combinations
from collections import deque

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print(min(a//2*c+a%2*b,a*b))


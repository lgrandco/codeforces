from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	c=Counter(a)
	print(sum(v==2 for v in c.values()))


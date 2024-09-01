from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
	a,b=map(int,input().split())
	l=sorted(map(int,input().split()))
	for e in Counter(l).values():
		if b<=e:
			print(b-1)
			break
	else:
		print(a)


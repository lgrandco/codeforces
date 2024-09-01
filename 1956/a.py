from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
	input()
	a=sorted(map(int,input().split()),reverse=True)
	r=[]
	for e in map(int,input().split()):
		l=[*range(1,e+1)]
		c=1
		while c:
			c=0
			for i in range(len(a)):
				try:
					l.pop(a[i]-1)
					c=1
				except:
					pass
		# print(l)
		r+=len(l),
	print(*r)
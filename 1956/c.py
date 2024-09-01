from itertools import combinations
from collections import deque
from collections import Counter

def getsum(n):
	r=0
	for i in range(1,n+1):
		r+=sum(max(j,i) for j in range(1,n+1))
	return r

for _ in range(int(input())):
	n=int(input())
	i=n
	j=i-1
	print(getsum(n),2*n-1)
	while i:
		if i:
			print(1,i," ".join([*map(str,range(1,n+1))]))
			i-=1
		if j:
			print(2,j," ".join([*map(str,range(1,n+1))]))
			j-=1

from itertools import combinations
from collections import deque
from collections import Counter

def is_impossible(a):
	if len(set(a))==1:
		return True
	x=a[0]
	for i in range(len(a)+1):
		if a[i]!=x:
			break
	x=a[-1]
	for j in range(1,len(a)+1):
		if a[-j]!=x:
			break
	return False

for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	x=a[0]
	i=0
	j=0
	if is_impossible(a):
		print(-1)
		continue
	while i<n and a[i]==x:
		i+=1
	x2=a[-1]
	while j<n and a[n-1-j]==x2:
		j+=1
	print(min(i,j))

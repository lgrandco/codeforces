from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
	n=int(input())
	l= sorted(map(int,input().split()))
	player=1
	x=0
	i=0
	print(l)
	while i<n:
		if len(l[i:]) == l[i:].count(l[i]):
			break
		if l[i] - x<= 0:
			print(i)
			i+=1
			continue
		if l[i]-x>1:
			x+=l[i]-x-1
			print("hi")
		else:
			x+=1
			i+=1
		print(l[i],i,"turn changed, not", player, "anymore")
		player = player == 0
	print("Alice" if  player else "Bob")


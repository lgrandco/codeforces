from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
	a,b=map(int,input().split())
	d1=d2=d3=d4=b1=b2=b3=b4=0
	for i in range(a):
		l=input()
		if i==0:
			c1=l[0]=='W'
			c2=l[-1]=='W'
			d1 = 'W' in l
			b1 = 'B' in l
		if not d3:
			d3 = l[0]=='W'
		if not b3:
			b3 = l[0]=='B'
		if not b4:
			b4 = l[-1]=='B'
		if not d4:
			d4 = l[-1]=='W'
	c3=l[0]=='W'
	c4=l[-1]=='W'
	d2 = 'W' in l
	b2 = 'B' in l
	if c1 == d2 == d4 or c2 == d2 == d3 or c3 == d1 == d4 or c4 == d1 == d3:
		print("YES")
	elif not c1 and b2 and b4 or not c2 and b2 and b3 or not c3 and b1 and b4 or not c4 and b1 and b3:
		print("YES")
	else:
		print("NO")
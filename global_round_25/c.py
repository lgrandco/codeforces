for _ in range(int(input())):
	n,m,k = map(int,input().split())
	l=[*map(int,input().split())]
	l2=sorted(l)
	d=dict(enumerate(l))
	nd={}
	for entry in sorted(d,key=d.get):
		su=min(k,m)
		nd[entry]=su
		k-=su
	r=0
	su=0
	for i in range(n):
		if nd[i]:
			r+=(d[i]+su)*nd[i]
			su+=nd[i]
	print(r)
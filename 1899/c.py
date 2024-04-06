for i in range(int(input())):
	n=int(input())
	m,*l=*map(int,input().split()),
	_sum=m
	last=m
	for e in l:
		if e+_sum>e and last%2 != e%2:
			_sum=e+_sum
		else:
			_sum=e
		last=e
		m=max(_sum,m)
	print(m)

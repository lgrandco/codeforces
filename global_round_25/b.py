for _ in range(int(input())):
	n,cow=map(int,input().split())
	cow-=1
	m=0
	l=[*map(int,input().split())]
	val=0
	for i in range(cow):
		if l[i]>l[cow]:
			val=i
			break
	for i in (0,val):
		l[i],l[cow]=l[cow],l[i]
		c=0
		for j in range(i+1,len(l)):
			if l[i]>l[j]:
				c+=1
			else:
				break
		c+=int(i!=0)
		m=max(m,c)
		l[i],l[cow]=l[cow],l[i]
	print(m)
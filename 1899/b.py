import math



def f(mm,n,l):
	div_max=0
	# test=0
	trucks=[]
	j=0
	while j<len(l):
		truck=0
		for i in range(n):
			truck+=l[j]
			j+=1
		trucks+=truck,
	return max(max(trucks)-min(trucks),mm)


for i in range(int(input())):
	mm=0
	n=int(input())
	divisors=()
	l=*map(int,input().split()),
	for i in range(1,int(math.sqrt(n)+1)):
		if n%i<1:
			divisors+=n//i,i
	for e in divisors:
		mm=f(mm,e,l)
	print(mm)

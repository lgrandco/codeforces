for _ in range(int(input())):
	n=int(input())
	a=input()
	b=input()
	for i in range(1,n,2):
		if a[i]==b[i-1]=='<' or (i+1 < n-1 and a[i]=='<'==b[i+1]):
			print("NO")
			break
	else:
		print("YES")

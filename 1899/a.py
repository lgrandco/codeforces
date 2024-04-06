for i in range(int(input())):
	j=0
	n=int(input())
	if ((n+1)%3<1 or (n-1)%3<1):
		print("First")
	else:
		print("Second")

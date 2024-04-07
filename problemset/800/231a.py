r=0
for _ in range(int(input())):
	r+=input().count("1")>1
print(r)
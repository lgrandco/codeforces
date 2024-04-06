for _ in range(int(input())):
	n=int(input())
	s=input()
	print("YES" if s.count("1")%2<1 and not (s.count("1")==2 and s[s.index("1")+1]=='1' ) else "NO")

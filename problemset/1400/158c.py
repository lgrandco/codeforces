path=[]
for _ in range(int(input())):
	cmd=input().split(" ")
	if cmd[0]=="pwd":
		print("/"+"/".join(path)+" /"[bool(path)])
	elif cmd[0]=="cd":
		if cmd[1][0]=="/":path=[]
		new_path = path + cmd[1].strip("/").split("/")
		path=[]
		for i in range(len(new_path)):
			if new_path[i]!="..":
				path.append(new_path[i])
			else:
				path.pop()
from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
	n,m,k=map(int,input().split())
	n-=n%2
	if n>1 and m>1 and k<n-n/m:
		print("YES")
	else:
		print("NO")



# 50       1      0
# 50       2      25
# 50       3      50/3*2
# 50       50     49

# 5        1	  0
# 5        2    2
# 5        3    3
# 5        4    3
# 5        5    4

# 1 1 0



# 2 1 0
# 2 2 1

# 3 1 0
# 3 2 1
# 3 3 2

# 4 1 0
# 4 2 2
# 4 3 3
# 4 4 3
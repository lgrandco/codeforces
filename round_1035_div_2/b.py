from itertools import combinations, product
from collections import deque
from collections import Counter
import math

for _ in range(int(input())):
    n=int(input())
    px,py, qx, qy = map(int, input().split())
    a= *map(int, input().split()),
    _sum = sum(a)
    if _sum < math.dist((px, py), (qx, qy)):
        print("NO")
    elif any(e > _sum - e + math.dist((px, py), (qx, qy))  for e in a):
        print("NO")
    else:
        print("YES")
    # print("dist:", math.dist((px, py), (qx, qy)))

# You are given two points (px,py)
#  and (qx,qy)
#  on a Euclidean plane.

# You start at the starting point (px,py)
#  and will perform n
#  operations. In the i
# -th operation, you must choose any point such that the Euclidean distance∗
#  between your current position and the point is exactly ai
# , and then move to that point.

# Determine whether it is possible to reach the terminal point (qx,qy)
#  after performing all operations.

# ∗
# The Euclidean distance between (x1,y1)
#  and (x2,y2)
#  is (x1−x2)2+(y1−y2)2−−−−−−−−−−−−−−−−−−√

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.

# The first line of each test case contains a single integer n
#  (1≤n≤103
# ) — the length of the sequence a
# .

# The second line of each test case contains four integers px,py,qx,qy
#  (1≤px,py,qx,qy≤107
# ) — the coordinates of the starting point and terminal point.

# The third line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤104
# ) — the distance to move in each operation.

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output "Yes" if it is possible to reach the terminal point (qx,qy)
#  after all operations; otherwise, output "No".

# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

# Example
# InputCopy
# 5
# 2
# 1 1 5 1
# 3 3
# 3
# 1 1 3 3
# 2 3 4
# 2
# 100 100 100 100
# 4 5
# 1
# 5 1 1 4
# 5
# 2
# 10000000 10000000 10000000 10000000
# 10000 10000
# OutputCopy
# Yes
# Yes
# No
# Yes
# Yes
from itertools import combinations
from collections import deque
from collections import Counter


def get_next_2_power(l, r):
    if l > r:
        return -1
    power = 1
    while power <= l:
        power *= 2
    if power > r:
        return -1
    return power


for _ in range(int(input())):
    n, l, r, k = map(int, input().split())
    if n % 2:
        print(l)
    else:
        next_2_power = get_next_2_power(l, r)
        if next_2_power == -1 or n <= 2:
            print(-1)
            continue
        if k == n or k == n - 1:
            print(next_2_power)
        else:
            print(l)

# You are given four positive integers n,l,r,k
# . You need to find the lexicographically smallest∗
#  array a
#  of length n
# , consisting of integers, such that:

# For every 1≤i≤n
# , l≤ai≤r
# .
# a1&a2&…&an=a1⊕a2⊕…⊕an
# , where &
#  denotes the bitwise AND operation and ⊕
#  denotes the bitwise XOR operation.
# If no such array exists, output −1
# . Otherwise, since the entire array might be too large to output, output ak
#  only.

# ∗
# An array a
#  is lexicographically smaller than an array b
#  if and only if one of the following holds:

# a
#  is a prefix of b
# , but a≠b
# ; or
# in the first position where a
#  and b
#  differ, the array a
#  has a smaller element than the corresponding element in b
# .
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.

# Each test case contains four positive integers n,l,r,k
#  (1≤k≤n≤1018
# , 1≤l≤r≤1018
# ).

# Output
# For each test case, output ak
#  or −1
#  if no array meets the conditions.

# Example
# InputCopy
# 9
# 1 4 4 1
# 3 1 3 3
# 4 6 9 2
# 4 6 9 3
# 4 6 7 4
# 2 5 5 1
# 2 3 6 2
# 999999999999999999 1000000000000000000 1000000000000000000 999999999999999999
# 1000000000000000000 1 999999999999999999 1000000000000000000
# OutputCopy
# 4
# 1
# 6
# 8
# -1
# -1
# -1
# 1000000000000000000
# 2
# Note
# In the first test case, the array a=[4]
# . It can be proven that there is no array that meets the above requirements and has a smaller lexicographic order.

# In the second test case, the array a=[1,1,1]
# . It can be proven that there is no array that meets the above requirements and has a smaller lexicographic order.

# In the third test case and the fourth test case, the array a=[6,6,8,8]
# . It can be proven that there is no array that meets the above requirements and has a smaller lexicographic order.

# In the fifth test case and the sixth test case, it can be proven that there is no array that meets the above requirements.

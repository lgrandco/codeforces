import math
from collections import Counter
n=int(input())
c=Counter(map(int,input().split()))
r=c[4]
r+=math.ceil(c[2]/2)
c[2]%=2
r+=c[3]
c[1]=max(0,c[1]-c[3])
c[1]=max(0,c[1]-2*c[2])
r+=math.ceil(c[1]/4)
print(r)
import sys

input = sys.stdin.readline

d = dict()
for i in range(1, int(2e5 + 1)):
    d[i] = d.get(i - 1, 0) + sum(map(int, str(i)))
# print(d)

for _ in range(int(input())):
    r = 0
    print(d[int(input())])

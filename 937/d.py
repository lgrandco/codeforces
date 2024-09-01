from itertools import combinations, product
from collections import deque
from collections import Counter

# l = []
# for i in range(2, int(100000)):
#     if all(e in "01" for e in str(i)):
#         l += [i]
# print(l)
l = [
    10,
    11,
    100,
    101,
    110,
    111,
    1000,
    1001,
    1010,
    1011,
    1100,
    1101,
    1110,
    1111,
    10000,
    10001,
    10010,
    10011,
    10100,
    10101,
    10110,
    10111,
    11000,
    11001,
    11010,
    11011,
    11100,
    11101,
    11110,
    11111,
]

for _ in range(int(input())):
    n = int(input())
    f = 1
    div = len(l) - 1
    while n != 1 and div >= 0:
        if n % l[div] < 1:
            n //= l[div]
        else:
            div -= 1
    if div < 0:
        print("NO")
    else:
        print("YES")

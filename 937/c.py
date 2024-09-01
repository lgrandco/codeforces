from itertools import combinations, product
from collections import deque
from collections import Counter

for _ in range(int(input())):
    a, b = map(int, input().split(":"))
    print(f'{a%12 + 12*(not a%12):02}:{b:02} {"AM" if a//12<1 else "PM"}')

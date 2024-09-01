from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(s.count("map") + s.count("pie") - s.count("mapie"))

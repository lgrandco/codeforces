from itertools import combinations, product
from collections import deque
from collections import Counter, defaultdict


for _ in range(int(input())):
    n, k, q = map(int, input().split())
    d = dict()
    points = [*map(int, input().split())]
    times = [*map(int, input().split())]
    for i in range(k):
        time = times[i]
        if i == 0:
            speed = time / points[i]
            _min = 0
        else:
            speed = (time - times[i - 1]) / (points[i] - points[i - 1])
            _min = points[i - 1] + 1
        d[(points[i])] = speed
    # print(d)
    # print("points", points)
    queries = [int(input()) for i in range(q)]
    d_query = defaultdict(int)
    i = 0
    last = 0
    last_2 = 0
    # print("points", points)
    for e in sorted(queries):
        while i < k and e > points[i]:
            # print("e,", e, "points[i]", points[i])
            last_2 += (points[i] - last) * d[points[i]]
            last = points[i]
            i += 1
            # print("e", e)
        d_query[e] += last_2 + (e - last) * d[points[i]]
        # print("e2,", e, "points[i]", points[i])
    # print(d_query)
    # print("qu", d_query)
    # print(*[e for e in queries])
    print(*[int(d_query[e]) for e in queries])

from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n, m, x = map(int, input().split())
    players = {x}
    for i in range(m):
        a, b = input().split()
        a = int(a)
        new_set = set()
        rotation = -1 if b == "1" else 1 if b == "0" else 0
        for elem in players:
            if rotation:
                rotation = -1 if b == "1" else 1
                new_elem = (elem + rotation * a - 1) % n + 1
                if new_elem == 0:
                    new_elem = n
                new_set.add(new_elem)
            else:
                new_elem = (elem - a - 1) % n + 1
                if new_elem == 0:
                    new_elem = n
                new_set.add(new_elem)
                new_elem = (elem + a) % n
                if new_elem == 0:
                    new_elem = n
                new_set.add(new_elem)
        players = new_set
    print(len(players))
    print(*(sorted(players)))

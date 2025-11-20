from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import sys, math


def input():
    return sys.stdin.readline().strip()


get = input


def p(x):
    if isinstance(x, bool):
        print("YES" if x else "NO")
    elif isinstance(x, list) or isinstance(x, tuple):
        print(*x)
    else:
        print(x)


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    r = 0
    monsters = [[e, f, 0] for e, f in zip(b, c)]
    # print(monsters)
    while a and monsters:
        for i, e in enumerate(monsters):
            monsters[i][2] = sum(
                e[1] >= health for health, _, _ in monsters
            ) - (e[1] >= e[0])
        # print(monsters, "z")
        try:
            idx_monster, monster = max(
                [(i, e) for i, e in enumerate(monsters) if e[0] <= max(a)],
                key=lambda x: [x[1][2], -x[1][1]],
            )
        except:
            break
        try:
            # print(monsters, "monster removed", idx_monster, monster)
            sword, idx_sword = min(
                (e, i) for i, e in enumerate(a) if e >= monster[0]
            )
            # print(a, "sword removed", idx_sword, sword)
            a.pop(idx_sword)
            a.append(monsters.pop(idx_monster)[1])
            # print(monsters, "fff", a)
        except:
            while 1:
                pass

    print(m - len(monsters))

    # print("\n\n\n")

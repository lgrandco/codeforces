from collections import deque

for _ in range(int(input())):
    n, m, x = map(int, input().split())
    stack = deque()
    stack.append(x)
    players = set()
    for i in range(m):
        a, b = input().split()
        a = int(a)
        new_stack = deque()
        for elem in stack:
            if b == "0":
                new_stack.append((elem + a) % n)
                players.add(new_stack[-1])
            elif b == "1":
                new_stack.append((elem - a) % n)
                players.add(new_stack[-1])
            else:
                new_stack.append((elem + a) % n)
                new_stack.append((elem - a) % n)
                players.add(new_stack[-1])
                players.add(new_stack[-2])
        stack = new_stack
    print(len(players))
    print(*(sorted(players)))

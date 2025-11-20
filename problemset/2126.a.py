for _ in range(int(input())):
    n = int(input())
    min = None
    for e in str(n):
        e = int(e)
        if min is None or e < min:
            min = e
    print(e)

from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
import math


def get_prime_factors(n):
    factors = set()
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.add(temp)
    return factors


for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    input()
    # s = 2
    # for a, b in combinations(a, 2):
    #     if math.gcd(a, b) > 1:
    #         s = 0
    #         break
    #     elif math.gcd(a, b + 1) > 1 or math.gcd(a + 1, b) > 1:
    #         s = min(1, s)
    # print(s)
    d = set()
    d2 = set()
    s = 2
    for e in a:
        if s == 0:
            break
        factors_e = get_prime_factors(e)
        factors_e_plus_1 = get_prime_factors(e + 1)
        if any(f in d for f in factors_e):
            s = 0
        else:
            if any(f in d2 for f in factors_e) or any(
                f in d for f in factors_e_plus_1
            ):
                s = min(s, 1)
        d.update(factors_e)
        d2.update(factors_e_plus_1)
    print(s)

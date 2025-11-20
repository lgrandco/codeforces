from itertools import combinations, product
from collections import deque, Counter, defaultdict
import math
from random import shuffle
from bisect import bisect_left, bisect_right

from typing import List
from itertools import combinations, product, permutations
from functools import lru_cache
from typing import List


class Solution:
    def fndMax(self, n: int, m: int, arr1: List[int], arr2: List[int]) -> int:
        arr1.sort()
        arr2.sort()

        @lru_cache(None)
        def helper(i, available):
            if i == n:
                return 0
            max_diff = float("-inf")
            for j in range(m):
                if available & (1 << j):
                    next_available = available ^ (1 << j)
                    diff = abs(arr1[i] - arr2[j]) + helper(i + 1, next_available)
                    max_diff = max(max_diff, diff)

            return max_diff

        return helper(0, (1 << m) - 1)

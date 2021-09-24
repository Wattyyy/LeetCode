from typing import List, Tuple
from itertools import combinations


class Solution:
    def count(self, order: Tuple[int, ...], arr: List[str]) -> int:
        checked = set()
        for i in order:
            for char in arr[i]:
                if char in checked:
                    return 0
                else:
                    checked.add(char)
        return len(checked)

    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        ans = 0
        for r in range(1, N + 1):
            for order in combinations([i for i in range(N)], r):
                res = self.count(order, arr)
                ans = max(ans, res)
        return ans

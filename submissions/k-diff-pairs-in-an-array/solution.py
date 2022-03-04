from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        if k == 0:
            cnt = Counter(nums)
            for _, val in cnt.items():
                if 2 <= val:
                    ans += 1
            return ans

        st = set([nums[0]])
        for i, num in enumerate(nums):
            if i == 0 or num in st:
                continue
            if num - k in st:
                ans += 1
            if num + k in st:
                ans += 1
        return ans

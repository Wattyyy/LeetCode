from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] < 0:
                return 0
            else:
                return 1
        N = len(nums)
        minus_len = [0] * N
        plus_len = [0] * N
        if nums[0] < 0:
            minus_len[0] = 1
        if 0 < nums[0]:
            plus_len[0] = 1
        for i in range(1, N):
            if nums[i] < 0:
                minus_len[i] = max(plus_len[i - 1] + 1, 1)
                if 0 < minus_len[i - 1]:
                    plus_len[i] = minus_len[i - 1] + 1
            if 0 < nums[i]:
                plus_len[i] = max(plus_len[i - 1] + 1, 1)
                if 0 < minus_len[i - 1]:
                    minus_len[i] = minus_len[i - 1] + 1
                    
        return max(plus_len)



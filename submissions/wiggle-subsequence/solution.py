# https://leetcode.com/problems/wiggle-subsequence


class Solution:
    def wiggleMaxLength(self, nums):
        N = len(nums)
        down, neutral, up = [0] * N, [1] * N, [0] * N
        for i in range(1, N):
            r_num = nums[i]
            for j in range(0, i):
                l_num = nums[j]
                # update down
                if l_num > r_num:
                    down[i] = max(down[i], neutral[j] + 1, up[j] + 1)
                # update up
                if l_num < r_num:
                    up[i] = max(up[i], neutral[j] + 1, down[j] + 1)
        return max(max(down), max(neutral), max(up))

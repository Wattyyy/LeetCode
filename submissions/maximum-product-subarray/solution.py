# https://leetcode.com/problems/maximum-product-subarray

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    def merge(self, l, m, r, nums):
        l_min, l_max = 0, 0
        l_prod = 1
        for i in reversed(range(l, m + 1)):
            l_prod *= nums[i]
            l_min = min(l_prod, l_min)
            l_max = max(l_prod, l_max)

        r_min, r_max = 0, 0
        r_prod = 1
        for i in range(m + 1, r + 1):
            r_prod *= nums[i]
            r_min = min(r_prod, r_min)
            r_max = max(r_prod, r_max)

        res = max(l_min * r_min, l_max * r_max)
        return res

    def divide_and_conquer(self, l, r, nums):
        if l == r:
            return nums[l]
        m = (l + r) // 2
        l_val = self.divide_and_conquer(l, m, nums)
        r_val = self.divide_and_conquer(m + 1, r, nums)
        merge_val = self.merge(l, m, r, nums)
        return max(l_val, r_val, merge_val)

    def maxProduct(self, nums):
        if not nums:
            return 0
        res = self.divide_and_conquer(0, len(nums) - 1, nums)
        return res

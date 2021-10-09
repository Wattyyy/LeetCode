from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        N = len(nums)
        odd_idx, even_idx = -1, -1
        for i, num in enumerate(nums):
            if i % 2 == 1 and num % 2 == 0 and odd_idx == -1:
                odd_idx = i
            if i % 2 == 0 and num % 2 == 1 and even_idx == -1:
                even_idx = i

        if odd_idx == even_idx == -1:
            return nums

        while odd_idx < N and even_idx < N:
            nums[odd_idx], nums[even_idx] = nums[even_idx], nums[odd_idx]
            while odd_idx < N:
                if odd_idx % 2 == 1 and nums[odd_idx] % 2 == 0:
                    break
                odd_idx += 1
            while even_idx < N:
                if even_idx % 2 == 0 and nums[even_idx] % 2 == 1:
                    break
                even_idx += 1

        return nums

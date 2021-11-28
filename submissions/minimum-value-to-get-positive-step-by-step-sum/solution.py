class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cum_sum = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                cum_sum[0] = nums[0]
            else:
                cum_sum[i] = cum_sum[i-1] + num
        
        min_val = min(cum_sum)
        if 0 < min_val:
            return 1
        return abs(min_val) + 1

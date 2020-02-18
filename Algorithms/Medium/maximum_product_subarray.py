# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        max_dp = [nums[0] for _ in range(len(nums))]
        min_dp = [nums[0] for _ in range(len(nums))]
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i]>0:
                max_dp[i] = max(max_dp[i-1]*nums[i], nums[i])
                min_dp[i] = min(min_dp[i-1]*nums[i], nums[i])
            else:
                max_dp[i] = max(min_dp[i-1]*nums[i], nums[i])
                min_dp[i] = min(max_dp[i-1]*nums[i], nums[i])
            ans = max(ans, max_dp[i])
        return ans
            
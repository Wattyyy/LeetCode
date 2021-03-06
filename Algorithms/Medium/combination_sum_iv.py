# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums, target):
        nums = sorted(nums)
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i-num>=0:
                    dp[i] += dp[i-num]
                else:
                    continue            
        return dp[target]
        

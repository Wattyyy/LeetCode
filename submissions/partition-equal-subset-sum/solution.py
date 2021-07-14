// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums):
        S = sum(nums)
        if S % 2 == 1:
            return False
        R, C = len(nums) + 1, int(S / 2) + 1
        dp = [[False for _ in range(C)] for __ in range(R)]
        dp[0][0] = True
        nums = [0] + nums
        for r in range(R):
            for c in range(C):
                if r == 0:
                    continue
                else:
                    if 0 <= c - nums[r]:
                        dp[r][c] = (dp[r-1][c] or dp[r-1][c - nums[r]])
                    else:
                        dp[r][c] = dp[r-1][c]
        return dp[-1][-1]
                                    
                        
        
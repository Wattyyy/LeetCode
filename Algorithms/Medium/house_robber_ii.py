# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        
        N = len(nums)
        
        # use nums[0]
        dp1 = [0 for _ in range(N)]
        dp1[0], dp1[1] = nums[0], nums[0]
        for i in range(2, N):
            if i==N-1:
                dp1[N-1] = dp1[N-2]
            else:
                dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])
        
        # use nums[1]
        dp2 = [0 for _ in range(N)]
        dp2[0], dp2[1] = 0, nums[1]
        for i in range(2, N):
            dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])
        
        return max(dp1[-1], dp2[-1])

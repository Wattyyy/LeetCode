// https://leetcode.com/problems/delete-and-earn

from collections import Counter
class Solution:
    def deleteAndEarn(self, nums):
        ls = [0] * 10001
        counter = Counter(nums)
        for num, cnt in counter.items():
            ls[num] = num * cnt
        
        dp = [0] * 10001
        dp[1] = ls[1]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2]+ls[i], dp[i-1])        
        
        return max(dp)


        
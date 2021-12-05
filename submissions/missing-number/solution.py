# https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums):
        N = len(nums)
        seq_sum = N * (N + 1) // 2
        return seq_sum - sum(nums)
    
        
        
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0

        def merge_sum(l, r, m):
            if l == r:
                return nums[l]
            left_sum = -float('inf')
            left_cum = 0
            for i in reversed(range(l, m+1)):
                left_cum += nums[i]
                left_sum = max(left_sum, left_cum)
            right_sum = -float('inf')
            right_cum = 0
            for i in range(m+1, r+1):
                right_cum += nums[i]
                right_sum = max(right_sum, right_cum)
            return left_sum + right_sum
            
        def divide_and_conquer(l, r):
            if l == r:
                return nums[l]
            m = (l + r) // 2
            left_val = divide_and_conquer(l, m)
            right_val = divide_and_conquer(m+1, r)
            merge_val = merge_sum(l, r, m)
            return max(left_val, right_val, merge_val)
        
        res = divide_and_conquer(0, len(nums)-1)
        return res
            
            
                
            
            
            

        

# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array

class Solution:
    def findMaximumXOR(self, nums):
        if not nums:
            return 0
        L = len(bin(max(nums))[2:])
        ans = 0
        for i in reversed(range(L)):
            ans = ans << 1
            num_set = {num >> i for num in nums}
            cur = ans | 1
            for num in num_set:
                if num ^ cur in num_set:
                    ans = cur
                    break
                    
        return ans
        
            
            
                    
            
        
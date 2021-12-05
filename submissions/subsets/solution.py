# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums):
        if not nums:
            return []
        res = []
        L = len(nums)
        for binary in range(2 ** L):
            tmp =[]
            i = 0
            while binary:
                if binary & 1:
                    tmp.append(nums[i])
                i += 1
                binary = binary >> 1
            res.append(tmp[:])
                
        return res
        
        
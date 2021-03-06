# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums):
        L = len(nums)
        output = []
        for i in range(2**L):
            tmp = []
            for j in range(L):
                flag = (i >> j) & 1
                if flag:
                    tmp.append(nums[j])
            output.append(tmp)
        return output
                
        

# https://leetcode.com/problems/permutations/

from copy import deepcopy
class Solution:
    def permute(self, nums):
        if not nums:
            return [[]]
    
        self.res = []
        def helper(nums, used, per):
            if len(per)==len(nums):
                self.res.append(per)
                return
            for num in nums:
                if num not in used:
                    tmp_used = deepcopy(used)
                    tmp_per = deepcopy(per)
                    tmp_used.add(num)
                    tmp_per.append(num)
                    helper(nums, tmp_used, tmp_per)
        used = set()
        per = []
        helper(nums, used, per)
        return self.res
        
        

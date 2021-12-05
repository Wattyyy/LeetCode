# https://leetcode.com/problems/3sum

from collections import defaultdict

class Solution:
    def threeSum(self, nums):
        val2idx = defaultdict(list)
        nums = sorted(nums)
        for i, v in enumerate(nums):
            val2idx[v].append(i)
        ans_set = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = -1 * (nums[i] + nums[j])
                if target in val2idx and j < val2idx[target][-1]:
                    k = val2idx[target][-1]
                    ans_set.add((nums[i], nums[j], nums[k]))
        
        ans = []
        for item in ans_set:
            ans.append(list(item))
        return ans

                    


                
                
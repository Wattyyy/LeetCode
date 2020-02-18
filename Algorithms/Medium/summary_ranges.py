# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        ans = []
        le, prev = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] - prev == 1:
                prev = nums[i]
            else:
                if le != prev:
                    ans.append(str(le) + "->" + str(prev))
                else:
                    ans.append(str(le))
                le, prev = nums[i], nums[i]
                
        if le != prev:
            ans.append(str(le) + "->" + str(prev))
        else:
            ans.append(str(le))
        return ans
        

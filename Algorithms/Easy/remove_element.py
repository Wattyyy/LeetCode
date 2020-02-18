# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val):
        lp, rp = 0, len(nums) - 1
        while lp <= rp:
            while nums[rp] == val:
                nums.pop()
                rp -= 1
                if (not nums) or (rp < lp):
                    return len(nums)    
            if nums[lp] != val:
                lp += 1
            else:
                nums[lp], nums[rp] = nums[rp], nums[lp]
                nums.pop()
                lp += 1
                rp -= 1
        return len(nums)


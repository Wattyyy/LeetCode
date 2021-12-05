# https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution:
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if 0 < mid and nums[mid-1] == nums[mid]:
                if (mid - 1) % 2 == 0:
                    l = mid + 1
                else:
                    r = mid - 2
            elif mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1
            else:
                return nums[mid]
        
        return nums[l]
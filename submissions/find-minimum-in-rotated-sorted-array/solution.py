# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid] <= nums[r]:
                r = mid - 1
            elif nums[l] >= nums[r]:
                if nums[mid] >= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]
            
                
                
        
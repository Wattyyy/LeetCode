from typing import List


class Solution:
    def __init__(self) -> None:
        self.ans = 5001

    def binSearch(self, left, right, nums) -> None:
        if left > right:
            return
        self.ans = min(self.ans, nums[left])
        mid = (left + right) // 2
        if nums[left] == nums[mid] == nums[right]:
            self.binSearch(left, mid - 1, nums)
            self.binSearch(mid + 1, right, nums)
        elif nums[left] <= nums[mid] <= nums[right]:
            self.binSearch(left, mid - 1, nums)
        elif nums[left] <= nums[mid] >= nums[right]:
            self.binSearch(mid + 1, right, nums)
        else:
            self.binSearch(left + 1, mid, nums)

    def findMin(self, nums: List[int]) -> int:
        self.binSearch(0, len(nums) - 1, nums)
        return self.ans

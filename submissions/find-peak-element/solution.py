# https://leetcode.com/problems/find-peak-element

class Solution:
    def binSearch(self, l, r, arr):
        N = len(arr)
        mid = (l + r) // 2
        
        # arr[mid-1] < arr[mid] > arr[mid+1]
        if (mid == 0 or arr[mid-1] < arr[mid]) and (mid == N-1 or arr[mid] > arr[mid+1]):
            return mid
        
        # arr[mid] < arr[mid+1]
        elif mid < N and arr[mid] < arr[mid+1]:
            return self.binSearch(mid+1, r, arr)
        
        # arr[mid-1] > arr[mid]
        else:
            return self.binSearch(l, mid-1, arr)
        
        
    def findPeakElement(self, nums: List[int]) -> int:
        res = self.binSearch(0, len(nums) - 1, nums)
        return res
        
        
        
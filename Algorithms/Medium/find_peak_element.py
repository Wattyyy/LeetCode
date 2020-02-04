# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums):
        def search(l, r, arr, N):
            mid = (l + r) // 2
            if (mid==0 or arr[mid-1]<arr[mid]) and (mid==N-1 or arr[mid]>arr[mid+1]):
                return mid
            elif arr[mid]<arr[mid+1]:
                return search(mid+1, r, arr, N)
            else:
                return search(l, mid-1, arr, N)
        N = len(nums)
        return search(0, N-1, nums, N)

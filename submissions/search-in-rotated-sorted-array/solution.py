# https://leetcode.com/problems/search-in-rotated-sorted-array


class Solution:
    def search(self, nums, target):
        N = len(nums)
        if N == 0:
            return -1
        if N == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        def find_rot_idx(l, r):
            if nums[l] < nums[r]:
                return 0

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[l] > nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1

        def search(l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1

        rot_idx = find_rot_idx(0, N - 1)

        if nums[rot_idx] == target:
            return rot_idx
        if rot_idx == 0:
            return search(0, N - 1)
        if target < nums[0]:
            return search(rot_idx, N - 1)
        else:
            return search(0, rot_idx)

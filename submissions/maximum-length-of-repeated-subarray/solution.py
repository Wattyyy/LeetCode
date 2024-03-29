# https://leetcode.com/problems/maximum-length-of-repeated-subarray


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = [-1] + nums1
        nums2 = [-1] + nums2
        dp = [[0 for _ in range(len(nums2))] for __ in range(len(nums1))]
        ans = 0
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans

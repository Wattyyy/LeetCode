# https://leetcode.com/problems/max-dot-product-of-two-subsequences


class Solution:
    def maxDotProduct(self, nums1, nums2):
        ans = 0
        n1 = [-float("inf")] + nums1
        n2 = [-float("inf")] + nums2
        R, C = len(n1), len(n2)
        dp = [[0 for _ in range(C)] for __ in range(R)]

        ans = -float("inf")
        for i in range(1, R):
            for j in range(1, C):
                dp[i][j] = max(
                    dp[i - 1][j - 1] + n1[i] * n2[j], dp[i - 1][j], dp[i][j - 1]
                )
                ans = max(ans, dp[i][j])

        if ans == 0:
            if all([n < 0 for n in nums1]):
                return max(nums1) * min(nums2)
            elif all([n < 0 for n in nums2]):
                return max(nums2) * min(nums1)

        return ans

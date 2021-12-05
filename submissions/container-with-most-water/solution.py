# https://leetcode.com/problems/container-with-most-water


class Solution:
    def maxArea(self, height):
        ans = 0
        N = len(height)
        lp, rp = 0, N - 1
        while lp < rp:
            ans = max(ans, min(height[lp], height[rp]) * (rp - lp))
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return ans

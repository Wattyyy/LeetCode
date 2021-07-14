// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height):
        if not height:
            return 0
        N = len(height)
        ans = 0
        lp, rp = 0, N-1
        l_max_h, r_max_h = height[lp], height[rp]
        while lp < rp:
            if height[lp] < height[rp]:
                lp += 1
                ans += max(0, l_max_h - height[lp])
                l_max_h = max(l_max_h, height[lp])
            else:
                rp -= 1
                ans += max(0, r_max_h - height[rp])
                r_max_h = max(r_max_h, height[rp])
        return ans

        
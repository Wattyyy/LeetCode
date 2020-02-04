# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        if not height or len(height)==1:
            return 0
        lp, rp = 0, len(height)-1
        ans = 0
        while lp < rp:
            if height[lp]>height[rp]:
                ans = max(ans, height[rp]*(rp-lp))
                rp -= 1
            else:
                ans = max(ans, height[lp]*(rp-lp))
                lp += 1
        return ans
                
            

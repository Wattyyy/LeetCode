# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        lp, rp = 0, 0
        ans = len(nums) + 1
        cur_sum = nums[rp]
        while lp <= rp:
            if cur_sum < s:
                if rp < len(nums) - 1:
                    rp += 1
                    cur_sum += nums[rp]
                else:
                    break
            else:
                ans = min(ans, rp-lp+1)
                cur_sum -= nums[lp]
                lp += 1
        
        if ans == len(nums) + 1:
            return 0
        else:
            return ans
# https://leetcode.com/problems/max-consecutive-ones


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        is_consec = False
        cnt, ans = 0, 0
        for i in range(len(nums)):
            if (nums[i] == 1) and is_consec:
                cnt += 1
                ans = max(ans, cnt)
            elif (nums[i] == 1) and (not is_consec):
                is_consec = True
                cnt = 1
                ans = max(ans, cnt)
            else:
                is_consec = False

        return ans

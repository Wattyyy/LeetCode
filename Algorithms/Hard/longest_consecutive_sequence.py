# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        num_set = set(nums)
        no_previous = []
        for num in nums:
            if num - 1 not in num_set:
                no_previous.append(num)
        ans = 1
        for num in no_previous:
            tmp = 1
            cur = num
            while True:
                if cur + 1 in num_set:
                    tmp += 1
                    cur += 1
                else:
                    break
            ans = max(tmp, ans)

        return ans

                    


        

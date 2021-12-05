# https://leetcode.com/problems/sliding-window-median

from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        s = SortedList()
        for i in range(k):
            s.add(nums[i])
            
        if k % 2 == 0:
            ans.append( (s[k // 2 - 1] + s[k // 2]) / 2 )
        else:
            ans.append(s[k // 2])
            
        for i in range(k, len(nums)):
            s.remove(nums[i - k])
            s.add(nums[i])
            if k % 2 == 0:
                ans.append( (s[k // 2 - 1] + s[k // 2]) / 2 )
            else:
                ans.append(s[k // 2])
        
        return ans

        
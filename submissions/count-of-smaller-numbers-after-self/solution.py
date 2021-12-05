# https://leetcode.com/problems/count-of-smaller-numbers-after-self

from sortedcontainers import SortedList
from collections import deque
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rev = nums[::-1]
        ans = deque([])
        s = SortedList()
        for num in rev:
            idx = s.bisect_left(num)
            ans.appendleft(idx)
            s.add(num)
        return list(ans)
                
            
        
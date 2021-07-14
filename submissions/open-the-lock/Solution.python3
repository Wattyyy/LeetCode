// https://leetcode.com/problems/open-the-lock

from typing import List
from collections import defaultdict, deque

class Solution:        
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        convert = defaultdict(list)
        for num in range(10):
            if num == 0:
                convert[str(num)] = ['1', '9']
            elif num == 9:
                convert[str(num)] = ['0', '8']
            else:
                convert[str(num)] = [str(num - 1), str(num + 1)]
        ans = -1
        visited = set()
        visited.add("0000")
        d_set = set(deadends)
        queue = deque([("0000", 0)])
        while queue:
            string, cnt = queue.popleft()
            if string == target:
                ans = cnt
                break
            for i in range(4):
                for char in convert[string[i]]:
                    new_str = string[:i] + char + string[i+1:]
                    if (new_str not in visited) and (new_str not in d_set):
                        visited.add(new_str)
                        queue.append( (new_str, cnt+1) )
        
        return ans


        
        
        
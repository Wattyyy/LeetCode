# https://leetcode.com/problems/count-binary-substrings

from collections import deque
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        queue = deque([0], maxlen=2)
        cnt = 0
        for i, char in enumerate(s):
            if i == 0:
                continue
            if s[i-1] == char:
                if len(queue) != 2:
                    continue
                diff = i - queue[1]
                if s[queue[0] + diff] != char:
                    cnt += 1
            else:
                queue.append(i)
                cnt += 1
        return cnt

                
            
            
        
        
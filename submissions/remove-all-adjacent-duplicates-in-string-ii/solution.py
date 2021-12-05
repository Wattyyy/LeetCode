# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

from collections import deque
from typing import List

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque([])
        stack.append((s[0], 1))
        for i, char in enumerate(s):
            if i == 0:
                continue
            if (len(stack) == 0) or (stack[-1][0] != char):
                stack.append((char, 1))
            else:
                cnt = stack[-1][1]
                stack.append((char, cnt+1))
                if stack[-1][1] == k:
                    for _ in range(k):
                        stack.pop()
        res = []
        for item in stack:
            res.append(item[0])
        return ''.join(res)
        

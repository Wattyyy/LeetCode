# https://leetcode.com/problems/generate-parentheses

from typing import List

class Solution:
    def is_valid(self, string_list: List) -> bool:
        stack = []
        for char in string_list:
            if len(stack) == 0:
                stack.append(char)
            elif stack[-1] == '(' and char == ')':
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0

    def generateParenthesis(self, n: int) -> List[str]:
        N = (n * 2) 
        ans = []
        for i in range(2 ** N):
            num = i
            ls = []
            for _ in range(N):
                if num & 1:
                    ls.append('(')
                else:
                    ls.append(')')
                num = num >> 1
            if self.is_valid(ls):
                ans.append(''.join(ls))
        return ans
        
        
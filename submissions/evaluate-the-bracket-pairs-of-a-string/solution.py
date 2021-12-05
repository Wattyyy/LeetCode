# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string

from collections import defaultdict
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = defaultdict(str)
        for k, v in knowledge:
            key = '(' + k + ')'
            d[key] = v
        
        stack = []
        new = []
        flag = False
        for char in s:
            if char == '(':
                flag = True
                new.append(char)
            elif char == ')':
                flag = False
                new.append(char)
                stack.append(''.join(new))
                new = []
            elif flag:
                new.append(char)
            else:
                stack.append(char)

        N = len(stack)
        for i in range(N):
            if stack[i][0] == '(':
                if stack[i] in d:
                    v = d[stack[i]]
                    stack[i] = v
                else:
                    stack[i] = '?'


            

        return ''.join(stack)

            
        
        
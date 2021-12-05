# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        valid = set()
        for idx, char in enumerate(s):
            if char == ')':
                if stack and stack[-1][0] == '(':
                    item = stack.pop()
                    valid.add(item[1])
                    valid.add(idx)
                else:
                    stack.append((char, idx))
            
            elif char == '(':
                stack.append((char, idx))
                
            else:
                valid.add(idx)    

        
        ans = []
        for idx, char in enumerate(s):
            if idx in valid:
                ans.append(char)
        return ''.join(ans)
            
        
                    


        
# https://leetcode.com/problems/decode-string/

from collections import deque
class Solution:
    def decodeString(self, s):
        nums = set([str(i) for i in range(10)])
        stack = []
        for item in s:
            if item == "]":
                char_deque = deque([])
                # get string between "[" and "]"
                while stack:
                    char = stack.pop()
                    if char=="[":
                        break
                    else:
                        char_deque.appendleft(char)
                
                # get number before "["
                num_deque = deque([])
                while stack:
                    char = stack.pop()
                    if char in nums:
                        num_deque.appendleft(char)
                    else:
                        stack.append(char)
                        break

                num = int("".join(num_deque))
                string = "".join(char_deque * num)
                stack.append(string)
                
            else:
                stack.append(item)

        return "".join(stack)    
        
        

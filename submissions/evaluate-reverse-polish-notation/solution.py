# https://leetcode.com/problems/evaluate-reverse-polish-notation

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for char in tokens:
            if char in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(str( int(num1) + int(num2) ))
                elif char == '-':
                    stack.append(str( int(num1) - int(num2) ))
                elif char == '*':
                    stack.append(str( int(num1) * int(num2) ))
                else:
                    stack.append(str( int( int(num1) / int(num2)) ))
            else:
                stack.append(char)
        return int(stack[0])
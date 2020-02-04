# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from math import (floor, ceil)
from collections import deque

class Solution:
    def trunc_div(self, a, b):
        c = a / b
        if c > 0:
            return floor(c)
        else:
            return ceil(c)

    def evalRPN(self, tokens):
        if not tokens:
            return 0
        N = len(tokens)
        operators = {"+", "-", "*", "/"}
        st = deque([])
        for i in range(N):
            item = tokens[i]
            if item in operators:
                b = int(st.pop())
                a = int(st.pop())
                if item == "+":
                    st.append(a + b)
                elif item == "-":
                    st.append(a - b)
                elif item == "*":
                    st.append(a * b)
                else:
                    st.append(self.trunc_div(a, b))
            else:
                st.append(item)
            
        return st[-1]
        

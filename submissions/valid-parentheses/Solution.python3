// https://leetcode.com/problems/valid-parentheses

from collections import deque
class Solution:
    def isValid(self, s: str):
        if not s:
            return True
        N = len(s)
        st = deque([s[0]])
        for i in range(1, N):
            if not st:
                st.append(s[i])
            else:
                top = st[-1]
                if (top=='(' and s[i]==')') or (top=='{' and s[i]=='}') or (top=='[' and s[i]==']'):
                    st.pop()
                else:
                    st.append(s[i])

        if len(st)==0:
            return True
        else:
            return False

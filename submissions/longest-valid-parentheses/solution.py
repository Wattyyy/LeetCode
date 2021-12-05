# https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        idx_list = []
        for idx, char in enumerate(s):
            if 0 < len(st) and st[-1][0] == '(' and char == ')':
                item = st.pop()
                idx_list.append(item[1])
                idx_list.append(idx)
            else:
                st.append((char, idx))
        
        idx_list = sorted(idx_list)
        if len(idx_list) < 2:
            return 0

        ret = 1
        tmp = 1
        for i, idx in enumerate(idx_list):
            if i == 0:
                continue
            if idx_list[i-1] + 1 == idx:
                tmp += 1
                ret = max(ret, tmp)
            else:
                tmp = 1
        return ret
            
            
        
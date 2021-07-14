// https://leetcode.com/problems/remove-all-occurrences-of-a-substring

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        N = len(part)
        part_ls = list(part)
        st = []
        for char in s:
            st.append(char)
            if N <= len(st) and st[-N:] == part_ls:
                for _ in range(N):
                    st.pop(-1)
        return ''.join(st)
                
            
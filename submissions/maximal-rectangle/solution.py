# https://leetcode.com/problems/maximal-rectangle


class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        R, C = len(matrix), len(matrix[0])
        for r in reversed(range(R)):
            for c in range(C):
                matrix[r][c] = int(matrix[r][c])
                if r == R - 1:
                    continue
                if matrix[r][c] == 1:
                    matrix[r][c] = matrix[r + 1][c] + 1

        ans = 0
        for r in range(R):
            histgram = matrix[r]
            idx = 1
            st = [0]
            while idx < C:
                while histgram[st[-1]] > histgram[idx]:
                    if len(st) == 1:
                        l_idx = st.pop(-1)
                        ans = max(ans, idx * histgram[l_idx])
                        break
                    l_idx = st.pop(-1)
                    ans = max(ans, (idx - (st[-1] + 1)) * histgram[l_idx])
                st.append(idx)
                idx += 1

            while 1 < len(st):
                l_idx = st.pop(-1)
                ans = max(ans, (C - (st[-1] + 1)) * histgram[l_idx])
            ans = max(ans, C * histgram[st[-1]])
        return ans

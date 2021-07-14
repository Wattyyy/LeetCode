// https://leetcode.com/problems/diagonal-traverse

class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or matrix == [[]]:
            return []
        R, C = len(matrix), len(matrix[0])
        ans = []
        def go_urd(r, c):
            ans.append(matrix[r][c])
            if c == C - 1:
                if r + 1 < R:
                    go_lld(r + 1, c)
                else:
                    return
            elif r == 0:
                go_lld(r, c + 1)
            else:
                go_urd(r - 1, c + 1)
    
        def go_lld(r, c):
            ans.append(matrix[r][c])
            if r == R - 1:
                if c + 1 < C:
                    go_urd(r, c + 1)
                else:
                    return
            elif c == 0:
                go_urd(r + 1, c)
            else:
                go_lld(r + 1, c - 1)

        go_urd(0, 0)
        return ans

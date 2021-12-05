# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        visited = set()
        ans = []
        def go_right(r, c):
            if r < 0 or R <= r or c < 0 or C <= c:
                return
            elif (r, c) in visited:
                if (r + 1, c - 1) not in visited:
                    go_lower(r + 1, c - 1)
                else:
                    return
            else:
                ans.append(matrix[r][c])
                visited.add((r, c))
                if c == C - 1:
                    go_lower(r + 1, c)
                else:
                    go_right(r, c + 1)

        def go_lower(r, c):
            if r < 0 or R <= r or c < 0 or C <= c:
                return
            elif (r, c) in visited:
                if (r - 1, c - 1) not in visited:
                    go_left(r - 1, c - 1)
                else:
                    return
            else:
                ans.append(matrix[r][c])
                visited.add((r, c))
                if r == R - 1:
                    go_left(r, c - 1)
                else:
                    go_lower(r + 1, c )


        def go_left(r, c):
            if r < 0 or R <= r or c < 0 or C <= c:
                return
            elif (r, c) in visited:
                if (r - 1, c + 1) not in visited:
                    go_upper(r - 1, c + 1)
                else:
                    return
            else:
                ans.append(matrix[r][c])
                visited.add((r, c))
                if c == 0:
                    go_upper(r - 1, c)
                else:
                    go_left(r, c - 1)


        def go_upper(r, c):
            if r < 0 or R <= r or c < 0 or C <= c:
                return
            if (r, c) in visited:
                if (r + 1, c + 1) not in visited:
                    go_right(r + 1, c + 1)
                else:
                    return
            else:
                ans.append(matrix[r][c])
                visited.add((r, c))
                go_upper(r - 1, c )

        go_right(0, 0)
        return ans

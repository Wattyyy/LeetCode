# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board, word):
        R, C = len(board), len(board[0])
        self.flag = False
        def backtrack(y, x, visited=set(), tmp=[]):
            if len(tmp) == len(word):
                self.flag = True
                return
            if self.flag:
                return
            idx = len(tmp)
            nexts = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
            for ny, nx in nexts:
                if 0 <= ny and ny < R and 0 <= nx and nx < C:
                    if ( (ny, nx) not in visited ) and ( board[ny][nx] == word[idx]):
                        visited.add((ny, nx))
                        tmp.append(word[idx])
                        backtrack(ny, nx, visited, tmp)
                        visited.remove((ny, nx))
                        tmp.pop(-1)
            
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    backtrack(r, c, visited=set([(r, c)]), tmp=[word[0]])

        return self.flag
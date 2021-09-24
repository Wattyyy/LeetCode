class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        for r in range(R):
            for c in range(C):
                nexts = [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                    (r + 1, c + 1),
                    (r + 1, c - 1),
                    (r - 1, c + 1),
                    (r - 1, c - 1),
                ]
                deads, lives = 0, 0
                for nr, nc in nexts:
                    if 0 <= nr < R and 0 <= nc < C:
                        if board[nr][nc] <= 0:
                            deads += 1
                        else:
                            lives += 1

                if board[r][c] == 0:
                    if lives == 3:
                        board[r][c] = -1
                else:
                    if lives < 2 or 3 < lives:
                        board[r][c] = 2

        for r in range(R):
            for c in range(C):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == -1:
                    board[r][c] = 1

        return

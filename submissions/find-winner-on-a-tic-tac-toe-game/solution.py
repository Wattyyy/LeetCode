from typing import List


class Solution:
    def check(self, board: List[List[str]], player: str) -> bool:
        # check vertically
        if any([board[0][c] == board[1][c] == board[2][c] == player for c in range(3)]):
            return True
        # check horizontally
        if any([board[r][0] == board[r][1] == board[r][2] == player for r in range(3)]):
            return True
        # check diagonally
        if any(
            [
                all([board[i][i] == player for i in range(3)]),
                all([board[2 - i][i] == player for i in range(3)]),
            ]
        ):
            return True

        return False

    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["", "", ""] for _ in range(3)]
        for i, move in enumerate(moves):
            r, c = move[0], move[1]
            if i % 2 == 0:
                board[r][c] = "A"
            else:
                board[r][c] = "B"
        if self.check(board, "A"):
            return "A"
        if self.check(board, "B"):
            return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"

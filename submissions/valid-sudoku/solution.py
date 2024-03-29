# https://leetcode.com/problems/valid-sudoku


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        matrix = [[set() for _ in range(3)] for __ in range(3)]

        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == ".":
                    continue

                if char in row[i]:
                    return False
                else:
                    row[i].add(char)

                if char in col[j]:
                    return False
                else:
                    col[j].add(char)

                if char in matrix[i // 3][j // 3]:
                    return False
                else:
                    matrix[i // 3][j // 3].add(char)

        return True

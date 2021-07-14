// https://leetcode.com/problems/word-search

class Solution:
    def __init__(self):
        self.ans = False
    
    def backtrack(self, current_length, visited, y, x, board, word):
        if self.ans:
            return
        if current_length == len(word):
            self.ans = True
            return
        nexts = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
        for ny, nx in nexts:
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and (ny, nx) not in visited and word[current_length] == board[ny][nx]:
                    visited.add((ny, nx))
                    self.backtrack(current_length+1, visited, ny, nx, board, word)
                    visited.remove((ny, nx))

    def exist(self, board, word):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    visited = {(y, x)}
                    self.backtrack(1, visited, y, x, board, word)
        return self.ans
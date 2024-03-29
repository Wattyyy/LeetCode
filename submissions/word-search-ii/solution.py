# https://leetcode.com/problems/word-search-ii

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.nexts = defaultdict(TrieNode)
        self.is_word = False


class Solution:
    def __init__(self):
        self.ans = set()

    def backtrack(self, y, x, cur_node, par_node, word_list, board, visited):
        if len(self.ans) == len(self.words):
            return
        if cur_node.is_word:
            word = "".join(word_list)
            self.ans.add(word)
        if not cur_node.nexts:
            par_node.nexts.pop(word_list[-1])
        neighbors = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
        for ny, nx in neighbors:
            if (
                0 <= ny < len(board)
                and 0 <= nx < len(board[0])
                and (ny, nx) not in visited
            ):
                char = board[ny][nx]
                if char in cur_node.nexts:
                    nx_node = cur_node.nexts[char]
                    visited.add((ny, nx))
                    word_list.append(char)
                    self.backtrack(ny, nx, nx_node, cur_node, word_list, board, visited)
                    visited.remove((ny, nx))
                    word_list.pop()

    def findWords(self, board, words):
        self.root = TrieNode()
        self.words = words
        for word in words:
            cur = self.root
            for char in word:
                if char not in cur.nexts:
                    cur.nexts[char] = TrieNode()
                cur = cur.nexts[char]
            cur.is_word = True

        for y in range(len(board)):
            for x in range(len(board[0])):
                char = board[y][x]
                if char in self.root.nexts:
                    cur_node = self.root.nexts[char]
                    word_list = [char]
                    visited = {(y, x)}
                    self.backtrack(y, x, cur_node, self.root, word_list, board, visited)

        return list(self.ans)

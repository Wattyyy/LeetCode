# https://leetcode.com/problems/implement-trie-prefix-tree

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.nexts = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.nexts:
                cur.nexts[char] = TrieNode()
            cur = cur.nexts[char]
        cur.is_word = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.nexts:
                return False
            cur = cur.nexts[char]
        return cur.is_word

    def startsWith(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.nexts:
                return False
            cur = cur.nexts[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

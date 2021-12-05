# https://leetcode.com/problems/stream-of-characters

from collections import defaultdict, deque


class TrieNode:
    __slots__ = ["children_dic", "is_word"]

    def __init__(self):
        self.children_dic = defaultdict(TrieNode)
        self.is_word = False


class StreamChecker:
    def __init__(self, words):
        self.root = TrieNode()
        self.stack = deque([])
        for word in words:
            cur = self.root
            for char in reversed(word):
                if char not in cur.children_dic.keys():
                    cur.children_dic[char] = TrieNode()
                cur = cur.children_dic[char]
            cur.is_word = True

    def query(self, letter):
        self.stack.append(letter)
        cur = self.root
        L = len(self.stack)
        for i in reversed(range(L)):
            char = self.stack[i]
            if char not in cur.children_dic.keys():
                return False
            else:
                cur = cur.children_dic[char]
                if cur.is_word:
                    return True


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

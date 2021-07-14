// https://leetcode.com/problems/design-add-and-search-words-data-structure

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)



class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word = True

    def backtrack(self, word, index, cur):
        if index == len(word):
            if cur.is_word:
                self.res = True
            return
        if word[index] == '.':
            for _, next_node in cur.children.items():
                self.backtrack(word, index+1, next_node)
        elif word[index] in cur.children:
            char = word[index]
            next_node = cur.children[char]
            self.backtrack(word, index+1, next_node)
        else:
            return
        



    def search(self, word):
        self.res = False
        cur = self.root
        self.backtrack(word, 0, cur)
        return self.res
        
        
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
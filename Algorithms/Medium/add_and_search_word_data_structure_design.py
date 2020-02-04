# https://leetcode.com/problems/add-and-search-word-data-structure-design/

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children_map = defaultdict(TrieNode)
        self.is_word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children_map.keys():
                cur.children_map[char] = TrieNode()
            cur = cur.children_map[char]
        cur.is_word = True
    
    def search(self, word):
        self.is_find = False
        def helper(cur, word, i, L):
            if i==L:
                if cur.is_word:
                    self.is_find = True
                    return 
                else:
                    return
            char = word[i]
            if char==".":
                if not cur.children_map.keys():
                    return 
                for key in cur.children_map.keys():
                    node = cur.children_map[key]
                    helper(node, word, i+1, L)
            else:
                if char not in cur.children_map.keys():
                    return 
                node = cur.children_map[char]
                helper(node, word, i+1, L)
        L = len(word)
        cur = self.root
        helper(cur, word, 0, L)
        return self.is_find

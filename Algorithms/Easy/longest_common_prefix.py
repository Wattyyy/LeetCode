# https://leetcode.com/problems/longest-common-prefix/
    
    
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children_dic = defaultdict(TrieNode)
        self.is_word = False

        
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        self.root = TrieNode()
        for string in strs:
            cur = self.root
            for char in string:
                if char not in cur.children_dic.keys():
                    cur.children_dic[char] = TrieNode()
                cur = cur.children_dic[char]
            cur.is_word = True
        
        cur = self.root
        ans = []
        while True:
            if cur.is_word or len(cur.children_dic.keys())!=1:
                return "".join(ans)
            else:
                key = list(cur.children_dic.keys())[0]
                ans.append(key)
                cur = cur.children_dic[key]

# https://leetcode.com/problems/maximum-product-of-word-lengths/

from collections import defaultdict
class Solution:
    def word2bit(self, word):
        res = 0
        for char in word:
            power = ord(char) - 97
            res = res | (2 ** power)
        return res

    def maxProduct(self, words):
        dic = defaultdict(int)
        for word in words:
            res = self.word2bit(word)
            dic[word] = res
        ans = 0
        for i, word1 in enumerate(words):
            for j in range(i+1, len(words)):
                word2 = words[j]
                bit1, bit2 = dic[word1], dic[word2]
                if bit1 & bit2 == 0:
                    ans = max(ans, len(word1) * len(word2))
        return ans
        
        

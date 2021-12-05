# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentences = sentence.split(' ')
        for i, word in enumerate(sentences):
            if word.startswith(searchWord):
                return i + 1
        return -1
            
# https://leetcode.com/problems/goat-latin

from collections import deque


class Solution:
    def toGoatLatin(self, S):
        S_list = S.split(" ")
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        ans = []
        for i, word in enumerate(S_list):
            listed_word = deque(word)
            if listed_word[0] not in vowels:
                char = listed_word.popleft()
                listed_word.append(char)
            listed_word.append("ma")
            suffix = "a" * (i + 1)
            listed_word.append(suffix)
            ans.append("".join(listed_word))

        return " ".join(ans)

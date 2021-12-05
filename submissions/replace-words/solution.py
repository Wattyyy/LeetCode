# https://leetcode.com/problems/replace-words


class TrieNode:
    def __init__(self):
        self.neighbors = {}
        self.is_word = False


class Solution:
    def replaceWords(self, dict, sentence):
        root = TrieNode()
        for word in dict:
            cur = root
            for char in word:
                if char not in cur.neighbors:
                    cur.neighbors[char] = TrieNode()
                cur = cur.neighbors[char]
            cur.is_word = True

        sentence_list = sentence.split(" ")
        N = len(sentence_list)
        for i in range(N):
            tmp_word = []
            cur = root
            for char in sentence_list[i]:
                if char not in cur.neighbors:
                    break
                cur = cur.neighbors[char]
                tmp_word.append(char)
                if cur.is_word:
                    tmp_word = "".join(tmp_word)
                    sentence_list[i] = tmp_word
                    break
        return " ".join(sentence_list)

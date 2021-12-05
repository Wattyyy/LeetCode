# https://leetcode.com/problems/unique-morse-code-words


class Solution:
    def __init__(self):
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        self.morse_dic = {chr(i + 97): morse[i] for i in range(26)}

    def converte(self, string):
        res = []
        for s in string:
            res.append(self.morse_dic[s])
        return "".join(res)

    def uniqueMorseRepresentations(self, words):
        st = set()
        for w in words:
            st.add(self.converte(w))
        return len(st)

# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s):
        if not s:
            return ""
        ans = []
        strings = s.split(" ")
        for i in reversed(range(len(strings))):
            if strings[i]=="":
                continue
            ans.append(strings[i])
        return " ".join(ans)
            

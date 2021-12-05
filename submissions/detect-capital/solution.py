# https://leetcode.com/problems/detect-capital


class Solution:
    def detectCapitalUse(self, word):
        caps = {chr(i) for i in range(65, 91)}
        if word[0] in caps:
            flag1 = all([word[i] not in caps for i in range(1, len(word))])
            flag2 = all([word[i] in caps for i in range(1, len(word))])
            return flag1 or flag2
        else:
            return all([word[i] not in caps for i in range(1, len(word))])

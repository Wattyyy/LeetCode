# https://leetcode.com/problems/permutation-in-string

# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt, s2_cnt = [0] * 26, [0] * 26
        for char in s1:
            key = ord(char) - 97
            s1_cnt[key] += 1
        for i, char in enumerate(s2):
            if len(s1) <= i:
                break
            key = ord(char) - 97
            s2_cnt[key] += 1
        
        if s1_cnt == s2_cnt:
            return True
        for i in range(1, len(s2)):
            if len(s2) <= i + len(s1) - 1:
                break
            key = ord(s2[i-1]) - 97
            s2_cnt[key] -= 1
            key = ord(s2[i + len(s1) - 1]) - 97
            s2_cnt[key] += 1
            if s1_cnt == s2_cnt:
                return True
        return False
            
# https://leetcode.com/problems/find-all-anagrams-in-a-string


class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        ans = []
        s_cnt, p_cnt = [0] * 26, [0] * 26
        for char in p:
            key = ord(char) - 97
            p_cnt[key] += 1
        for i in range(len(p)):
            key = ord(s[i]) - 97
            s_cnt[key] += 1

        if s_cnt == p_cnt:
            ans.append(0)

        for i in range(1, len(s)):
            if len(s) <= i + len(p) - 1:
                break
            key = ord(s[i - 1]) - 97
            s_cnt[key] -= 1
            key = ord(s[i + len(p) - 1]) - 97
            s_cnt[key] += 1
            if p_cnt == s_cnt:
                ans.append(i)

        return ans

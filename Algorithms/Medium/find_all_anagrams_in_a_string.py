# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        ans = []

        p_arr = [0 for _ in range(26)]
        for char in p:
            p_arr[ord(char) - 97] += 1

        s_arr = [0 for _ in range(26)]
        for char in s[:len(p)]:
            s_arr[ord(char) - 97] += 1
        
        if p_arr == s_arr:
            ans.append(0)
        
        for i in range(1, len(s)):
            if len(s) <= i + len(p) -1:
                break
            prev, new = s[i - 1], s[i + len(p) - 1]
            s_arr[ord(prev) - 97] -= 1
            s_arr[ord(new) - 97] += 1
            if s_arr == p_arr:
                ans.append(i)

        return ans


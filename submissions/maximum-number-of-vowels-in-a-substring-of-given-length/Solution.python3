// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution:
    def maxVowels(self, s, k):
        cnt = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        ans = cnt
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cnt -= 1
            if s[i] in vowels:
                cnt += 1
            ans = max(ans, cnt)
        return ans    
        
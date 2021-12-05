# https://leetcode.com/problems/determine-if-string-halves-are-alike


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        cnt1, cnt2 = 0, 0
        N = len(s)
        for i in range(N // 2):
            if s[i] in vowels:
                cnt1 += 1
        for i in range(N // 2, N):
            if s[i] in vowels:
                cnt2 += 1

        return cnt1 == cnt2

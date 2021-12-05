# https://leetcode.com/problems/longest-substring-without-repeating-characters

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s):
        N = len(s)
        freq_map = defaultdict(int)
        lp, rp = 0, 0
        ans = 0
        while rp < N:
            char = s[rp]
            if freq_map[char] == 0:
                freq_map[char] += 1
                ans = max(ans, rp - lp + 1)
                rp += 1
            else:
                freq_map[char] += 1
                while freq_map[char] != 1:
                    lp_char = s[lp]
                    freq_map[lp_char] -= 1
                    lp += 1
                rp += 1
        return ans

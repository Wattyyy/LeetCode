# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0
        lp, rp = 0, 0
        ans = 0
        char_cnt = Counter()
        while rp < len(s):
            rp_char = s[rp]
            char_cnt[rp_char] += 1
            while len(char_cnt.keys()) > k:
                lp_char = s[lp]
                char_cnt[lp_char] -= 1
                if char_cnt[lp_char] == 0:
                    del char_cnt[lp_char]
                lp += 1
            ans = max(rp - lp + 1, ans)
            rp += 1

        return ans

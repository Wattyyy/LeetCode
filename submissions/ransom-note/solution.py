# https://leetcode.com/problems/ransom-note

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_cnt = Counter(ransomNote)
        m_cnt = Counter(magazine)
        for key in r_cnt:
            if r_cnt[key] > m_cnt[key]:
                return False
        return True
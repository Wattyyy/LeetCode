# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) <= k:
            return False
        num_set = set()
        reversed_s = s[::-1]
        
        # initialization
        val = int(s[:k], 2)
        num_set.add(val)
        for i in range(k, len(s)):
            val = val - int(s[i - k])
            val = val // 2
            val = val + int(s[i]) * 2 ** (k - 1)
            num_set.add(val)
        
        return len(num_set) == (2 ** k)

        
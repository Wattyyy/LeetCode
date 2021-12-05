# https://leetcode.com/problems/binary-trees-with-factors

from math import sqrt
from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10 ** 9 + 7 
        arr = sorted( list(set(arr)) )
        dp = defaultdict(int)
        
        for num in arr:
            factors = set()
            # prime factrization
            for d in range(1, int(sqrt(num)) + 1):
                if num % d != 0:
                    continue
                low_f, high_f = d, num // d 
                if low_f == 1:
                    dp[num] += 1
                elif low_f == high_f:
                    dp[num] += dp[low_f] * dp[high_f]
                else:
                    dp[num] += 2 * dp[low_f] * dp[high_f]
            dp[num] = dp[num] % MOD
        
        ans = 0
        for k, v in dp.items():
            ans += v
        
        return ans % MOD
        

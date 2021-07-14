// https://leetcode.com/problems/minimum-operations-to-make-array-equal

class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        if n % 2 == 1:
            val = 2
        else:
            val = 1
        for _ in range(n // 2):
            res += val
            val += 2
        return res
    

            

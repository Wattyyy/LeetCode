# https://leetcode.com/problems/power-of-three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        max_val = pow(2, 31) - 1
        p_set = set()
        val = 1
        while val <= max_val:
            p_set.add(val)
            val *= 3
        return (n in p_set)
            
        
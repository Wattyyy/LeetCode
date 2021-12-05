# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers


class Solution:
    def minPartitions(self, n: str) -> int:
        val = -1
        for char in n:
            val = max(int(char), val)
        return val

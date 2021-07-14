// https://leetcode.com/problems/pascals-triangle

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1,1]]
        if numRows == 1 or numRows == 2:
            return res[:numRows]
        for i in range(2, numRows):
            tmp = []
            prev = res[i-1]
            for i, _ in enumerate(prev):
                if i == 0:
                    tmp.append(1)
                else:
                    tmp.append(prev[i] + prev[i-1])
            tmp.append(1)
            res.append(tmp[:])
        return res
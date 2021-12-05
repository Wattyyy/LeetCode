# https://leetcode.com/problems/gray-code


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]
        for v in range(1, n):
            new = res[:]
            add = 2 ** v
            for i in reversed(range(len(res))):
                new.append(add + res[i])
            res = new
        return res

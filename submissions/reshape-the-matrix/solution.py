# https://leetcode.com/problems/reshape-the-matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        V, H = len(mat), len(mat[0])
        if V * H == r * c:
            res = []
            tmp = []
            for v in range(V):
                for h in range(H):
                    tmp.append(mat[v][h])
                    if len(tmp) == c:
                        res.append(tmp[:])
                        tmp = []
            return res
        else:
            return mat
        
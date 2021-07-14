// https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        h, w = len(A), len(A[0])
        trans_A = [[0 for i in range(h)] for j in range(w)]
        for i in range(h):
            for j in range(w):
                trans_A[j][i] = A[i][j]
        
        return trans_A
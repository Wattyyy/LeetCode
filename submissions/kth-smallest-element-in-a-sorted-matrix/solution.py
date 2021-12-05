# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ls = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ls.append(matrix[r][c])
        ls = sorted(ls)
        return ls[k-1]
        
// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n):
        if n<3:
            tri = [0 for _ in range(3)]
            tri[1], tri[2] = 1, 1
            return tri[n]
        
        tri = [0 for _ in range(n+1)]
        tri[1], tri[2] = 1, 1
        for i in range(3, n+1):
            tri[i] = tri[i-3] + tri[i-2] + tri[i-1]
        return tri[n]
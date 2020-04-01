# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle):
        if triangle == [[]]:
            return 0
        INF = float('inf')
        level = len(triangle)
        dp = []
        for item in triangle:
            length = len(item)
            tmp = [INF for _ in range(length)]
            dp.append(tmp)
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            current = triangle[i]
            for j in range(len(current)):
                if 0 <= j - 1 and j - 1 < i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + current[j])
                if 0 <= j and j < i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + current[j])
    
        return min(dp[-1])

        

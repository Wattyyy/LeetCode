// https://leetcode.com/problems/minimum-falling-path-sum-ii

class Solution:
    def minFallingPathSum(self, arr):
        R, C = len(arr), len(arr[0])
        dp = [[float("inf") for _ in range(C)] for __ in range(R)]
        # (DPvalue, index)
        min_two = [(float("inf"), -1), (float("inf"), -1)]
        for c in range(C):
            dp[0][c] = arr[0][c]
            if dp[0][c] < min_two[1][0]:
                min_two[1] = (dp[0][c], c)
                min_two = sorted(min_two)
        
        for r in range(1, R):
            tmp_min_two = [(float("inf"), -1), (float("inf"), -1)]
            for c in range(C):
                if min_two[0][1] == c:
                    dp[r][c] = arr[r][c] + min_two[1][0]
                else:
                    dp[r][c] = arr[r][c] + min_two[0][0]
                if dp[r][c] < tmp_min_two[1][0]:
                    tmp_min_two[1] = (dp[r][c], c)
                    tmp_min_two = sorted(tmp_min_two)
            min_two = tmp_min_two
            
        return min(dp[R-1])
        
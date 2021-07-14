// https://leetcode.com/problems/largest-plus-sign

class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        ans = 0
        mines = set(map(tuple, mines))
        if len(mines) == N**2:
            return 0
        # count left 1s at (i, j)
        l_dp = [[0 for j in range(N)] for i in range(N)]
        # count right 1s at (i, j)
        r_dp = [[0 for j in range(N)] for i in range(N)]
        # count upper 1s at (i, j)
        u_dp = [[0 for j in range(N)] for i in range(N)]
        # count downward 1s at (i, j)
        d_dp = [[0 for j in range(N)] for i in range(N)]

        for i in range(N):
            for j in range(N):
                # l_dp
                if 0 <= j-1:
                    l_dp[i][j] = (1 + l_dp[i][j-1]) if (i, j-1) not in mines else 0
                # u_dp
                if 0 <= i-1:
                    u_dp[i][j] = (1 + u_dp[i-1][j]) if (i-1, j) not in mines else 0
        
        for i in reversed(range(N)):
            for j in reversed(range(N)):
                # r_dp
                if j+1 <= N-1:
                    r_dp[i][j] = (1 + r_dp[i][j+1]) if (i, j+1) not in mines else 0
                # d_dp
                if i+1 <= N-1:
                    d_dp[i][j] = (1 + d_dp[i+1][j]) if (i+1, j) not in mines else 0

        for i in range(N):
            for j in range(N):
                if (i, j) in mines:
                    continue
                ans = max(ans, min(l_dp[i][j], r_dp[i][j], u_dp[i][j], d_dp[i][j]))
                
        return ans + 1
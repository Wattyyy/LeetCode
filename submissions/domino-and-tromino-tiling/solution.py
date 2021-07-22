class Solution:
    def numTilings(self, n: int) -> int:
        '''
        0 -> #
             .
             
        1 -> .
             #
             
        2 -> #
             #
             
        '''
        M = 10 ** 9 + 7 
        if n == 1 or n == 2:
            return n
        dp = [[0 for _ in range(3)] for __ in range(n)]
        dp[0][2] = 1
        dp[1][0], dp[1][1], dp[1][2] = 1, 1, 2
        for i in range(2, n):
            dp[i][0] = (dp[i-2][2] + dp[i-1][1]) % M
            dp[i][1] = (dp[i-2][2] + dp[i-1][0]) % M
            dp[i][2] = (dp[i-2][2] + dp[i-1][2] + dp[i-1][0] + dp[i-1][1]) % M
        
        return dp[-1][-1]

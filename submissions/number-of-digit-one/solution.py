# https://leetcode.com/problems/number-of-digit-one


class Solution:
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        # number of digits
        N = str(n)
        L = len(N)
        # dp[i][j][k] i: number of digits, j: is less than n, k: number of "1"
        dp = [[[0 for k in range(L + 1)] for j in range(2)] for i in range(L + 1)]
        dp[0][0][0] = 1
        for i in range(L):
            for j in range(2):
                for k in range(L + 1):
                    num = int(N[i])

                    # less than n
                    if j == 1:
                        # add 0 ~ 9 except 1
                        dp[i + 1][j][k] += dp[i][j][k] * 9
                        # add 1
                        if k < L:
                            dp[i + 1][j][k + 1] += dp[i][j][k]

                    # equal to n
                    elif j == 0:
                        if num == 0:
                            dp[i + 1][0][k] += dp[i][j][k]
                        elif num == 1:
                            # add 0
                            dp[i + 1][1][k] += dp[i][j][k]
                            # add 1
                            if k < L:
                                dp[i + 1][0][k + 1] += dp[i][j][k]
                        else:
                            # add num
                            dp[i + 1][0][k] += dp[i][j][k]
                            # add 0, 2 ~ num-1
                            dp[i + 1][1][k] += dp[i][j][k] * (num - 1)
                            # add 1
                            if k < L:
                                dp[i + 1][1][k + 1] += dp[i][j][k]

        ans = 0
        for k in range(L + 1):
            ans += k * (dp[-1][0][k] + dp[-1][1][k])
        return ans

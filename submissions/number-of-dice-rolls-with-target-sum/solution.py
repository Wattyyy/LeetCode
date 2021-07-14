// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum

class Solution:
    def numRollsToTarget(self, d, f, target):
        # dp[(d, target)] = count
        dp = {(1, t):0 for t in range(1, target+1)}
        for f_val in range(1, f+1):
            dp[(1, f_val)] = 1
      
        for d_val in range(2, d+1):
            for f_val in range(1, f+1):
                for t in range(1, target+1):
                    if (d_val, t) not in dp.keys():
                        dp[(d_val, t)] = 0
                    if t - f_val >= 1:
                        dp[(d_val, t)] += dp[(d_val - 1, t - f_val)]
        return dp[(d, target)] % (10**9 + 7)
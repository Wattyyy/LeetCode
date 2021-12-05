# https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        tmp1 = ' ' + word1
        tmp2 = ' ' + word2
        dp = [[0 for _ in range(len(tmp2))] for __ in range(len(tmp1))]
        for r in range(1, len(tmp1)):
            for c in range(1, len(tmp2)):
                if tmp1[r] == tmp2[c]:
                    dp[r][c] = max(dp[r][c], dp[r-1][c-1] + 1)
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        return len(word1) - dp[-1][-1] + len(word2) - dp[-1][-1]
                
                
                
        
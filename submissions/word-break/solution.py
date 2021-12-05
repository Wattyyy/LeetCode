# https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s = " " + s
        dp = [False for _ in range(len(s))]
        dp[0] = True
        for i in range(len(s)):
            for j in range(i):
                if (dp[j]==True) and (s[j+1:i+1] in wordDict):
                    dp[i] = True
                    break
        
        return dp[len(s)-1]
    
            
            
        
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows):
        if numRows==1:
            return [[1]]
        dp = {} 
        dp[(1,1)] = 1
        for i in range(2, numRows+1):
            for j in range(1, i+1):
                if j==1:
                    dp[(i, j)] = 1
                elif j==i:
                    dp[(i, j)] = 1
                else:
                    dp[(i, j)] = dp[(i-1, j-1)] + dp[(i-1, j)]
        ans = []
        for i in range(1, numRows+1):
            tmp = []
            for j in range(1, i+1):
                tmp.append(dp[(i, j)])
            ans.append(tmp)
            
        return ans
        
        
        
        
        

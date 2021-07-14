// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        res = [1]
        for i in range(1, rowIndex + 1):
            item = ( res[-1] * (rowIndex - i + 1) ) // i
            res.append(item)
        return res
            
        
        
// https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        tmp = []
        for num in nums:
            if len(tmp) == 0:
                tmp.append(num)
            elif num - tmp[-1] == 1:
                tmp.append(num)
            else:
                ranges.append(tmp[:])
                tmp = [num]
        if len(tmp) != 0:
            ranges.append(tmp[:])
        
        res = []
        for item in ranges:
            if len(item) == 1:
                res.append(str(item[0]))
            else:
                res.append( str(item[0]) + "->" + str(item[-1]) )
        return res
            


            
        
            
        
        
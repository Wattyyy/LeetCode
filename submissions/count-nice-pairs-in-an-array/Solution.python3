// https://leetcode.com/problems/count-nice-pairs-in-an-array

from collections import defaultdict
from bisect import bisect_right

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 7 + 10 ** 9
        ls = []
        num2indices = defaultdict(list)
        for i, num in enumerate(nums):
            rev = int( str(num)[::-1] )
            num2indices[num - rev].append(i)
            ls.append(num - rev)
        
        ret = 0
        for i, val in enumerate(ls):
            length = len(num2indices[val])
            ret += length - bisect_right(num2indices[val], i)
            ret = ret % MOD
        
        return ret % MOD

        


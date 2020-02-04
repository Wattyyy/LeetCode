# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from bisect import bisect_left
def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

class Solution:
    def twoSum(self, numbers, target):
        if not numbers:
            return []
        N = len(numbers)
        diffs = [target-numbers[i] for i in range(N)]
        for i in range(N):
            j = index(numbers, diffs[i])
            if j!=-1 and i!=j:
                return sorted([i+1, j+1])
            else:
                continue
            
        

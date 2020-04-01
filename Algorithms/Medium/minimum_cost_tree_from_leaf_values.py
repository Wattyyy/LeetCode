# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

from collections import defaultdict
class Solution:
    def mctFromLeafValues(self, arr):
        # rec(l, r) -> [max_leef, sum_val]
        memo = defaultdict(int)
        def rec(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            elif l == r:
                memo[(l, r)] = (arr[l], 0)
                return (arr[l], 0)
            else:
                max_leef, min_sum = 0, float('inf')
                for i in range(l, r):
                    l_max, l_sum = rec(l, i)
                    r_max, r_sum = rec(i+1, r)
                    max_leef = max(max_leef, max(l_max, r_max))
                    min_sum = min(min_sum, (l_max * r_max) + l_sum + r_sum)
                memo[(l, r)] = (max_leef, min_sum)
                return (max_leef, min_sum)
        
        ans = rec(0, len(arr)-1)[1]
        return ans
                
        

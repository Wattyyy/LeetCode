# https://leetcode.com/problems/grumpy-bookstore-owner

from itertools import accumulate
class Solution:
    def maxSatisfied(self, customers, grumpy, x):
        grumpy_customers = [0] * len(grumpy)
        for i, v in enumerate(customers):
            grumpy_customers[i] = abs(1 - grumpy[i]) * v
        
        cum_customers = list(accumulate(customers))
        cum_customers = [0] + cum_customers
        cum_grumpy = list(accumulate(grumpy_customers))
        cum_grumpy = [0] + cum_grumpy
        
        ans = cum_grumpy[-1]
        for i in range(x, len(cum_customers)):
            gain = (cum_customers[i] - cum_customers[i-x]) - (cum_grumpy[i] - cum_grumpy[i-x])
            ans = max(ans, cum_grumpy[-1] + gain)
        
        return ans
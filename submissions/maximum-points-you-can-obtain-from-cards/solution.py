# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

from typing import List
from itertools import accumulate

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cum_sum = [0] + list(accumulate(cardPoints))
        rev_cum_sum = [0] + list(accumulate(cardPoints[::-1]))
        ans = -float('inf')
        for i in range(k+1):            
            ans = max(cum_sum[i] + rev_cum_sum[k-i], ans)
        return ans


